import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.pharmaceutical_data import Truths, Actions, Outcomes

@registry.register_environment("PharmaceuticalEnv")
class PharmaceuticalEnv(BaseEnv):
    
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
Please write a pharmaceutical analysis guidebook that introduces the following pharmaceutical compounds and clinical trials in natural language according to the following information.

Pharmaceutical compounds: {truths}

Clinical trials / Bioassays: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the pharmaceutical compounds that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Trial1" is:
    
    "Trial1":
    {
        "states": {
            "Outcome_1": ["Compound1", "Compound2"],
            "Outcome_2": ["Compound3", "Compound4"]
        }
    }
        
    This means:
    - When “Trial1” is performed and “Outcome_1” is observed, “Compound1” and "Compound2" are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which compounds are valid or related.

2. Explain the pharmaceutical compounds and trials in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rules should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a pharmaceutical compound based on trial outcomes. Each round, you'll be presented with a list of possible pharmaceutical compounds and available clinical trials. You need to systematically rule out pharmaceutical compounds that do not match the observed outcomes until only one plausible compound remains. Your objective is to identify the compound accurately in the fewest steps.

How to Play:

(1) View the list of possible pharmaceutical compounds and available clinical trials.

(2) Choose one trial from the list to perform.

(3) Use the outcomes to eliminate pharmaceutical compounds that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the compound.

This is the initial state of the game:

Pharmaceutical Compounds: {self.env.truth_space}

Clinical Trials / Bioassays: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a pharmaceutical analysis guidebook to introduce the pharmaceutical compounds and clinical trials:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt