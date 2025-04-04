import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.leadership_data import Truths, Actions, Outcomes

@registry.register_environment("LeadershipEnv")
class LeadershipEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Leadership styles
        self.all_actions = Actions    # Behavioral observation / decision-making pattern analysis
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a guide on analyzing and identifying leadership styles of managers in natural language format, using the information provided below.

Leadership styles: {truths}

Methods for analysis: {actions}

Observed Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the leadership styles that must be **excluded or ruled out** when the corresponding behavior or decision pattern is observed.

For example,

    If the analysis of "Behavior1" results in:
    
    "Behavior1":
    {
        "states": {
            "Outcome_1": ["Style1", "Style2"],
            "Outcome_2": ["Style3", "Style4"]
        }
    }
        
    This means:
    - When “Behavior1” is observed and “Outcome_1” occurs, “Style1” and “Style2” are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming which styles are appropriate or related.

2. Explain the leadership styles and analytical methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This challenge is designed to help you identify the leadership style of a manager based on observed behaviors and decision-making patterns. Each round, you'll be presented with a list of possible leadership styles and available methods of analysis. You need to systematically rule out leadership styles that do not match the observed behaviors until only one plausible style remains. Your objective is to identify the style accurately in the fewest steps.

How to Play:

(1) View the list of possible leadership styles and available methods of analysis.

(2) Choose one method of analysis from the list to apply.

(3) Use the outcomes to eliminate leadership styles that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the style.

This is the initial state of the challenge:

Leadership Styles: {self.env.truth_space}

Methods of Analysis: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a guide to analyzing and identifying leadership styles:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt