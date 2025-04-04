import os
import json
from env.engine import Environment

class BaseEnv:
    
    def __init__(self, datapoint=None):
        self.all_truths = None
        self.all_actions = None
        self.ta_mapping = None
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)
        else:
            self._check_env()
    
    def reset(
        self, datapoint,
    ):
        self.env = Environment(
            datapoint['truths'], 
            datapoint['actions'], 
            self.ta_mapping, 
            datapoint['observations'], 
            datapoint['seed']
        )
        
    def _check_env(self,):
        self._check_truth_not_rule_out()
        self._check_all_truths_actions_in_outcome()
        
    def _check_truth_not_rule_out(self,):
        keys = []
        for key, value in self.ta_mapping.items():
            # check if one state will be always ruled out for some action
            for truth in self.all_truths:
                flag = True
                for state in value["states"].values():
                    if truth not in state:
                        flag = False
                        break
                if flag:
                    print(f'{truth} will be always ruled out for {key}')
                    keys.append(key)
        
        assert len(keys) == 0

    
    def _check_all_truths_actions_in_outcome(self):
        
        truths_new = set()
        for key, value in self.ta_mapping.items():
            for v in value["states"].values():
                #print(v)
                truths_new.update(v)
                #print(truths_new)
        outcomes_keys = self.ta_mapping.keys()
        print(f'truth: {truths_new}')
    
        print(set(self.all_truths) - truths_new)
        print(truths_new - set(self.all_truths))
        
        assert set(self.all_truths) == truths_new
        in_actions_not_in_outcomes = set(self.all_actions) - set(outcomes_keys)
        in_outcomes_not_in_actions = set(outcomes_keys) - set(self.all_actions)
        print(in_actions_not_in_outcomes)
        print(in_outcomes_not_in_actions)
        assert len(in_actions_not_in_outcomes) == 0
        assert len(in_outcomes_not_in_actions) == 0
        
    def get_reduced_ta_mapping(self, ta_mapping=None):
        if ta_mapping is None:
            ta_mapping = self.ta_mapping
        seen_observations = {action: ta_mapping[action]['states'] for action in self.env.action_space}
        
        for k, v in seen_observations.items():
            new_v = {
                state: {value for value in v[state] if value in self.env.truth_space}
                for state in v
            }
            seen_observations[k] = new_v
        return seen_observations