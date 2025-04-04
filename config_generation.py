import json
import os
import shutil
import importlib.util

from transformers import HfArgumentParser

from common.configs import LLM_Arguments, Config_Generate_Arguments
from common.utils import get_llm


def _check_truth_not_rule_out(all_truths, all_actions, ta_mapping):
    """
    Check if any truth is always ruled out for a specific action in every state.
    If such a case is found, print a message and record the action key.
    """
    keys = []
    for key, value in ta_mapping.items():
        # Check each truth to see if it is always missing in every state's outcomes
        for truth in all_truths:
            flag = True
            for state in value["states"].values():
                if truth not in state:
                    flag = False
                    break
            if flag:
                print(f'{truth} will be always ruled out for {key}')
                keys.append(key)
    assert len(keys) == 0


def _check_all_truths_actions_in_outcome(all_truths, all_actions, ta_mapping):
    """
    Ensure that the set of truths and actions used in the outcomes mapping
    matches the provided lists. Adjust the lists accordingly.
    """
    truths_new = set()
    for key, value in ta_mapping.items():
        for state in value["states"].values():
            truths_new.update(state)
    
    outcomes_keys = ta_mapping.keys()
    print(f'truth: {truths_new}')

    # Remove any truths that are not present in the mapping
    if len(set(all_truths) - truths_new) > 0:
        print('delete:', set(all_truths) - truths_new)
        all_truths = set(all_truths) - (set(all_truths) - truths_new)
    
    print(truths_new - set(all_truths))
    print('set(all_truths): ', set(all_truths))
    print('truths_new: ', truths_new)

    try:
        assert set(all_truths) == truths_new, 'Please regenerate or delete the truths in the outcomes'
    except Exception as e:
        print(e)
        # Add new truths into all_truths if needed
        all_truths = set(list(all_truths) + list(truths_new - set(all_truths)))
    
    in_actions_not_in_outcomes = set(all_actions) - set(outcomes_keys)
    in_outcomes_not_in_actions = set(outcomes_keys) - set(all_actions)

    if len(in_actions_not_in_outcomes) > 0:
        print('delete:', set(all_actions) - outcomes_keys)
        all_actions = set(all_actions) - (set(all_actions) - set(outcomes_keys))
        
    in_actions_not_in_outcomes = set(all_actions) - set(outcomes_keys)
    in_outcomes_not_in_actions = set(outcomes_keys) - set(all_actions)
    
    print(in_outcomes_not_in_actions)
    assert len(in_actions_not_in_outcomes) == 0
    assert len(in_outcomes_not_in_actions) == 0, (
        'Please regenerate or delete the actions in the outcomes {}'.format(in_outcomes_not_in_actions)
    )
    
    return all_truths, all_actions, ta_mapping


if __name__ == "__main__":
    # Parse command-line arguments
    parser = HfArgumentParser((LLM_Arguments, Config_Generate_Arguments))
    llm_args, generate_args = parser.parse_args_into_dataclasses()
    domain_data_path = generate_args.data_path
    template_path = generate_args.template_path
    example_path = generate_args.example_path

    # Ensure required file paths exist
    assert os.path.exists(domain_data_path), f"Data path {domain_data_path} does not exist."
    assert os.path.exists(example_path), f"Example path {example_path} does not exist."

    # Read domain data (each line is a JSON object)
    with open(domain_data_path, "r", encoding="utf-8") as f:
        data = [json.loads(line) for line in f]

    # Initialize the language model (LLM)
    llm = get_llm(llm_args)
    
    # Load the prompt template and example environment configuration
    with open(template_path, 'r') as f:
        template = f.read()
    with open(example_path, 'r') as f:
        example_env = f.read()

    # Iterate over each domain configuration
    for domain in data:
        # Convert actions list to a single string separated by '/'
        domain['Actions'] = '/'.join(domain['Actions'])
        
        # Construct the prompt for LLM to generate the config prompt
        prompt_template = template + f'''
        Please generate a prompt in the domain of this:

        {domain}
        '''
        prompt = llm.call_llm(prompt_template)
        prompt = f'''
        Follow this prompt to generate the configs of this reasoning game:

        {prompt}
        '''
        prompt += (
            "- Generate at least 30 actions and 50 truths. Each action should have its outcomes in the Outcomes dict. "
            "The action cannot rule out one truth in every state."
        )
        check_prompt = (
            "\nCheck this generation is ended or not. "
            "If not, outputs: <STATUS>NO_END</STATUS>. If yes, outputs: <STATUS>END</STATUS>.\n"
        )

        messages = [{"role": "user", "content": prompt}]
        times = 0

        # Loop until the generation is complete or maximum attempts reached
        while True:
            if times >= 5:
                print('The generation is failed.')
                break
            generated_configs = llm.call_llm(messages)
            messages.append({'role': 'assistant', 'content': generated_configs})
    
            check_messages = messages.copy()
            check_messages.append({'role': 'user', 'content': check_prompt})
    
            check_end = llm.call_llm(check_messages)
            check_end = check_end.split('<STATUS>')[-1].split('</STATUS>')[0]
    
            if check_end == 'END':
                break
            else:
                messages.append({'role': 'user', 'content': 'Continue to generate the configs.'})
                times += 1

        # Extract the full configuration from the conversation history
        extract_messages = messages.copy()
        extract_messages.append({
            'role': 'user',
            'content': 'Extract the full configs into python data structure based on the history messages.'
        })
        configs = llm.call_llm(extract_messages)
        configs = configs.split('```')[1].strip()
        configs = configs.split('python')[1].strip()

        # Create environment folder based on the domain goal
        goal_string = 'ds' + '_'.join(domain['Goal'].split(' '))
        env_file = f'env_data/{goal_string}'
        os.makedirs(env_file, exist_ok=True)

        # Write the configuration to a Python file
        with open(f'{env_file}/configs.py', 'w') as f:
            f.write(configs)

        # Dynamically load the generated configuration module
        env_file_path = f'env_data/{goal_string}/configs.py'
        if os.path.exists(env_file_path):
            spec = importlib.util.spec_from_file_location("configs", env_file_path)
            configs_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(configs_module)
            print('Load the module dynamically')
            # Extract variables from the module
            for attr in dir(configs_module):
                if not attr.startswith("__"):
                    if attr == 'Actions':
                        Actions = getattr(configs_module, attr)
                    elif attr == 'Outcomes':
                        Outcomes = getattr(configs_module, attr)
                    else:
                        Truths = getattr(configs_module, attr)
        else:
            print(f"File not found: {env_file_path}")

        # Validate the configuration consistency
        _check_truth_not_rule_out(Truths, Actions, Outcomes)
        new_truths, new_actions, new_outcomes = _check_all_truths_actions_in_outcome(Truths, Actions, Outcomes)

        # Overwrite the configuration file with the updated values
        with open(env_file_path, 'w') as f:
            f.write(f'''Truths = {new_truths}
Actions = {new_actions}
Outcomes = {new_outcomes}
''')
            
        # Generate the environment file based on the example template
        env_prompt = f'''
        Please generate the environment file based on the following template:

        ```python
        {example_env}
        ```

        Here's the domain for the environment:
        {domain}

        You only need to revise: knowledge_book_prompt, system_prompt, "xxxEnV" in registry and class name, and "from env.data.xxx_data import Truths, Actions, Outcomes" based on the given domain.
        '''
        generated_env = llm.call_llm(env_prompt)
        # Extract the environment configuration from the generated text
        generated_env_1 = generated_env.split('```')[1].strip()
        generated_env_2 = generated_env_1.split('python')[1].strip()

        # Retrieve environment name and data file name from the generated code
        env_name = generated_env_2.split('class')[1].split('(')[0].strip()
        env_data_file_name = 'ds' + generated_env_2.split('from env.data.')[1].split(' import')[0].strip()

        # Save the generated environment file and metadata
        with open(f'env_data/{goal_string}/env.py', 'w') as f:
            f.write(generated_env_2)

        with open(f'env_data/{goal_string}/metadata.json', 'w') as f:
            json.dump(
                {
                    'env_name': env_name,
                    'env_data_file_name': env_data_file_name,
                    'goal': domain['Goal'],
                    'actions': domain['Actions'],
                    'truths': domain['Truths'],
                },
                f
            )

        # Determine class name and copy files to proper locations
        class_name = env_name[:-3]
        os.makedirs(f'env/data/', exist_ok=True)
        shutil.copy(f'env_data/{goal_string}/configs.py', f'env/data/{env_data_file_name}.py')
        shutil.copy(f'env_data/{goal_string}/env.py', f'env/ds{class_name.lower()}_env.py')

        # Register the environment in the __init__.py file in the env folder
        init_file = 'env/__init__.py'
        with open(init_file, 'r') as file:
            lines = file.readlines()

        new_import = f'from .{class_name.lower()}_env import {class_name}Env\n'
        new_env = f"    '{class_name}Env',\n"

        import_index = next(i for i, line in enumerate(lines) if line.startswith('from'))
        all_index = next(i for i, line in enumerate(lines) if line.startswith('__all__'))

        lines.insert(import_index, new_import)
        lines.insert(all_index + 2, new_env)

        with open(init_file, 'w') as file:
            file.writelines(lines)
