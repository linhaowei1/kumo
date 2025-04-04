import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.chemicalcompounds_data import Truths, Actions, Outcomes

@registry.register_environment("ChemicalCompoundsEnv")
class ChemicalCompoundsEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Chemical compounds
        self.all_actions = Actions    # Chromatography / IR spectroscopy
        self.ta_mapping = Outcomes    # Outcomes of the experiments
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a chemical analysis guidebook that introduces the following chemical substances and experiments in natural language according to the following information.

Chemical substances: {truths}

Experiments: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the chemical substances that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Experiment1" is:
    
    "Experiment1":
    {
        "states": {
            "Outcome_1": ["Substances1", "Substances2"],
            "Outcome_2": ["Substances3", "Substances4"]
        }
    }
        
    This means:
    - When “Experiment1” is performed and “Outcome_1” is observed, “Substances1” and Substances2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which substances are valid or related.

2. Explain the chemical substances and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rules should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a chemical compound based on test outcomes. Each round, you'll be presented with a list of possible chemical compounds and available experiments. You need to systematically rule out chemical compounds that do not match the observed outcomes until only one plausible compound remains. Your objective is to identify the compound accurately in the fewest steps.

How to Play:

(1) View the list of possible chemical compounds and available experiments.

(2) Choose one experiment from the list to perform (e.g., Chromatography or IR spectroscopy).

(3) Use the outcomes to eliminate chemical compounds that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the compound.

This is the initial state of the game:

Chemical Compounds: {self.env.truth_space}

Experiments: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a chemical analysis guidebook to introduce the chemical substances and experiments:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt