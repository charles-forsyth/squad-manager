# Design Document: Squad Manager

## 1. Project Overview
**Mission:** Develop and maintain "Squad Manager", an autonomous development team for the Gemini CLI.
**Goal:** Empower users to orchestrate a squad of specialized AI agents (Architect, DevOps, Sentinel, Grunt, Gatekeeper, UAT) to execute full engineering lifecycles—from architecture to release.

## 2. Language & Stack Selection
**Language:** Python 3.12+
**Reasoning:** Python provides the ideal ecosystem for CLI tools and AI agent orchestration. The project leverages `uv` for superior dependency management and speed, aligning with the "Skywalker" workflow.

## 3. Toolchain & Standards
We utilize the strict "Skywalker" standard toolchain:
*   **Package Manager:** `uv` (for project management, virtual environments, and tool installation).
*   **Linter/Formatter:** `ruff` (enforcing strict code style and quality).
*   **Type Checker:** `mypy` (strict static typing).
*   **Testing:** `pytest` (comprehensive unit and integration testing).
*   **CI/CD:** GitHub Actions (automating the "Gatekeeper" checks).

## 4. Architectural Layout
The project follows a `src` layout with a clear separation of concerns for each agent persona.

```text
squad-manager/
├── .squad/                 # Agent-specific configurations and memory
│   ├── architect/
│   ├── devops/
│   ├── gatekeeper/
│   ├── grunt/
│   ├── sentinel/
│   └── uat/
├── assets/                 # Static assets (templates, prompts)
├── personas/               # Markdown definitions of agent personas
├── scripts/                # Helper scripts for agent execution
├── src/
│   └── squad_manager/      # Main package
│       ├── __init__.py
│       ├── core/           # Core logic for agent orchestration
│       ├── agents/         # Implementation of individual agents
│       └── utils/          # Shared utilities (git, gh, file ops)
├── tests/                  # Test suite
│   ├── __init__.py
│   └── test_*.py
├── .gitignore
├── .python-version
├── pyproject.toml          # Central configuration
├── README.md               # User documentation
├── SKILL.md                # Gemini CLI skill definition
└── uv.lock
```

## 5. Configuration (`pyproject.toml`)
The project is configured for strict adherence to standards:

```toml
[project]
name = "squad-manager"
version = "0.1.0" # Managed by DevOps/Semantic Versioning
description = "The Ultimate Autonomous Development Team for Gemini CLI"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "typer",        # For CLI interface
    "rich",         # For beautiful terminal output
    "pydantic",     # For data validation
    "google-generativeai", # For Gemini API interaction
]

[tool.uv]
dev-dependencies = [
    "mypy>=1.0",
    "pytest>=8.0",
    "ruff>=0.3.0",
    "types-requests",
    "types-PyYAML",
]

[tool.ruff]
line-length = 88
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP"] 

[tool.mypy]
strict = true
python_version = "3.12"
```

## 6. Implementation Plan
1.  **Core Framework**: Establish the `squad_manager` package structure and CLI entry point using `typer`.
2.  **Agent Logic**: Implement the `Director` to parse prompts and dispatch tasks to specific agents.
3.  **Integration**: Connect the `SKILL.md` to the Python CLI, allowing `gemini` to invoke `squad-manager` commands.
4.  **Testing**: Develop a comprehensive test suite to verify agent interactions and tool execution.
5.  **Release**: Use `uv tool` for easy installation and updates.
