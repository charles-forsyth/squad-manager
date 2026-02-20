# Design Document: new-project (Agent Calls Update)

## 1. Project Overview
**Mission:** Update our calls to our agents with a model declaration in the gemini CLI: `--yolo -r --model gemini-3.1-pro-preview`.
**Goal:** Enhance the autonomous agent orchestration by explicitly defining the advanced reasoning model (`gemini-3.1-pro-preview`) and leveraging bypass flags (`--yolo`, `-r`) for seamless, uninterrupted execution.

## 2. Language & Stack Selection
**Language:** Python 3.12+
**Reasoning:** Since this updates the existing `squad-manager` infrastructure (or acts as a companion automation), Python remains the optimal choice. It provides robust tools (`subprocess`, `shlex`) for constructing and executing CLI commands, and aligns perfectly with the "Skywalker" development workflow.

## 3. Toolchain & Standards
The update will strictly adhere to the project's established "Skywalker" standard toolchain:
*   **Package Manager:** `uv` (for rapid dependency management).
*   **Linter/Formatter:** `ruff` (to maintain clean, consistent command construction logic).
*   **Type Checker:** `mypy` (strict mode, to ensure type safety when passing command arguments).
*   **Testing:** `pytest` (to mock CLI calls and verify the correct flags are appended).
*   **CI/CD:** GitHub Actions (for automated validation before merging).

## 4. Architectural Layout
The core changes will occur within the existing agent dispatch/calling logic.

```text
squad-manager/
├── .github/
│   └── workflows/
│       └── ci.yml          # Executes the Gauntlet on PRs
├── src/
│   └── squad_manager/
│       ├── __init__.py
│       └── core/
│           └── dispatcher.py # Target file: update the gemini CLI invocation logic
├── tests/
│   ├── __init__.py
│   └── test_dispatcher.py  # Target file: add tests to verify the new flags
├── .gitignore
├── .python-version
├── pyproject.toml          # Enforces the toolchain standards
└── README.md               # Must be updated to document the new model usage
```

## 5. Configuration (`pyproject.toml`)
Ensure the project maintains its strict configuration:

```toml
[project]
name = "squad-manager"
version = "0.1.0"
description = "Autonomous Development Team - Updated to gemini-3.1-pro-preview"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "typer",
    "rich",
    "pydantic",
]

[tool.uv]
dev-dependencies = [
    "mypy>=1.0",
    "pytest>=8.0",
    "ruff>=0.3.0",
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
1.  **Codebase Investigation**: Locate the exact functions where the `gemini` command is constructed and dispatched to the agents (likely in `dispatcher.py` or similar).
2.  **Implementation**: Update the command construction logic to append the required flags: `--yolo -r --model gemini-3.1-pro-preview`.
3.  **Testing Strategy**: Update or write new `pytest` cases that mock the `subprocess.run` (or equivalent) call to assert that the constructed command string correctly includes the new flags.
4.  **Local Gauntlet**: Run `ruff check`, `ruff format`, `mypy`, and `pytest` locally to ensure no regressions.
5.  **Documentation**: Update the `README.md` to indicate that the agents now default to the `gemini-3.1-pro-preview` model.
6.  **Release**: Commit via a feature branch, create a PR, and merge following the Skywalker workflow.