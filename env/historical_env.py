import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.history_data import Truths, Actions, Outcomes

@registry.register_environment("HistoricalEnv")
class HistoricalEnv(BaseEnv):
    
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
Please write a historical analysis guidebook that introduces the following historical events or periods and research methods in natural language according to the following information.

Historical events or periods: {truths}

Research methods: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the historical events or periods that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "ResearchMethod1" is:
    
    "ResearchMethod1":
    {
        "states": {
            "Outcome_1": ["Event1", "Event2"],
            "Outcome_2": ["Event3", "Event4"]
        }
    }
        
    This means:
    - When “ResearchMethod1” is employed and “Outcome_1” is observed, “Event1” and Event2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which events are valid or related.

2. Explain the historical events or periods and research methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a historical event or period based on research method outcomes. Each round, you'll be presented with a list of possible historical events or periods and available research methods. You need to systematically rule out events or periods that do not match the observed outcomes until only one plausible event or period remains. Your objective is to identify the event or period accurately in the fewest steps.

How to Play:

(1) View the list of possible historical events or periods and available research methods.

(2) Choose one research method from the list to employ.

(3) Use the outcomes to eliminate historical events or periods that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the event or period.

This is the initial state of the game:

Historical Events or Periods: {self.env.truth_space}

Research Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a historical analysis guidebook to introduce the historical events or periods and research methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt