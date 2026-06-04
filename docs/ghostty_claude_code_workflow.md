# Ghostty + Claude Code Workflow

Use Ghostty manually for parallel Claude Code optimization sessions. The
launcher scripts create one git worktree per task, so each pane can work on a
different kernel folder without sharing generated files, Humanize state, or git
commits.

This workflow is for the current standalone diffusion task layout. The old
SGLang overlay, export, and shape-capture machinery is intentionally gone.
Every diffusion task now copies the upstream SGLang kernel source into its own
`baseline/` directory and benchmarks that copied baseline against the candidate
through a matching local ABI.

## Prerequisites

Start from a committed branch that contains the current task skeletons:

```bash
cd /Users/bbuf/工作目录/Common/kernel-pilot
git status
git log --oneline -3
```

Check the launcher scripts:

```bash
bash -n scripts/launch_kda_kernel_task.sh scripts/launch_kernels/*.sh
```

If the task needs remote GPU validation, use the matching Claude/Codex remote
skill for the target host:

```bash
ls ~/.codex/skills/ion-b200/SKILL.md
ls ~/.codex/skills/ion8-h200/SKILL.md
ls ~/.codex/skills/ion9-h200/SKILL.md
```

B200 tasks should run benchmark/profiling on B200. H200 tasks should run on an
H200 host. Before a remote run, check that the host alias is reachable and has
an idle GPU:

```bash
ssh -o ConnectTimeout=5 ion-b200  'hostname && nvidia-smi --query-gpu=name --format=csv,noheader | head -1'
ssh -o ConnectTimeout=5 ion8-h200 'hostname && nvidia-smi --query-gpu=name --format=csv,noheader | head -1'
ssh -o ConnectTimeout=5 ion9-h200 'hostname && nvidia-smi --query-gpu=name --format=csv,noheader | head -1'
```

For gated model shape-audit reruns such as FLUX or FLUX.2, export an authorized
Hugging Face token in the launching shell:

```bash
export HF_TOKEN=hf_...
```

Normal standalone kernel benchmarks should not import or patch SGLang at
runtime. Read these documents before changing any task:

- [`standalone_diffusion_benchmark.md`](standalone_diffusion_benchmark.md)
- [`diffusion_kernel_rules.md`](diffusion_kernel_rules.md)
- [`diffusion_correctness_contract.md`](diffusion_correctness_contract.md)
- [`diffusion_benchmark_shape_coverage.md`](diffusion_benchmark_shape_coverage.md)

## Ghostty Shortcuts

| Shortcut | Action |
|---|---|
| `Cmd + D` | Split current pane to the right |
| `Cmd + Shift + D` | Split current pane downward |
| `Cmd + W` | Close current pane/tab/window surface |
| `Cmd + T` | Open a new tab |
| `Cmd + Shift + [` | Previous tab |
| `Cmd + Shift + ]` | Next tab |
| `Cmd + ,` | Open Ghostty config |
| `Cmd + Shift + ,` | Reload Ghostty config |
| `Ctrl + backquote` | Toggle quick terminal |
| `Cmd + backquote` | Toggle quick terminal |

Validate config with:

```bash
ghostty +validate-config
```

## Parallel Policy

There is no priority split in this document. Pick any unclaimed diffusion task
whose target GPU is available. With four panes, a practical pattern is:

1. Open four panes in one Ghostty tab.
2. Launch one `scripts/launch_kernels/kXX_*.sh` script in each pane.
3. When a pane finishes or blocks on unavailable hardware, start another
   unclaimed task.
4. Keep B200 tasks on B200 and H200 tasks on H200.

The `K` number is only the launcher file number under `scripts/launch_kernels/`;
it is not an optimization priority.

## Launch Command

Run scripts from the repository root:

```bash
cd /Users/bbuf/工作目录/Common/kernel-pilot
./scripts/launch_kernels/k03_b200_diffusion_qknorm_rope__multi_shape.sh
```

For an ad-hoc task folder:

```bash
./scripts/launch_kda_kernel_task.sh kernels/<task-folder>
```

Set `KDA_NO_CLAUDE=1` to create the task worktree and print commands without
starting Claude:

```bash
KDA_NO_CLAUDE=1 ./scripts/launch_kernels/k03_b200_diffusion_qknorm_rope__multi_shape.sh
```

The launcher creates:

- one task-owned git branch
- one task-owned git worktree
- one pinned local review-base branch named `kda-base/<task-label>-<run-id>`
- `.humanize/kernel-agent/draft.md` from the task's `prompt.md`

Use the printed review-base branch for RLCR. Do not guess it.

Useful launcher overrides:

```bash
KDA_BASE_BRANCH=<ref>   # optional; defaults to the current checkout branch
KDA_WORKTREE_BASE=/path/to/kernel-pilot-worktrees
KDA_RUN_ID=my-run
KDA_BRANCH_PREFIX=kda
KDA_NO_CLAUDE=1
CLAUDE_BIN=claude
CLAUDE_MODEL=opus
CLAUDE_EFFORT=max
HUMANIZE_CODEX_BYPASS_SANDBOX=true
```

## Humanize Flow

The launcher enters the task directory inside the generated worktree. From
there, generate the plan:

```text
/humanize:gen-plan --input .humanize/kernel-agent/draft.md --output .humanize/kernel-agent/refined-plan.md --direct
```

Do not run `refine-plan` by default. Use it only when the generated plan has
manual review comment blocks such as `CMT:` / `ENDCMT`, `<cmt>` / `</cmt>`, or
`<comment>` / `</comment>`.

Start RLCR with the review-base branch printed by the launcher:

```text
/humanize:start-rlcr-loop kernels/<kernel-folder>/.humanize/kernel-agent/refined-plan.md --skip-quiz --claude-answer-codex --max 12 --codex-model gpt-5.5:high --codex-timeout 5400 --base-branch <printed-kda-base-branch>
```

After RLCR starts, continue from the generated
`.humanize/rlcr/<timestamp>/round-0-prompt.md`.

## Task Contract

Each diffusion task starts with only:

```text
prompt.md
config.toml
baseline/.gitkeep
solution/.gitkeep
bench/.gitkeep
docs/.gitkeep
```

The first agent milestone must fill:

```text
baseline/
  copied upstream SGLang source files
  local baseline ABI wrapper
solution/
  candidate implementation with the same ABI
bench/
  workloads.json
  correctness.py
  benchmark.py
  adapter.py
docs/
  baseline_source.md
  benchmark_method.md
  benchmark_preset_audit.md
  run_log.md
```

`baseline_source.md` must identify the latest upstream SGLang `main` commit
resolved at baseline-recovery time, plus the copied files and any local adapter
edits.

The benchmark is invalid if it imports SGLang at runtime, patches an SGLang
checkout, compares different wrapper overheads, silently skips a production
workload, changes workloads after tuning without remeasuring both sides, or
keeps timing numbers without provenance.

## Launchers

There are 16 launch scripts: two reference tasks and 14 diffusion tasks. The
diffusion rows are listed in launcher-number order only.

| Launcher | Folder |
|---|---|
| `k01_b200_int8_scaled_mm.sh` | `kernels/b200_int8_scaled_mm__m64_n2048_k2048_bias` |
| `k02_b200_fa4_mha.sh` | `kernels/b200_fa4_mha__bf16_head128_total32768` |
| `k03_b200_diffusion_qknorm_rope__multi_shape.sh` | `kernels/b200_diffusion_qknorm_rope__multi_shape` |
| `k04_h200_diffusion_qknorm_rope__multi_shape.sh` | `kernels/h200_diffusion_qknorm_rope__multi_shape` |
| `k05_b200_diffusion_norm_infer__multi_shape.sh` | `kernels/b200_diffusion_norm_infer__multi_shape` |
| `k06_h200_diffusion_norm_infer__multi_shape.sh` | `kernels/h200_diffusion_norm_infer__multi_shape` |
| `k07_b200_diffusion_group_norm_silu__multi_shape.sh` | `kernels/b200_diffusion_group_norm_silu__multi_shape` |
| `k08_h200_diffusion_group_norm_silu__multi_shape.sh` | `kernels/h200_diffusion_group_norm_silu__multi_shape` |
| `k09_b200_diffusion_rotary_embedding__multi_shape.sh` | `kernels/b200_diffusion_rotary_embedding__multi_shape` |
| `k10_h200_diffusion_rotary_embedding__multi_shape.sh` | `kernels/h200_diffusion_rotary_embedding__multi_shape` |
| `k11_b200_diffusion_fuse_scale_shift__multi_shape.sh` | `kernels/b200_diffusion_fuse_scale_shift__multi_shape` |
| `k12_h200_diffusion_fuse_scale_shift__multi_shape.sh` | `kernels/h200_diffusion_fuse_scale_shift__multi_shape` |
| `k13_b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape.sh` | `kernels/b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape` |
| `k14_h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape.sh` | `kernels/h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape` |
| `k15_b200_diffusion_cutedsl_norm_scale_shift__multi_shape.sh` | `kernels/b200_diffusion_cutedsl_norm_scale_shift__multi_shape` |
| `k16_h200_diffusion_cutedsl_norm_scale_shift__multi_shape.sh` | `kernels/h200_diffusion_cutedsl_norm_scale_shift__multi_shape` |

## Diffusion Task Cards

These cards are a compact chooser. The full requirements live in each task's
`prompt.md`.

| Launchers | Family | SGLang entry points copied as baseline |
|---|---|---|
| K3 / K4 | QKNorm + RoPE | `qknorm_rope:fused_inplace_qknorm_rope` |
| K5 / K6 | Norm infer | `norm:norm_infer`, `rmsnorm_onepass:triton_one_pass_rms_norm` |
| K7 / K8 | GroupNorm + SiLU | `group_norm_silu:apply_group_norm_silu`, `triton.group_norm_silu:triton_group_norm_silu` |
| K9 / K10 | Rotary embedding | `rotary:apply_rotary_embedding`, `ltx2_rotary:apply_ltx2_split_rotary_emb` |
| K11 / K12 | Scale-shift | `scale_shift:fuse_scale_shift_kernel`, `fuse_layernorm_scale_shift_gate_select01_kernel`, `fuse_residual_layernorm_scale_shift_gate_select01_kernel` |
| K13 / K14 | Norm + tanh + mul + add | `norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add`, `fused_norm_tanh_mul_add_norm_scale` |
| K15 / K16 | Norm-scale-shift | `scale_residual_norm_scale_shift:fused_norm_scale_shift`, `fused_scale_residual_norm_scale_shift` |

For shapes and live preset coverage, use
[`diffusion_benchmark_shape_coverage.md`](diffusion_benchmark_shape_coverage.md).
If the coverage document says a preset is blocked, do not invent shape rows.
Either rerun the model on B200/H200 and record a valid native capture, or add a
live no-call proof to `docs/benchmark_preset_audit.md` inside the task.

## Completion Log

Keep one row per launched task. Record both wins and no-go outcomes.

| Task | Status | Outcome | Host/GPU | Commit | Claude Code cost |
|---|---|---|---|---|---|
| K3 | pending | to be filled | to be filled | to be filled | to be filled |
| K4 | pending | to be filled | to be filled | to be filled | to be filled |
| K5 | pending | to be filled | to be filled | to be filled | to be filled |
| K6 | pending | to be filled | to be filled | to be filled | to be filled |
| K7 | pending | to be filled | to be filled | to be filled | to be filled |
| K8 | pending | to be filled | to be filled | to be filled | to be filled |
| K9 | pending | to be filled | to be filled | to be filled | to be filled |
| K10 | pending | to be filled | to be filled | to be filled | to be filled |
| K11 | pending | to be filled | to be filled | to be filled | to be filled |
| K12 | pending | to be filled | to be filled | to be filled | to be filled |
| K13 | pending | to be filled | to be filled | to be filled | to be filled |
| K14 | pending | to be filled | to be filled | to be filled | to be filled |
| K15 | pending | to be filled | to be filled | to be filled | to be filled |
| K16 | pending | to be filled | to be filled | to be filled | to be filled |

Closed-row fields:

- outcome: `IMPROVEMENT`, `NO-GO`, or `BLOCKED`
- measured speedup or geomean
- host, GPU id, and GPU model
- baseline commit/source and candidate commit
- benchmark command and result path
- Claude Code `/usage` cost
