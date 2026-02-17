---
name: squad-manager
description: Manage and deploy "Skywalker Squad" agents for git-based development workflows.
---

# Squad Manager (Skywalker Edition)

This skill deploys a specialized team of AI agents to execute the **Skywalker Development Workflow**.

## Requirements
*   `git` installed and configured.
*   `gh` (GitHub CLI) installed and authenticated.
*   Appropriate toolchain for the project (e.g., `uv` for Python, `npm` for Node.js, `go` for Go).

## Commands

### `/squad deploy`
Deploys the Skywalker Squad (Architect, Grunt, Sentinel, Gatekeeper, DevOps, UAT) to the current directory.

### `/squad call <agent> <prompt>`
Runs a specific agent.

### `/squad build <mission>`
**Director Mode:** Orchestrates the full development lifecycle:
1.  Creates a Git Feature Branch.
2.  Architect designs.
3.  Sentinel writes tests.
4.  DevOps bumps version.
5.  Grunt implements code (and runs Gauntlet).
6.  Gatekeeper audits & merges.
7.  DevOps releases.
8.  UAT verifies.

## Examples
1. `gemini "/squad deploy"`
2. `gemini "/squad build 'Add user login feature'"`
