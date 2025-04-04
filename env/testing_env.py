import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.testing_env_data import Truths, Actions, Outcomes

@registry.register_environment("TestingEnv")
class TestingEnv(BaseEnv):
    
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
Please develop a guide for identifying software testing types, focusing specifically on verifying system performance under load, using natural language based on the following details.

Testing Types: {truths}

Analyses: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the testing types that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Load Testing Analysis" is:
    
    "Load Testing Analysis":
    {
        "states": {
            "Outcome_1": ["Type1", "Type2"],
            "Outcome_2": ["Type3", "Type4"]
        }
    }
        
    This means:
    - When “Load Testing Analysis” is performed and “Outcome_1” is observed, “Type1” and Type2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which types are valid or related.

2. Explain the testing types and analyses in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rules should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a software testing type based on analysis outcomes on system performance under load. Each round, you'll be presented with a list of possible testing types and available analyses. You need to systematically rule out testing types that do not match the observed outcomes until only one plausible type remains. Your objective is to identify the correct testing type accurately in the fewest steps.

How to Play:

(1) View the list of possible testing types and available analyses.

(2) Choose one analysis from the list to perform.

(3) Use the outcomes to eliminate testing types that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the testing type.

This is the initial state of the game:

Testing Types: {self.env.truth_space}

Analyses: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a guide for identifying software testing types and analyses based on system performance:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt