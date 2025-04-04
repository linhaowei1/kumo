import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.astronomy_data import Truths, Actions, Outcomes

@registry.register_environment("AstronomyEnv")
class AstronomyEnv(BaseEnv):
    
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
Please write an astronomy guidebook that introduces the following astronomical objects and observations in natural language according to the following information.

Astronomical objects: {truths}

Observations: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the astronomical objects that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Observation1" is:
    
    "Observation1":
    {
        "states": {
            "Outcome_1": ["Object1", "Object2"],
            "Outcome_2": ["Object3", "Object4"]
        }
    }
        
    This means:
    - When “Observation1” is performed and “Outcome_1” is observed, “Object1” and "Object2" are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which objects are valid or related.

2. Explain the astronomical objects and observations in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify an astronomical object based on observational data. Each round, you'll be presented with a list of possible astronomical objects and available observations. You need to systematically rule out astronomical objects that do not match the observed outcomes until only one plausible object remains. Your objective is to identify the object accurately in the fewest steps.

How to Play:

(1) View the list of possible astronomical objects and available observations.

(2) Choose one observation from the list to perform.

(3) Use the outcomes to eliminate astronomical objects that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the object.

This is the initial state of the game:

Astronomical Objects: {self.env.truth_space}

Observations: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is an astronomy guidebook to introduce the astronomical objects and observations:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt