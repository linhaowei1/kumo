import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.musicgenres_data import Truths, Actions, Outcomes

@registry.register_environment("MusicGenresEnv")
class MusicGenresEnv(BaseEnv):
    
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
Please write a musical genre identification guide that introduces the following musical elements and analysis methods in natural language according to the following information.

Musical Genres: {truths}

Analysis Methods: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the musical genres that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "RhythmAndTempoAnalysis" is:
    
    "RhythmAndTempoAnalysis":
    {
        "states": {
            "Outcome_1": ["Genre1", "Genre2"],
            "Outcome_2": ["Genre3", "Genre4"]
        }
    }
        
    This means:
    - When “Rhythm and Tempo Analysis” is performed and “Outcome_1” is observed, “Genre1” and Genre2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which genres are valid or related.

2. Explain the musical genres and analysis methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a musical genre based on the song's features. Each round, you'll be presented with a list of possible genres and available analysis methods. You need to systematically rule out genres that do not match the observed outcomes until only one plausible genre remains. Your objective is to identify the genre accurately in the fewest steps.

How to Play:

(1) View the list of possible musical genres and available analysis methods.

(2) Choose one analysis method from the list to employ.

(3) Use the outcomes to eliminate musical genres that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the genre.

This is the initial state of the game:

Musical Genres: {self.env.truth_space}

Analysis Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a musical genre identification guide to introduce the musical genres and analysis methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt