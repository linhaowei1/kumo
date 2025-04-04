import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.beverage_data import Truths, Actions, Outcomes

@registry.register_environment("BeverageEnv")
class BeverageEnv(BaseEnv):
    
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
Please write a fermentation analysis guidebook that introduces the following fermentation processes and byproduct/microbial strain tests in natural language according to the following information.

Fermentation processes: {truths}

Byproduct/Microbial strain tests: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the fermentation processes that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Test1" is:
    
    "Test1":
    {
        "states": {
            "Outcome_1": ["Process1", "Process2"],
            "Outcome_2": ["Process3", "Process4"]
        }
    }
        
    This means:
    - When “Test1” is performed and “Outcome_1” is observed, “Process1” and Process2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which processes are valid or related.

2. Explain the fermentation processes and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the fermentation process of a beverage based on test outcomes. Each round, you'll be presented with a list of possible fermentation processes and available tests. You need to systematically rule out fermentation processes that do not match the observed outcomes until only one plausible process remains. Your objective is to identify the process accurately in the fewest steps.

How to Play:

(1) View the list of possible fermentation processes and available tests.

(2) Choose one test from the list to perform.

(3) Use the outcomes to eliminate fermentation processes that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the process.

This is the initial state of the game:

Fermentation Processes: {self.env.truth_space}

Byproduct/Microbial Strain Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a fermentation analysis guidebook to introduce the fermentation processes and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt