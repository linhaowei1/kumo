import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.inventor_data import Truths, Actions, Outcomes

@registry.register_environment("InventorEnv")
class InventorEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths  # Inventors
        self.all_actions = Actions  # Archival research, patent searches, interviews
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a guidebook on identifying the true inventor of a certain prototype. Use natural language to cover the following information.

Inventors: {truths}

Research Actions: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the inventors that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Interview1" is:
    
    "Interview1":
    {
        "states": {
            "Outcome_1": ["InventorA", "InventorB"],
            "Outcome_2": ["InventorC", "InventorD"]
        }
    }
        
    This means:
    - When “Interview1” is conducted and “Outcome_1” is observed, “InventorA” and InventorB are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which inventors are valid or related.

2. Explain the inventors and research processes in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the true inventor of a prototype based on research outcomes. Each round, you'll be presented with a list of possible inventors and available research methods. You need to systematically rule out inventors that do not match the observed outcomes until only one plausible inventor remains. Your objective is to identify the inventor accurately in the fewest steps.

How to Play:

(1) View the list of possible inventors and available research methods.

(2) Choose one research method from the list to perform.

(3) Use the outcomes to eliminate inventors that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the inventor.

This is the initial state of the game:

Inventors: {self.env.truth_space}

Research Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a guidebook to introduce the inventors and research methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt