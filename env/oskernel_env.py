import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.os_kernel_data import Truths, Actions, Outcomes

@registry.register_environment("OSKernelEnv")
class OSKernelEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Operating system kernels
        self.all_actions = Actions    # Benchmarking / compatibility tests
        self.ta_mapping = Outcomes    # Mapping between tests and the kernels they rule out
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write an analysis guidebook that introduces the following operating system kernels and benchmarking/compatibility tests in natural language according to the following information.

Operating System Kernels: {truths}

Benchmarking / Compatibility Tests: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the operating system kernels that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Test1" is:
    
    "Test1":
    {
        "states": {
            "Outcome_1": ["Kernel1", "Kernel2"],
            "Outcome_2": ["Kernel3", "Kernel4"]
        }
    }
        
    This means:
    - When “Test1” is performed and “Outcome_1” is observed, “Kernel1” and "Kernel2" are ruled out.
	- This exclusion approach is applied instead of confirming or indicating which kernels are valid or related.

2. Explain the operating system kernels and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This challenge is to determine which operating system kernel handles a device's drivers best, based on test outcomes. Each round, you'll be presented with a list of possible operating system kernels and available benchmarking/compatibility tests. You need to systematically rule out kernels that do not match the observed outcomes until only one plausible kernel remains. Your objective is to identify the kernel correctly in the fewest steps.

How to Play:

(1) View the list of possible operating system kernels and available tests.

(2) Choose one test from the list to perform.

(3) Use the outcomes to eliminate kernels that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the kernel.

This is the initial state of the game:

Operating System Kernels: {self.env.truth_space}

Benchmarking / Compatibility Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is an analysis guidebook to introduce the operating system kernels and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt