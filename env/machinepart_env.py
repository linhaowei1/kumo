import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.machinepart_data import Truths, Actions, Outcomes

@registry.register_environment("MachinePartEnv")
class MachinePartEnv(BaseEnv):
    
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
Please write a diagnostic analysis guidebook that describes the following machine parts and diagnostic tests in natural language according to the following information.

Machine parts: {truths}

Diagnostic tests: {actions}

Test outcomes and rulings: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Test outcomes and rulings” represent the machine parts that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Vibration Analysis" is:
    
    "Vibration Analysis":
    {
        "states": {
            "Outcome_1": ["Part1", "Part2"],
            "Outcome_2": ["Part3", "Part4"]
        }
    }
        
    This means:
    - When “Vibration Analysis” is performed and “Outcome_1” is observed, “Part1” and "Part2" are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which parts are valid or related.

2. Explain the machine parts and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This diagnostic challenge asks you to identify a failing machine part based on test outcomes. Each round, you'll be presented with a list of possible machine parts and available diagnostic tests. You need to systematically rule out machine parts that do not match the observed outcomes until only one plausible part remains. Your objective is to identify the failing part accurately in the fewest steps.

How to Diagnose:

(1) View the list of possible machine parts and available diagnostic tests.

(2) Choose one diagnostic test from the list to perform.

(3) Use the outcomes to eliminate machine parts that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the failing part.

This is the initial state of the challenge:

Machine Parts: {self.env.truth_space}

Diagnostic Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a diagnostic analysis guidebook to describe the machine parts and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt