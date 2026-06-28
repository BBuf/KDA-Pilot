#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  scripts/launch_kda_kernel_task.sh <kernel-task-dir> [extra claude args...]

Creates a task-owned git worktree, enters the LLM kernel task directory
inside that worktree, and launches Claude Code with CLAUDE_PROJECT_DIR set to
the kernel directory so official Humanize hooks stay local to that task's
.humanize state.

<kernel-task-dir> must be repo-relative, e.g.
  llm/<model_slug>__<op_slug>      (flat e2e task; usually launched via its own launch.sh)

Environment overrides:
  KDA_BASE_BRANCH       Base branch/ref for the worktree
                        (default: current checkout branch, or HEAD if detached)
  KDA_WORKTREE_BASE     Parent directory for generated worktrees
                        (default: ../KDA-Pilot-worktrees next to this repo)
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
  KDA_BASH_BIN          Bash used for KDA-Pilot launch + spawned Claude hooks.
                        Must survive empty-array expansion under set -u
                        (default: first usable bash from PATH, Homebrew paths).
  KDA_LAUNCHER_NAME     Friendly launcher/task-card name, normally set by
                        scripts/launch_kernels/kXX_*.sh
  KDA_TASK_LABEL        Override the friendly label used for branch/worktree names
  KDA_BOOTSTRAP_DRAFT=0 Skip automatic .humanize/kernel-agent/draft.md creation
  KDA_NO_CLAUDE=1       Create the worktree and print commands without launching Claude
  IS_SANDBOX            Forwarded to the spawned Claude process (default: 1).
                        Required for Claude/Codex sessions that may run under a
                        root user inside Docker.
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
REPO_ROOT="$(cd "$SCRIPT_DIR" && git rev-parse --show-toplevel)"
if [[ -n "${KDA_BASE_BRANCH:-}" ]]; then
  BASE_BRANCH="$KDA_BASE_BRANCH"
else
  BASE_BRANCH="$(
    git -C "$REPO_ROOT" symbolic-ref --quiet --short HEAD ||
      git -C "$REPO_ROOT" rev-parse --verify HEAD
  )"
fi
DEFAULT_WORKTREE_BASE="$(cd "$REPO_ROOT/.." && pwd)/KDA-Pilot-worktrees"
WORKTREE_BASE="${KDA_WORKTREE_BASE:-$DEFAULT_WORKTREE_BASE}"
RUN_ID="${KDA_RUN_ID:-$(date +%Y%m%d-%H%M%S)-$$}"
TASK_SLUG="${TASK_DIR##*/}"
# Flat layout: task dir is llm/<model_slug>__<op_slug>. Model slug is the 2nd path
# component up to the "__" op separator (older layout llm/<model>/<arch>/... has no "__",
# so this is a no-op for it).
MODEL_SLUG="$(printf '%s' "$TASK_DIR" | awk -F/ '{print $2}')"
MODEL_SLUG="${MODEL_SLUG%%__*}"
[[ -z "$MODEL_SLUG" ]] && MODEL_SLUG="LLM"
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

# Target arch: flat tasks record it in config.toml (arch = "b200"); the older
# layout encodes it in the path (llm/<model>/<arch>/kernels/...). Prefer config.toml,
# fall back to the path.
TASK_ARCH="$(sed -n 's/^[[:space:]]*arch[[:space:]]*=[[:space:]]*"\([^"]*\)".*/\1/p' "$REPO_ROOT/$TASK_DIR/config.toml" 2>/dev/null | head -1)"
case "${TASK_ARCH}::/$TASK_DIR/" in
  b200::*|*/b200/*)
    TARGET_GPU_LABEL="B200"
    # Keep B200 runners behind the public community alias; do not embed internal hostnames.
    REMOTE_HOST_HINT="ion-b200"
    ;;
  h200::*|*/h200/*)
    TARGET_GPU_LABEL="H200"
    REMOTE_HOST_HINT="ion8-h200 or ion9-h200"
    ;;
  *)
    TARGET_GPU_LABEL="target"
    REMOTE_HOST_HINT="the task prompt's target host"
    ;;
esac

# Optional pinned GPU. Per-kernel wrappers set KDA_GPU_ID to a round-robin id so
# kernels spread across GPUs 0-7; unset means the task auto-selects an idle GPU.
GPU_PIN_DESC=""
if [[ -n "${KDA_GPU_ID:-}" ]]; then
  if [[ ! "$KDA_GPU_ID" =~ ^[0-9]+$ ]]; then
    echo "error: KDA_GPU_ID must be a non-negative integer GPU id: $KDA_GPU_ID" >&2
    exit 2
  fi
  GPU_PIN_DESC=" id=$KDA_GPU_ID"
fi

bash_is_kda_safe() {
  local candidate="$1"
  [[ -n "$candidate" && -x "$candidate" ]] || return 1
  "$candidate" -c 'set -euo pipefail; a=(); : "${a[@]}"; [[ ${BASH_VERSINFO[0]} -gt 3 ]]' >/dev/null 2>&1
}

find_kda_bash() {
  local candidate
  if [[ -n "${KDA_BASH_BIN:-}" ]]; then
    bash_is_kda_safe "$KDA_BASH_BIN" && printf '%s\n' "$KDA_BASH_BIN"
    return
  fi

  for candidate in "$(command -v bash 2>/dev/null || true)" /opt/homebrew/bin/bash /usr/local/bin/bash; do
    if bash_is_kda_safe "$candidate"; then
      printf '%s\n' "$candidate"
      return
    fi
  done
}

KDA_SELECTED_BASH="$(find_kda_bash || true)"
if [[ -z "$KDA_SELECTED_BASH" ]]; then
  echo "error: KDA-Pilot requires a modern bash for Humanize hooks; /bin/bash 3.2 is not supported" >&2
  echo "hint: install Homebrew bash and/or set KDA_BASH_BIN=/opt/homebrew/bin/bash" >&2
  exit 127
fi
KDA_SELECTED_BASH_DIR="$(cd "$(dirname "$KDA_SELECTED_BASH")" && pwd)"
KDA_LAUNCH_PATH="$KDA_SELECTED_BASH_DIR:$PATH"

if ! bash_is_kda_safe "$BASH"; then
  if [[ "${KDA_BASH_REEXECED:-}" == "1" ]]; then
    echo "error: failed to re-exec KDA-Pilot with safe bash: $KDA_SELECTED_BASH" >&2
    exit 127
  fi
  export KDA_BASH_REEXECED=1
  export KDA_BASH_BIN="$KDA_SELECTED_BASH"
  export PATH="$KDA_LAUNCH_PATH"
  exec "$KDA_SELECTED_BASH" "$0" "$TASK_DIR" "$@"
fi

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

echo "== KDA-Pilot ${MODEL_SLUG} KDA task launcher =="
echo "repo:      $REPO_ROOT"
echo "launcher:  $LAUNCHER_NAME"
echo "label:     $TASK_LABEL"
echo "task:      $TASK_DIR"
echo "gpu:       $TARGET_GPU_LABEL$GPU_PIN_DESC ($REMOTE_HOST_HINT)"
echo "base:      $BASE_BRANCH"
echo "review:    $REVIEW_BASE"
echo "branch:    $BRANCH"
echo "worktree:  $WORKTREE_ROOT"
echo "bash:      $KDA_SELECTED_BASH ($("$KDA_SELECTED_BASH" --version | head -1))"
echo

git -C "$REPO_ROOT" branch "$REVIEW_BASE" "$BASE_BRANCH"
git -C "$REPO_ROOT" worktree add -b "$BRANCH" "$WORKTREE_ROOT" "$BASE_BRANCH"
# Linked worktrees do not auto-checkout submodules. The external/ skill
# submodules are required by the task draft; objects are cached in the main
# repo's .git/modules, so this is offline + fast. Non-fatal on failure.
git -C "$WORKTREE_ROOT" submodule update --init --recursive \
  || echo "warning: submodule init failed; run 'git submodule update --init --recursive' in the worktree" >&2

cd "$WORKTREE_ROOT/$TASK_DIR"

if [[ -n "${KDA_GPU_ID:-}" ]]; then
  GPU_SELECTION_POLICY="- This task is pinned to ${TARGET_GPU_LABEL} GPU id ${KDA_GPU_ID} (the launchers assign the kernels across GPUs 0-7 in a round robin). Export REMOTE_GPU_ID=${KDA_GPU_ID} and use exactly that GPU for baseline, candidate, benchmark, profiler, and NCU commands in this run.
- Before measuring, verify GPU ${KDA_GPU_ID} is idle (no active compute processes, no meaningful memory occupancy). If it is busy, wait or retry briefly; ask before measuring on a different GPU or changing the benchmark environment."
else
  GPU_SELECTION_POLICY="- Before GPU work, inspect the remote GPU state and select a ${TARGET_GPU_LABEL} GPU with no active compute processes and no meaningful memory occupancy. Export that id as REMOTE_GPU_ID and use it consistently for baseline, candidate, benchmark, profiler, and NCU commands in the current run.
- If no idle ${TARGET_GPU_LABEL} GPU is available, wait or retry briefly. Ask before changing the benchmark environment or running measurements on a busy GPU."
fi

if [[ "${KDA_BOOTSTRAP_DRAFT:-1}" != "0" ]]; then
  mkdir -p .humanize/kernel-agent
  DRAFT_FILE=".humanize/kernel-agent/draft.md"
  if [[ ! -f "$DRAFT_FILE" ]]; then
    {
      cat <<EOF
# Humanize Gen-Plan Draft For ${TASK_SLUG}

Use this draft to generate a Humanize RLCR implementation plan for the
${MODEL_SLUG} SGLang kernel optimization task in this directory. Preserve the source prompt's
kernel-interface definition, captured-shape coverage, baseline requirements,
benchmark requirements, correctness tests, remote-GPU constraints,
source-lineage requirements, and local folder contract.

## Source Prompt

The task source is the local \`prompt.md\` below.

\`\`\`markdown
EOF
      cat prompt.md
      cat <<EOF
\`\`\`

## Mandatory Humanize/KDA-Pilot Constraints

- Use this current kernel folder as the optimization workspace.
- Keep \`.humanize*\` untracked.
- Use official Humanize commands installed in the agent environment. Do not use
  any vendored or repository-local Humanize implementation from KDA-Pilot.
- Read the local \`prompt.md\` and \`config.toml\` for the exact kernel
  interface, captured shapes, build/benchmark policy, and correctness contract.
- MANDATORY before implementation: read
  \`${WORKTREE_ROOT}/llm/docs/standalone_llm_benchmark.md\`,
  \`${WORKTREE_ROOT}/llm/docs/llm_kernel_optimization_rules.md\`, and
  \`${WORKTREE_ROOT}/llm/docs/llm_correctness_contract.md\`. Their benchmark
  timing/fairness rules, baseline-pairing and compile-flag symmetry, ABI rules,
  per-category correctness oracle + dtype tolerances (incl. fp8/quant,
  integer/top-k/tree exact-match, non-contiguous inputs, and in-place
  semantics), provenance fields, and completion bar are mandatory.
- Build the task folder contract from \`standalone_llm_benchmark.md\`: copy
  \`${WORKTREE_ROOT}/llm/docs/standalone_llm_benchmark_template.py\` to
  \`bench/benchmark.py\` (do not invent a different timing harness), and create
  \`bench/workloads.json\` (frozen, deduplicated from the captured variants in
  \`prompt.md\`/\`docs/evidence.json\`, with production vs regression rows and
  headline tagging), \`bench/adapter.py\`, \`bench/correctness.py\`,
  \`baseline/\`, \`solution/\`, and the \`docs/\` artifacts
  (\`baseline_source.md\`, \`benchmark_method.md\`, \`results.md\`,
  \`run_log.md\`, and \`dispatch.md\` when specialized).
- Do not use macOS \`/bin/bash\` or any Bash 3.x runtime for local Humanize,
  hook, launcher, or helper scripts. The launcher exports \`KDA_BASH_BIN\` and
  prepends its directory to \`PATH\`; preserve that environment so
  \`#!/usr/bin/env bash\` resolves to the selected modern bash.
- Read \`${WORKTREE_ROOT}/external/KernelWiki/SKILL.md\`,
  \`${WORKTREE_ROOT}/external/ncu-report-skill/SKILL.md\`, and
  \`${WORKTREE_ROOT}/external/warp-specialization-report-skill/SKILL.md\`
  before implementation. The launcher auto-runs
  git submodule update --init --recursive in this worktree so these are
  checked out; if any SKILL.md is missing, re-run that command from the
  worktree root.
- Use KernelWiki for upstream design ideas and ncu-report-skill for
  evidence-backed kernel diagnosis when profiling would change the next edit.
- IMPLEMENTATION LANGUAGE (CUDA only): iterate and implement the candidate in
  native CUDA. The final candidate that is benchmarked and promoted must be a
  CUDA kernel built from workspace-owned C++/CUDA source (\`.cu\`, \`.cuh\`,
  \`.cpp\`, \`.h\`) compiled with nvcc or an equivalent CUDA extension build
  (CUTLASS / CuTe C++ templates are allowed because they are CUDA C++). Do NOT
  use Triton, TileLang, CuTe-DSL (Python \`cute.compile\`), \`torch.compile\`, or
  any other DSL / prebuilt op as the candidate execution path. The upstream
  SGLang kernel and such DSL sources may be studied or ported into
  workspace-owned C++/CUDA, but the promoted candidate must be the native CUDA
  implementation. Python is allowed only for harnesses, bindings, benchmark
  scripts, and dispatch glue, never as the primary kernel implementation. If the
  recovered SGLang baseline is itself Triton/Python, keep it unchanged as the
  baseline oracle and write the candidate as a new native CUDA kernel.
- WARP-SPECIALIZATION PROFILING (mandatory when applicable): whenever a
  candidate is a warp-specialized CUDA C++ kernel (e.g. CUTLASS/CuTe templates,
  with producer/consumer warp roles coordinated by mbarrier / named-barrier /
  pipeline objects), use
  the \`warp-specialization-report-skill\` to profile it as a closed loop
  (predict feeds-and-speeds -> stamp clock() timeline -> reconcile): locate
  per-warp stalls, confirm the producer/consumer data dependencies, and verify
  that the specialized warps actually overlap. The skill does NOT apply to
  Triton kernels (use ncu-report-skill for those); record in
  \`docs/results.md\` which kernels were warp-specialization-profiled and what
  the timeline showed, or why the skill did not apply.
- PER-SHAPE KERNEL DISPATCH (expected): the captured interface spans many
  distinct shapes (see the Shape Summary and Captured Variants in the source
  prompt; e.g. different token counts / hidden sizes / dtypes / contiguity).
  You are expected to write more than one specialized kernel when a single
  configuration cannot win across all regimes, and dispatch among them at
  runtime by inspecting the input shape/dtype/contiguity (for example a
  small-batch decode path vs a large-batch prefill path, or per hidden-size
  variants). Keep the dispatch logic cheap (no host syncs on the hot path) and
  make every shape/parameter combination that no specialized path covers fall
  back to the recovered SGLang baseline so correctness is never lost. Record the
  dispatch table (shape regime -> chosen kernel) and per-regime
  baseline-vs-candidate results in \`docs/results.md\`.
- In every RLCR iteration, refresh the context from the source prompt, current
  benchmark/profile evidence, KernelWiki, ncu-report-skill, and (for
  warp-specialized candidates) the warp-specialization timeline before choosing
  the next edit, profiling command, benchmark command, or no-go conclusion.
- Recover K/R/W from the source prompt before implementation:
  - K: kernel semantics and Python-interface callsite contract
  - R: correctness oracle and baseline path
  - W: captured workload shape set and benchmark methodology
- Do not implement kernels, run long benchmarks, or collect NCU evidence before
  RLCR is active.
- Check GPU state before and after every benchmark/profile run, and treat
  performance data as valid only when the selected card is idle.
- Do not fabricate benchmark, NCU, warp-timeline, correctness, topology,
  source-lineage, or GPU-id evidence.
- Keep all candidate code, benchmark logs, profile artifacts, NCU reports,
  warp-specialization timelines, and final notes inside this kernel folder
  unless the user explicitly asks for a wider integration patch.
- Keep raw profiler/NCU/timeline/build/scratch artifacts local for evidence, but
  do not stage them for the final PR. The PR should contain only kernel-related
  code, benchmark/correctness harnesses, small provenance notes, the dispatch
  table, and per-shape baseline-vs-candidate performance results.
- Keep copied upstream baseline code under \`baseline/\`, candidate code under
  \`solution/\`, benchmark/correctness harnesses under \`bench/\`, and
  provenance/results under \`docs/\`.
- Resolve the latest upstream SGLang \`main\` commit at baseline-recovery time
  and copy the relevant kernel source for this exact Python interface from that
  exact commit. Record the SGLang repository URL, branch, resolved commit SHA,
  resolution time, and copied files in \`docs/baseline_source.md\`.
- Do not import, patch, monkey-patch, or install into a live SGLang server or
  checkout during correctness or benchmark runtime. Copy the SGLang
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
${GPU_SELECTION_POLICY}
- Treat minimal, reversible, task-owned setup work as approved: creating remote
  workspaces, checking out commits, building inside the task workspace,
  installing local editable packages there, collecting profiler traces, and
  writing benchmark/NCU/timeline artifacts.
- If the dependency stack cannot run the baseline, create a task-owned remote
  workspace and pin/rebuild dependencies there. Ask only if the matching commit
  cannot be inferred, the rebuild repeatedly fails, or a destructive change
  outside the task workspace would be required.
- Do not finalize an evidence-backed no-go just because the first candidate did
  not win. A no-go needs correctness, baseline numbers, candidate attempts,
  benchmark or NCU evidence, and a named active bound or blocker.

## Expected Plan Shape

- Recover the baseline source, exact Python-interface callsite, and captured
  workload shape set.
- Resolve upstream SGLang \`main\` to its latest commit, copy the matching
  baseline source into \`baseline/\`, and record upstream URL, branch, commit,
  resolution time, copied files, and local edits in
  \`docs/baseline_source.md\`.
- Define matching baseline and candidate entry points using the same ABI,
  argument order, stream behavior, output allocation policy, and build path.
- Fill \`bench/correctness.py\` before optimization, covering every retained
  captured variant or an explicitly justified representative subset.
- Establish \`bench/benchmark.py\`, frozen workloads, and immutable baseline
  numbers.
- Group the captured shapes into regimes, decide where one kernel suffices vs
  where per-shape specialized kernels plus runtime dispatch are needed, and make
  uncovered shapes fall back to the baseline.
- Rank candidate directions by expected benefit and risk.
- Implement bounded optimization attempts under RLCR.
- At the start of every RLCR iteration, record the refreshed KernelWiki,
  ncu-report-skill, and (for warp-specialized candidates)
  warp-specialization-report-skill context that affects the next edit, or
  explain why no new query/profile is needed for that iteration.
- Include a remote phase that records selected host/GPU id/model, before/after
  GPU idleness, exact commands, benchmark artifacts, NCU artifacts, and any
  warp-specialization timelines.
- Use NCU/profile and warp-specialization-timeline evidence for non-obvious
  bottlenecks.
- Update \`docs/results.md\` (including the per-shape dispatch table and
  per-regime baseline-vs-candidate numbers) and keep raw
  benchmark/profiler/timeline artifacts in this kernel folder before final
  completion.
- Before committing or opening a PR, inspect the staged diff and exclude raw
  NCU reports, Nsight traces, profiler directories, warp-timeline dumps,
  temporary harness binaries, build outputs, scratch logs, failed experiment
  dumps, and large intermediate benchmark files.
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
  PATH="$KDA_LAUNCH_PATH" \
  SHELL="$KDA_SELECTED_BASH" \
  KDA_BASH_BIN="$KDA_SELECTED_BASH" \
  CLAUDE_PROJECT_DIR="$PWD" \
  IS_SANDBOX="${IS_SANDBOX:-1}" \
  HUMANIZE_CODEX_BYPASS_SANDBOX="${HUMANIZE_CODEX_BYPASS_SANDBOX:-true}" \
  "$CLAUDE_BIN" \
  --permission-mode bypassPermissions \
  --model "$CLAUDE_MODEL" \
  --effort "$CLAUDE_EFFORT" \
  "$@"
