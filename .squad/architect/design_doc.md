# Design Document: Stability & Logging Improvements

## 1. Project Overview
**Mission:** Implement a comprehensive stability review, deploy critical improvements, and add robust logging across the system.
**Goal:** Enhance the reliability, observability, and debuggability of the Squad Manager application by establishing a uniform logging strategy and shoring up error handling around critical agent orchestrations and API calls.

## 2. Language & Stack Selection
**Language:** Python 3.12+
**Reasoning:** Since this is an enhancement to the existing `squad-manager` framework, we will continue using Python. The standard library's `logging` module (or an advanced library like `structlog` or `loguru`, though standard `logging` integrated with `rich` is preferred for CLI tools) provides exactly what is needed to fulfill this mission while conforming to the project's ecosystem.

## 3. Toolchain & Standards
The update adheres to the strict "Skywalker Development Workflow":
*   **Package Manager:** `uv` (for ensuring consistent environments while testing improvements).
*   **Linter/Formatter:** `ruff` (to enforce clean syntax around logging statements).
*   **Type Checker:** `mypy` (strict mode, to catch potential regressions introduced during the stability review).
*   **Testing:** `pytest` (to verify that logging outputs correctly without breaking core logic).
*   **CI/CD:** GitHub Actions (for validating the Gauntlet on the stability feature branch).

## 4. Architectural Layout
Changes will be distributed across the core agent modules, establishing a central logging configuration.

```text
squad-manager/
├── src/
│   └── squad_manager/
│       ├── __init__.py
│       ├── utils/
│       │   └── logger.py       # NEW: Centralized logging configuration
│       ├── core/
│       │   └── dispatcher.py   # Add robust try/except blocks and trace logging
│       └── agents/
│           └── base.py         # Ensure all agents inherit standard logging methods
├── tests/
│   ├── __init__.py
│   └── test_logger.py          # NEW: Verify logging initialization and levels
├── .gitignore
├── pyproject.toml              
└── README.md                   # Document the new debugging/logging flags (e.g., --verbose)
```

## 5. Configuration (`pyproject.toml`)
The project maintains its core configuration. If a third-party logging library is chosen over `rich.logging`, it would be added here. Currently assuming standard library `logging` enhanced by `rich`.

```toml
[project]
name = "squad-manager"
version = "0.1.0"
description = "Autonomous Development Team - Stability & Logging Update"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "typer",
    "rich",         # Contains rich.logging.RichHandler
    "pydantic",
    "google-generativeai",
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
1.  **Logging Infrastructure**: Create `src/squad_manager/utils/logger.py` configuring a structured, leveled logging system (DEBUG, INFO, WARNING, ERROR, CRITICAL) utilizing `rich.logging.RichHandler` for clean CLI output.
2.  **Stability Audit**: Review all subprocess calls (e.g., `git`, `gh`, `uv`), API calls to Gemini, and file operations. Wrap vulnerable calls in specific `try/except` blocks.
3.  **Instrumentation**: Inject logging statements:
    *   `INFO`: High-level workflow progress (e.g., "Agent Architect deployed").
    *   `DEBUG`: Command strings, payload data, and intermediate state (e.g., "Running command: `uv run pytest`").
    *   `ERROR`: Exception stack traces and failure contexts.
4.  **CLI Updates**: Add a `--verbose` or `-v` flag to the main `typer` entry point to dynamically set the log level to `DEBUG`.
5.  **Local Gauntlet**: Run `uv run ruff check . --fix`, `uv run ruff format .`, `uv run mypy src`, and `uv run pytest` to ensure the logging integration introduces no regressions.
6.  **Release**: Branch (`feature/stability-logging`), push, PR, merge, and upgrade.