import pytest
from pathlib import Path
import tomllib

@pytest.fixture
def project_root():
    """Returns the project root directory."""
    return Path(__file__).parent.parent

@pytest.fixture
def project_name(project_root):
    """Extracts the project name from pyproject.toml."""
    pyproject_path = project_root / "pyproject.toml"
    if not pyproject_path.exists():
        return "unknown_project"
    
    with open(pyproject_path, "rb") as f:
        data = tomllib.load(f)
        return data.get("project", {}).get("name", "unknown_project")

def test_src_layout_exists(project_root, project_name):
    """Test that the standard src layout is used."""
    src_dir = project_root / "src"
    assert src_dir.exists(), "The 'src' directory is missing from the project root."
    assert src_dir.is_dir(), "'src' must be a directory."
    
    # Check for the inner package directory
    # Converts something like "squad-manager" to "squad_manager"
    package_name = project_name.replace("-", "_")
    package_dir = src_dir / package_name
    
    assert package_dir.exists(), f"Package directory 'src/{package_name}' is missing."
    assert package_dir.is_dir(), f"'src/{package_name}' must be a directory."
    assert (package_dir / "__init__.py").exists(), f"'src/{package_name}/__init__.py' is missing."

def test_github_workflows_exists(project_root):
    """Test that the .github/workflows directory exists for CI/CD."""
    workflows_dir = project_root / ".github" / "workflows"
    assert workflows_dir.exists(), "'.github/workflows' directory is missing."
    assert workflows_dir.is_dir(), "'.github/workflows' must be a directory."
    
    # Optional: check if at least one .yml file exists
    yml_files = list(workflows_dir.glob("*.yml")) + list(workflows_dir.glob("*.yaml"))
    assert len(yml_files) > 0, "No workflow YAML files found in '.github/workflows'."
