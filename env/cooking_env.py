import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.cooking_data import Truths, Actions, Outcomes

@registry.register_environment("CookingEnv")
class CookingEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Cooking methods
        self.all_actions = Actions    # Texture analysis / ingredient transformation testing
        self.ta_mapping = Outcomes    # Texture-Method mapping
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a culinary analysis guidebook that introduces the following cooking methods and tests in natural language according to the following information.

Cooking methods: {truths}

Tests: {actions}

Outcomes (Textures): {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the cooking methods that must be **excluded or ruled out** when the corresponding texture is observed.

For example,

    If the state of "Test1" is:
    
    "Test1":
    {
        "states": {
            "Outcome_1": ["Method1", "Method2"],
            "Outcome_2": ["Method3", "Method4"]
        }
    }
        
    This means:
    - When “Test1” is performed and “Outcome_1” is observed, “Method1” and Method2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which methods are valid or related.

2. Explain the cooking methods and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a cooking method based on texture outcomes. Each round, you'll be presented with a list of possible cooking methods and available tests. You need to systematically rule out cooking methods that do not match the observed textures until only one plausible method remains. Your objective is to identify the method accurately in the fewest steps.

How to Play:

(1) View the list of possible cooking methods and available tests.

(2) Choose one test from the list to perform.

(3) Use the outcomes to eliminate cooking methods that don't match the observed textures.

(4) Repeat steps 2 and 3 until you can confidently identify the method.

This is the initial state of the game:

Cooking Methods: {self.env.truth_space}

Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a culinary analysis guidebook to introduce the cooking methods and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt