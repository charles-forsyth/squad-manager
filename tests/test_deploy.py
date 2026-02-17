import json
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


def test_deploy_creates_squad_structure(
    tmp_path: Path, scripts_dir: Path, project_root: Path
) -> None:
    """Test that deploy.sh creates the correct directory structure and files."""
    deploy_script = scripts_dir / "deploy.sh"

    # We need to copy the script and personas to the temp dir to simulate running
    # from the project root or adjust the script to handle relative paths correctly
    # when run from elsewhere. The script uses `dirname $0` to find its location,
    # so we can run it from anywhere as long as we point to it.
    # However, it expects `personas/` to be relative to `scripts/../personas`.

    # Let's run the script from the project root, but target the tmp_path.
    # deploy.sh creates .squad in the current working directory.
    # So we should change the current working directory to tmp_path when running script.

    result = subprocess.run(
        [str(deploy_script)], cwd=tmp_path, capture_output=True, text=True
    )

    assert result.returncode == 0, (
        f"Script failed with output:\n{result.stdout}\n{result.stderr}"
    )

    squad_dir = tmp_path / ".squad"
    assert squad_dir.exists()
    assert squad_dir.is_dir()

    # Check for agent directories
    agents = ["architect", "grunt", "sentinel", "gatekeeper", "uat", "devops"]
    for agent in agents:
        agent_dir = squad_dir / agent / ".gemini"
        assert agent_dir.exists(), f"Agent directory for {agent} not found"
        gemini_md = agent_dir / "GEMINI.md"
        assert gemini_md.exists(), f"GEMINI.md for {agent} not found"

        # Verify content matches source persona
        source_persona = project_root / "personas" / f"{agent}.md"
        if source_persona.exists():
            assert gemini_md.read_text() == source_persona.read_text()

    # Check project.json
    project_json = squad_dir / "project.json"
    assert project_json.exists()

    data = json.loads(project_json.read_text())
    assert data["project_name"] == "new-project"
    assert data["status"] == "planning"
    assert data["version"] == "0.1.0"


def test_deploy_idempotency(tmp_path: Path, scripts_dir: Path) -> None:
    """Test that running deploy.sh twice respects existing project.json."""
    deploy_script = scripts_dir / "deploy.sh"

    # First run
    subprocess.run([str(deploy_script)], cwd=tmp_path, check=True)

    # Modify project.json
    project_json = tmp_path / ".squad" / "project.json"
    original_data = json.loads(project_json.read_text())
    original_data["project_name"] = "modified-project"
    project_json.write_text(json.dumps(original_data))

    # Second run
    result = subprocess.run(
        [str(deploy_script)], cwd=tmp_path, capture_output=True, text=True
    )
    assert result.returncode == 0

    # Check that project.json was NOT overwritten
    data = json.loads(project_json.read_text())
    assert data["project_name"] == "modified-project"
