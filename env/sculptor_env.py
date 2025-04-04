import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.sculptor_data import Truths, Actions, Outcomes

@registry.register_environment("SculptorEnv")
class SculptorEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      #
        self.all_actions = Actions    #
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write an art evaluation guidebook that introduces the following sculptors and analysis techniques in natural language according to the following information.

Sculptors: {truths}

Analysis Techniques: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the sculptors that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Chisel mark analysis" is:
    
    "Chisel mark analysis":
    {
        "states": {
            "Outcome_1": ["Sculptor1", "Sculptor2"],
            "Outcome_2": ["Sculptor3", "Sculptor4"]
        }
    }
        
    This means:
    - When “Chisel mark analysis” is performed and “Outcome_1” is observed, “Sculptor1” and Sculptor2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which sculptors are valid or related.

2. Explain the sculptors and analysis techniques in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify which sculptor carved a particular statue based on analysis outcomes. Each round, you'll be presented with a list of possible sculptors and available analysis techniques. You need to systematically rule out sculptors whose styles do not match the observed outcomes until only one plausible sculptor remains. Your objective is to identify the sculptor accurately in the fewest steps.

How to Play:

(1) View the list of possible sculptors and available analysis techniques.

(2) Choose one analysis technique from the list to perform.

(3) Use the outcomes to eliminate sculptors that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the sculptor.

This is the initial state of the game:

Sculptors: {self.env.truth_space}

Analysis Techniques: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is an art evaluation guidebook to introduce the sculptors and analysis techniques:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt