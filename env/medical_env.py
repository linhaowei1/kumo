import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.medical_data import *

@registry.register_environment("MedicalEnv")
class MedicalEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Diseases      
        self.all_actions = Diagnosis   
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a medical analysis guidebook that introduces the following diseases and diagnostic tests in natural language according to the following information.

Diseases: {truths}

Diagnosis: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the diseases that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Test1" is:
    
    "Test1":
    {
        "states": {
            "Outcome_1": ["Disease1", "Disease2"],
            "Outcome_2": ["Disease3", "Disease4"]
        }
    }
        
    This means:
    - When "Test1" is performed and "Outcome_1" is observed, "Disease1" and "Disease2" are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which artifacts are valid or related.

2. Explain the diseases and diagnostic tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rules should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a disease based on diagnostic results. Each round, you'll see possible diseases and available diagnostic tests. You need to rule out diseases that don't fit the observed outcomes until only one plausible disease remains. Your objective is to accurately identify the only one disease in the fewest actions.

How to Play:

(1) View the list of possible diseases and available diagnostic tests.

(2) Select one diagnostic test per round to see its outcome.

(3) Use the outcomes to eliminate diseases that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the disease.

This is the initial state of the game:

Disease: {self.env.truth_space}

Diagnostic Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a medical diagnosis guidebook to introduce the diseases and diagnostic tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
                
            return system_prompt

    
