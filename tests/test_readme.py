from pathlib import Path


def test_readme_exists():
    """Test that the README.md file exists."""
    readme_path = Path("README.md")
    assert readme_path.exists(), "README.md should exist in the project root."


def test_readme_not_empty():
    """Test that the README.md file is not empty."""
    readme_path = Path("README.md")
    content = readme_path.read_text(encoding="utf-8")
    assert len(content) > 100, "README.md should have substantial content."


def test_readme_required_sections():
    """Test that the README.md contains key sections required by the mission."""
    readme_path = Path("README.md")
    content = readme_path.read_text(encoding="utf-8")

    required_sections = [
        "# Squad Manager",
        "## 🔥 Features",
        "### 🎬 Director Mode",
        "### 👥 The Agent Roster",
        "## 🚀 Installation",
        "## 🎮 Usage",
        "## ⚙️ Configuration",
        "## 🛠️ Troubleshooting",
    ]

    missing_sections = [
        section for section in required_sections if section not in content
    ]
    assert not missing_sections, (
        f"README.md is missing required sections: {missing_sections}"
    )


def test_no_placeholders():
    """Test that the README.md does not contain any TBD or placeholders."""
    readme_path = Path("README.md")
    content = readme_path.read_text(encoding="utf-8")
    placeholders = ["[TBD]", "FIXME", "TODO", "INSERT HERE"]

    found_placeholders = [p for p in placeholders if p in content]
    assert not found_placeholders, (
        f"README.md contains placeholders: {found_placeholders}"
    )
