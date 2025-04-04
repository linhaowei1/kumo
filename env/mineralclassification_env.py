import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.mineralclassification_data import Truths, Actions, Outcomes

@registry.register_environment("MineralClassificationEnv")
class MineralClassificationEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths =Truths  # Replacing with domain-specific truths
        self.all_actions = Actions
        self.ta_mapping = Outcomes  # Assuming Outcomes is structured properly for minerals, adjust as needed.
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a mineral classification guidebook that introduces the following mineral types and experiments in natural language according to the following information.

Mineral Types: {truths}

Experiments: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the mineral types that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Hardness test" is:
    
    "Hardness test":
    {
        "states": {
            "Outcome_1": ["MineralType1", "MineralType2"],
            "Outcome_2": ["MineralType3", "MineralType4"]
        }
    }
        
    This means:
    - When “Hardness test” is performed and “Outcome_1” is observed, “MineralType1” and MineralType2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which minerals are valid or related.

2. Explain the mineral types and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a mineral based on test outcomes. Each round, you'll be presented with a list of possible mineral types and available tests. You need to systematically rule out mineral types that do not match the observed outcomes until only one plausible mineral type remains. Your objective is to identify the mineral type accurately in the fewest steps.

How to Play:

(1) View the list of possible mineral types and available tests.

(2) Choose one test from the list to perform.

(3) Use the outcomes to eliminate mineral types that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the mineral type.

This is the initial state of the game:

Mineral Types: {self.env.truth_space}

Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a mineral analysis guidebook to introduce the mineral types and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt