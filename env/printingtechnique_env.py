import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.printing_technique_data import Truths, Actions, Outcomes  # Updated import

@registry.register_environment("PrintingTechniqueEnv")  # Updated registry and class name
class PrintingTechniqueEnv(BaseEnv):

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
Please write an analysis guidebook that introduces the following printing techniques and examinations in natural language according to the following information.

Printing techniques: {truths}

Examinations: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the printing techniques that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Examination1" is:
    
    "Examination1":
    {
        "states": {
            "Outcome_1": ["Techniques1", "Techniques2"],
            "Outcome_2": ["Techniques3", "Techniques4"]
        }
    }
        
    This means:
    - When “Examination1” is performed and “Outcome_1” is observed, “Techniques1” and Techniques2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which techniques are valid or related.

2. Explain the printing techniques and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a printing technique based on examination outcomes. Each round, you'll be presented with a list of possible printing techniques and available examinations. You need to systematically rule out printing techniques that do not match the observed outcomes until only one plausible technique remains. Your objective is to identify the technique accurately in the fewest steps.

How to Play:

(1) View the list of possible printing techniques and available examinations.

(2) Choose one examination from the list to perform.

(3) Use the outcomes to eliminate printing techniques that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the technique.

This is the initial state of the game:

Printing Techniques: {self.env.truth_space}

Examinations: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is an analysis guidebook to introduce the printing techniques and examinations:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt