import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.theatrical_data import Truths, Actions, Outcomes

@registry.register_environment("TheatricalEnv")
class TheatricalEnv(BaseEnv):
    
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
Please write a theatrical script analysis guidebook that introduces the following theatrical genres and script checks in natural language according to the following information.

Theatrical genres: {truths}

Script analysis activities: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the theatrical genres that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "DialogueAnalysis1" is:

    "DialogueAnalysis1":
    {
        "states": {
            "Outcome_1": ["Genre1", "Genre2"],
            "Outcome_2": ["Genre3", "Genre4"]
        }
    }
        
    This means:
    - When “DialogueAnalysis1” is performed and “Outcome_1” is observed, “Genre1” and Genre2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which genres are valid or related.

2. Explain the theatrical genres and analysis activities in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the theatrical genre a play script belongs to based on script analysis outcomes. Each round, you'll be presented with a list of possible theatrical genres and available analysis activities. You need to systematically rule out genres that do not match the observed outcomes until only one plausible genre remains. Your objective is to identify the genre accurately in the fewest steps.

How to Play:

(1) View the list of possible theatrical genres and available analysis activities.

(2) Choose one analysis activity from the list to perform.

(3) Use the outcomes to eliminate genres that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the genre.

This is the initial state of the game:

Theatrical Genres: {self.env.truth_space}

Script Analysis Activities: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a theatrical script analysis guidebook to introduce the theatrical genres and script checks:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt