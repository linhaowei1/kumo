import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.software_data import Truths, Actions, Outcomes

@registry.register_environment("SoftwareEnv")
class SoftwareEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Coding paradigms
        self.all_actions = Actions    # Code pattern analysis / architecture examination
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a software development analysis guidebook that introduces the following coding paradigms and analysis techniques in natural language according to the following information.

Coding paradigms: {truths}

Analysis techniques: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the coding paradigms that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Analysis1" is:
    
    "Analysis1":
    {
        "states": {
            "Outcome_1": ["Paradigm1", "Paradigm2"],
            "Outcome_2": ["Paradigm3", "Paradigm4"]
        }
    }
        
    This means:
    - When “Analysis1” is performed and “Outcome_1” is observed, “Paradigm1” and Paradigm2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which paradigms are valid or related.

2. Explain the coding paradigms and analysis techniques in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a coding paradigm a software library follows based on code analysis outcomes. Each round, you'll be presented with a list of possible coding paradigms and available analysis techniques. You need to systematically rule out coding paradigms that do not match the observed outcomes until only one plausible paradigm remains. Your objective is to identify the paradigm accurately in the fewest steps.

How to Play:

(1) View the list of possible coding paradigms and available analysis techniques.

(2) Choose one analysis technique from the list to perform.

(3) Use the outcomes to eliminate coding paradigms that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the paradigm.

This is the initial state of the game:

Coding Paradigms: {self.env.truth_space}

Analysis Techniques: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a software development analysis guidebook to introduce the coding paradigms and techniques:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt