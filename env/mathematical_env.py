import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.mathematical_data import Truths, Actions, Outcomes

@registry.register_environment("MathematicalEnv")
class MathematicalEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Mathematical theorems
        self.all_actions = Actions    # Logical deduction / theorem-matching checks
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a mathematical guidebook that introduces the following theorems and deduction methods in natural language according to the following information.

Mathematical Theorems: {truths}

Logical Deductions / Theorem-Matching Checks: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the theorems that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Deduction1" is:
    
    "Deduction1":
    {
        "states": {
            "Outcome_1": ["Theorem1", "Theorem2"],
            "Outcome_2": ["Theorem3", "Theorem4"]
        }
    }
        
    This means:
    - When “Deduction1” is performed and “Outcome_1” is observed, “Theorem1” and Theorem2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which theorems are valid or related.

2. Explain the mathematical theorems and deduction checks in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the correct mathematical theorem applied in a proof based on deduction outcomes. Each round, you'll be presented with a list of possible theorems and available logical deduction checks. You need to systematically rule out theorems that do not match the observed outcomes until only one plausible theorem remains. Your objective is to identify the theorem accurately in the fewest steps.

How to Play:

(1) View the list of possible theorems and available logical deduction checks.

(2) Choose one deduction check from the list to perform.

(3) Use the outcomes to eliminate theorems that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the theorem.

This is the initial state of the game:

Mathematical Theorems: {self.env.truth_space}

Logical Deductions / Theorem-Matching Checks: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a mathematical guidebook to introduce the theorems and deductions:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt