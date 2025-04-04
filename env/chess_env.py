import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.chess_data import Truths, Actions, Outcomes

@registry.register_environment("ChessEnv")
class ChessEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Chess openings
        self.all_actions = Actions    # Move sequences
        self.ta_mapping = Outcomes    # Outcomes based on move sequences
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a chess opening guidebook that details the following openings and strategies in natural language according to the following information.

Chess Openings: {truths}

Move Sequences: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the chess openings that must be **excluded or ruled out** when the corresponding move sequence is observed.

For example,

    If the state of "Move Sequence 1" is:
    
    "Move Sequence 1":
    {
        "states": {
            "Outcome_1": ["Opening1", "Opening2"],
            "Outcome_2": ["Opening3", "Opening4"]
        }
    }
        
    This means:
    - When “Move Sequence 1” is performed and “Outcome_1” is observed, “Opening1” and Opening2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which openings are valid or related.

2. Explain the chess openings and strategies in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a chess opening from a recorded game based on move sequences. Each round, you'll be presented with a list of possible chess openings and available move sequences. You need to systematically rule out openings that do not match the observed move sequence outcomes until only one plausible opening remains. Your objective is to identify the opening accurately in the fewest steps.

How to Play:

(1) View the list of possible chess openings and available move sequences.

(2) Choose one move sequence from the list to perform.

(3) Use the outcomes to eliminate chess openings that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the opening.

This is the initial state of the game:

Chess Openings: {self.env.truth_space}

Move Sequences: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a chess opening guidebook to introduce the chess openings and strategies:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt