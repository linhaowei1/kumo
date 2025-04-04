import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.energy_data import Truths, Actions, Outcomes

@registry.register_environment("EnergyEnv")
class EnergyEnv(BaseEnv):
    
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
Please write an energy source analysis guidebook that introduces the following energy sources and diagnostic tests in natural language according to the following information.

Energy sources: {truths}

Diagnostic tests: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the energy sources that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Test1" is:
    
    "Test1":
    {
        "states": {
            "Outcome_1": ["Source1", "Source2"],
            "Outcome_2": ["Source3", "Source4"]
        }
    }
        
    This means:
    - When “Test1” is performed and “Outcome_1” is observed, “Source1” and Source2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which sources are valid or related.

2. Explain the energy sources and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify an energy source that powers a hidden device based on test outcomes. Each round, you'll be presented with a list of possible energy sources and available diagnostic tests. You need to systematically rule out energy sources that do not match the observed outcomes until only one plausible source remains. Your objective is to identify the source accurately in the fewest steps.

How to Play:

(1) View the list of possible energy sources and available diagnostic tests.

(2) Choose one test from the list to perform.

(3) Use the outcomes to eliminate energy sources that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the source.

This is the initial state of the game:

Energy Sources: {self.env.truth_space}

Diagnostic Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is an energy source analysis guidebook to introduce the energy sources and diagnostic tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt