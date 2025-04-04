Below is a prompt for an LLM to generate a configuration for a reasoning game. Your task is to propose a situation for the game by filling in the missing values for the prompt. For example:

**TRUTH**: The domain or topic of knowledge for the game (e.g., “Diseases”).

**ACTION**: The primary activity or process the player engages in (e.g., “Diagnosis”).

**GOAL**: The objective or outcome the player seeks to achieve (e.g., “identify the disease of a patient”).

**<u>you only need to create the prompt instead of the configuration!!!</u>**

# Prompt Template

Generate a configuration in Python for a {DOMAIN} reasoning game. The goal of the game is to determine {GOAL} based on observed test outcomes. The configuration should follow the same format as the example.

**Requirements:**

1. **Truths**: Define a list of {TRUTH} for {GOAL}, such as {TRUTH_EXAMPLE1}, {TRUTH_EXAMPLE2}, {TRUTH_EXAMPLE3}. 
2. **Actions**: Define a list of {ACTION} for {GOAL}, such as {ACTION_EXAMPLE1}, {ACTION_EXAMPLE2}, {ACTION_EXAMPLE3}. 
3. **Outcomes**: For each {ACTION}, specify the type of outcomes (e.g., “str” or “float”) and define possible outcome states. Each outcome state should **rule out** certain {TRUTH} rather than confirming them. Avoid 1-to-1 mappings wherever possible; make outcomes broader and applicable to multiple {TRUTHS}. For instance:
   - A {STATE_EXAMPLE1} on a {ACTION_EXAMPLE1} could rule out a lack of {TRUTH_EXAMPLE1} and {TRUTH_EXAMPLE2}.
4. Ensure that the configuration is comprehensive and maintains logical relationships between {TRUTH}, {ACTION}, and outcomes.

**Example of {TRUTHS}, {ACTIONS}, and Outcomes:**

- **{TRUTH} (Truths)**: [{TRUTH_EXAMPLE1}, {TRUTH_EXAMPLE2}, {TRUTH_EXAMPLE3}, {TRUTH_EXAMPLE4}]
- **{ACTIONS} (Actions)**: [{ACTION_EXAMPLE1}, {ACTION_EXAMPLE2}, {ACTION_EXAMPLE3}, {ACTION_EXAMPLE4}]
- **Outcomes**: Define the outcomes for each {ACTION} with states that correspond to **ruling out** certain {TRUTH}.

Use the following format:

```python
Truths = [
    # List of {TRUTHS}
]

Actions = [
    # List of {ACTIONS}
]

Outcomes = {
    # Define outcomes for each test
    "Test Name": {
        "type": "str or float",
        "states": {
            "Outcome State 1": set(),  # Set of ruled-out {TRUTH}
            "Outcome State 2": set(),  # Set of ruled-out {TRUTH}
            ...
        }
    },
    ...
}
```

Generate the configuration as requested, ensuring that:

- Use tuple to represent float type. e.g., (85, 100). Do not use inf (assume all values are in a reasonable range).
- We allow for some states that correspond to empty set.
- Float type and string type outcomes should both exist.
- Each test has at least 2 possible outcome states.

- The outcome states relate to several truths, and it would be better to avoid 1-to-1 mappings between actions and truths (**not enforced, sometimes 1-to-1 is allowed**).

- The relationships between outcomes and truths are meaningful and logical within the {DOMAIN} domain.

- Generate at least 30 actions and 50 truths. Each action should have its outcomes in the Outcomes dict. The action cannot rule out one truth in every state.

- **The set of truths for a state SHOULD BE ruled out by the state outcome**.
