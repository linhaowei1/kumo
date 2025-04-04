import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.archaeological_data import Truths, Actions, Outcomes

@registry.register_environment("ArchaeologicalEnv")
class ArchaeologicalEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths       # Historical periods/eras
        self.all_actions = Actions     # Radiocarbon dating, stratigraphic analysis
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write an archaeological analysis guidebook that introduces the following historical periods and analysis methods in natural language according to the following information.

Historical periods: {truths}

Analysis methods: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the historical periods that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Radiocarbon Dating" is:
    
    "Radiocarbon Dating":
    {
        "states": {
            "Outcome_1": ["Period1", "Period2"],
            "Outcome_2": ["Period3", "Period4"]
        }
    }
        
    This means:
    - When "Radiocarbon Dating" is performed and “Outcome_1” is observed, “Period1” and “Period2” are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which periods are valid or related.

2. Explain the historical periods and methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the correct historical period of a discovered artifact based on analysis outcomes. Each round, you'll be presented with a list of possible historical periods and available analysis methods. You need to systematically rule out periods that do not match the observed outcomes until only one plausible period remains. Your objective is to identify the period accurately in the fewest steps.

How to Play:

(1) View the list of possible historical periods and available analysis methods.

(2) Choose one analysis method from the list to perform.

(3) Use the outcomes to eliminate periods that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the period.

This is the initial state of the game:

Historical Periods: {self.env.truth_space}

Analysis Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is an archaeological analysis guidebook to introduce the historical periods and methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt