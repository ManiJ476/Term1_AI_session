# Copilot Instructions for AI Coding Agents

## Project Overview
This workspace contains Python scripts and Jupyter notebooks for AI coursework, exercises, and Project Euler problems. The codebase is organized by session and topic, with a focus on algorithmic problem solving and supervised learning.

## Directory Structure
- `session 0/` and `session 1/`: Main folders for coursework and exercises
- `project euler/`: Contains individual Python scripts for specific Project Euler problems
- Jupyter notebooks (e.g., `test.ipynb`) for interactive exploration

## Key Patterns and Conventions
- Each Project Euler problem is solved in a separate `.py` file named after the problem
- Scripts are standalone and do not import from each other
- No central package or module structure; treat each file as independent unless otherwise noted
- Naming follows the problem or exercise title for clarity

## Developer Workflows
- No build system or test framework detected; run scripts directly with Python
- For Jupyter notebooks, use the notebook interface for cell execution
- Debug by running scripts individually and inspecting output

## Integration Points
- No external dependencies or package requirements found; all code uses standard Python libraries
- If adding new dependencies, document them in a `requirements.txt` at the workspace root

## Examples
- To solve a new Project Euler problem, create a new `.py` file in `project euler/` with a descriptive name
- For supervised learning exercises, use or extend `supervised learning.py` in `session 1/`

## Recommendations for AI Agents
- When generating new solutions, follow the file naming and organization conventions
- Keep code self-contained unless explicitly refactoring for reuse
- Reference existing files for examples of problem-solving approaches
- Update this document if new workflows, dependencies, or conventions are introduced

## Key Files
- `README.md`: Minimal project description
- `session 1/supervised learning.py`: Example of a supervised learning exercise
- `session 1/project euler/`: Contains multiple algorithmic solutions

---
For questions or updates, ask the user for clarification on unclear workflows or conventions.
