import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.ocean_data import Truths, Actions, Outcomes

@registry.register_environment("OceanEnv")
class OceanEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      #
        self.all_actions = Actions    #
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write an oceanography analysis guidebook that introduces the following ocean currents and measurement techniques in natural language according to the following information.

Ocean Currents: {truths}

Measurement Techniques: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the ocean currents that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "TemperatureMeasurement1" is:
    
    "TemperatureMeasurement1":
    {
        "states": {
            "Outcome_1": ["Current1", "Current2"],
            "Outcome_2": ["Current3", "Current4"]
        }
    }
        
    This means:
    - When “TemperatureMeasurement1” is performed and “Outcome_1” is observed, “Current1” and “Current2” are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which currents are valid or related.

2. Explain the ocean currents and measurement techniques in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify which ocean current is influencing a coastal climate based on measurement outcomes. Each round, you'll be presented with a list of possible ocean currents and available measurement techniques. You need to systematically rule out ocean currents that do not match the observed outcomes until only one plausible ocean current remains. Your objective is to identify the current accurately in the fewest steps.

How to Play:

(1) View the list of possible ocean currents and available measurement techniques.

(2) Choose one measurement technique from the list to perform.

(3) Use the outcomes to eliminate ocean currents that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the ocean current.

This is the initial state of the game:

Ocean Currents: {self.env.truth_space}

Measurement Techniques: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is an oceanographic analysis guidebook to introduce the ocean currents and measurement techniques:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt