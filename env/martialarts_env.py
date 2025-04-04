import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.martial_arts_data import Truths, Actions, Outcomes

@registry.register_environment("MartialArtsEnv")
class MartialArtsEnv(BaseEnv):

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
Please write a martial arts analysis guidebook that introduces various martial arts styles and movement patterns in natural language according to the following information.

Martial Arts Styles: {truths}

Movement Patterns / Techniques: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the martial arts styles that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "MovementPattern1" is:
    
    "MovementPattern1":
    {
        "states": {
            "Outcome_1": ["Style1", "Style2"],
            "Outcome_2": ["Style3", "Style4"]
        }
    }
        
    This means:
    - When “MovementPattern1” is observed and “Outcome_1” is detected, “Style1” and "Style2" are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which styles are valid or related.

2. Explain the martial arts styles and techniques in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a martial arts style based on movement patterns and techniques. Each round, you'll be presented with a list of possible martial arts styles and available analyses. You need to systematically rule out martial arts styles that do not match the observed patterns until only one plausible style remains. Your objective is to identify the style accurately in the fewest steps.

How to Play:

(1) View the list of possible martial arts styles and available movement pattern analyses.

(2) Choose one analysis from the list to perform.

(3) Use the outcomes to eliminate martial arts styles that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the style.

This is the initial state of the game:

Martial Arts Styles: {self.env.truth_space}

Movement Patterns / Techniques: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a martial arts analysis guidebook to introduce the martial arts styles and movement patterns:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt