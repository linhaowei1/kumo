import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.audio_data import Truths, Actions, Outcomes

@registry.register_environment("AudioDialectEnv")
class AudioDialectEnv(BaseEnv):
    
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
Please write a guidebook on audio dialect analysis that introduces language dialects and phonetic analysis experiments in natural language according to the following information.

Language Dialects: {truths}

Experiments: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the language dialects that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Phonetic Experiment1" is:
    
    "Phonetic Experiment1":
    {
        "states": {
            "Outcome_1": ["Dialect1", "Dialect2"],
            "Outcome_2": ["Dialect3", "Dialect4"]
        }
    }
        
    This means:
    - When “Phonetic Experiment1” is performed and “Outcome_1” is observed, “Dialect1” and “Dialect2” are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which dialects are valid or related.

2. Explain the language dialects and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a language dialect based on phonetic analysis and lexical frequency outcomes. Each round, you'll be presented with a list of possible dialects and available experiments. You need to systematically rule out dialects that do not match the observed outcomes until only one plausible dialect remains. Your objective is to accurately identify the dialect in the fewest steps.

How to Play:

(1) View the list of possible dialects and available experiments.

(2) Choose one experiment from the list to perform.

(3) Use the outcomes to eliminate dialects that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the dialect.

This is the initial state of the game:

Language Dialects: {self.env.truth_space}

Experiments: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a guidebook on audio dialect analysis to introduce the language dialects and experiments:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt