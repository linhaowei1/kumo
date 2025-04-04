import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.literary_data import Truths, Actions, Outcomes

@registry.register_environment("LiteraryEnv")
class LiteraryEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Authors
        self.all_actions = Actions    # Literary style analysis / handwriting and ink tests
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a literary analysis guidebook that introduces the following literary assessments and experiments in natural language according to the following information.

Authors: {truths}

Analysis Methods: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the authors that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Analysis1" is:
    
    "Analysis1":
    {
        "states": {
            "Outcome_1": ["Author1", "Author2"],
            "Outcome_2": ["Author3", "Author4"]
        }
    }
        
    This means:
    - When “Analysis1” is performed and “Outcome_1” is observed, “Author1” and Author2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which authors are valid or related.

2. Explain the authors and analysis techniques in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the author of a newly discovered poem based on literary assessment outcomes. Each round, you'll be presented with a list of possible authors and available analysis methods. You need to systematically rule out authors that do not match the observed outcomes until only one plausible author remains. Your objective is to identify the author accurately in the fewest steps.

How to Play:

(1) View the list of possible authors and available analysis methods.

(2) Choose one analysis method from the list to perform.

(3) Use the outcomes to eliminate authors that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the author.

This is the initial state of the game:

Authors: {self.env.truth_space}

Analysis Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a literary analysis guidebook to introduce the authors and analysis methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt