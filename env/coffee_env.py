import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.coffee_data import Truths, Actions, Outcomes

@registry.register_environment("CoffeeEnv")
class CoffeeEnv(BaseEnv):
    
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
Please write a coffee analysis guidebook that introduces the following coffee bean varieties and testing methods in natural language according to the following information.

Coffee Bean Varieties: {truths}

Testing Methods: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the coffee bean varieties that must be **excluded or ruled out** when the corresponding outcome is observed.

For example,

    If the state of "TestingMethod1" is:
    
    "TestingMethod1":
    {
        "states": {
            "Outcome_1": ["Variety1", "Variety2"],
            "Outcome_2": ["Variety3", "Variety4"]
        }
    }
        
    This means:
    - When “TestingMethod1” is performed and “Outcome_1” is observed, “Variety1” and “Variety2” are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which varieties are valid or related.

2. Explain the coffee bean varieties and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a coffee bean variety based on test outcomes. Each round, you'll be presented with a list of possible coffee bean varieties and available testing methods. You need to systematically rule out coffee bean varieties that do not match the observed outcomes until only one plausible variety remains. Your objective is to identify the variety accurately in the fewest steps.

How to Play:

(1) View the list of possible coffee bean varieties and available testing methods.

(2) Choose one testing method from the list to perform.

(3) Use the outcomes to eliminate coffee bean varieties that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the variety.

This is the initial state of the game:

Coffee Bean Varieties: {self.env.truth_space}

Testing Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a coffee analysis guidebook to introduce the coffee bean varieties and testing methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt