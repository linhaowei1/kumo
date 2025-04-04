import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.programming_data import Truths, Actions, Outcomes

@registry.register_environment("AlgorithmEnv")
class AlgorithmEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Algorithms
        self.all_actions = Actions    # Benchmarks / analyses / simulations
        self.ta_mapping = Outcomes    # Exclusions based on outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please create a programming analysis guidebook that introduces the following algorithms and experiments based on the information given below.

Algorithms: {truths}

Experiments: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the algorithms that must be **excluded or ruled out** when the corresponding analysis outcome is observed.

For example,

    If the outcome of "Test1" is:
    
    "Test1":
    {
        "outcomes": {
            "Outcome_1": ["Algorithm1", "Algorithm2"],
            "Outcome_2": ["Algorithm3", "Algorithm4"]
        }
    }
        
    This means:
    - When “Test1” is performed and “Outcome_1” is observed, “Algorithm1” and Algorithm2 are ruled out (i.e., they are not suitable for the problem).
	- Follow this exclusion method instead of signaling which algorithms are appropriate.

2. Describe the algorithms and tests clearly to provide context and clarify relationships.

3. Communicate all relevant exclusion rules coherently and completely.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This analytical task challenges you to identify which algorithm is best suited for a given problem based on test results. Each session, you'll be provided with a list of potential algorithms and available tests. You must systematically exclude algorithms that do not match the observed outcomes until only the most suitable algorithm remains. Your goal is to make the most accurate selection in the fewest steps.

How to Proceed:

(1) Examine the list of potential algorithms and available tests.

(2) Choose one test from the list to execute.

(3) Use the results to exclude algorithms that don't align with the observed outcomes.

(4) Repeat steps 2 and 3 until the algorithm can be confidently identified.

This is the initial state of the task:

Algorithms: {self.env.truth_space}

Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a programming analysis guidebook to introduce the algorithms and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt