import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.mythical_data import Truths, Actions, Outcomes

@registry.register_environment("MythicalEnv")
class MythicalEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Mythical creatures
        self.all_actions = Actions    # Magical detection methods / lore reference checks
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a guidebook that introduces the following mythical creatures and magical detection methods or lore reference checks in natural language according to the following information.

Mythical creatures: {truths}

Detection methods / Lore checks: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the mythological creatures that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "LoreCheck1" is:
    
    "LoreCheck1":
    {
        "states": {
            "Outcome_1": ["Creature1", "Creature2"],
            "Outcome_2": ["Creature3", "Creature4"]
        }
    }
        
    This means:
    - When “LoreCheck1” is performed and “Outcome_1” is observed, “Creature1” and "Creature2" are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which creatures are valid or related.

2. Explain the mythological creatures and detection methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a mythical creature based on lore checks and magical detection outcomes. Each round, you'll be presented with a list of possible creatures and available detection methods. You need to systematically rule out creatures that do not match the observed outcomes until only one plausible creature remains. Your objective is to identify the creature accurately in the fewest steps.

How to Play:

(1) View the list of possible mythical creatures and available detection methods.

(2) Choose one method from the list to perform.

(3) Use the outcomes to eliminate creatures that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the creature.

This is the initial state of the game:

Mythical Creatures: {self.env.truth_space}

Detection Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a guidebook to introduce the mythical creatures and detection methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt