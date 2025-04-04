"""
The main script for conducting evalution for LLMs across different domains.
See `./common/config.py` for detailed arguments definitions.
"""

import json
import os

from transformers import HfArgumentParser

from common.configs import LLM_Arguments, Eval_Arguments, Data_Arguments
from common.utils import get_testcase, get_llm


if __name__ == "__main__":
    
    llm_args, eval_args, data_args = HfArgumentParser((LLM_Arguments, Eval_Arguments, Data_Arguments)).parse_args_into_dataclasses()
    llm = get_llm(llm_args)
    testcase_generator = get_testcase(llm, eval_args, data_args)

    result_file = os.path.join(
        eval_args.result_dir,
        llm_args.model_name_or_path.split('/')[-1],
        eval_args.agent_type,
        data_args.domain,
        f'truth_num={data_args.truth_num}+action_num={data_args.action_num}+valid_truth_num={data_args.valid_truth_num}',
        f'eval_times={eval_args.eval_times}.jsonl',
    )
    
    seed_list = [] # Used for resume evalution
    if os.path.exists(result_file):
        if eval_args.resume:
            with open(result_file, "r") as f:
                lines = f.readlines()
                data = [json.loads(line) for line in lines]
                seed_list = [int(d['seed']) for d in data]
                print("skip seeds: ", seed_list)
        else:
            os.remove(result_file)
    
    if not os.path.exists(os.path.dirname(result_file)):
        os.makedirs(os.path.dirname(result_file))
        
    for env, agent in testcase_generator:
        
        if env.env.seed in seed_list:
            continue
    
        trajs = {
            'trajectories': [],
            'seed': env.env.seed,
        }
        
        for eval_time in range(eval_args.eval_times):
            
            traj = {
                'actions': [],
                'generated_text': [],
                'consumed_tokens': 0,
                'observations': [],
            }
            
            agent.reset()
            observation = None
            
            parse_error_flag = False
            successful_flag = False

            for _ in range(eval_args.max_steps):
                action, outputs = agent.response(observation)
                
                traj['actions'].append(action)
                traj['consumed_tokens'] += outputs['consumed_tokens']
                traj['generated_text'].append(outputs['generated_text'])
                traj['observations'].append(observation)

                if action in env.env.truth_space:
                    print(f"Agent's answer: {action}")
                    traj['actions'].append({'predicted_truth': action})
                    cur_correct = int(env.env.evaluate_answer(action))
                    successful_flag = bool(cur_correct)
                    break
                elif action in env.env.action_space:
                    observation = {
                        'action': action,
                        'observation': env.env.get_observation(action)
                    }
                    print(f"Agent's action: {action}, observation: {observation['observation']}")
                else:
                    parse_error_flag = True
                    break

            traj['successful'] = successful_flag
            traj['parse_error'] = parse_error_flag
            
            print(f"Current evaluation time: {eval_time + 1} | Current correct: {successful_flag} | Current parse error: {parse_error_flag} | Current action number: {len(traj['actions'])} | Current tokens number: {traj['consumed_tokens']}")
        
            trajs['trajectories'].append(traj)
        
        trajs['average_actions'] = sum([len(traj_['actions']) for traj_ in trajs['trajectories']]) / eval_args.eval_times
        trajs['average_tokens'] = sum([traj_['consumed_tokens'] for traj_ in trajs['trajectories']]) / eval_args.eval_times
        trajs['average_correct'] = sum([int(traj_['successful']) for traj_ in trajs['trajectories']]) / eval_args.eval_times
        trajs['average_parse_error'] = sum([int(traj_['parse_error']) for traj_ in trajs['trajectories']]) / eval_args.eval_times
        trajs['average_successful_action_num'] = sum([len(traj_['actions']) for traj_ in trajs['trajectories'] if traj_['successful']]) / sum([int(traj_['successful']) for traj_ in trajs['trajectories']]) if sum([int(traj_['successful']) for traj_ in trajs['trajectories']]) else 0
        trajs['average_successful_tokens'] = sum([traj_['consumed_tokens'] for traj_ in trajs['trajectories'] if traj_['successful']]) / sum([int(traj_['successful']) for traj_ in trajs['trajectories']]) if sum([int(traj_['successful']) for traj_ in trajs['trajectories']]) else 0
        
        with open(result_file, "a") as f:
            f.write(json.dumps(trajs) + "\n")
