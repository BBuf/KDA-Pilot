#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/launch_kda_kernel_task.sh <kernel-task-dir> [extra claude args...]

Creates a task-owned git worktree, enters the kernel task directory inside that
worktree, and launches Claude Code with CLAUDE_PROJECT_DIR set to the kernel
directory so official Humanize hooks stay local to that task's .humanize state.

Environment overrides:
  KDA_BASE_BRANCH       Base branch/ref for the worktree
                        (default: current checkout branch, or HEAD if detached)
  KDA_WORKTREE_BASE     Parent directory for generated worktrees
                        (default: ../kernel-pilot-worktrees next to this repo)
  KDA_RUN_ID            Run suffix (default: timestamp-pid)
  KDA_BRANCH            Exact branch name to create
  KDA_BRANCH_PREFIX     Branch prefix when KDA_BRANCH is unset (default: kda)
  KDA_REVIEW_BASE       Exact local branch name to create for RLCR review base
  KDA_REVIEW_BASE_PREFIX
                        Review-base branch prefix when KDA_REVIEW_BASE is unset
                        (default: kda-base)
  KDA_WORKTREE_ROOT     Exact worktree path to create
  CLAUDE_BIN            Claude executable (default: claude)
  CLAUDE_MODEL          Claude model flag value (default: opus)
  CLAUDE_EFFORT         Claude effort flag value (default: max)
  KDA_LAUNCHER_NAME     Friendly launcher/task-card name, normally set by
                        scripts/launch_kernels/kXX_*.sh
  KDA_TASK_LABEL        Override the friendly label used for branch/worktree names
  KDA_BOOTSTRAP_DRAFT=0 Skip automatic .humanize/kernel-agent/draft.md creation
  KDA_NO_CLAUDE=1       Create the worktree and print commands without launching Claude
  HUMANIZE_CODEX_BYPASS_SANDBOX
                        Forwarded to the spawned Claude process (default: true).
                        Lets Codex inside the RLCR loop skip its per-call sandbox /
                        approval prompts. Set to anything other than true|1 to
                        re-enable the sandbox; only safe to leave on for trusted
                        dev environments (the worktree is task-isolated already).
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ $# -lt 1 ]]; then
  usage >&2
  exit 2
fi

TASK_DIR="${1%/}"
shift

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
if [[ -n "${KDA_BASE_BRANCH:-}" ]]; then
  BASE_BRANCH="$KDA_BASE_BRANCH"
else
  BASE_BRANCH="$(
    git -C "$REPO_ROOT" symbolic-ref --quiet --short HEAD ||
      git -C "$REPO_ROOT" rev-parse --verify HEAD
  )"
fi
DEFAULT_WORKTREE_BASE="$(cd "$REPO_ROOT/.." && pwd)/kernel-pilot-worktrees"
WORKTREE_BASE="${KDA_WORKTREE_BASE:-$DEFAULT_WORKTREE_BASE}"
RUN_ID="${KDA_RUN_ID:-$(date +%Y%m%d-%H%M%S)-$$}"
TASK_SLUG="${TASK_DIR##*/}"
LAUNCHER_NAME="${KDA_LAUNCHER_NAME:-direct}"
TASK_LABEL="${KDA_TASK_LABEL:-${LAUNCHER_NAME%.sh}}"
if [[ "$TASK_LABEL" == "direct" || -z "$TASK_LABEL" ]]; then
  TASK_LABEL="$TASK_SLUG"
fi
BRANCH_PREFIX="${KDA_BRANCH_PREFIX:-kda}"
BRANCH="${KDA_BRANCH:-${BRANCH_PREFIX}/${TASK_LABEL}-${RUN_ID}}"
REVIEW_BASE_PREFIX="${KDA_REVIEW_BASE_PREFIX:-kda-base}"
REVIEW_BASE="${KDA_REVIEW_BASE:-${REVIEW_BASE_PREFIX}/${TASK_LABEL}-${RUN_ID}}"
WORKTREE_ROOT="${KDA_WORKTREE_ROOT:-${WORKTREE_BASE}/${TASK_LABEL}-${RUN_ID}}"
CLAUDE_BIN="${CLAUDE_BIN:-claude}"
CLAUDE_MODEL="${CLAUDE_MODEL:-opus}"
CLAUDE_EFFORT="${CLAUDE_EFFORT:-max}"

case "$TASK_SLUG" in
  b200_*)
    TARGET_GPU_LABEL="B200"
    REMOTE_HOST_HINT="ion-b200"
    ;;
  h200_*)
    TARGET_GPU_LABEL="H200"
    REMOTE_HOST_HINT="ion8-h200 or ion9-h200"
    ;;
  *)
    TARGET_GPU_LABEL="target"
    REMOTE_HOST_HINT="the task prompt's target host"
    ;;
esac

if [[ "$TASK_DIR" = /* || "$TASK_DIR" == *".."* ]]; then
  echo "error: task dir must be repo-relative and must not contain '..': $TASK_DIR" >&2
  exit 2
fi

if [[ ! -d "$REPO_ROOT/$TASK_DIR" ]]; then
  echo "error: task dir does not exist in repo: $REPO_ROOT/$TASK_DIR" >&2
  exit 2
fi

if [[ "${KDA_NO_CLAUDE:-}" != "1" ]] && ! command -v "$CLAUDE_BIN" >/dev/null 2>&1; then
  echo "error: Claude executable not found: $CLAUDE_BIN" >&2
  exit 127
fi

if ! git -C "$REPO_ROOT" rev-parse --verify --quiet "$BASE_BRANCH" >/dev/null; then
  echo "error: base branch/ref not found: $BASE_BRANCH" >&2
  exit 2
fi

if ! git -C "$REPO_ROOT" cat-file -e "$BASE_BRANCH:$TASK_DIR" 2>/dev/null; then
  echo "error: base branch/ref does not contain task dir: $BASE_BRANCH:$TASK_DIR" >&2
  echo "hint: commit the kernel task folder or set KDA_BASE_BRANCH to a ref that contains it" >&2
  exit 2
fi

if [[ -e "$WORKTREE_ROOT" ]]; then
  echo "error: worktree path already exists: $WORKTREE_ROOT" >&2
  echo "hint: set KDA_RUN_ID or KDA_WORKTREE_ROOT to choose a fresh path" >&2
  exit 2
fi

if git -C "$REPO_ROOT" show-ref --verify --quiet "refs/heads/$REVIEW_BASE"; then
  echo "error: review base branch already exists: $REVIEW_BASE" >&2
  echo "hint: set KDA_RUN_ID or KDA_REVIEW_BASE to choose a fresh branch" >&2
  exit 2
fi

mkdir -p "$WORKTREE_BASE"

echo "== KernelPilot KDA task launcher =="
echo "repo:      $REPO_ROOT"
echo "launcher:  $LAUNCHER_NAME"
echo "label:     $TASK_LABEL"
echo "task:      $TASK_DIR"
echo "base:      $BASE_BRANCH"
echo "review:    $REVIEW_BASE"
echo "branch:    $BRANCH"
echo "worktree:  $WORKTREE_ROOT"
echo

git -C "$REPO_ROOT" branch "$REVIEW_BASE" "$BASE_BRANCH"
git -C "$REPO_ROOT" worktree add -b "$BRANCH" "$WORKTREE_ROOT" "$BASE_BRANCH"

cd "$WORKTREE_ROOT/$TASK_DIR"

if [[ "${KDA_BOOTSTRAP_DRAFT:-1}" != "0" ]]; then
  mkdir -p .humanize/kernel-agent
  DRAFT_FILE=".humanize/kernel-agent/draft.md"
  if [[ ! -f "$DRAFT_FILE" ]]; then
    {
      cat <<EOF
# Humanize Gen-Plan Draft For ${TASK_SLUG}

Use this draft to generate a Humanize RLCR implementation plan for the kernel
optimization task in this directory. Preserve the source prompt's problem
definition, baseline requirements, benchmark requirements, correctness tests,
remote-GPU constraints, source-lineage requirements, and local folder contract.

## Source Prompt

The task source is the local \`prompt.md\` below.

\`\`\`markdown
EOF
      cat prompt.md
      cat <<EOF
\`\`\`

## Mandatory Humanize/KernelPilot Constraints

- Use this current kernel folder as the optimization workspace.
- Keep \`.humanize*\` untracked.
- Use official Humanize commands installed in the agent environment. Do not use
  any vendored or repository-local Humanize implementation from KernelPilot.
- Read \`../../docs/standalone_diffusion_benchmark.md\` if it exists for this
  task. Its local-baseline and A/B benchmark rules are mandatory for diffusion
  kernels.
- Read \`../../docs/diffusion_kernel_rules.md\` and
  \`../../docs/diffusion_correctness_contract.md\` if they exist for this task.
  Their compile-flag, registration, correctness-grid, profiling, and completion
  rules are mandatory for diffusion kernels.
- Read \`${WORKTREE_ROOT}/external/KernelWiki/SKILL.md\` and
  \`${WORKTREE_ROOT}/external/ncu-report-skill/SKILL.md\` before implementation.
- Use KernelWiki for upstream design ideas and ncu-report-skill for
  evidence-backed kernel diagnosis when profiling would change the next edit.
- In every RLCR iteration, refresh the context from the source prompt,
  diffusion rules, current benchmark/profile evidence, KernelWiki, and
  ncu-report-skill before choosing the next edit, profiling command, benchmark
  command, or no-go conclusion.
- Recover K/R/W from the source prompt before implementation:
  - K: kernel semantics and callsite contract
  - R: correctness oracle and baseline path
  - W: workload shape set and benchmark methodology
- Do not implement kernels, run long benchmarks, or collect NCU evidence before
  RLCR is active.
- Check GPU state before and after every benchmark/profile run, and treat
  performance data as valid only when the selected card is idle.
- Do not fabricate benchmark, NCU, correctness, topology, source-lineage, or
  GPU-id evidence.
- Keep all candidate code, benchmark logs, profile artifacts, NCU reports, and
  final notes inside this kernel folder unless the user explicitly asks for a
  wider integration patch.
- Keep raw profiler/NCU/build/scratch artifacts local for evidence, but do not
  stage them for the final PR. The PR should contain only kernel-related code,
  benchmark/correctness harnesses, small provenance notes, and per-shape
  baseline-vs-candidate performance results.
- Keep copied upstream baseline code under \`baseline/\`, candidate code under
  \`solution/\`, benchmark/correctness harnesses under \`bench/\`, and
  provenance/results under \`docs/\`.
- For diffusion kernels, resolve the latest upstream SGLang \`main\` commit at
  baseline-recovery time and copy the relevant kernel source from that exact
  commit. Record the SGLang repository URL, branch, resolved commit SHA,
  resolution time, and copied files in \`docs/baseline_source.md\`.
- For diffusion kernels, do not import, patch, monkey-patch, or install into an
  SGLang checkout during correctness or benchmark runtime. Copy the SGLang
  implementation into \`baseline/\` and expose it through the same low-overhead
  local entry ABI used by the candidate.
- Always ask before destructive operations, global machine/container changes,
  deleting another task's artifacts, changing shared production checkouts in
  place, or relaxing correctness/baseline/promotion requirements.

## Default Decision Policy

The plan should minimize user-choice prompts during RLCR. Bake these defaults
into the plan unless the source prompt explicitly says otherwise:

- Remote ${TARGET_GPU_LABEL} validation is a normal part of the loop. After
  local scaffold, correctness, and implementation checks are committed, proceed
  to the remote GPU phase autonomously.
- Use the matching remote host (${REMOTE_HOST_HINT}) unless the source prompt
  provides a stricter host choice.
- Before GPU work, inspect the remote GPU state and select a
  ${TARGET_GPU_LABEL} GPU with no active compute processes and no meaningful
  memory occupancy. Export that id as \`REMOTE_GPU_ID\` and use it consistently
  for baseline, candidate, benchmark, profiler, and NCU commands in the current
  run.
- If no idle ${TARGET_GPU_LABEL} GPU is available, wait or retry briefly. Ask
  before changing the benchmark environment or running measurements on a busy
  GPU.
- Treat minimal, reversible, task-owned setup work as approved: creating remote
  workspaces, checking out commits, building inside the task workspace,
  installing local editable packages there, collecting profiler traces, and
  writing benchmark/NCU artifacts.
- If the dependency stack cannot run the baseline, create a task-owned remote
  workspace and pin/rebuild dependencies there. Ask only if the matching commit
  cannot be inferred, the rebuild repeatedly fails, or a destructive change
  outside the task workspace would be required.
- Do not finalize an evidence-backed no-go just because the first candidate did
  not win. A no-go needs correctness, baseline numbers, candidate attempts,
  benchmark or NCU evidence, and a named active bound or blocker.

## Expected Plan Shape

- Recover the baseline source, exact callsite, and workload shape set.
- Resolve upstream SGLang \`main\` to its latest commit, copy the matching
  baseline source into \`baseline/\`, and record upstream URL, branch, commit,
  resolution time, copied files, and local edits in
  \`docs/baseline_source.md\`.
- Define matching baseline and candidate entry points using the same ABI,
  argument order, stream behavior, output allocation policy, and build path.
- Fill \`bench/correctness.py\` before optimization.
- Establish \`bench/benchmark.py\`, frozen workloads, and immutable baseline
  numbers.
- Rank candidate directions by expected benefit and risk.
- Implement bounded optimization attempts under RLCR.
- At the start of every RLCR iteration, record the refreshed KernelWiki and
  ncu-report-skill context that affects the next edit or explain why no new
  query/profile is needed for that iteration.
- Include a remote phase that records selected host/GPU id/model, before/after
  GPU idleness, exact commands, benchmark artifacts, and NCU artifacts.
- Use NCU/profile evidence for non-obvious bottlenecks.
- Update \`docs/results.md\` and keep raw benchmark/profiler artifacts in this
  kernel folder before final completion.
- Before committing or opening a PR, inspect the staged diff and exclude raw
  NCU reports, Nsight traces, profiler directories, temporary harness binaries,
  build outputs, scratch logs, failed experiment dumps, and large intermediate
  benchmark files.
EOF
    } > "$DRAFT_FILE"
  fi
fi

echo
echo "== Claude project root =="
echo "$PWD"
echo
echo "Draft: .humanize/kernel-agent/draft.md"
echo "Inside Claude Code, use:"
echo "/humanize:gen-plan --input .humanize/kernel-agent/draft.md --output .humanize/kernel-agent/refined-plan.md --direct"
echo "/humanize:start-rlcr-loop .humanize/kernel-agent/refined-plan.md --skip-quiz --claude-answer-codex --max 12 --codex-model gpt-5.5:high --codex-timeout 5400 --base-branch $REVIEW_BASE"
echo

if [[ "${KDA_NO_CLAUDE:-}" == "1" ]]; then
  echo "KDA_NO_CLAUDE=1 set; worktree prepared without launching Claude."
  exit 0
fi

exec env \
  CLAUDE_PROJECT_DIR="$PWD" \
  HUMANIZE_CODEX_BYPASS_SANDBOX="${HUMANIZE_CODEX_BYPASS_SANDBOX:-true}" \
  "$CLAUDE_BIN" \
  --permission-mode bypassPermissions \
  --model "$CLAUDE_MODEL" \
  --effort "$CLAUDE_EFFORT" \
  "$@"
