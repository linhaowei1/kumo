import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.fish_data import Truths, Actions, Outcomes

@registry.register_environment("FishEnv")
class FishEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths     
        self.all_actions = Actions    
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a fishing analysis guidebook that introduces the following fish species and identification methods in natural language according to the following information.

Fish species: {truths}

Identification methods: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the fish species that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "ScalePatternCheck" is:
    
    "ScalePatternCheck":
    {
        "states": {
            "Outcome_1": ["Species1", "Species2"],
            "Outcome_2": ["Species3", "Species4"]
        }
    }
        
    This means:
    - When “ScalePatternCheck” is performed and “Outcome_1” is observed, “Species1” and “Species2” are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which species are valid or related.

2. Explain the fish species and identification methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a fish species based on scale pattern and gill structure checks. Each round, you'll be presented with a list of possible fish species and available identification methods. You need to systematically rule out fish species that do not match the observed outcomes until only one plausible species remains. Your objective is to identify the species accurately in the fewest steps.

How to Play:

(1) View the list of possible fish species and available identification methods.

(2) Choose one identification method from the list to perform.

(3) Use the outcomes to eliminate fish species that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the fish species.

This is the initial state of the game:

Fish Species: {self.env.truth_space}

Identification Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a fishing analysis guidebook to introduce the fish species and identification methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt