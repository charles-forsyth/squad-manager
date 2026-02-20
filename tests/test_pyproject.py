import tomllib
from pathlib import Path
from typing import Any

import pytest


@pytest.fixture
def pyproject_data() -> dict[str, Any]:
    """Returns the parsed pyproject.toml data."""
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    if not pyproject_path.exists():
        pytest.fail("pyproject.toml does not exist in the project root.")

    with open(pyproject_path, "rb") as f:
        return tomllib.load(f)


def test_pyproject_has_project_section(pyproject_data: dict[str, Any]) -> None:
    """Test that the [project] section exists and has required fields."""
    assert "project" in pyproject_data, (
        "pyproject.toml is missing the [project] section."
    )
    project = pyproject_data["project"]

    assert "name" in project, "Project name is missing."
    assert "version" in project, "Project version is missing."
    assert "description" in project, "Project description is missing."
    assert "readme" in project, "Project readme is missing."
    assert "requires-python" in project, "Project requires-python is missing."


def test_pyproject_dependencies(pyproject_data: dict[str, Any]) -> None:
    """Test that required project dependencies are specified."""
    assert "project" in pyproject_data, "Missing [project] section"
    project = pyproject_data["project"]

    deps = project.get("dependencies", [])
    deps_str = " ".join(deps).lower()

    assert "typer" in deps_str, "typer is missing from dependencies."
    assert "rich" in deps_str, "rich is missing from dependencies."
    assert "pydantic" in deps_str, "pydantic is missing from dependencies."
    assert "google-generativeai" in deps_str, (
        "google-generativeai is missing from dependencies."
    )


def test_pyproject_dev_dependencies(pyproject_data: dict[str, Any]) -> None:
    """Test that required dev dependencies (pytest, ruff, mypy) are specified."""
    assert "tool" in pyproject_data, "Missing [tool] section"
    assert "uv" in pyproject_data["tool"], "Missing [tool.uv] section"

    dev_deps = pyproject_data["tool"]["uv"].get("dev-dependencies", [])

    dev_deps_str = " ".join(dev_deps).lower()

    assert "pytest" in dev_deps_str, "pytest is missing from dev-dependencies."
    assert "ruff" in dev_deps_str, "ruff is missing from dev-dependencies."
    assert "mypy" in dev_deps_str, "mypy is missing from dev-dependencies."


def test_pyproject_ruff_config(pyproject_data: dict[str, Any]) -> None:
    """Test that ruff is configured correctly per the design doc."""
    assert "tool" in pyproject_data
    assert "ruff" in pyproject_data["tool"]

    ruff_config = pyproject_data["tool"]["ruff"]
    assert ruff_config.get("line-length") == 88, "ruff line-length should be 88"
    assert ruff_config.get("target-version") == "py312", (
        "ruff target-version should be py312"
    )

    assert "lint" in ruff_config, "Missing [tool.ruff.lint] section"
    lint_select = ruff_config["lint"].get("select", [])

    expected_lints = ["E", "F", "I", "B", "UP"]
    for expected in expected_lints:
        assert expected in lint_select, f"ruff lint.select is missing '{expected}'"


def test_pyproject_mypy_config(pyproject_data: dict[str, Any]) -> None:
    """Test that mypy is configured strictly."""
    assert "tool" in pyproject_data
    assert "mypy" in pyproject_data["tool"]

    mypy_config = pyproject_data["tool"]["mypy"]
    assert mypy_config.get("strict") is True, "mypy strict mode must be enabled (true)"
    assert mypy_config.get("python_version") == "3.12", (
        "mypy python_version should be 3.12"
    )
