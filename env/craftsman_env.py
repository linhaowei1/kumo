import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.craftsman_data import Truths, Actions, Outcomes

@registry.register_environment("CraftsmanEnv")
class CraftsmanEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Represents the tools
        self.all_actions = Actions    # Represents material compatibility tests, tool function trials, ergonomic checks
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a craftsman tool analysis guidebook that introduces the following tools and tests in natural language according to the following information.

Tools: {truths}

Tests: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the tools that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Test1" is:
    
    "Test1":
    {
        "states": {
            "Outcome_1": ["Tool1", "Tool2"],
            "Outcome_2": ["Tool3", "Tool4"]
        }
    }
        
    This means:
    - When “Test1” is performed and “Outcome_1” is observed, “Tool1” and Tool2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which tools are valid or related.

2. Explain the tools and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the correct tool needed by a craftsman based on test outcomes. Each round, you'll be presented with a list of possible tools and available tests. You need to systematically rule out tools that do not match the observed outcomes until only one plausible tool remains. Your objective is to identify the tool accurately in the fewest steps.

How to Play:

(1) View the list of possible tools and available tests.

(2) Choose one test from the list to perform.

(3) Use the outcomes to eliminate tools that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the tool.

This is the initial state of the game:

Tools: {self.env.truth_space}

Tests: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a craftsman tool analysis guidebook to introduce the tools and tests:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt