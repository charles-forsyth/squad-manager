#!/bin/bash
# Usage: ./deploy.sh <squad_name>

SQUAD_NAME=${1:-skywalker}
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
SKILL_ROOT=$(dirname "$SCRIPT_DIR")
PERSONAS_DIR="$SKILL_ROOT/personas"
PROJECT_SQUAD_DIR=".squad"

echo "Deploying $SQUAD_NAME squad from $PERSONAS_DIR..."

mkdir -p "$PROJECT_SQUAD_DIR"

# Added DevOps to the list
AGENTS=("Architect" "Grunt" "Sentinel" "Gatekeeper" "UAT" "DevOps")

for agent in "${AGENTS[@]}"; do
  agent_lower=$(echo "$agent" | tr '[:upper:]' '[:lower:]')
  mkdir -p "$PROJECT_SQUAD_DIR/$agent_lower/.gemini"
  
  # The personas are stored as lowercase .md files in the skill
  PERSONA_FILE="$PERSONAS_DIR/$agent_lower.md"
  
  if [ -f "$PERSONA_FILE" ]; then
    # Copy instead of link, so it's self-contained in the project
    cp "$PERSONA_FILE" "$PROJECT_SQUAD_DIR/$agent_lower/.gemini/GEMINI.md"
    echo "Deployed $agent persona."
  else
    echo "Warning: Persona file for $agent not found at $PERSONA_FILE"
  fi
done

# Initialize project.json (Shared Memory)
PROJECT_JSON="$PROJECT_SQUAD_DIR/project.json"
if [ ! -f "$PROJECT_JSON" ]; then
  cat <<EOF > "$PROJECT_JSON"
{
  "project_name": "new-project",
  "mission": "No mission defined yet.",
  "status": "planning",
  "version": "0.1.0",
  "current_phase": "init",
  "artifacts": {
    "design_doc": "",
    "tests": [],
    "source_code": []
  }
}
EOF
  echo "Initialized project.json (Shared Memory)."
else
  echo "project.json already exists. Skipping initialization."
fi

echo "Squad deployed successfully!"
