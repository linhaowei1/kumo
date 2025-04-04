import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.motif_analysis_data import Truths, Actions, Outcomes

@registry.register_environment("MotifAnalysisEnv")
class MotifAnalysisEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths
        self.all_actions = Actions
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a guidebook on classical motif analysis that introduces the following classical motifs and analysis techniques in natural language according to the following information.

Classical motifs: {truths}

Thematic motif analysis techniques: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the classical motifs that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Analysis1" is:
    
    "Analysis1":
    {
        "states": {
            "Outcome_1": ["Motif1", "Motif2"],
            "Outcome_2": ["Motif3", "Motif4"]
        }
    }
        
    This means:
    - When “Analysis1” is performed and “Outcome_1” is observed, “Motif1” and Motif2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which motifs are valid or related.

2. Explain the classical motifs and analysis techniques in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify which classical composer's motif is woven into a symphony based on thematic motif analysis outcomes. Each round, you'll be presented with a list of possible classical motifs and available analysis techniques. You need to systematically rule out motifs that do not match the observed outcomes until only one plausible motif remains. Your objective is to identify the motif accurately in the fewest steps.

How to Play:

(1) View the list of possible classical motifs and available thematic motif analysis techniques.

(2) Choose one analysis technique from the list to perform.

(3) Use the outcomes to eliminate motifs that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the motif.

This is the initial state of the game:

Classical Motifs: {self.env.truth_space}

Thematic Motif Analysis Techniques: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a guidebook on classical motif analysis to introduce the classical motifs and analysis techniques:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt