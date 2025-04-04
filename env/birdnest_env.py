import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.bird_nest_data import Truths, Actions, Outcomes

@registry.register_environment("BirdNestEnv")
class BirdNestEnv(BaseEnv):
    
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
Please write a guidebook on bird nest identification in forests, introducing the following nest types and examination methods in natural language according to the following information.

Nest types: {truths}

Examination methods: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the nest types that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Examination1" is:
    
    "Examination1":
    {
        "states": {
            "Outcome_1": ["NestType1", "NestType2"],
            "Outcome_2": ["NestType3", "NestType4"]
        }
    }
        
    This means:
    - When “Examination1” is performed and “Outcome_1” is observed, “NestType1” and "NestType2" are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which nest types are valid or related.

2. Explain the nest types and examination methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the type of bird's nest found in a forest based on examination outcomes. Each round, you'll be presented with a list of possible nest types and available examination methods. You need to systematically rule out nest types that do not match the observed outcomes until only one plausible nest type remains. Your objective is to identify the nest type accurately in the fewest steps.

How to Play:

(1) View the list of possible nest types and available examination methods.

(2) Choose one examination method from the list to perform.

(3) Use the outcomes to eliminate nest types that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the nest type.

This is the initial state of the game:

Nest Types: {self.env.truth_space}

Examination Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a guidebook on bird nest identification to introduce the nest types and examination methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt