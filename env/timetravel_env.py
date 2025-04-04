import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.time_travel_data import Truths, Actions, Outcomes

@registry.register_environment("TimeTravelEnv")
class TimeTravelEnv(BaseEnv):
    
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
Please write a temporal analysis guidebook that introduces the following types of time travel paradoxes and temporal experiments in natural language according to the following information.

Types of time travel paradoxes: {truths}

Experiments: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the time travel paradoxes that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "TemporalExperiment1" is:
    
    "TemporalExperiment1":
    {
        "states": {
            "Outcome_1": ["Paradox1", "Paradox2"],
            "Outcome_2": ["Paradox3", "Paradox4"]
        }
    }
        
    This means:
    - When “TemporalExperiment1” is performed and “Outcome_1” is observed, “Paradox1” and Paradox_2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which paradoxes are valid or related.

2. Explain the time travel paradoxes and experiments in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to resolve a timeline paradox based on experimental outcomes. Each round, you'll be presented with a list of possible paradoxes and available temporal experiments. You need to systematically rule out paradoxes that do not match the observed outcomes until only one plausible paradox remains. Your objective is to resolve the paradox accurately in the fewest steps.

How to Play:

(1) View the list of possible paradoxes and available temporal experiments.

(2) Choose one experiment from the list to perform.

(3) Use the outcomes to eliminate paradoxes that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently resolve the paradox.

This is the initial state of the game:

Types of Time Travel Paradoxes: {self.env.truth_space}

Temporal Experiments: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a temporal analysis guidebook to introduce the paradoxes and experiments:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt