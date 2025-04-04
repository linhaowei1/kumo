import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.philosophy_data import Truths, Actions, Outcomes

@registry.register_environment("PhilosophyEnv")
class PhilosophyEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Philosophical arguments
        self.all_actions = Actions    # Argument structure analysis / cross-checking philosophical texts
        self.ta_mapping = Outcomes    # Map between actions and outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a philosophical analysis guidebook that introduces the following philosophical arguments and assessment methods according to the information provided.

Philosophical arguments: {truths}

Argument assessment methods: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the philosophical arguments that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Assessment1" is:
    
    "Assessment1":
    {
        "states": {
            "Outcome_1": ["Argument1", "Argument2"],
            "Outcome_2": ["Argument3", "Argument4"]
        }
    }
        
    This means:
    - When “Assessment1” is performed and “Outcome_1” is observed, “Argument1” and “Argument2” are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which arguments are valid or related.

2. Explain the philosophical arguments and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify which philosopher's argument a debate club is referencing based on evaluation outcomes. Each round, you'll be presented with a list of potential philosophical arguments and available assessment methods. You need to systematically rule out arguments that do not match the observed outcomes until only one plausible argument remains. Your objective is to identify the argument accurately in the fewest steps.

How to Play:

(1) View the list of potential philosophical arguments and available assessment methods.

(2) Choose one method from the list to perform.

(3) Use the outcomes to eliminate arguments that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the argument.

This is the initial state of the game:

Philosophical Arguments: {self.env.truth_space}

Assessment Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a philosophical analysis guidebook to introduce the arguments and assessment methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt