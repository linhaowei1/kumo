import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.education_data import *

@registry.register_environment("EducationEnv")
class EducationEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Abilities     
        self.all_actions = Tests   
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a educational analysis guidebook that introduces the following abilities and tests in natural language according to the following information.

Abilities: {truths}

Tests: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of "Outcomes" represent the abilities that are **not lacked** when the corresponding state is observed.

For example,

    If the state of "Test1" is:
    
    "Test1":
    {
        "states": {
            "Outcome_1": ["Ability1", "Ability2"],
            "Outcome_2": ["Ability3", "Ability4"]
        }
    }
        
    This means:
    - When “Test1” is performed and “Outcome_1” is observed, “Ability1” and "Ability2" are ruled out (i.e., they are not lacked, so should be eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which abilities are lacked.

2. Explain the abilities and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rules should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a lacked ability based on test outcomes for a student. Each round, you'll be presented with a list of possible abilities and available tests. You need to systematically rule out abilities that do not match the observed outcomes until only one plausible ability remains. Your objective is to identify the lacked ability accurately in the fewest steps.

How to Play:

(1) View the list of possible abilities and available tests.

(2) Choose one test from the list to perform.

(3) Use the outcomes to eliminate abilities that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the ability.

This is the initial state of the game:

Abilities: {self.env.truth_space}

Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a educational analysis guidebook to introduce the abilities and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt

        
        elif agent_type == 'ReactAgent':
            raise NotImplementedError("ReactAgent is not implemented for the Env yet.")