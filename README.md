# KernelPilot

KernelPilot is a Kernel Design Agents style prompt repository for B200 and H200
GPU kernel experiments, currently focused on SGLang diffusion (non-gemm,
non-attention) kernels and a couple of legacy reference tasks. Each optimization
target lives in a self-contained `kernels/<task>/` folder, and each run starts
from an isolated git worktree with official Humanize commands.

This repository does not vendor or patch Humanize. Install and use the official
Humanize runtime in your agent environment, then launch one kernel task at a
time from the scripts in this repo.

## Layout

```text
external/KernelWiki/          # upstream kernel evidence and PR knowledge
external/ncu-report-skill/    # Nsight Compute profiling workflow
kernels/
  b200_int8_scaled_mm__m64_n2048_k2048_bias/
  b200_fa4_mha__bf16_head128_total32768/
  {b200,h200}_diffusion_qknorm_rope__multi_shape/
  {b200,h200}_diffusion_norm_infer__multi_shape/
  {b200,h200}_diffusion_group_norm_silu__multi_shape/
  {b200,h200}_diffusion_rotary_embedding__multi_shape/
  {b200,h200}_diffusion_fuse_scale_shift__multi_shape/
  {b200,h200}_diffusion_cutedsl_norm_tanh_mul_add__multi_shape/
  {b200,h200}_diffusion_cutedsl_norm_scale_shift__multi_shape/
scripts/
  launch_kda_kernel_task.sh
  launch_kernels/
    k01_b200_int8_scaled_mm.sh
    k02_b200_fa4_mha.sh
    k03_b200_diffusion_qknorm_rope__multi_shape.sh
    k04_h200_diffusion_qknorm_rope__multi_shape.sh
    ...
    k18_h200_diffusion_cutedsl_norm_scale_shift__multi_shape.sh
```

Each kernel folder owns its prompt, interface contract, benchmark scaffold,
correctness scaffold, candidate ledger, benchmark ledger, notes, profiles, and
NCU reports. Nothing in the workflow depends on a repo-local Humanize copy.

## Install

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/BBuf/kernel-pilot.git
cd kernel-pilot
```

For an existing checkout:

```bash
git submodule update --init --recursive
```

Install official Humanize separately, following the upstream Humanize
instructions used by your Claude Code environment. After installation, Claude
Code should expose commands such as:

```text
/humanize:gen-plan
/humanize:start-rlcr-loop
```

## Optimization Workflow

Use [`docs/ghostty_claude_code_workflow.md`](docs/ghostty_claude_code_workflow.md)
for the cold-terminal flow that opens four parallel Claude Code RLCR panes
against the diffusion task queue, including the four-pane first wave,
prerequisites (the three local `ion-*` skills + `HF_TOKEN` + remote
`cat.png`), launcher invocation pattern, Humanize gen-plan / start-rlcr-loop
prep block, and per-task prompt cards.

## Shipping Optimized Kernels (`kda_kernels/` + sglang patch)

Once a KDA task lands a promoted candidate, run

```bash
python3 scripts/export_kda_kernels/export.py <task-slug>
```

to copy the task's `src/` into [`kda_kernels/_impls/<task-slug>/`](kda_kernels)
and rewire the matching [`kda_kernels/diffusion/<file>.py`](kda_kernels) stub
to import from it (flipping `KDA_OPTIMIZED_<fn> = True`). Activating every
promoted kernel inside an sglang checkout is one command:

```bash
export PYTHONPATH=/path/to/kernel-pilot:$PYTHONPATH
cd /path/to/sglang
git apply /path/to/kernel-pilot/patches/sglang_kda_kernels.patch
```

The patch adds 16 lines at the end of `python/sglang/__init__.py` that try
`import kda_kernels; kda_kernels.install()`. Functions still on the baseline
(not yet promoted via `export.py`) are untouched, so partial promotion is
safe. Inspect, undo at runtime, or revert the patch any time:

```python
import kda_kernels
print(kda_kernels.status())     # currently-swapped sglang paths
kda_kernels.uninstall()         # restore baseline without removing patch
```

See [`kda_kernels/README.md`](kda_kernels/README.md),
[`patches/README.md`](patches/README.md), and
[`scripts/export_kda_kernels/README.md`](scripts/export_kda_kernels/README.md)
for the full contract (the `EXPORTS = {...}` rule each task's
`src/register.py` follows, revert flow, per-function `KDA_TASK_<fn>` /
`KDA_COMMIT_<fn>` / `KDA_DATE_<fn>` / `KDA_SPEEDUP_<fn>` stamps, and
patch-regeneration when upstream sglang edits `__init__.py`).

## Kernel Tasks

### Reference Tasks (single fixed shape)

| Kernel | Goal | Launcher |
| --- | --- | --- |
| [`b200_int8_scaled_mm__m64_n2048_k2048_bias`](kernels/b200_int8_scaled_mm__m64_n2048_k2048_bias/prompt.md) | Optimize SGLang `int8_scaled_mm` for `M=64, N=2048, K=2048`, fp16 output, `bias=true` on B200. | `scripts/launch_kernels/k01_b200_int8_scaled_mm.sh` |
| [`b200_fa4_mha__bf16_head128_total32768`](kernels/b200_fa4_mha__bf16_head128_total32768/prompt.md) | Build a standalone BF16 forward-only MHA kernel and compare against FlashAttention-4 on B200. | `scripts/launch_kernels/k02_b200_fa4_mha.sh` |

### SGLang Diffusion Multi-Shape Tasks

These tasks cover the SGLang non-gemm/non-attention diffusion kernels under
`python/sglang/jit_kernel/diffusion/`. Each task's shape table is captured from
accepted live SGLang diffusion benchmark preset runs on the corresponding remote
GPU box. Presets only contribute shapes when the native SGLang run finishes with
a valid denoise/refinement perf dump, so gated or failed runs are excluded from
the workload tables. The preset sweep runs on `ion-b200` for the B200 variants
and on `ion8-h200` / `ion9-h200` for the H200 variants.

Each task's `prompt.md` carries the full shape table and explicitly allows
shape-bucketed dispatchers, per-bucket configs, and per-bucket kernel variants
(in the style of `b200_fa4_mha__bf16_head128_total32768`).

| Kernel | Arch | Goal | Launcher |
| --- | --- | --- | --- |
| [`b200_diffusion_qknorm_rope__multi_shape`](kernels/b200_diffusion_qknorm_rope__multi_shape/prompt.md) | B200 | Fused in-place QKNorm + RoPE (CUDA) across all diffusion preset shapes. | `scripts/launch_kernels/k03_b200_diffusion_qknorm_rope__multi_shape.sh` |
| [`h200_diffusion_qknorm_rope__multi_shape`](kernels/h200_diffusion_qknorm_rope__multi_shape/prompt.md) | H200 | Same as B200 variant, H200 target. | `scripts/launch_kernels/k04_h200_diffusion_qknorm_rope__multi_shape.sh` |
| [`b200_diffusion_norm_infer__multi_shape`](kernels/b200_diffusion_norm_infer__multi_shape/prompt.md) | B200 | Inference-only LN/RMSN baseline (`norm_infer` and `triton_one_pass_rms_norm`). | `scripts/launch_kernels/k07_b200_diffusion_norm_infer__multi_shape.sh` |
| [`h200_diffusion_norm_infer__multi_shape`](kernels/h200_diffusion_norm_infer__multi_shape/prompt.md) | H200 | Same as B200 variant, H200 target. | `scripts/launch_kernels/k08_h200_diffusion_norm_infer__multi_shape.sh` |
| [`b200_diffusion_group_norm_silu__multi_shape`](kernels/b200_diffusion_group_norm_silu__multi_shape/prompt.md) | B200 | Fused GroupNorm + SiLU across image (2D/3D) and video (3D/5D) VAE inputs. | `scripts/launch_kernels/k09_b200_diffusion_group_norm_silu__multi_shape.sh` |
| [`h200_diffusion_group_norm_silu__multi_shape`](kernels/h200_diffusion_group_norm_silu__multi_shape/prompt.md) | H200 | Same as B200 variant, H200 target. | `scripts/launch_kernels/k10_h200_diffusion_group_norm_silu__multi_shape.sh` |
| [`b200_diffusion_rotary_embedding__multi_shape`](kernels/b200_diffusion_rotary_embedding__multi_shape/prompt.md) | B200 | Standard RoPE and LTX-2 split RoPE across all diffusion preset token counts. | `scripts/launch_kernels/k11_b200_diffusion_rotary_embedding__multi_shape.sh` |
| [`h200_diffusion_rotary_embedding__multi_shape`](kernels/h200_diffusion_rotary_embedding__multi_shape/prompt.md) | H200 | Same as B200 variant, H200 target. | `scripts/launch_kernels/k12_h200_diffusion_rotary_embedding__multi_shape.sh` |
| [`b200_diffusion_fuse_scale_shift__multi_shape`](kernels/b200_diffusion_fuse_scale_shift__multi_shape/prompt.md) | B200 | Triton fused scale-shift modulation (`fuse_scale_shift_kernel` + dual-modulation Z-Image variants). | `scripts/launch_kernels/k13_b200_diffusion_fuse_scale_shift__multi_shape.sh` |
| [`h200_diffusion_fuse_scale_shift__multi_shape`](kernels/h200_diffusion_fuse_scale_shift__multi_shape/prompt.md) | H200 | Same as B200 variant, H200 target. | `scripts/launch_kernels/k14_h200_diffusion_fuse_scale_shift__multi_shape.sh` |
| [`b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape`](kernels/b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape/prompt.md) | B200 | CuTe-DSL `fused_norm_tanh_mul_add` (Z-Image residual modulation) and the second-norm scale combined kernel. | `scripts/launch_kernels/k15_b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape.sh` |
| [`h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape`](kernels/h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape/prompt.md) | H200 | Same as B200 variant, H200 target. | `scripts/launch_kernels/k16_h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape.sh` |
| [`b200_diffusion_cutedsl_norm_scale_shift__multi_shape`](kernels/b200_diffusion_cutedsl_norm_scale_shift__multi_shape/prompt.md) | B200 | CuTe-DSL `fused_norm_scale_shift` (and `fused_scale_residual_norm_scale_shift`) across all diffusion presets. | `scripts/launch_kernels/k17_b200_diffusion_cutedsl_norm_scale_shift__multi_shape.sh` |
| [`h200_diffusion_cutedsl_norm_scale_shift__multi_shape`](kernels/h200_diffusion_cutedsl_norm_scale_shift__multi_shape/prompt.md) | H200 | Same as B200 variant, H200 target. | `scripts/launch_kernels/k18_h200_diffusion_cutedsl_norm_scale_shift__multi_shape.sh` |

## Launch

Run one kernel launcher from the repository root:

```bash
scripts/launch_kernels/k01_b200_int8_scaled_mm.sh
```

or:

```bash
scripts/launch_kernels/k02_b200_fa4_mha.sh
```

The launcher creates a task-specific worktree, enters the selected kernel
folder, sets `CLAUDE_PROJECT_DIR` to that folder, and creates
`.humanize/kernel-agent/draft.md` from the local `prompt.md`.

The selected `KDA_BASE_BRANCH` must already contain the target kernel folder.
After editing these task definitions, commit them first or set `KDA_BASE_BRANCH`
to a ref that contains them.

Inside Claude Code, run the two commands printed by the launcher:

```text
/humanize:gen-plan --input .humanize/kernel-agent/draft.md --output .humanize/kernel-agent/refined-plan.md --direct
/humanize:start-rlcr-loop .humanize/kernel-agent/refined-plan.md --skip-quiz --claude-answer-codex --max 12 --codex-model gpt-5.5:high --codex-timeout 5400 --base-branch <printed-review-base>
```

### Humanize / Codex Hook Caveat

If Codex review appears stuck for a long time with a status like
`running stop hook` while tokens keep increasing, check the local Humanize
runtime before blaming the kernel task. Older Humanize hook scripts may launch
nested Codex review with only `--disable codex_hooks`. Newer Codex builds use
the `hooks` feature name, so that does not actually disable hooks; the nested
review can re-enter the Humanize Stop hook and loop inside the reviewer.

Avoid this before launching a large RLCR run:

- Keep the official `--codex-timeout 5400` unless a task has a specific reason
  to fail faster or run longer.
- Use an updated Humanize runtime whose nested `codex exec` calls disable all
  known hook feature names: `--disable hooks --disable plugin_hooks --disable
  codex_hooks`.
- On macOS, ensure the Humanize portable timeout kills the whole child process
  group, not only the direct `codex` parent. Otherwise timed-out reviewer
  descendants can keep running.
- If hook files were edited locally, re-trust the Codex hook when Codex asks.

Useful overrides:

```bash
KDA_BASE_BRANCH=main                         # base ref for the task worktree
KDA_WORKTREE_BASE=/path/to/kernel-worktrees  # parent directory for worktrees
KDA_RUN_ID=my-run                            # stable branch/worktree suffix
KDA_NO_CLAUDE=1                              # prepare the worktree only
CLAUDE_BIN=claude                            # Claude executable
CLAUDE_MODEL=opus                            # Claude model flag
CLAUDE_EFFORT=max                            # Claude effort flag
HUMANIZE_CODEX_BYPASS_SANDBOX=true           # default; forwarded into Claude's env so
                                             # Codex in the RLCR loop skips per-call
                                             # sandbox/approval prompts. Set anything
                                             # other than true|1 to re-enable.
```

## Kernel Folder Contract

```text
prompt.md                 # source task prompt
interface.md              # expected candidate wrapper/register contract
benchmark.py              # local timing scaffold
benchmark.csv             # append-only benchmark evidence ledger
solutions.jsonl           # append-only candidate lineage ledger
src/                      # candidate implementation entry point
tests/test_correctness.py # correctness scaffold
docs/                     # plan notes, source notes, run logs
profile/                  # profiler traces
ncu/                      # Nsight Compute reports
```

The Humanize plan should recover `K/R/W` from `prompt.md` before implementation:

- `K`: kernel semantics and callsite contract
- `R`: correctness oracle and baseline path
- `W`: workload shapes and benchmark methodology

Keep generated `.humanize*` state untracked.

## Maintenance

Validate the external knowledge submodule when updating it:

```bash
cd external/KernelWiki
python3 scripts/validate.py
```

Check launcher syntax after edits:

```bash
bash -n scripts/launch_kda_kernel_task.sh scripts/launch_kernels/*.sh
```

Update external skills with:

```bash
git submodule update --remote external/KernelWiki
git submodule update --remote external/ncu-report-skill
```

## References

- [`BBuf/kernel-design-agents`](https://github.com/BBuf/kernel-design-agents):
  KernelPilot reuses this repository's kernel-design-agent method and workflow.
- [`BBuf/kernel-design-agent-with-sglang-omini`](https://github.com/BBuf/kernel-design-agent-with-sglang-omini):
  KernelPilot follows its `kernels/` folder style and per-kernel launch script
  pattern.
- [`PolyArch/humanize`](https://github.com/PolyArch/humanize): official
  Humanize runtime used by the launch flow.
- [`BBuf/KernelWiki`](https://github.com/BBuf/KernelWiki): upstream kernel
  evidence and prior-art source used by the prompts.
- [`DongyunZou/ncu-report-skill`](https://github.com/DongyunZou/ncu-report-skill):
  Nsight Compute profiling workflow used when profiler evidence is needed.
