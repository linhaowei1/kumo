from abc import abstractmethod
from collections import defaultdict
import copy
import random

class Environment:
    def __init__(self, truth_space, action_space, ta_mapping, observations, seed=None):
        self.truth_space = truth_space
        self.action_space = action_space
        self.ta_mapping = ta_mapping
        self.observations = observations
        self.seed = seed    # for id identifcation
    
    def get_observation(self, action):
        if action in self.observations:
            return self.observations[action]
        else:
            raise ValueError(f"Action {action} not in valid action space")
    
    def evaluate_answer(self, answer):
        # evaluate if answer is ruled out by the observations. Return True if ruled out.
        
        if answer not in self.truth_space:
            # print(f"Answer {answer} not in valid truth space")
            return False

        for action, observation in self.observations.items():
            action_info = self.ta_mapping[action]
            for state, impossible_diseases in action_info["states"].items():
                if (action_info['type'] == 'str' and observation == state) or (action_info['type'] == 'float' and observation >= state[0] and observation <= state[1]):
                    if answer in impossible_diseases:
                        return False
        
        return True
    
    def evaluate_actions(self, actions):
        truch_space = set(self.truth_space)
        for action in actions:
            action_info = self.ta_mapping.get(action, None)
            if action_info is None:
                continue
            observation = self.observations.get(action, None)
            if observation is None:
                continue
            for state, impossible_diseases in action_info["states"].items():
                if (action_info['type'] == 'str' and observation == state) or (action_info['type'] == 'float' and observation >= state[0] and observation <= state[1]):
                    truch_space.difference_update(impossible_diseases)
                    continue
        return len(truch_space) == 1

    
    def evaluate_search_engine(self, search_engine):
        action = None
        observation = None

        num_actions = 0
        while True:
            res = search_engine.search_step(action, observation)
            # SearchEngine returns a list of truths
            if isinstance(res, list):
                break
            action = res
            observation = self.get_observation(action)
            # print("Environment: ", action, observation)

            num_actions += 1
        
        for truth in res:
            assert self.evaluate_answer(truth) == True
        
        # print(f"Number of actions: {num_actions}")

        return num_actions, res


class SearchEngine:
    def __init__(self, truth_space, action_space, ta_mapping):
        self.truth_space = copy.deepcopy(truth_space)
        self.action_space = copy.deepcopy(action_space)
        self.ta_mapping = copy.deepcopy(ta_mapping)
    
    @abstractmethod
    def search_step(self, last_action, observation):
        """Give the next action to take based on the current observation"""
        raise NotImplementedError


class VanillaSearchEngine(SearchEngine):
    def __init__(self, truth_space, action_space, ta_mapping):
        super().__init__(truth_space, action_space, ta_mapping)
    
    def search_step(self, last_action, last_observation):
        # Update truth space based on the last action and observation
        if last_action is not None:
            self.action_space.remove(last_action)
            for state in self.ta_mapping[last_action]["states"]:
                if self.ta_mapping[last_action]["type"] == "str":
                    if last_observation == state:
                        # print("Remove,", last_action, last_observation, [t for t in self.truth_space if t in self.ta_mapping[last_action]["states"][state]])
                        self.truth_space = [t for t in self.truth_space if t not in self.ta_mapping[last_action]["states"][state]]
                        break
                elif self.ta_mapping[last_action]["type"] == "float":
                    if last_observation >= state[0] and last_observation <= state[1]:
                        # print("Remove,", last_action, last_observation, [t for t in self.truth_space if t in self.ta_mapping[last_action]["states"][state]])
                        self.truth_space = [t for t in self.truth_space if t not in self.ta_mapping[last_action]["states"][state]]
                        break
            
        # Stop if there is only one truth left or no action left
        if len(self.truth_space) <= 1 or len(self.action_space) == 0:
            return self.truth_space

        return self.action_space[0]



class GreedySearchEngine(SearchEngine):
    def __init__(self, truth_space, action_space, ta_mapping):
        super().__init__(truth_space, action_space, ta_mapping)

    def _calculate_expected_ablated_truth_num(self, current_truth_space, action):
        """
        Calculate the expected number of truths that can be ablated by the action
        """
        ablation_truth_num = []
        for state in self.ta_mapping[action]["states"]:
            ablation_truth_num.append(len(self.ta_mapping[action]["states"][state]))
        
        return sum(ablation_truth_num) / len(ablation_truth_num)
    
        
    def _greedy_search(self, truth_space, action_space):
        best_action = None
        best_score = float("-inf")
        for action in action_space:
            action_score = self._calculate_expected_ablated_truth_num(truth_space, action)
            if action_score > best_score:
                best_score = action_score
                best_action = action
        
        return best_action
    

    def search_step(self, last_action, last_observation):
        # Update truth space based on the last action and observation
        if last_action is not None:
            self.action_space.remove(last_action)
            for state in self.ta_mapping[last_action]["states"]:
                if self.ta_mapping[last_action]["type"] == "str":
                    if last_observation == state:
                        self.truth_space = [t for t in self.truth_space if t not in self.ta_mapping[last_action]["states"][state]]
                        break
                elif self.ta_mapping[last_action]["type"] == "float":
                    if last_observation >= state[0] and last_observation <= state[1]:
                        self.truth_space = [t for t in self.truth_space if t not in self.ta_mapping[last_action]["states"][state]]
                        break
            
        # Stop if there is only one truth left or no action left
        if len(self.truth_space) <= 1 or len(self.action_space) == 0:
            return self.truth_space

        # Greedy search for the next action
        next_action = self._greedy_search(self.truth_space, self.action_space)
        
        return next_action



class OracleSearchEngine(SearchEngine):
    def __init__(self, truth_space, action_space, ta_mapping):
        super().__init__(truth_space, action_space, ta_mapping)
        self.best_action_dict = dict()
        self.truth_space = set(truth_space)
        self.action_space = set(action_space)
        self.str2num = {k:i for i, k in enumerate(self.truth_space)}
        self.inverse_truth_bitmask = 2 ** len(self.truth_space) - 1
        self.str2num.update({k:i+len(self.truth_space) for i, k in enumerate(self.action_space)})
        self.obtain_related_actions()
    
    def obtain_related_actions(self):
        self.truth_to_action = {}
        
        for truth in self.truth_space:
            self.truth_to_action[truth] = set()
            for action in self.action_space:
                for states in self.ta_mapping[action]["states"]:
                    if truth in self.ta_mapping[action]["states"][states]:
                        self.truth_to_action[truth].add(action)
        
    def _to_bitmask(self, truth_space, action_space):
        # bitmask = self.inverse_truth_bitmask
        # for t in truth_space:
        #     bitmask ^= (1 << self.str2num[t])
        # for a in action_space:
        #     bitmask |= (1 << self.str2num[a])
        bitmask = 0
        for t in truth_space:
            bitmask |= (1 << self.str2num[t])
        for a in action_space:
            bitmask |= (1 << self.str2num[a])
        
        return bitmask
    
    def _prune(self, cur_bitmask, steps_upperbound):
        """
        Prune the search space based on the current bitmask
        """
        for key in self.best_action_dict:
            # indicate that the current bitmask is a subset of the key
            # then the expected steps of the key is the lowerbound of the current bitmask
            if key & cur_bitmask == cur_bitmask and self.best_action_dict[key][0] > steps_upperbound:
                return self.best_action_dict[key]

        return None



    def _calculate_expected_stpes(self, current_truth_space, current_action_space, steps_upperbound=float("+inf")):
        """
        Calculate the expected number of steps (maybe lowerbound) under the current truth space and action space
        """
        
        # if only one truth left or no action left
        if len(current_truth_space) <= 1 or len(current_action_space) == 0:
            return 0.0, None
        
        # Check if there is any truth that cannot be ablated by any action
        for truth in current_truth_space:
            related_actions = self.truth_to_action[truth]
            related_actions = set(current_action_space) & related_actions
            if len(related_actions) == 0:
                return 0.0, None
        
        # Memoization
        key = self._to_bitmask(current_truth_space, current_action_space)
        if key in self.best_action_dict:
            # print("Use memory") # DEBUG
            return self.best_action_dict[key]
        # # Prune the search space FIXME: can be further improve
        # res = self._prune(key, steps_upperbound)
        # if res is not None:
        #     # print("Prune") # DEBUG
        #     return res
        


        min_expected_steps = float("+inf")
        best_action = None
        for action in current_action_space:
            cur_expected_steps = 0
            num_states = len(self.ta_mapping[action]["states"])
            next_action_space = [a for a in current_action_space if a != action]
            
            # reweight the states based on the number of truths
            prob = [len(current_truth_space) for _ in range(num_states)]
            for i, state in enumerate(self.ta_mapping[action]["states"]):
                prob[i] -= len(self.ta_mapping[action]['states'][state] & set(current_truth_space))
            prob = [p / (sum(prob) + 1e-9) for p in prob]
            
            for i, state in enumerate(self.ta_mapping[action]["states"]):
                next_truth_space = [t for t in current_truth_space if t not in self.ta_mapping[action]["states"][state]]
                num_steps_left, _ = self._calculate_expected_stpes(next_truth_space, next_action_space)
                cur_expected_steps += num_steps_left * prob[i]

                # Prune the search space
                if cur_expected_steps >= min_expected_steps:
                    break
            
            # Update the best action
            if cur_expected_steps < min_expected_steps:
                min_expected_steps = cur_expected_steps
                best_action = action
        
        self.best_action_dict[key] = (min_expected_steps + 1, best_action) 
            
        return min_expected_steps + 1, best_action
    
    def search_step(self, last_action, last_observation):
        # Update truth space based on the last action and observation
        if last_action is not None:
            self.action_space.remove(last_action)
            for state in self.ta_mapping[last_action]["states"]:
                if self.ta_mapping[last_action]["type"] == "str":
                    if last_observation == state:
                        self.truth_space = [t for t in self.truth_space if t not in self.ta_mapping[last_action]["states"][state]]
                        break
                elif self.ta_mapping[last_action]["type"] == "float":
                    if last_observation >= state[0] and last_observation <= state[1]:
                        self.truth_space = [t for t in self.truth_space if t not in self.ta_mapping[last_action]["states"][state]]
                        break
            
        # Stop if there is only one truth left or no action left
        if len(self.truth_space) <= 1 or len(self.action_space) == 0:
            return self.truth_space[0]

        # Check if there is any truth that cannot be ablated by any action
        for truth in self.truth_space:
            related_actions = self.truth_to_action[truth]
            related_actions = set(self.action_space) & related_actions
            if len(related_actions) == 0:
                return truth
        
        # Greedy search for the next action
        _, next_action = self._calculate_expected_stpes(self.truth_space, self.action_space)
        
        return next_action