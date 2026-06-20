<div align="center">

# KDA-Pilot

**Evidence-first autonomous GPU-kernel optimization campaigns for SGLang.**

KDA-Pilot turns real serving-framework kernels into reproducible optimization
tasks: frozen production shapes, copied upstream baselines, symmetric
benchmarks, correctness gates, Nsight Compute evidence, KernelWiki references,
and RLCR-style agent iteration in one place.

[![GitHub stars](https://img.shields.io/github/stars/BBuf/KDA-Pilot?style=social)](https://github.com/BBuf/KDA-Pilot/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/BBuf/KDA-Pilot?style=social)](https://github.com/BBuf/KDA-Pilot/forks)
[![Last commit](https://img.shields.io/github/last-commit/BBuf/KDA-Pilot?style=flat-square)](https://github.com/BBuf/KDA-Pilot/commits/main)
[![B200 diffusion](https://img.shields.io/badge/B200_diffusion-7_kernel_tasks-2ea44f?style=flat-square)](#b200-diffusion-results)
[![AI Infra Skills](https://img.shields.io/badge/sibling-AI--Infra--Auto--Driven--SKILLS-2f80ed?style=flat-square)](https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS)

</div>

Most AI kernel demos optimize a snippet. KDA-Pilot optimizes the parts that
actually show up in SGLang diffusion and LLM serving workflows, then keeps the
evidence needed to tell whether the agent really improved the production path.

If you care about autonomous CUDA/Triton/CuTe-DSL optimization that can be
replayed, reviewed, and compared against real framework baselines, this is the
repo to watch.

## Why It Matters

- **Real workloads, not toy shapes.** Diffusion tasks were built from 20 real
  SGLang diffusion models and collapsed into per-kernel multi-shape workloads.
- **Wall-time metrics.** The headline numbers include Python, dispatch,
  wrappers, kernel launch, and `cuda.synchronize()` overhead, not just isolated
  device time.
- **No reward-hacking path.** Baseline and candidate use matching local ABIs;
  the task does not monkey-patch or import SGLang at runtime.
- **Knowledge-guided iteration.** Tasks can pull from `KernelWiki` and
  `ncu-report-skill`, so prior Blackwell/Hopper kernel work and NCU bottleneck
  evidence become part of the optimization loop.
- **Agent loop with review.** Candidate promotion is tied to correctness gates,
  run logs, and code review rather than "one fast row wins".

## B200 Diffusion Results

These are wall geomean speedups against the corresponding SGLang/Triton/CuTe-DSL
baselines on B200. The measurements include dispatch and synchronization
overheads, so they are closer to what a user sees from the public kernel path.

| Kernel task | B200 wall geomean | Representative wins |
| --- | ---: | --- |
| `qknorm_rope` | 1.1341x | large rows 1.145-1.279x |
| `norm_infer` | 1.3523x | RMS small 1.634-1.641x |
| `rotary_embedding` | 1.4912x | HunyuanVideo 2.087x; LTX2 1.133-1.622x |
| `cutedsl_norm_tanh_mul_add` | 1.4953x | v1 1.602-1.625x |
| `cutedsl_norm_scale_shift` | 1.3201x | Hunyuan 1.388-1.516x; JoyAI 1.477-1.495x |
| `fuse_scale_shift` | 2.7499x | small broadcast rows 7.365-7.891x |
| `group_norm_silu` | 2.3118x | small/mid C rows 1.369-4.982x; NC rows up to 3.648x |

## KernelWiki-Guided Highlights

| Kernel | KernelWiki / reference | Key techniques |
| --- | --- | --- |
| `qknorm_rope` | **TensorRT-LLM PR-13052/11869 DiT QKNorm+RoPE; SGLang PR-15141/19059/21440/21654 fused QKNorm/RoPE; memory-bound pattern** | Shared RoPE staging, Q/K reuse, staged path only for large rows |
| `norm_infer` | **KernelWiki memory-bound/vectorized-loads/register-budgeting; vLLM PR-31828 SM100 RMSNorm opt-in path** | Warp-row RMS, tiled persistent RMS, 8B/16B vector paths |
| `rotary_embedding` | **SGLang PR-24411 LTX2 split RoPE; vLLM PR-21126/30729 FlashInfer RoPE routing; vectorized-loads** | 128-bit vector I/O, cos/sin hoisting, LTX2 block matching |
| `cutedsl_norm_tanh_mul_add` | **KernelWiki memory-bound/vectorized-loads/register-budgeting; NCU long-scoreboard and launch-bounds evidence** | Hoisted row-invariant math, launch-bounds tuning, exact `tanhf` |
| `cutedsl_norm_scale_shift` | **SGLang PR-14717 CuTe-DSL norm/scale/shift fusion; vectorized-loads; register-budgeting** | Operand-class dispatch, 16B/32B vectors, two-pass variance |
| `fuse_scale_shift` | **SGLang PR-14717 fused norm/scale/shift family; vectorized-loads; cache-policy; memory-bound pattern** | Rowgrid/flatvec/exact-C paths, cache hints, one-pass reduction |
| `group_norm_silu` | **SGLang PR-22814/23148/23938 GroupNorm+SiLU; memory-bound pattern; vectorized-loads** | Split-group stats, generation counters, channels-last transpose |

The companion write-up records the benchmark interpretation, kernel-specific
optimization paths, KernelWiki/reference links, and AKO4X comparison:
[KDA-Pilot optimizing SGLang Diffusion Kernel](https://github.com/BBuf/how-to-optim-algorithm-in-cuda/blob/main/large-language-model/sglang/KDA-Pilot%20%E4%BC%98%E5%8C%96%20SGLang%20Diffusion%20Kernel%20%E6%95%88%E6%9E%9C%E4%B8%8E%E7%BB%8F%E9%AA%8C.md).

## What Is Inside

```text
diffusion/    SGLang diffusion-operator kernel tasks.
              Each task owns a copied baseline, optimized solution, benchmark,
              correctness contract, run logs, and result ledger.

llm/          SGLang autoregressive-model kernel-workflow campaign.
              Serve priority models on B200/H200, benchmark low/mid/high
              concurrency, profile forward passes, and turn >=1% non-attention
              kernels into optimization task cards.

external/     Optional shared knowledge submodules.
              KernelWiki/         Blackwell/Hopper kernel design references
              ncu-report-skill/   Nsight Compute profiling/report helper
```

Start with:

- [`diffusion/README.md`](diffusion/README.md) for standalone diffusion kernel
  tasks and benchmark rules.
- [`llm/README.md`](llm/README.md) for the LLM kernel-workflow campaign.
- [`diffusion/docs/standalone_diffusion_benchmark.md`](diffusion/docs/standalone_diffusion_benchmark.md)
  for the baseline/candidate benchmark contract.
- [`diffusion/docs/diffusion_kernel_rules.md`](diffusion/docs/diffusion_kernel_rules.md)
  for correctness, fallback, and promotion guardrails.

## Task Lifecycle

Every diffusion kernel task follows the same shape:

```text
prompt.md       task card for the agent
config.toml     benchmark/build defaults
baseline/       copied upstream SGLang baseline source
solution/       optimized candidate source
bench/          standalone benchmark and correctness harness
docs/           run logs, profile notes, source notes, decision ledger
```

The important rule is symmetry: the agent must compare the copied baseline and
candidate through matching local interfaces, fixed workload rows, preallocated
outputs, CUDA-event timing, interleaved A/B sampling, strict correctness checks,
and full provenance.

## Run A Task

Clone submodules when you want the optional knowledge references:

```bash
git submodule update --init --recursive
```

Launch a task from the repo root:

```bash
diffusion/scripts/launch_kernels/k03_b200_diffusion_qknorm_rope__multi_shape.sh
```

Useful environment switches:

```bash
KDA_NO_CLAUDE=1                 # prepare the worktree without launching an agent
KDA_BASE_BRANCH=<ref>           # launch from a specific committed ref
KDA_BASH_BIN=/opt/homebrew/bin/bash
```

macOS `/bin/bash` 3.2 is rejected by the launcher because nested Humanize/Codex
hooks rely on modern Bash behavior.

## How I Drive The Agents

These campaigns are run with coding agents in full-autonomy mode. For
reproducibility, here is exactly how I launch them on a prepared task worktree.

**Claude Code** — the same combo the diffusion launcher uses (Opus 4.8 + max
effort + auto/bypass-permission mode, i.e. the "Effort (Max)" + "Auto mode"
toggles in the Claude Code UI):

```bash
claude --permission-mode bypassPermissions --model opus --effort max
```

`diffusion/scripts/launch_kda_kernel_task.sh` invokes exactly this (defaults
`CLAUDE_MODEL=opus`, `CLAUDE_EFFORT=max`, `--permission-mode bypassPermissions`),
so launching a task and running Claude by hand are equivalent. To iterate a
long-running goal across model switches, resume the session:

```bash
claude --resume <session-uuid>
```

**Ultracode mode** — the maximum-thoroughness setting (the "Effort (Ultracode –
xhigh + workflows)" entry in the Claude Code effort menu, paired with Auto mode).
Ultracode is *not* a launch-flag effort value: `claude --effort ultracode` warns
(`Unknown --effort value 'ultracode'`) and falls back to the default — the valid
`--effort` flag levels are `low, medium, high, xhigh, max`. Ultracode is a
composite of **xhigh effort + dynamic workflows enabled**, so the agent reasons
at xhigh and authors multi-agent workflows on substantive tasks. Enable dynamic
workflows once — the **Dynamic workflows** toggle in `/config` (settings key
`enableWorkflows`) — then launch at xhigh:

```bash
claude --permission-mode bypassPermissions --model opus --effort xhigh
```

Or do it in one self-contained command:

```bash
claude --permission-mode bypassPermissions --model opus --effort xhigh --settings '{"enableWorkflows": true}'
```

With workflows enabled, the in-session `/effort` menu shows "Ultracode" and
selecting it pins xhigh. To opt a single prompt in instead of the whole session,
include the keyword `ultracode` in that message.

**Codex** — full-access, no approval prompts:

```bash
codex --yolo --sandbox danger-full-access --ask-for-approval never
```

Both run unsandboxed / auto-approve because each task lives in an isolated
prepared worktree with its own benchmark + correctness gates; an agent's wins
only count when the correctness contract and run logs agree.

## Current Campaigns

- **Diffusion kernels:** qk norm + RoPE, norm inference, rotary embedding,
  fused scale/shift, group norm + SiLU, CuTe-DSL norm/tanh/mul/add, and
  CuTe-DSL norm/scale/shift across B200 and H200 task folders.
- **LLM kernel workflow:** model-level serving commands, benchmark sweeps,
  torch profiler traces, and kernel inventories for future optimization tasks.
- **Open frontier:** compute-bound kernels such as FA4/MHA and GEMM-like paths
  remain harder; this repo keeps the failed and partial attempts visible so the
  next loop can start from evidence instead of folklore.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=BBuf/KDA-Pilot&type=Date)](https://star-history.com/#BBuf/KDA-Pilot&Date)
