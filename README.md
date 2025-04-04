# KUMO: Generative Evaluation of Complex Reasoning in Large Language Models

Official Repository for the paper: [Generative Evaluation of Complex Reasoning in Large Language Models]().

**KUMO** is a benchmark designed to systematically evaluate complex reasoning capabilities of Large Language Models (LLMs) through procedurally generated reasoning games.

Visit our [website]() to view the leaderboard and detailed results.

---

## Quick Links
- [Benchmark Dataset](#benchmark-dataset)
- [Benchmark Format](#benchmark-format)
- [Environment Setup](#environment-setup)
- [Dataset Generation](#dataset-generation)
- [Evaluation](#evaluation)

---

## Benchmark Dataset

The **KUMO** benchmark introduces procedurally generated reasoning games to evaluate the complex reasoning abilities of LLMs. Each game is defined by:

- **Truth Set ($T$)**: A finite set of possible truths.
- **Action Set ($A$)**: A finite set of possible actions.
- **Outcomes ($\mathcal{O}$)**: Mapping from each action to corresponding outcomes.
- **Knowledge Book ($K$)**: A detailed document explaining the relationships between truths, actions, and outcomes, aiding the elimination of invalid truths based on observed outcomes.

In each game instance:
- A valid truth ($t^*$) is selected at initialization.
- Outcomes consistent with $t^*$ are generated.
- Players select actions and observe outcomes to deduce the valid truth efficiently.

**Example**: A medical diagnosis scenario, where the player uses diagnostic tests (actions) to deduce the correct disease (truth).

We provide 100 automatically generated exemplar domains spanning 18 categories such as Computer Science, Biology, and Art. Each domain typically includes 50 truths and 30 actions.

![KUMO Example](https://github.com/linhaowei1/kumo/blob/main/miscs/fig1.png)

---

## Benchmark Format

The KUMO dataset is structured in JSON format for easy accessibility, available at [KUMO/env](https://github.com/linhaowei1/kumo/tree/main/env).

Structure for each domain `[DomainName]`:

```
kumo/
└── env/
    ├── data/
    │   └── [DomainName]_data.py          # Python format data
    ├── [DomainName]/
    │   ├── knowledge_book/
    │   │   └── truth_num=4+action_num=6+valid_truth_num=1/
    │   │       ├── seed=0.txt
    │   │       └── ...
    │   └── truth_num=4+action_num=6+valid_truth_num=1.jsonl  # Task configurations
    └── [DomainName].py                   # Domain class definition
```

Default settings (`truth_num=4+action_num=6+valid_truth_num=1`) can be customized as needed.

---

## Environment Setup

### Clone Repository

```bash
git clone https://github.com/linhaowei1/kumo.git
cd kumo
```

### Set Up Environment

We recommend using Conda and Python (3.10 to 3.12):

```bash
conda create -n kumo python=3.12
conda activate kumo
pip install -r requirements.txt
```

---

## Dataset Generation

Create your custom domains through the following steps:

### 1. Seed Configuration Generation

Generate scenarios using an LLM:

```bash
python generate/config_generation.py \
  --load_type OPENAI \
  --api_base http://localhost:8001/v1 \
  --api_key EMPTY \
  --data_path ./templates/config_generation.jsonl
```

See [examples/config_generation.sh](https://github.com/linhaowei1/kumo/blob/main/generate.ipynb) for additional details.

### 2. Task Instance Generation

Generate specific instances using SAT sampling:

```bash
python SAT_sampling.py \
  --truth_num 4 \
  --action_num 6 \
  --valid_truth_num 1 \
  --data_num 50 \
  --domain MedicalEnv
```

See [examples/SAT_sampling.sh](https://github.com/linhaowei1/kumo/blob/main/generate.ipynb).

### 3. Knowledge Book Generation

Create comprehensive knowledge books:

```bash
python knowledge_book_generation.py \
  --load_type OPENAI \
  --api_base http://localhost:8001/v1 \
  --api_key EMPTY \
  --data_num 50 \
  --truth_num 4 \
  --action_num 6 \
  --valid_truth_num 1 \
  --domain MedicalEnv
```

Check [examples/knowledge_book_generation.sh](https://github.com/linhaowei1/kumo/blob/main/generate.ipynb).

### 4. Knowledge Book Revision (Optional)

Optionally refine knowledge books:

```bash
python generate/knowledge_book_revision.py \
  --load_type OPENAI \
  --api_base http://localhost:8001/v1 \
  --api_key EMPTY \
  --domain MedicalEnv \
  --revision_template_path ./templates/revision_template.md
```

Detailed guide: [examples/knowledge_book_revision.sh](https://github.com/linhaowei1/kumo/blob/main/generate.ipynb).

---

## Evaluation

### Vanilla Agent

Supports OpenAI and Anthropic APIs. Evaluation scripts for models such as GPT-4o and o1-mini are available:

- Results: [results/](https://github.com/linhaowei1/kumo/tree/main/results)
- Scripts: [scripts/eval](https://github.com/linhaowei1/kumo/tree/main/scripts/eval)

Customize by modifying provided scripts with your API keys.

### SFT Agent

Train supervised fine-tuned (SFT) agents using provided golden trajectories:

- Example fine-tuning: [scripts/sft/demo.sh](https://github.com/linhaowei1/kumo/blob/main/scripts/sft/demo.sh)

### Custom Agents

To create your own custom agents (e.g., ReactAgent), see [agents/](https://github.com/linhaowei1/kumo/tree/main/agents).

---

**For additional support or inquiries, please contact the repository maintainers or open an issue.**
