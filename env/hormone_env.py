import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.hormone_data import Truths, Actions, Outcomes

@registry.register_environment("HormoneEnv")
class HormoneEnv(BaseEnv):
    
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
Please write a hormonal analysis guidebook that introduces the following hormones and assays or tests in natural language according to the following information.

Hormones: {truths}

Hormone assays / endocrine function tests: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the hormones that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Test1" is:
    
    "Test1":
    {
        "states": {
            "Outcome_1": ["Hormone1", "Hormone2"],
            "Outcome_2": ["Hormone3", "Hormone4"]
        }
    }
        
    This means:
    - When “Test1” is performed and “Outcome_1” is observed, “Hormone1” and “Hormone2” are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which hormones are valid or related.

2. Explain the hormones and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify which hormone is causing a physiological response based on test outcomes. Each round, you'll be presented with a list of possible hormones and available hormone assays or endocrine function tests. You need to systematically rule out hormones that do not match the observed outcomes until only one plausible hormone remains. Your objective is to identify the hormone accurately in the fewest steps.

How to Play:

(1) View the list of possible hormones and available hormone assays or tests.

(2) Choose one test from the list to perform.

(3) Use the outcomes to eliminate hormones that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the hormone.

This is the initial state of the game:

Hormones: {self.env.truth_space}

Hormone assays / endocrine function tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a hormonal analysis guidebook to introduce the hormones and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt