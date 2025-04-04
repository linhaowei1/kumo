import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.gemstone_data import Truths, Actions, Outcomes  # Assuming imported data is correctly established

@registry.register_environment("GemstoneEnv")
class GemstoneEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Refers to 'Gemstones'
        self.all_actions = Actions    # Refers to 'Refractive index tests / hardness and UV fluorescence checks'
        self.ta_mapping = Outcomes    # Represents suitable outcomes for the tests
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write an analysis guidebook to identify real gemstones among synthetic ones using the natural language guidelines outlined below.

Gemstones: {truths}

Tests: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets under the state of "Outcomes" represent the gemstones that must be **excluded or ruled out** based on the test observations.

For example,

    If the test result is observed as follows:
    
    "Test Example":
    {
        "states": {
            "Outcome_1": ["Synthetic1", "Synthetic2"],
            "Outcome_2": ["Synthetic3", "Synthetic4"]
        }
    }
        
    This means:
    - If "Test Example" is conducted and "Outcome_1" is observed, "Synthetic1" and "Synthetic2" are ruled out.
	- This exclusion method implies dismissing options based on mismatches instead of identifying valid gemstones.

2. Explain the gemstones and tests in a simple, clear language to make relationships understandable.

3. Ensure all relevant information is communicated completely with every "rule-out" articulated clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the real gemstone based on the outcomes of specific tests. Each round, you'll encounter possible gemstones and various tests. Systematically eliminate synthetic gemstones that don't match the observed test outcomes until only the real gemstone is left. Your aim is to precisely identify it in the fewest moves.

How to Play:

(1) Review the list of possible gemstones and available tests.

(2) Select a test from the list to perform.

(3) Utilize the outcomes to exclude gemstones that don't align with the observed results.

(4) Repeat steps 2 and 3 until you confidently identify the real gemstone.

This is the initial state of the game:

Gemstones: {self.env.truth_space}

Tests: {self.env.action_space}
                
"""
            
            if book:
                system_prompt += f"\n\nHere is an analysis guidebook for understanding the gemstones and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt