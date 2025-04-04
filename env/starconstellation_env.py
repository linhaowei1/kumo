import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.constellation_data import Truths, Actions, Outcomes

@registry.register_environment("StarConstellationEnv")
class StarConstellationEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Constellations
        self.all_actions = Actions    # Stellar coordinate measurements / star pattern recognition / brightness comparisons
        self.ta_mapping = Outcomes    # Rules related to observations and exclusions
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a star observation guidebook that introduces the following constellations and observational techniques in natural language according to the following information.

Constellations: {truths}

Observational Techniques: {actions}

Exclusions based on Observations: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Exclusions based on Observations” represent the constellations that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "StarPatternRecognition1" is:
    
    "StarPatternRecognition1":
    {
        "states": {
            "Outcome_1": ["Constellation1", "Constellation2"],
            "Outcome_2": ["Constellation3", "Constellation4"]
        }
    }
        
    This means:
    - When "StarPatternRecognition1" is performed and "Outcome_1" is observed, "Constellation1" and "Constellation2" are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which constellations are visible or relevant.

2. Explain the constellations and observation techniques in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant exclusion information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a star constellation based on observational outcomes. Each round, you'll be presented with a list of possible constellations and available observational techniques. You need to systematically rule out constellations that do not match the observed outcomes until only one plausible constellation remains. Your objective is to identify the constellation accurately in the fewest steps.

How to Play:

(1) View the list of possible constellations and available observational techniques.

(2) Choose one technique from the list to perform.

(3) Use the outcomes to eliminate constellations that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the constellation.

This is the initial state of the game:

Constellations: {self.env.truth_space}

Observational Techniques: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a star observation guidebook to introduce the constellations and observational techniques:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt