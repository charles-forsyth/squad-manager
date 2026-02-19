# Design Document: new-project

## 1. Project Overview
**Mission:** Check for errors and publish.
**Goal:** Implement an automated workflow to validate code quality (linting, type checking, testing) and handle the publishing process, adhering to the "Skywalker" standards.

## 2. Language & Stack Selection
**Language:** Python 3.12+
**Reasoning:** Python is the primary language for the Skywalker ecosystem. Its toolchain (`uv`, `ruff`, `mypy`) provides the best support for "checking for errors", and its integration with GitHub Actions (`gh`) makes "publishing" seamless.

## 3. Toolchain & Standards
The project will enforce the "Local Gauntlet" and "Gatekeeper" standards:
*   **Package Manager:** `uv`
*   **Linter/Formatter:** `ruff`
*   **Type Checker:** `mypy` (strict mode)
*   **Testing:** `pytest`
*   **Publishing Tool:** `uv build` and `gh release` / `twine` (if PyPI).

## 4. Architectural Layout
The project structure is designed to support automated validation and publishing.

```text
new-project/
├── .github/
│   └── workflows/
│       ├── ci.yml          # The "Gatekeeper": Runs the Gauntlet on PRs
│       └── release.yml     # The "Publisher": Handles versioning and releases
├── src/
│   └── new_project/
│       ├── __init__.py
│       └── core.py         # Logic for error checking or the tool itself
├── tests/
│   ├── __init__.py
│   └── test_core.py      
├── .gitignore
├── .python-version
├── pyproject.toml          # Central configuration for all tools
└── README.md               
```

## 5. Configuration (`pyproject.toml`)
```toml
[project]
name = "new-project"
version = "0.1.0"
description = "A Skywalker-standard project for automated error checking and publishing."
readme = "README.md"
requires-python = ">=3.12"
dependencies = []

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
1.  **Environment Setup**: Initialize with `uv init` and configure `pyproject.toml`.
2.  **Validation Logic**: Implement or configure `ruff`, `mypy`, and `pytest` to ensure zero errors.
3.  **CI/CD Integration**: Create GitHub Action workflows (`ci.yml`) to automate the "Gauntlet".
4.  **Publishing Workflow**: Define the release process (version bumping, tagging, and deployment).
5.  **Final Verification**: Manually trigger the Gauntlet and a dry-run of the publish command.
