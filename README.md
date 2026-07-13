# Python for AI & Data

## Repository Overview

This repository contains a curated set of Jupyter notebooks designed to build a strong Python foundation for data and AI work. It is structured to learn and progress from core language skills to advanced topics used in modern AI engineering:
- `decorators` and advanced function patterns
- `pydantic` for validation and data modeling
- `asyncio` for asynchronous programming  
- Building <b>AI agents using plain Python</b> without external frameworks

The notebooks focus on practical examples and runnable code so we can explore and adapt the patterns for Data and AI use cases.

### Learning Path Diagram

```
[Decorators] --> [Pydantic] --> [Async Python] --> [AI Agents]
      |                |               |                 |                 
      v                v               v                 v               
   Better            Strong          Concurrent       Framework-
abstractions        validation       executions      free AI logic
```

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

If `uv` is not available, use your preferred package manager.

3. Install dependencies required by a notebook environment. If you are using a Python virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Repository Structure

| Module | Description |
| ------ | --- |
| `01-decorators` | Decorator patterns, higher-order functions, and practical uses in data pipelines and AI|
| `02-pydantic_models` | Data validation, typed models, settings, and best practices using `pydantic` with AI|
| `03-async_runs` | Step bt step progess with Async programming with `asyncio`, concurrency patterns |
| `04-ai-agent_building` | Building simple AI agents and workflows using bare Python logic, without external frameworks |

## Learning Path

The repository follows a step-by-step learning path:

1. Master decorators to build reusable abstractions.
2. Use `pydantic` to validate and structure data.
3. Add async programming skills for scalable API calls, IO and workflows.
4. Build AI agent logic with bare Python, focusing on design rather than framework usage.

## How to Use the Notebooks

- Open each notebook sequentially to follow the learning flow.
- Run the examples and modify code blocks to experiment with behavior.
- Use the notebooks as templates for new AI and data projects.
- Combine patterns from multiple notebooks to build more advanced applications.


## Notes

- This repository is ideal for learners who want to move beyond libraries and understand the Python foundations underpinning modern AI systems.
- The emphasis is on simple, practical examples that can be reused in real projects.
