from pathlib import Path

import pytest


@pytest.fixture
def project_root() -> Path:
    """Returns the project root directory."""
    return Path(__file__).parent.parent


def test_readme_exists(project_root: Path) -> None:
    """Test that the README.md file exists in the project root."""
    readme_path = project_root / "README.md"
    assert readme_path.exists(), f"README.md should exist at {readme_path}"


def test_readme_content_not_empty(project_root: Path) -> None:
    """Test that the README.md file is not empty."""
    readme_path = project_root / "README.md"
    if readme_path.exists():
        assert readme_path.stat().st_size > 0, "README.md should not be empty"


def test_readme_required_sections(project_root: Path) -> None:
    """Test that the README.md contains key sections defined in the design doc."""
    readme_path = project_root / "README.md"
    if not readme_path.exists():
        pytest.fail("README.md does not exist, cannot check sections.")

    content = readme_path.read_text(encoding="utf-8")

    # Required sections per Design Doc
    required_sections = ["Features", "Installation", "Usage", "Development", "License"]

    missing_sections = [
        section for section in required_sections if section not in content
    ]

    assert not missing_sections, (
        f"README.md is missing required sections: {missing_sections}"
    )


def test_readme_mentions_new_model(project_root: Path) -> None:
    """Test README explicit mention of new gemini-3.1-pro-preview model."""
    readme_path = project_root / "README.md"
    if not readme_path.exists():
        pytest.fail("README.md does not exist, cannot check for model mention.")

    content = readme_path.read_text(encoding="utf-8")
    assert "gemini-3.1-pro-preview" in content, (
        "README.md must mention the gemini-3.1-pro-preview model."
    )
