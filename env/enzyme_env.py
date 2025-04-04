import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.enzyme_data import Truths, Actions, Outcomes

@registry.register_environment("EnzymeEnv")
class EnzymeEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths       # Domain-specific truths
        self.all_actions = Actions  # Domain-specific actions
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a biochemical analysis guidebook that introduces the following enzymes and enzyme assays in natural language according to the following information.

Enzymes: {truths}

Enzyme assays / kinetic studies: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the enzymes that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Experiment1" is:
    
    "Experiment1":
    {
        "states": {
            "Outcome_1": ["Enzyme1", "Enzyme2"],
            "Outcome_2": ["Enzyme3", "Enzyme4"]
        }
    }
        
    This means:
    - When an enzyme assay is performed and “Outcome_1” is observed, “Enzyme1” and Enzyme2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which enzymes are valid or related.

2. Explain the enzymes and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the enzyme that catalyzes a biochemical reaction based on assay outcomes. Each round, you'll be presented with a list of possible enzymes and available assays. You need to systematically rule out enzymes that do not match the observed outcomes until only one plausible enzyme remains. Your objective is to identify the enzyme accurately in the fewest steps.

How to Play:

(1) View the list of possible enzymes and available assays.

(2) Choose one assay from the list to perform.

(3) Use the outcomes to eliminate enzymes that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the enzyme.

This is the initial state of the game:

Enzymes: {self.env.truth_space}

Enzyme assays / kinetic studies: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a biochemical analysis guidebook to introduce the enzymes and assays:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt