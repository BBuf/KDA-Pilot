# Ghostty + Claude Code Workflow (Diffusion Multi-Shape Tasks)

Use Ghostty manually for 4 parallel Claude Code optimization sessions against
the SGLang diffusion non-gemm/non-attention kernels in this repository. There
is no one-shot launcher in this repo; open panes yourself so each task stays
visible.

## Prerequisites

The 16 diffusion kernel tasks all run remote work through one of three Claude
Code skills. Before opening any pane verify these three SKILL.md files exist
locally:

```bash
ls ~/.claude/skills/ion-b200/SKILL.md
ls ~/.claude/skills/ion8-h200/SKILL.md
ls ~/.claude/skills/ion9-h200/SKILL.md
```

If any of them is missing, install it before continuing — the prompts
deliberately point each task at its skill name (`ion-b200` for B200 tasks,
`ion8-h200`/`ion9-h200` for H200 tasks) and **do not** paraphrase the SSH /
docker exec pattern themselves. The skill owns the SSH alias, the
`sglang_bbuf` Docker container lifecycle (privileged + `cap-add=SYS_ADMIN` +
`seccomp=unconfined` so `ncu --set basic` can collect counters), the
idle-GPU selection rule, and the `kill-idle` shortcut.

Verify the host aliases are reachable:

```bash
ssh -o ConnectTimeout=5 ion-b200    'hostname && nvidia-smi --query-gpu=name --format=csv,noheader | head -1'
ssh -o ConnectTimeout=5 ion8-h200   'hostname && nvidia-smi --query-gpu=name --format=csv,noheader | head -1'
ssh -o ConnectTimeout=5 ion9-h200   'hostname && nvidia-smi --query-gpu=name --format=csv,noheader | head -1'
```

For the gated FLUX / FLUX.2 paths, export your Hugging Face token in the
shell that launches the run (the skill picks it up through the existing
docker exec env propagation):

```bash
export HF_TOKEN=hf_...
```

For `qwen-edit`, `wan-ti2v`, and `wan-i2v` correctness work the remote
container must have
`/home/sglang-omni/bbuf/repos/sglang/inputs/diffusion_benchmark/figs/cat.png`
in place. The capture-tooling README under `scripts/diffusion_shape_capture/`
documents the one-line `docker cp` to deploy it.

Finally, make sure the latest task definitions are committed on `main` so the
launcher's git-worktree-base check passes:

```bash
cd /Users/bbuf/工作目录/Common/kernel-pilot
git status
git log --oneline -3
```

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

## Current Task Policy

`kernels/` has two reference tasks (`b200_int8_scaled_mm__*`,
`b200_fa4_mha__*`) plus 16 diffusion multi-shape tasks named
`{arch}_diffusion_{family}__multi_shape/`. The diffusion bucket is the active
optimization queue; the reference tasks remain as worked examples.

The 16 diffusion tasks split by hardware target (B200 / H200). Tensor shapes
are arch-independent, so each task can be picked up on the matching arch
without re-capturing shapes — the per-task
`docs/captured_shapes_<arch>.{jsonl,md}` and the cross-task
`kernels/diffusion_shapes_ledger.md` are the same regardless of which arch's
prompt the agent picks. Start with the high-impact diffusion families first,
because they each cover many sweep presets and live on the DiT critical path.

With four Ghostty panes, launch K3-K6 first (the B200 quartet of the four
highest-impact diffusion families); start the H200 variants in the first pane
that becomes free or in a second tab if you want to run both arches in
parallel.

| Priority | Suggested pane | Folder | Why this wave |
|---:|---|---|---|
| K3 | Top-left | `kernels/b200_diffusion_qknorm_rope__multi_shape` | Fused QKNorm + RoPE (CUDA) — fires on **qwen, qwen-edit, zimage, flux, flux2, helios** (6 of 12 presets); native CUDA implementation, biggest leverage on attention setup latency. |
| K4 | Top-right | `kernels/b200_diffusion_cutedsl_norm_scale_shift__multi_shape` | CuTe-DSL norm-scale-shift (+ residual variant) — fires on **qwen, qwen-edit, wan-ti2v, wan-t2v, hunyuanvideo, helios** (6 presets); Z-Image / Qwen-Image / Wan modulation. |
| K5 | Bottom-left | `kernels/b200_diffusion_fuse_scale_shift__multi_shape` | Triton fused scale-shift modulation including dual-modulation `select01` variants — fires on qwen, qwen-edit, hunyuanvideo, helios; adaLN-Zero analog used by every DiT block. |
| K6 | Bottom-right | `kernels/b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape` | CuTe-DSL `fused_norm_tanh_mul_add` (+ second-norm-scale variant) — Z-Image residual modulation primary; the only family that ships D=3840 / 4128 token-count shapes. |

After this first wave, queue the second wave (H200 mirrors of the same four
families, plus the remaining four families in either arch):

| Priority | Folder |
|---:|---|
| K4 (H200) | `kernels/h200_diffusion_qknorm_rope__multi_shape` |
| K17→K18 (H200 norm-scale-shift) | `kernels/h200_diffusion_cutedsl_norm_scale_shift__multi_shape` |
| K13→K14 (H200 fuse-scale-shift) | `kernels/h200_diffusion_fuse_scale_shift__multi_shape` |
| K15→K16 (H200 cutedsl tanh) | `kernels/h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape` |
| K11 / K12 | `*_diffusion_rotary_embedding__multi_shape` — standard RoPE (hunyuanvideo) + LTX-2 split RoPE. |
| K7 / K8 | `*_diffusion_norm_infer__multi_shape` — 2-pass LN/RMSN baseline + one-pass per-head RMSN. |
| K9 / K10 | `*_diffusion_group_norm_silu__multi_shape` — VAE GroupNorm + SiLU (hunyuanvideo 5D shapes). |
| K5 / K6 (rms_norm_fn) | `*_diffusion_rms_norm_fn__multi_shape` — analytical-only; no current preset hits this entry point. Optimize last. |

### Task Completion Log

| Task | Status | Outcome | Claude Code cost (from `/usage`) |
|---|---|---|---|
| **K3** `kernels/b200_diffusion_qknorm_rope__multi_shape` | _pending_ | _to be filled_ | _to be filled_ |
| **K4** `kernels/h200_diffusion_qknorm_rope__multi_shape` | _pending_ | _to be filled_ | _to be filled_ |
| **K5** `kernels/b200_diffusion_rms_norm_fn__multi_shape` | _pending_ | _to be filled_ | _to be filled_ |
| **K6** `kernels/h200_diffusion_rms_norm_fn__multi_shape` | _pending_ | _to be filled_ | _to be filled_ |
| **K7-K18** all other diffusion tasks | _pending_ | _to be filled_ | _to be filled_ |

Closed-row template (from the upstream kernel-design-agent-with-sglang-omini workflow): record outcome (`IMPROVEMENT | NO-GO`), measured speedup or geomean, host + GPU id, base/candidate commits, and Claude Code `/usage` cost.

## Claude Code Command

For parallel RLCR runs, do not share one checkout. Use the task scripts under
`scripts/launch_kernels/`; each script creates one task-owned git worktree and
launches Claude from that worktree's kernel folder.

In each Ghostty pane, run one script from the repository root:

```bash
cd /Users/bbuf/工作目录/Common/kernel-pilot
./scripts/launch_kernels/k03_b200_diffusion_qknorm_rope__multi_shape.sh
```

First-wave launcher scripts (B200 high-impact quartet):

| Priority | Script |
|---:|---|
| K3 | `./scripts/launch_kernels/k03_b200_diffusion_qknorm_rope__multi_shape.sh` |
| K17 | `./scripts/launch_kernels/k17_b200_diffusion_cutedsl_norm_scale_shift__multi_shape.sh` |
| K13 | `./scripts/launch_kernels/k13_b200_diffusion_fuse_scale_shift__multi_shape.sh` |
| K15 | `./scripts/launch_kernels/k15_b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape.sh` |

Full launcher list:

| Launcher | Folder |
|---|---|
| `k01_b200_int8_scaled_mm.sh` | reference task (single shape) |
| `k02_b200_fa4_mha.sh` | reference task (single shape) |
| `k03_b200_diffusion_qknorm_rope__multi_shape.sh` | B200 fused QKNorm + RoPE |
| `k04_h200_diffusion_qknorm_rope__multi_shape.sh` | H200 fused QKNorm + RoPE |
| `k05_b200_diffusion_rms_norm_fn__multi_shape.sh` | B200 flash-attn-style 1-pass LN/RMSN |
| `k06_h200_diffusion_rms_norm_fn__multi_shape.sh` | H200 flash-attn-style 1-pass LN/RMSN |
| `k07_b200_diffusion_norm_infer__multi_shape.sh` | B200 inference-only LN/RMSN + one-pass RMSN |
| `k08_h200_diffusion_norm_infer__multi_shape.sh` | H200 inference-only LN/RMSN + one-pass RMSN |
| `k09_b200_diffusion_group_norm_silu__multi_shape.sh` | B200 VAE GroupNorm + SiLU |
| `k10_h200_diffusion_group_norm_silu__multi_shape.sh` | H200 VAE GroupNorm + SiLU |
| `k11_b200_diffusion_rotary_embedding__multi_shape.sh` | B200 standard RoPE + LTX-2 split RoPE |
| `k12_h200_diffusion_rotary_embedding__multi_shape.sh` | H200 standard RoPE + LTX-2 split RoPE |
| `k13_b200_diffusion_fuse_scale_shift__multi_shape.sh` | B200 Triton fused scale-shift (+ select01) |
| `k14_h200_diffusion_fuse_scale_shift__multi_shape.sh` | H200 Triton fused scale-shift (+ select01) |
| `k15_b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape.sh` | B200 CuTe-DSL norm + tanh + mul + add (+ norm2-scale) |
| `k16_h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape.sh` | H200 CuTe-DSL norm + tanh + mul + add (+ norm2-scale) |
| `k17_b200_diffusion_cutedsl_norm_scale_shift__multi_shape.sh` | B200 CuTe-DSL norm * (1+scale) + shift (+ residual + gate) |
| `k18_h200_diffusion_cutedsl_norm_scale_shift__multi_shape.sh` | H200 CuTe-DSL norm * (1+scale) + shift (+ residual + gate) |

For an ad-hoc task folder, use:

```bash
./scripts/launch_kda_kernel_task.sh kernels/<task-folder>
```

Do not pass `prompt.md` as the final positional CLI argument if you want the
live Claude Code TUI.

Why this shape:
- In a linked git worktree, Humanize resolves the loop project root to the
  worktree root. The plan file therefore must be passed as a path relative
  to the worktree root, even though `gen-plan` writes it inside the current
  kernel folder.
- Each task has a separate git worktree, so Humanize's git-clean gate,
  commits, and generated code do not collide with other parallel kernel
  tasks.
- Each `scripts/launch_kernels/kXX_*.sh` wrapper passes its script name as
  the task-card label. The default branch and worktree names use that
  label (for example
  `kda/k03_b200_diffusion_qknorm_rope__multi_shape-<run-id>`), while the
  RLCR plan path still points at the real kernel folder under `kernels/`.
- The launcher also creates a pinned local review-base branch named
  `kda-base/<task-label>-<run-id>`. Use that printed branch for
  `--base-branch`; it freezes the review base at worktree creation time
  so later pushes to the source branch do not change the RLCR diff.
- Do not run multiple RLCR sessions from different kernel folders inside
  the same checkout; Git status and commits are repo-wide and the sessions
  will interfere.

Override knobs the launcher honors (set them before invoking the script):

```bash
KDA_BASE_BRANCH=main                              # base ref (default main)
KDA_WORKTREE_BASE=/path/to/kernel-pilot-worktrees # worktree parent dir
KDA_RUN_ID=my-run                                 # stable suffix
KDA_NO_CLAUDE=1                                   # prepare worktree only
CLAUDE_BIN=claude
CLAUDE_MODEL=opus
CLAUDE_EFFORT=max
HUMANIZE_CODEX_BYPASS_SANDBOX=true                # default; forwarded into Claude's env
                                                  # so Codex in the RLCR loop skips its
                                                  # per-call sandbox/approval prompts.
                                                  # Set anything other than true|1 to
                                                  # re-enable the sandbox.
```

## Prep Block

The launcher creates `.humanize/kernel-agent/draft.md` automatically from the
task's `prompt.md` plus the shared remote-GPU / KernelWiki / ncu /
remote-workspace constraints. This avoids the `INPUT_NOT_FOUND` prompt from
`/humanize:gen-plan` in fresh worktrees.

Then run Humanize gen-plan and write the final RLCR plan path directly:

```text
/humanize:gen-plan --input .humanize/kernel-agent/draft.md --output .humanize/kernel-agent/refined-plan.md --direct
```

Do not run `refine-plan` by default. `refine-plan` is only for a plan that
already contains human review comment blocks such as `CMT:` / `ENDCMT`,
`<cmt>` / `</cmt>`, or `<comment>` / `</comment>`. If you did manually
annotate `.humanize/kernel-agent/refined-plan.md`, run this optional command
before RLCR:

```text
/humanize:refine-plan --input .humanize/kernel-agent/refined-plan.md --qa-dir .humanize/kernel-agent/plan_qa --direct
```

If `refine-plan` reports `INPUT_NOT_FOUND` or `Input file has no comment
blocks`, skip it and start RLCR from `.humanize/kernel-agent/refined-plan.md`.
Do not add dummy `CMT:` blocks just to satisfy `refine-plan`.

Then start RLCR (the launcher prints the exact `--base-branch` value — paste
it back rather than guessing):

```text
/humanize:start-rlcr-loop kernels/<kernel-folder>/.humanize/kernel-agent/refined-plan.md --skip-quiz --claude-answer-codex --max 12 --codex-model gpt-5.5:xhigh --codex-timeout 5400 --base-branch <printed-kda-base-branch>
```

After RLCR starts, Claude should continue only from the generated
`.humanize/rlcr/<timestamp>/round-0-prompt.md`.

The default remote-phase policy is autonomous. Once local code and local
checks are committed, Claude should idle-check the GPU host listed in the
task prompt's `## Required Claude Code Skill` block (`ion-b200` for B200
tasks, `ion8-h200` / `ion9-h200` for H200 tasks), select a suitable idle
GPU or GPU set, sync the committed task branch to a task-owned remote
workspace, and run correctness, benchmarks, profiler captures, and NCU
evidence without asking for another confirmation. It should record the host,
GPU id, and GPU model. It should stop and ask only if no suitable idle GPU
is available, credentials/network access fail, a destructive operation is
required, or the plan's correctness/benchmark/baseline/promotion policy
would need to change.

The default decision policy is also autonomous for common kernel-loop forks:
if a remote baseline fails because the dependency stack is
version-inconsistent, Claude should pin/rebuild the matching dependency
checkout inside the task-owned remote workspace before asking; if the first
low-level kernel candidate is a well-evidenced no-win and profiler evidence
points to a higher-payoff runtime, callsite, CUDA-graph, batching, or fusion
path inside the same Python-level task boundary, Claude should pivot there
by default. It should ask before destructive global changes, shared checkout
rewrites, deleting another task's artifacts, or changing
correctness/baseline/promotion requirements.

## Prompt Cards

Each diffusion task card lists the wrapped SGLang entry points, the captured
preset shapes, the canonical SGLang test grid that must still pass, and the
remote host. The full text lives in the linked `prompt.md`; this card is a
quick chooser.

### K3 / K4. Fused QKNorm + RoPE (CUDA)

- Folder: `kernels/{b200,h200}_diffusion_qknorm_rope__multi_shape/`
- Prompt: [`b200 prompt.md`](../kernels/b200_diffusion_qknorm_rope__multi_shape/prompt.md) · [`h200 prompt.md`](../kernels/h200_diffusion_qknorm_rope__multi_shape/prompt.md)
- Launcher: `./scripts/launch_kernels/k03_b200_diffusion_qknorm_rope__multi_shape.sh` · `./scripts/launch_kernels/k04_h200_diffusion_qknorm_rope__multi_shape.sh`
- Wrapped baseline: `sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope` (native CUDA, templated by `head_dim`, `rope_dim`, `is_neox`, `dtype`).
- Why first: fires on **qwen, qwen-edit, zimage, flux, flux2, helios** (6 of 12 sweep presets), `num_heads` in {24, 30, 48}; `head_dim=128`, `rope_dim=128` (Qwen/Z-Image/FLUX joint) or `rope_dim=96` (LTX-style). Native CUDA candidate must also be CUDA.

### K17 / K18. CuTe-DSL norm-scale-shift (+ residual)

- Folder: `kernels/{b200,h200}_diffusion_cutedsl_norm_scale_shift__multi_shape/`
- Prompt: [`b200 prompt.md`](../kernels/b200_diffusion_cutedsl_norm_scale_shift__multi_shape/prompt.md) · [`h200 prompt.md`](../kernels/h200_diffusion_cutedsl_norm_scale_shift__multi_shape/prompt.md)
- Launcher: `./scripts/launch_kernels/k17_b200_diffusion_cutedsl_norm_scale_shift__multi_shape.sh` · `./scripts/launch_kernels/k18_h200_diffusion_cutedsl_norm_scale_shift__multi_shape.sh`
- Wrapped baseline: `sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_norm_scale_shift` + `fused_scale_residual_norm_scale_shift`.
- Why second: fires on **qwen, qwen-edit, wan-ti2v, wan-t2v, hunyuanvideo, helios** (6 presets); D in {3072, 5120}; live shapes include `(1, 4096, 3072)`, `(1, 18144, 3072)` (Wan-TI2V), `(1, 37800, 5120)` (Wan-T2V, FP32 scale/shift), `(1, 11040, 5120)` (Helios). D constraint: `D % 256 == 0` and `D <= 8192`.

### K13 / K14. Triton fused scale-shift + dual-modulation select01

- Folder: `kernels/{b200,h200}_diffusion_fuse_scale_shift__multi_shape/`
- Prompt: [`b200 prompt.md`](../kernels/b200_diffusion_fuse_scale_shift__multi_shape/prompt.md) · [`h200 prompt.md`](../kernels/h200_diffusion_fuse_scale_shift__multi_shape/prompt.md)
- Launcher: `./scripts/launch_kernels/k13_b200_diffusion_fuse_scale_shift__multi_shape.sh` · `./scripts/launch_kernels/k14_h200_diffusion_fuse_scale_shift__multi_shape.sh`
- Wrapped baseline: `sglang.jit_kernel.diffusion.triton.scale_shift:fuse_scale_shift_kernel`, plus the `fuse_layernorm_scale_shift_gate_select01_kernel` and `fuse_residual_layernorm_scale_shift_gate_select01_kernel` Qwen-Image-Edit variants.
- Why third: every DiT block calls this; live captures from qwen, qwen-edit, hunyuanvideo, helios. Covers `(B,C)`, `(1,C)`, `(B,F,1,C)` scale/shift layouts.

### K15 / K16. CuTe-DSL norm + tanh + mul + add (Z-Image residual)

- Folder: `kernels/{b200,h200}_diffusion_cutedsl_norm_tanh_mul_add__multi_shape/`
- Prompt: [`b200 prompt.md`](../kernels/b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape/prompt.md) · [`h200 prompt.md`](../kernels/h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape/prompt.md)
- Launcher: `./scripts/launch_kernels/k15_b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape.sh` · `./scripts/launch_kernels/k16_h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape.sh`
- Wrapped baseline: `sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add` + `fused_norm_tanh_mul_add_norm_scale`.
- Why fourth: Z-Image residual modulation is the primary callsite. Captured shapes use **D=3840** (Z-Image-Turbo specific) and S in {4096, 4128}. Same `D % 256 == 0` and `D <= 8192` constraint as K17/K18.

### K11 / K12. Standard RoPE + LTX-2 split RoPE

- Folder: `kernels/{b200,h200}_diffusion_rotary_embedding__multi_shape/`
- Wrapped baseline: `sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding` (HunyuanVideo standard RoPE) and `sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb` (LTX-2 split rotary with non-contiguous cos/sin).
- Live captures: hunyuanvideo (1, 27030, 24, 128) bf16 + (27030, 64) cos/sin fp32; ltx2 (1/2, S, inner_dim) with `num_heads=32`, `half_dim` in {32, 64}.

### K7 / K8. Norm infer + one-pass RMSN

- Folder: `kernels/{b200,h200}_diffusion_norm_infer__multi_shape/`
- Wrapped baseline: `sglang.jit_kernel.diffusion.triton.norm:norm_infer` (helios 2-pass LayerNorm at `(8640, 5120)` fp32) + `sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm` (zimage / hunyuanvideo per-head RMSNorm tiles, including the dramatic `(648720, 128)` HunyuanVideo joint regime).

### K9 / K10. VAE GroupNorm + SiLU

- Folder: `kernels/{b200,h200}_diffusion_group_norm_silu__multi_shape/`
- Wrapped baseline: `sglang.jit_kernel.diffusion.triton.group_norm_silu:triton_group_norm_silu` + `sglang.jit_kernel.diffusion.group_norm_silu:apply_group_norm_silu`.
- Live captures: hunyuanvideo VAE decoder — `(1, 512, 5, 32, 32)/fp16` and `(1, 128, 17, 256, 256)/fp16`, `num_groups=32`.

### K5 / K6. Flash-attn-style 1-pass LN/RMSN

- Folder: `kernels/{b200,h200}_diffusion_rms_norm_fn__multi_shape/`
- Wrapped baseline: `sglang.jit_kernel.diffusion.triton.norm:rms_norm_fn` (ported from Dao-AILab flash-attention).
- Status: analytical-only. No sweep preset currently dispatches here; queue last in case a future model lands on this path. Use the canonical SGLang test grid (`tests/test_rmsnorm.py`) as the primary regression contract.

### Continue The Queue

After the first wave, continue from
[`kernels/diffusion_kernel_coverage.md`](../kernels/diffusion_kernel_coverage.md)
and
[`kernels/diffusion_shapes_ledger.md`](../kernels/diffusion_shapes_ledger.md).
Re-run `scripts/diffusion_shape_capture/sweep_models.sh` +
`scripts/diffusion_shape_capture/finalize.sh` when a new model preset goes
into the SGLang diffusion benchmark skill or after a CuTe-DSL kernel
signature changes; that refresh keeps every task's
`docs/captured_shapes_<arch>.{jsonl,md}` aligned with production.
