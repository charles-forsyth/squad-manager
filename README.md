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

---

## 🚀 Installation

### Option 1: Install as a Gemini Skill (Recommended)
Install directly from GitHub to use the `/squad` commands within Gemini:

```bash
gemini skills install https://github.com/charles-forsyth/squad-manager.git
```

**Note:** To use the scripts (Director Mode) directly from your shell, add the skill's script directory to your PATH:
```bash
export PATH="$HOME/.gemini/skills/squad-manager/scripts:$PATH"
```

### Option 2: Clone for Local Development
If you want to modify the squad or run scripts locally without installing as a skill:
1.  **Clone:** `git clone https://github.com/charles-forsyth/squad-manager.git`
2.  **Setup:** `cd squad-manager && chmod +x scripts/*.sh`
3.  **Path:** `export PATH="$PWD/scripts:$PATH"`

### Prerequisites
*   **Git:** `sudo apt install git` (or equivalent)
*   **GitHub CLI (gh):** `sudo apt install gh`
*   **Gemini CLI:** Ensure you have the Gemini CLI installed and configured.

---

## 📦 Publishing & Sharing

There is currently no centralized "Extension Gallery" for Gemini skills. To share your squad with the world:

1.  **Push to GitHub:** Ensure your repository is public.
2.  **Share the URL:** Users can install your skill immediately using:
    ```bash
    gemini skills install https://github.com/your-username/squad-manager.git
    ```

---

## ⚙️ Configuration

Before deploying your squad, ensure your environment is ready.

1.  **Gemini API Key:**
    ```bash
    export GEMINI_API_KEY="your_api_key_here"
    ```

2.  **GitHub Authentication:**
    The squad needs to create PRs and Releases on your behalf.
    ```bash
    gh auth login
    ```

3.  **Git Identity:**
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"
    ```

---

## 🎮 Usage

You can interact with the Squad in two ways: via the **Gemini CLI** (Agentic Mode) or directly via **Shell Scripts** (Manual Mode).

### Method 1: Agentic Mode (Recommended)
This requires the `squad-manager` skill to be active in your Gemini session.

```bash
# Deploy the squad to the current directory
gemini "/squad deploy"

# Start a new mission
gemini "/squad build 'Create a CLI tool to fetch weather data'"
```

### Method 2: Manual Mode (Scripting)
You can invoke the director script directly to bypass the chat interface.

```bash
# Initialize a new project with the squad
./scripts/deploy.sh

# Run the Director with a mission
./scripts/director.sh "Build a REST API using FastAPI"
```

---

## 💡 Examples

### Example 1: The Python CLI
**Mission:** "Create a tool called 'weather-cli' that takes a city name and returns the temperature."

**Workflow:**
1.  **Architect** chooses Python + `typer` + `httpx`.
2.  **Sentinel** writes `test_weather.py` checking for valid/invalid city inputs.
3.  **DevOps** creates `pyproject.toml` and bumps version to `0.1.0`.
4.  **Grunt** implements the API call logic.
5.  **Gatekeeper** runs `pytest` and passes.
6.  **UAT** installs the tool and runs `weather-cli London`.

### Example 2: The Node.js Microservice
**Mission:** "Create an Express.js server with a health check endpoint."

**Workflow:**
1.  **Architect** chooses Node.js + `express` + `typescript`.
2.  **Sentinel** writes a `supertest` spec.
3.  **DevOps** runs `npm init` and `npm version patch`.
4.  **Grunt** writes `src/index.ts`.
5.  **Gatekeeper** runs `npm test`.

---

## 💻 Development

We welcome contributions! Please follow the **Skywalker Development Workflow**:

1.  **Branch:** Always work in a feature branch (`feature/my-feature`).
2.  **Bump:** Increment the version in `pyproject.toml`.
3.  **Gauntlet:** Ensure `uv run ruff check` and `uv run pytest` pass locally.
4.  **PR:** Open a Pull Request via `gh pr create`.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
