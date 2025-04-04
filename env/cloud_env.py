import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.cloud_data import Truths, Actions, Outcomes

@registry.register_environment("CloudEnv")
class CloudEnv(BaseEnv):
    
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
Please write a cloud analysis guidebook that introduces the following cloud types and observation methods in natural language according to the following information.

Cloud types: {truths}

Observation methods: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the cloud types that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Method1" is:
    
    "Method1":
    {
        "states": {
            "Outcome_1": ["CloudTypes1", "CloudTypes2"],
            "Outcome_2": ["CloudTypes3", "CloudTypes4"]
        }
    }
        
    This means:
    - When “Method1” is performed and “Outcome_1” is observed, “CloudTypes1” and CloudTypes2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which cloud types are valid or related.

2. Explain the cloud types and observation methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a cloud type based on observation outcomes. Each round, you'll be presented with a list of possible cloud types and available observation methods. You need to systematically rule out cloud types that do not match the observed outcomes until only one plausible cloud type remains. Your objective is to identify the cloud type accurately in the fewest steps.

How to Play:

(1) View the list of possible cloud types and available observation methods.

(2) Choose one observation method from the list to perform.

(3) Use the outcomes to eliminate cloud types that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the cloud type.

This is the initial state of the game:

Cloud Types: {self.env.truth_space}

Observation Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a cloud analysis guidebook to introduce the cloud types and observation methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt