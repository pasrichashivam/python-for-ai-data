# Python for AI & Data

## Repository Overview

This repository contains a curated set of Jupyter notebooks designed to build a strong Python foundation for data and AI work. It is structured to help learners progress from core language skills to advanced topics used in modern AI engineering:
- Python basics and data handling
- decorators and advanced function patterns
- `pydantic` for validation and data modeling
- asynchronous programming with `asyncio`
- Building AI agents using plain Python without external frameworks

The notebooks focus on practical examples and runnable code so learners can explore and adapt the patterns for Data and AI use cases.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/pasrichashivam/python-for-ai-data.git
cd python-for-ai-data
```

2. Sync the project with `uv` if available in your environment:

```bash
uv sync
```

This opens the project in a compatible editor or syncs the workspace. If `uv` is not available, use your preferred editor or IDE.

3. Install dependencies if required by a notebook environment. If you are using a Python virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If there is no requirements file, the notebooks are designed to work with a standard Python setup and common AI/data libraries.

## Repository Structure

| Path | Description |
| --- | --- |
| `01-python-basics.ipynb` | Python fundamentals for AI and data work, variables, control flow, collections, and functions |
| `02-decorators.ipynb` | Decorator patterns, higher-order functions, and practical uses in data pipelines |
| `03-pydantic.ipynb` | Data validation, typed models, settings, and best practices using `pydantic` |
| `04-async-python.ipynb` | Async programming with `asyncio`, concurrency patterns, and network IO examples |
| `05-ai-agents.ipynb` | Building simple AI agents and workflows using bare Python logic, without external frameworks |

## Learning Path

The repository follows a step-by-step learning path:

1. Learn Python fundamentals and idiomatic code.
2. Master decorators to build reusable abstractions.
3. Use `pydantic` to validate and structure data.
4. Add async programming skills for scalable IO and workflows.
5. Build AI agent logic with bare Python, focusing on design rather than framework usage.

### Learning Path Diagram

```
[Decorators] --> [Pydantic] --> [Async Python] --> [AI Agents]
      |                |               |                 |                 
      v                v               v                 v               
    Better            Strong          Concurrent       Framework-
    abstractions      validation      pipelines        free AI logic
```

## How to Use the Notebooks

- Open each notebook sequentially to follow the learning flow.
- Run the examples and modify code blocks to experiment with behavior.
- Use the notebooks as templates for new AI and data projects.
- Combine patterns from multiple notebooks to build more advanced applications.


## Notes

- This repository is ideal for learners who want to move beyond libraries and understand the Python foundations underpinning modern AI systems.
- The emphasis is on simple, practical examples that can be reused in real projects.
- If you add new notebooks or resources, update the table above so the structure stays accurate.
