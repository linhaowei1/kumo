import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.geological_data import Truths, Actions, Outcomes

@registry.register_environment("GeologicalEnv")
class GeologicalEnv(BaseEnv):
    
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
Please write a geological analysis guidebook that introduces the following geological formations and experiments in natural language according to the following information.

Geological formations: {truths}

Mineralogical analysis / geological mapping: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the geological formations that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Experiment1" is:
    
    "Experiment1":
    {
        "states": {
            "Outcome_1": ["Formation1", "Formation2"],
            "Outcome_2": ["Formation3", "Formation4"]
        }
    }
        
    This means:
    - When “Experiment1” is performed and “Outcome_1” is observed, “Formation1” and Formation2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which formations are valid or related.

2. Explain the geological formations and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rules should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a geological formation based on test outcomes. Each round, you'll be presented with a list of possible geological formations and available mineralogical analyses / geological mappings. You need to systematically rule out geological formations that do not match the observed outcomes until only one plausible formation remains. Your objective is to identify the formation accurately in the fewest steps.

How to Play:

(1) View the list of possible geological formations and available mineralogical analyses / geological mappings.

(2) Choose one experiment from the list to perform.

(3) Use the outcomes to eliminate geological formations that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the formation.

This is the initial state of the game:

Geological Formations: {self.env.truth_space}

Mineralogical Analyses / Geological Mappings: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a geological analysis guidebook to introduce the geological formations and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt