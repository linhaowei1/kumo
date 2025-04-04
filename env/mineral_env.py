import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.mineral_data import Truths, Actions, Outcomes

@registry.register_environment("MineralEnv")
class MineralEnv(BaseEnv):
    
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
Please write a mineral identification guidebook that introduces the following extraterrestrial minerals and tests in natural language according to the following information.

Extraterrestrial minerals: {truths}

Tests: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the extraterrestrial minerals that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the test of "X-ray diffraction" is:
    
    "X-ray diffraction":
    {
        "states": {
            "Outcome_1": ["Mineral1", "Mineral2"],
            "Outcome_2": ["Mineral3", "Mineral4"]
        }
    }
        
    This means:
    - When “X-ray diffraction” is performed and “Outcome_1” is observed, “Mineral1” and Mineral2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which minerals are valid or related.

2. Explain the extraterrestrial minerals and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rules should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify which extraterrestrial mineral is in a meteorite sample based on test outcomes. Each round, you'll be presented with a list of possible minerals and available tests. You need to systematically rule out minerals that do not match the observed outcomes until only one plausible mineral remains. Your objective is to identify the mineral accurately in the fewest steps.

How to Play:

(1) View the list of possible extraterrestrial minerals and available tests.

(2) Choose one test from the list to perform.

(3) Use the outcomes to eliminate minerals that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the mineral.

This is the initial state of the game:

Extraterrestrial Minerals: {self.env.truth_space}

Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a mineral identification guidebook to introduce the extraterrestrial minerals and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt