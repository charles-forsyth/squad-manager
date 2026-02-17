#!/bin/bash
# Usage: ./call.sh <agent> <prompt>

AGENT=$1
PROMPT=$2

if [ -z "$AGENT" ] || [ -z "$PROMPT" ]; then
  echo "Usage: ./call.sh <agent> <prompt>"
  exit 1
fi

AGENT_DIR=".squad/$AGENT"

if [ ! -d "$AGENT_DIR" ]; then
  echo "Error: Agent '$AGENT' not found in .squad/"
  echo "Did you run '/squad deploy' first?"
  exit 1
fi

# Capture the Project Root (where the script is run from)
PROJECT_ROOT=$(pwd)

echo "Calling $AGENT (Memory: Enabled, Traversal: Enabled)..."

# Logic: Try to resume the latest session. If it fails (likely first run), start fresh.
# Both attempts include the --include-directories flag for project-wide access.
(cd "$AGENT_DIR" && gemini --yolo -p "$PROMPT" --include-directories "$PROJECT_ROOT" --resume latest) || \
(cd "$AGENT_DIR" && gemini --yolo -p "$PROMPT" --include-directories "$PROJECT_ROOT")
