#!/bin/bash
# Usage: ./director.sh "Mission Description"

MISSION=$1

if [ -z "$MISSION" ]; then
  echo "Usage: /squad build <mission_description>"
  exit 1
fi

SCRIPT_DIR=$(dirname "$0")
PROJECT_JSON=".squad/project.json"

if [ ! -f "$PROJECT_JSON" ]; then
  echo "Error: .squad/project.json not found. Run '/squad deploy' first."
  exit 1
fi

# 1. Initialize Git if needed
if [ ! -d ".git" ]; then
    echo "Initializing Git..."
    git init
    git branch -m master
    if [ ! -f "README.md" ]; then
      echo "# Project" > README.md
    fi
    git add README.md
    git commit -m "Initial commit"
fi

# 2. Update project.json mission
echo "🎬 Director: Updating mission in project.json..."
python3 -c "
import json
import sys
import os

path = '$PROJECT_JSON'
mission = sys.argv[1]

if os.path.exists(path):
    with open(path, 'r') as f:
        data = json.load(f)
    data['mission'] = mission
    data['status'] = 'active'
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
" "$MISSION"

# 3. Create Feature Branch
BRANCH_NAME="feature/mission-$(date +%s)"
echo "🌿 Creating branch: $BRANCH_NAME"
git checkout -b "$BRANCH_NAME"

# 4. Architect
echo "------------------------------------------------"
echo "🏗️ Architect: Designing..."
"$SCRIPT_DIR/call.sh" architect "Read the mission in '../project.json'. Determine the best language/stack. Generate/Update 'design_doc.md' using write_file."

# 5. Sentinel
echo "------------------------------------------------"
echo "🛡️ Sentinel: Writing Tests..."
"$SCRIPT_DIR/call.sh" sentinel "Read '../architect/design_doc.md'. Generate/update test files (e.g. tests/test_*.py or *.test.ts) using write_file."

# 6. DevOps (Bump)
echo "------------------------------------------------"
echo "📦 DevOps: Preparing Version..."
"$SCRIPT_DIR/call.sh" devops "Read 'design_doc.md'. Check for package config (pyproject.toml/package.json/go.mod). Initialize if missing. Bump patch version. Git add/commit."

# 7. Grunt
echo "------------------------------------------------"
echo "🛠️ Grunt: Implementing Code..."
"$SCRIPT_DIR/call.sh" grunt "Read specs. Implement code in the chosen language. Run appropriate linters/tests (e.g. uv run ruff/pytest, npm test). If pass, git add & commit."

# 8. Gatekeeper
echo "------------------------------------------------"
echo "👿 Gatekeeper: Auditing..."
"$SCRIPT_DIR/call.sh" gatekeeper "Audit the branch '$BRANCH_NAME'. Run appropriate tests. If pass, merge into master."

# 9. DevOps (Release)
echo "------------------------------------------------"
echo "🚀 DevOps: Releasing..."
"$SCRIPT_DIR/call.sh" devops "Create a git tag. If 'gh' is configured, create a GitHub Release."

# 10. UAT
echo "------------------------------------------------"
echo "🎮 UAT: Verifying..."
"$SCRIPT_DIR/call.sh" uat "Play/Run the application based on the mission. Verify installation and functionality."

echo "------------------------------------------------"
echo "🏁 Director: Mission Complete."
