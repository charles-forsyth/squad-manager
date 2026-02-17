# Squad Manager 🤖🚀
**The Ultimate Autonomous Development Team for Gemini CLI**

Stop babysitting your AI. Start directing a squad.

**Squad Manager** is not just another coding assistant. It's a **fully autonomous software development agency** living in your terminal. You give the order, and a specialized team of AI agents executes the entire engineering lifecycle—from architecture to release.

---

## 🔥 Features

### 🎬 Director Mode: One Prompt -> Full App
Forget chat-pong. With **Director Mode**, you provide **one high-level mission**, and the Squad takes over.

```bash
gemini "/squad build 'Create a snake game in Python'"
```

The Director orchestrates the entire workflow:
1.  **🏗️ Architect:** Designs the system & chooses the best stack (Python/Node/Go).
2.  **🛡️ Sentinel:** Writes the test suite *before* a single line of code is written (TDD).
3.  **📦 DevOps:** Initializes the repo, manages `pyproject.toml` or `package.json`, and bumps versions.
4.  **🛠️ Grunt:** Implements the actual code to pass the tests.
5.  **👿 Gatekeeper:** Audits the PR, runs the final gauntlet, and enforces quality before merging.
6.  **🚀 DevOps (Release):** Tags the version and creates a GitHub Release.
7.  **🎮 UAT:** Verifies the installation and functionality from a user's perspective.

### 👥 The Agent Roster
Your new team is ready to work 24/7. No coffee breaks. No complaints.

*   **🏗️ Architect:** The visionary. Decides the tech stack, file structure, and high-level design in `design_doc.md`.
*   **🛠️ Grunt:** The builder. Writes the implementation code. Polyglot expert in Python, Node, and Go.
*   **🛡️ Sentinel:** The protector. Writes comprehensive test suites (pytest, vitest, etc.) before implementation.
*   **📦 DevOps:** The release manager. Handles packaging, versioning, git tags, and release notes.
*   **👿 Gatekeeper:** The enforcer. Strict CI/CD auditor that prevents bad code from reaching `master`.
*   **🎮 UAT:** The user. Actually installs and verifies the application works as expected.

### 🌐 Polyglot Powerhouse
The Squad speaks your language. Whether it's **Python (uv)**, **Node.js (npm)**, or **Go (go mod)**, the agents adapt their tools and workflows automatically.

### 🚫 The End of Babysitting
Most AI coding tools require you to copy-paste code, fix imports, and debug errors. **Squad Manager** does the debugging for you. If a test fails, the Grunt fixes it. If the build breaks, DevOps repairs it. **You simply review the PR.**

---

## 🚀 Installation

Install simply with `uv`:

```bash
uv tool install squad-manager
```

*Requires `git`, `gh` (GitHub CLI), and the `gemini-cli`.*

---

## 🎮 Usage

### 1. Deploy the Squad
Initialize your project with a full team of agents.
```bash
gemini "/squad deploy"
```

### 2. Give a Mission
Launch a full development cycle.
```bash
gemini "/squad build 'Build a CLI tool to track crypto prices'"
```

### 3. Call Specific Agents
Need a quick fix? Call an agent directly.
```bash
gemini "/squad call grunt 'Fix the bug in main.py'"
```

---

## ⚙️ Configuration

Squad Manager respects your environment. Ensure the following tools are configured:

- **Git:** Configured with your user name and email.
- **GitHub CLI (gh):** Authenticated via `gh auth login`.
- **Gemini CLI:** Installed and your API key set in `GEMINI_API_KEY`.
- **uv:** Highly recommended for Python projects.

---

## 🛠️ Troubleshooting

- **Agent Stalls:** If an agent seems stuck, check the logs or try calling them individually.
- **Git Conflicts:** Squad Manager works best on clean repositories. If you have uncommitted changes, stash or commit them first.
- **Model Errors:** Ensure you are using a supported model like `gemini-2.5-pro` for complex missions.

---

**Ready to fire your old workflow?**
Deploy your Squad today.

---
*Powered by Gemini CLI & The Skywalker Workflow.*
