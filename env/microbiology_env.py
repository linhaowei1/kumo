import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.microbiology_data import Truths, Actions, Outcomes

@registry.register_environment("MicrobiologyEnv")
class MicrobiologyEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Microorganisms (bacteria, yeasts)
        self.all_actions = Actions    # Microbiological culturing / microscopy
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a microbiological analysis guidebook that introduces the following microorganisms and experiments in natural language according to the following information.

Microorganisms: {truths}

Experiments: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the microorganisms that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Experiment1" is:
    
    "Experiment1":
    {
        "states": {
            "Outcome_1": ["Microorganism1", "Microorganism2"],
            "Outcome_2": ["Microorganism3", "Microorganism4"]
        }
    }
        
    This means:
    - When “Experiment1” is performed and “Outcome_1” is observed, "Microorganism1" and "Microorganism2" are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which microorganisms are valid.

2. Explain the microorganisms and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the correct microorganism causing a fermentation issue based on test outcomes. Each round, you'll be presented with a list of possible microorganisms and available experiments. You need to systematically rule out microorganisms that do not match the observed outcomes until only one plausible microorganism remains. Your objective is to identify the microorganism accurately in the fewest steps.

How to Play:

(1) View the list of possible microorganisms and available experiments.

(2) Choose one experiment from the list to perform.

(3) Use the outcomes to eliminate microorganisms that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the microorganism.

This is the initial state of the game:

Microorganisms: {self.env.truth_space}

Experiments: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a microbiological analysis guidebook to introduce the microorganisms and experiments:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt