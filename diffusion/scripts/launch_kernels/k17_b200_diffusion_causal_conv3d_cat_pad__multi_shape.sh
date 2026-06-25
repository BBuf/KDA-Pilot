#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TASK_DIR="diffusion/kernels/b200_diffusion_causal_conv3d_cat_pad__multi_shape"
KDA_LAUNCHER_NAME="${KDA_LAUNCHER_NAME:-$(basename "$0")}"
export KDA_LAUNCHER_NAME
if [[ -z "${KDA_BASE_BRANCH:-}" ]]; then
  REPO_ROOT="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel)"
  CURRENT_BASE="$(
    git -C "$REPO_ROOT" symbolic-ref --quiet --short HEAD ||
      git -C "$REPO_ROOT" rev-parse --verify HEAD
  )"
  if ! git -C "$REPO_ROOT" cat-file -e "$CURRENT_BASE:$TASK_DIR" 2>/dev/null; then
    TASK_DEF_REF="${KDA_DIFFUSION_TASK_DEFS_REF:-kda/task-defs-b200-diffusion-20260625}"
    if git -C "$REPO_ROOT" cat-file -e "$TASK_DEF_REF:$TASK_DIR" 2>/dev/null; then
      KDA_BASE_BRANCH="$TASK_DEF_REF"
      export KDA_BASE_BRANCH
    fi
  fi
fi
# Round-robin GPU assignment across the 8 B200 cards (override by exporting KDA_GPU_ID).
KDA_GPU_ID="${KDA_GPU_ID:-0}"
export KDA_GPU_ID
exec "$SCRIPT_DIR/../launch_kda_kernel_task.sh" "$TASK_DIR" "$@"
