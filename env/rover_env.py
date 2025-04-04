import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.rover_data import Truths, Actions, Outcomes

@registry.register_environment("RoverEnv")
class RoverEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths  # Rover prototypes
        self.all_actions = Actions  # Field tests / sensor calibration checks
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a rover identification guidebook that introduces the following rover prototypes and tests in natural language according to the following information.

Rover Prototypes: {truths}

Field Tests / Sensor Calibration Checks: {actions}

Results: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Results” represent the rover prototypes that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Test1" is:
    
    "Test1":
    {
        "states": {
            "Result_1": ["Rover1", "Rover2"],
            "Result_2": ["Rover3", "Rover4"]
        }
    }
        
    This means:
    - When “Test1” is performed and “Result_1” is observed, “Rover1” and Rover2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which rovers are valid or related.

2. Explain the rover prototypes and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the correct rover prototype based on test results. Each round, you'll be presented with a list of possible rover prototypes and available field tests or sensor calibration checks. You need to systematically rule out rover prototypes that do not match the observed results until only one plausible prototype remains. Your objective is to identify the prototype accurately in the fewest steps.

How to Play:

(1) View the list of possible rover prototypes and available tests.

(2) Choose one test from the list to perform.

(3) Use the results to eliminate rover prototypes that don't match the observed findings.

(4) Repeat steps 2 and 3 until you can confidently identify the prototype.

This is the initial state of the game:

Rover Prototypes: {self.env.truth_space}

Field Tests / Sensor Calibration Checks: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a rover identification guidebook to introduce the rover prototypes and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt