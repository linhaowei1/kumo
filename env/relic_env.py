import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.relic_data import Truths, Actions, Outcomes

@registry.register_environment("RelicEnv")
class RelicEnv(BaseEnv):
    
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
Please write a guidebook on ancient relics that introduces the attributes of these relics and examination methods in natural language according to the following information.

Attributes of Ancient Relics: {truths}

Examination/Testing Methods and Activation Steps: {actions}

Outcomes of Research: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the relic attributes that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Examination1" is:
    
    "Examination1":
    {
        "states": {
            "Outcome_1": ["Attribute1", "Attribute2"],
            "Outcome_2": ["Attribute3", "Attribute4"]
        }
    }
        
    This means:
    - When “Examination1” is performed and “Outcome_1” is observed, “Attribute1” and Attribute2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which attributes are valid or related.

2. Explain the relic attributes and examination methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify an ancient relic that can unlock hidden knowledge based on test outcomes. Each round, you'll be presented with a list of possible attributes of ancient relics and available examination/testing methods. You need to systematically rule out relic attributes that do not match the observed outcomes until only one plausible relic remains. Your objective is to identify the relic accurately in the fewest steps.

How to Play:

(1) View the list of possible attributes of ancient relics and available examination/testing methods.

(2) Choose one examination or testing method from the list to perform.

(3) Use the outcomes to eliminate relic attributes that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the relic.

This is the initial state of the game:

Attributes of Ancient Relics: {self.env.truth_space}

Examination/Testing Methods and Activation Steps: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a guidebook on ancient relics to introduce the relic attributes and examination methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt