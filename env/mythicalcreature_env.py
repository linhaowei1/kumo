import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.mythical_creature_data import Truths, Actions, Outcomes

@registry.register_environment("MythicalCreatureEnv")
class MythicalCreatureEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Mythical creatures
        self.all_actions = Actions    # Symbol interpretation / folklore comparison / trait cataloging
        self.ta_mapping = Outcomes    # Outcomes related to mythological analysis
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a comprehensive guidebook on identifying mythical creatures from various legends according to the following information.

Mythical Creatures: {truths}

Methods: {actions}

Elimination Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Elimination Outcomes” represent the mythical creatures that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Symbol Interpretation" is:
    
    "Symbol Interpretation":
    {
        "states": {
            "Outcome_1": ["Creature1", "Creature2"],
            "Outcome_2": ["Creature3", "Creature4"]
        }
    }
        
    This means:
    - When “Symbol Interpretation” is performed and “Outcome_1” is observed, “Creature1” and “Creature2” are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which creatures are valid or related.

2. Explain mythical creatures and methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a mythical creature based on your interpretations and comparisons. Each round, you'll be presented with a list of possible mythical creatures and methods. You need to systematically rule out creatures that do not match the observed outcomes until only one plausible creature remains. Your objective is to identify the creature accurately in the fewest steps.

How to Play:

(1) View the list of possible mythical creatures and available methods.

(2) Choose one method from the list to apply.

(3) Use the outcomes to eliminate mythical creatures that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the creature.

This is the initial state of the game:

Mythical Creatures: {self.env.truth_space}

Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a guidebook on identifying mythical creatures and using the methods effectively:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt