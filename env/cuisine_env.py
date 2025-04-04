import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.cuisine_data import Truths, Actions, Outcomes

@registry.register_environment("CuisineEnv")
class CuisineEnv(BaseEnv):
    
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
Please write a culinary analysis guidebook that introduces the following cuisines and exploration techniques in natural language according to the following information.

Cuisines: {truths}

Exploration Techniques: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the cuisines that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Spice Profiling" is:
    
    "Spice Profiling":
    {
        "states": {
            "Outcome_1": ["Cuisine1", "Cuisine2"],
            "Outcome_2": ["Cuisine3", "Cuisine4"]
        }
    }
        
    This means:
    - When “Spice Profiling” is performed and “Outcome_1” is observed, “Cuisine1” and Cuisine2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which cuisines are valid or related.

2. Explain the cuisines and techniques in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a specific type of cuisine based on dish descriptions and culinary analysis. Each round, you'll be presented with a list of possible cuisines and available exploration techniques. You need to systematically rule out cuisines that do not match the observed outcomes until only one plausible cuisine remains. Your objective is to identify the cuisine accurately in the fewest steps.

How to Play:

(1) View the list of possible cuisines and available exploration techniques.

(2) Choose one exploration technique from the list to apply.

(3) Use the outcomes to eliminate cuisines that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the cuisine.

This is the initial state of the game:

Cuisines: {self.env.truth_space}

Exploration Techniques: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a culinary analysis guidebook to introduce the cuisines and exploration techniques:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt