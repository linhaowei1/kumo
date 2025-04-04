import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.marketing_data import Truths, Actions, Outcomes

@registry.register_environment("MarketingEnv")
class MarketingEnv(BaseEnv):
    
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
Please write a marketing analysis guidebook that introduces the following marketing strategies and analysis techniques in natural language according to the following information.

Marketing strategies: {truths}

Advertising content analysis / target demographic checks: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the marketing strategies that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Analysis1" is:
    
    "Analysis1":
    {
        "states": {
            "Outcome_1": ["Strategy1", "Strategy2"],
            "Outcome_2": ["Strategy3", "Strategy4"]
        }
    }
        
    This means:
    - When “Analysis1” is performed and “Outcome_1” is observed, “Strategy1” and Strategy2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which strategies are valid or related.

2. Explain the marketing strategies and analyses in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a marketing strategy based on analysis outcomes. Each round, you'll be presented with a list of possible marketing strategies and available analyses. You need to systematically rule out strategies that do not match the observed outcomes until only one plausible strategy remains. Your objective is to identify the strategy accurately in the fewest steps.

How to Play:

(1) View the list of possible marketing strategies and available analyses.

(2) Choose one analysis from the list to perform.

(3) Use the outcomes to eliminate strategies that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the strategy.

This is the initial state of the game:

Marketing Strategies: {self.env.truth_space}

Analyses: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a marketing analysis guidebook to introduce the marketing strategies and analyses:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt