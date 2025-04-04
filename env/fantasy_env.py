import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.fantasy_data import *

@registry.register_environment("FantasyEnv")
class FantasyEnv(BaseEnv):
    
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
Please write a fantasy artifacts analysis guidebook that introduces the following fantasy artifacts and tests in natural language according to the following information.

Fantasy artifacts: {truths}

Tests: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the fantasy artifacts that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Test1" is:
    
    "Test1":
    {
        "states": {
            "Outcome_1": ["FantasyArtifact1", "FantasyArtifact2"],
            "Outcome_2": ["FantasyArtifact3", "FantasyArtifact4"]
        }
    }
        
    This means:
    - When “Test1” is performed and “Outcome_1” is observed, “FantasyArtifact1” and “FantasyArtifact2” are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which artifacts are valid or related.

2. Explain the fantasy artifacts and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rules should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
The goal of the game is to determine the identity of a fantasy artifact based on observed traits and characteristics. Each round, you'll be presented with a list of fantasy artifacts and available tests. You need to systematically rule out fantasy artifacts that do not match the observed outcomes until only one plausible fantasy artifact remains. Your objective is to identify the fantasy artifact accurately in the fewest steps.

How to Play:

(1) View the list of possible fantasy artifacts and available tests.

(2) Choose one test from the list to perform.

(3) Use the outcomes to eliminate fantasy artifacts that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the fantasy artifact.

This is the initial state of the game:

Fantasy artifacts: {self.env.truth_space}

Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a fantasy artifact analysis guidebook to introduce the fantasy artifacts and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt

        
        elif agent_type == 'ReactAgent':
            raise NotImplementedError("ReactAgent is not implemented for the Env yet.")