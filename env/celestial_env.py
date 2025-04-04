import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.celestial_data import Truths, Actions, Outcomes

@registry.register_environment("CelestialEnv")
class CelestialEnv(BaseEnv):
    
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
Please write an observational astronomy guidebook that introduces the following celestial events and observational techniques in natural language according to the following information.

Celestial Events: {truths}

Observational Techniques: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the celestial events that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Observational Technique1" is:
    
    "Observational Technique1":
    {
        "states": {
            "Outcome_1": ["Event1", "Event2"],
            "Outcome_2": ["Event3", "Event4"]
        }
    }
        
    This means:
    - When “Observational Technique1” is applied and “Outcome_1” is observed, “Event1” and “Event2” are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which events are valid or related.

2. Explain the celestial events and observations in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a celestial event based on observational outcomes. Each round, you'll be presented with a list of possible celestial events and available observational techniques. You need to systematically rule out celestial events that do not match the observed outcomes until only one plausible event remains. Your objective is to identify the event accurately in the fewest steps.

How to Play:

(1) View the list of possible celestial events and available observational techniques.

(2) Choose one observational technique from the list to apply.

(3) Use the outcomes to eliminate celestial events that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the event.

This is the initial state of the game:

Celestial Events: {self.env.truth_space}

Observational Techniques: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is an observational astronomy guidebook to introduce the celestial events and observational techniques:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt