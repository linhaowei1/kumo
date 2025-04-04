import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.quantum_data import Truths, Actions, Outcomes

@registry.register_environment("QuantumEnv")
class QuantumEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths
        self.all_actions = Actions
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a quantum analysis guidebook that introduces the following quantum states and experiments in natural language according to the following information.

Quantum states: {truths}

Experiments: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the quantum states that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Experiment1" is:
    
    "Experiment1":
    {
        "states": {
            "Outcome_1": ["States1", "States2"],
            "Outcome_2": ["States3", "States4"]
        }
    }
        
    This means:
    - When “Experiment1” is performed and “Outcome_1” is observed, “States1” and States2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which states are valid or related.

2. Explain the quantum states and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a quantum state affecting the device's performance based on test outcomes. Each round, you'll be presented with a list of possible quantum states and available experiments. You need to systematically rule out quantum states that do not match the observed outcomes until only one plausible state remains. Your objective is to identify the state accurately in the fewest steps.

How to Play:

(1) View the list of possible quantum states and available experiments.

(2) Choose one experiment from the list to perform.

(3) Use the outcomes to eliminate quantum states that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the state.

This is the initial state of the game:

Quantum States: {self.env.truth_space}

Experiments: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a quantum analysis guidebook to introduce the quantum states and experiments:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt