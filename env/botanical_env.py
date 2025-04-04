import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.botanical_data import Truths, Actions, Outcomes

@registry.register_environment("BotanicalEnv")
class BotanicalEnv(BaseEnv):
    
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
Please write a botanical analysis guidebook that introduces the following plant adaptations and inspection methods in natural language according to the following information.

Plant Adaptations: {truths}

Inspection Methods: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the plant adaptations that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "InspectionMethod1" is:
    
    "InspectionMethod1":
    {
        "states": {
            "Outcome_1": ["Adaptation1", "Adaptation2"],
            "Outcome_2": ["Adaptation3", "Adaptation4"]
        }
    }
        
    This means:
    - When “InspectionMethod1” is performed and “Outcome_1” is observed, “Adaptation1” and “Adaptation2” are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which adaptations are valid or related.

2. Explain the plant adaptations and inspection methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify which botanical adaptation a plant species evolved based on inspection outcomes. Each round, you'll be presented with a list of possible plant adaptations and available inspection methods. You need to systematically rule out adaptations that do not match the observed outcomes until only one plausible adaptation remains. Your objective is to identify the adaptation accurately in the fewest steps.

How to Play:

(1) View the list of possible plant adaptations and available inspection methods.

(2) Choose one inspection method from the list to perform.

(3) Use the outcomes to eliminate plant adaptations that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the adaptation.

This is the initial state of the game:

Plant Adaptations: {self.env.truth_space}

Inspection Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a botanical analysis guidebook to introduce the plant adaptations and inspection methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt