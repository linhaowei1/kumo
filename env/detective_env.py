import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.detective_data import Truths, Actions, Outcomes

@registry.register_environment("DetectiveEnv")
class DetectiveEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Define potential suspects
        self.all_actions = Actions    # Define available actions such as interrogation, fingerprint analysis, etc.
        self.ta_mapping = Outcomes    # Define how outcomes relate to the suspects
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a detective guidebook that introduces the prime suspect identification process according to the following information.

Suspects: {truths}

Investigation Actions: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the suspects that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Interrogation1" is:
    
    "Interrogation1":
    {
        "states": {
            "Outcome_1": ["Suspect1", "Suspect2"],
            "Outcome_2": ["Suspect3", "Suspect4"]
        }
    }
        
    This means:
    - When “Interrogation1” is performed and “Outcome_1” is observed, “Suspect1” and “Suspect2” are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which suspects are valid or related.

2. Explain the investigation actions and suspects in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the prime suspect based on investigation outcomes. Each round, you'll be presented with a list of possible suspects and available actions. You need to systematically rule out suspects that do not match the observed outcomes until only one plausible suspect remains. Your objective is to identify the suspect accurately in the fewest steps.

How to Play:

(1) View the list of possible suspects and available investigation actions.

(2) Choose one action from the list to perform.

(3) Use the outcomes to eliminate suspects that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the prime suspect.

This is the initial state of the game:

Suspects: {self.env.truth_space}

Investigation Actions: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a detective analysis guidebook to introduce the suspects and investigation actions:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt