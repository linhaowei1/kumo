import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.computation_data import Truths, Actions, Outcomes

@registry.register_environment("ComputationEnv")
class ComputationEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Data structures
        self.all_actions = Actions    # Algorithmic complexity tests / performance benchmarks
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a computational analysis guidebook that introduces the following data structures and performance benchmarks in natural language according to the following information.

Data Structures: {truths}

Algorithmic Complexity Tests: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the data structures that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Benchmark1" is:
    
    "Benchmark1":
    {
        "states": {
            "Outcome_1": ["DataStructures1", "DataStructures2"],
            "Outcome_2": ["DataStructures3", "DataStructures4"]
        }
    }
        
    This means:
    - When “Benchmark1” is performed and “Outcome_1” is observed, “DataStructures1” and DataStructures2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which data structures are valid or related.

2. Explain the data structures and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rules should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the optimal data structure based on performance benchmarks. Each round, you'll be presented with a list of possible data structures and available complexity tests. You need to systematically rule out data structures that do not match the observed performance outcomes until only one plausible structure remains. Your objective is to identify the data structure accurately in the fewest steps.

How to Play:

(1) View the list of possible data structures and available complexity tests.

(2) Choose one benchmark from the list to perform.

(3) Use the outcomes to eliminate data structures that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the data structure.

This is the initial state of the game:

Data Structures: {self.env.truth_space}

Complexity Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a computational analysis guidebook to introduce the data structures and complexity tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt