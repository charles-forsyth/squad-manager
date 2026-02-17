import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest


@pytest.fixture
def project_root() -> Path:
    """Returns the project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture
def scripts_dir(project_root: Path) -> Path:
    """Returns the scripts directory."""
    return project_root / "scripts"


@pytest.fixture
def setup_squad_env(tmp_path: Path, scripts_dir: Path) -> tuple[Path, Path]:
    """Sets up a temporary environment with necessary scripts and project.json."""
    # Copy scripts to tmp_path/scripts so we can mock call.sh
    tmp_scripts = tmp_path / "scripts"
    tmp_scripts.mkdir()

    # Copy director.sh
    shutil.copy(scripts_dir / "director.sh", tmp_scripts / "director.sh")

    # Create a mock call.sh
    mock_call = tmp_scripts / "call.sh"
    mock_call.write_text('#!/bin/bash\necho "Mock Call: Agent=$1 Prompt=$2"\n')
    mock_call.chmod(0o755)

    # Create .squad directory and project.json
    squad_dir = tmp_path / ".squad"
    squad_dir.mkdir()

    project_json = squad_dir / "project.json"
    initial_data = {
        "project_name": "test-project",
        "mission": "old mission",
        "status": "planning",
        "version": "0.1.0",
    }
    project_json.write_text(json.dumps(initial_data))

    # Configure git locally to avoid failures
    subprocess.run(
        ["git", "config", "--global", "user.email", "you@example.com"], cwd=tmp_path
    )
    subprocess.run(
        ["git", "config", "--global", "user.name", "Your Name"], cwd=tmp_path
    )

    # Let's just set environment variables for git commits.
    os.environ["GIT_AUTHOR_NAME"] = "Test User"
    os.environ["GIT_AUTHOR_EMAIL"] = "test@example.com"
    os.environ["GIT_COMMITTER_NAME"] = "Test User"
    os.environ["GIT_COMMITTER_EMAIL"] = "test@example.com"

    return tmp_path, tmp_scripts


def test_director_updates_mission(setup_squad_env: tuple[Path, Path]) -> None:
    """Test that director.sh updates the mission in project.json."""
    tmp_path, tmp_scripts = setup_squad_env
    director_script = tmp_scripts / "director.sh"

    mission = "New Mission: Build a Death Star"

    # Run director.sh
    result = subprocess.run(
        [str(director_script), mission], cwd=tmp_path, capture_output=True, text=True
    )

    assert result.returncode == 0, f"Script failed:\n{result.stdout}\n{result.stderr}"

    # Verify project.json update
    project_json = tmp_path / ".squad" / "project.json"
    data = json.loads(project_json.read_text())

    assert data["mission"] == mission
    assert data["status"] == "active"


def test_director_init_git(setup_squad_env: tuple[Path, Path]) -> None:
    """Test that director.sh initializes git if missing."""
    tmp_path, tmp_scripts = setup_squad_env
    director_script = tmp_scripts / "director.sh"

    mission = "Git Init Test"

    subprocess.run(
        [str(director_script), mission], cwd=tmp_path, check=True, capture_output=True
    )

    assert (tmp_path / ".git").exists()
    assert (tmp_path / ".git").is_dir()
    assert (tmp_path / "README.md").exists()


def test_director_creates_branch(setup_squad_env: tuple[Path, Path]) -> None:
    """Test that director.sh creates a feature branch."""
    tmp_path, tmp_scripts = setup_squad_env
    director_script = tmp_scripts / "director.sh"

    mission = "Branch Test"

    subprocess.run(
        [str(director_script), mission], cwd=tmp_path, check=True, capture_output=True
    )

    # Check current branch
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )

    branch_name = result.stdout.strip()
    assert branch_name.startswith("feature/mission-")
