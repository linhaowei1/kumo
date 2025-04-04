import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.musical_data import Truths, Actions, Outcomes

@registry.register_environment("MusicalEnv")
class MusicalEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths  # Change from "Truths" to "Composers"
        self.all_actions = Actions  # Change from "Actions" to "Analyses"
        self.ta_mapping = Outcomes  # Change from "Outcomes" to "StylisticOutcomes"
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, composers, analyses, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a musical analysis guidebook that introduces the following musical composers and analyses in natural language according to the following information.

Musical composers: {composers}

Musical analyses: {analyses}

Stylistic outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Stylistic outcomes” represent the musical composers that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Analysis1" is:
    
    "Analysis1":
    {
        "states": {
            "Outcome_1": ["Composer1", "Composer2"],
            "Outcome_2": ["Composer3", "Composer4"]
        }
    }
        
    This means:
    - When “Analysis1” is performed and “Outcome_1” is observed, “Composer1” and Composer2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which composers are valid or related.

2. Explain the musical composers and analyses in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a musical composer based on stylistic analyses. Each round, you'll be presented with a list of possible musical composers and available analyses. You need to systematically rule out musical composers that do not match the observed outcomes until only one plausible composer remains. Your objective is to identify the composer accurately in the fewest steps.

How to Play:

(1) View the list of possible musical composers and available analyses.

(2) Choose one analysis from the list to perform.

(3) Use the stylistic outcomes to eliminate composers that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the composer.

This is the initial state of the game:

Musical Composers: {self.env.truth_space}

Analyses: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a musical analysis guidebook to introduce the composers and analyses:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt