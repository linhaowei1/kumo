import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.historical_data import Truths, Actions, Outcomes

@registry.register_environment("HistoricalBattleEnv")
class HistoricalBattleEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Historical battles
        self.all_actions = Actions    # Artifact analysis / historical record comparisons
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a historical analysis guidebook that introduces the following historical battles, artifacts, and analysis methods in natural language according to the following information.

Historical Battles: {truths}

Artifact Analysis Methods / Historical Record Comparisons: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the historical battles that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If an analysis method or record comparison reveals:
    
    "Method1":
    {
        "states": {
            "Outcome_1": ["Battle1", "Battle2"],
            "Outcome_2": ["Battle3", "Battle4"]
        }
    }
        
    This means:
    - When “Method1” is applied and “Outcome_1” is observed, “Battle1” and Battle2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which battles are related or validated.

2. Explain the historical battles and analysis methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the historical battle a set of relics originates from based on analysis outcomes. Each round, you'll be presented with a list of possible historical battles and available analysis methods. You need to systematically rule out battles that do not match the observed outcomes until only one plausible battle remains. Your objective is to identify the battle accurately in the fewest steps.

How to Play:

(1) View the list of possible historical battles and available analysis methods.

(2) Choose one method or comparison from the list to perform.

(3) Use the outcomes to eliminate battles that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the battle.

This is the initial state of the game:

Historical Battles: {self.env.truth_space}

Analysis Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a historical analysis guidebook to introduce the historical battles and analysis methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt