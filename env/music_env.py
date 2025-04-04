import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.music_data import *

@registry.register_environment("MusicEnv")
class MusicEnv(BaseEnv):
    
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
Please write a Music Genre analysis guidebook that introduces the following Music Genres and analysis in natural language according to the following information.

Music Genres: {truths}

Analyses: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the music genres that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Analysis1" is:
    
    "Analysis1":
    {
        "states": {
            "Outcome_1": ["Genres1", "Genres2"],
            "Outcome_2": ["Genres3", "Genres4"]
        }
    }
        
    This means:
    - When "Analysis1" is performed and "Outcome_1" is observed, "Genres1" and "Genres2" are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which genres are valid or related.

2. Explain the music genres and analyses in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rules should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
The goal of the game is to determine the identity of a music genre based on observed traits and characteristics. Each round, you'll be presented with a list of music genres and available analyses. You need to systematically rule out music genres that do not match the observed outcomes until only one plausible music genre remains. Your objective is to identify the music genre accurately in the fewest steps.

How to Play:

(1) View the list of possible music genres and available analyses.

(2) Choose one analysis from the list to perform.

(3) Use the outcomes to eliminate music genres that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the music genre.

This is the initial state of the game:

Music genres: {self.env.truth_space}

Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a music genre analysis guidebook to introduce the music genres and analyses:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}\n\n"
            return system_prompt

        
        elif agent_type == 'ReactAgent':
            raise NotImplementedError("ReactAgent is not implemented for the Env yet.")