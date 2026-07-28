#!/usr/bin/env bash
# KDA launcher for this e2e kernel-optimization task. Creates a task-owned git
# worktree and starts Claude Code inside this task folder. See
# ../scripts/launch_kda_kernel_task.sh -h for environment overrides.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR" && git rev-parse --show-toplevel)"
KDA_LAUNCHER_NAME="${KDA_LAUNCHER_NAME:-$(basename "$SCRIPT_DIR").sh}"
export KDA_LAUNCHER_NAME
CLAUDE_MODEL="${CLAUDE_MODEL:-fable}"
export CLAUDE_MODEL
TASK_REL="${SCRIPT_DIR#"$REPO_ROOT"/}"
exec "$REPO_ROOT/llm/scripts/launch_kda_kernel_task.sh" "$TASK_REL" "$@"
