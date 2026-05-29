# KDA Prompt: h200_diffusion_fuse_scale_shift__multi_shape

Optimize the SGLang diffusion `Fused scale_shift + dual-modulation (Z-Image adaLN)` kernel(s) for the full set of
production diffusion-model shapes captured from the SGLang diffusion benchmark
skill on NVIDIA H200. This prompt follows the Kernel Design Agents workflow
with official Humanize, KernelWiki, and `ncu-report-skill` available.

This is a multi-shape KDA prompt in the style of
`BBuf/kernel-design-agents`: first recover the baseline and correctness
contract, then run profiling-guided optimization, then specialize per shape
bucket with a dispatcher when measured evidence justifies it.

## Kernel Information

- Kernel folder: `h200_diffusion_fuse_scale_shift__multi_shape`
- Source project: SGLang (`python/sglang/jit_kernel/diffusion/`)
- Description: Optimize the SGLang diffusion fused-modulation Triton kernels: `fuse_scale_shift_kernel` (x*(1+scale)+shift on 3D BLC inputs with optional 4D scale/shift), `fuse_layernorm_scale_shift_gate_select01_kernel` (LN + adaLN + gate, dual-modulation per token), and `fuse_residual_layernorm_scale_shift_gate_select01_kernel` (additional residual+gate input).
- Hardware target: NVIDIA H200
- Wrapped baseline entry points:
- `sglang.jit_kernel.diffusion.triton.scale_shift:fuse_scale_shift_kernel`
- `sglang.jit_kernel.diffusion.triton.scale_shift:fuse_layernorm_scale_shift_gate_select01_kernel`
- `sglang.jit_kernel.diffusion.triton.scale_shift:fuse_residual_layernorm_scale_shift_gate_select01_kernel`
- Correctness oracle reference test:
`python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py`
- Promotion target: optimize toward the active hardware performance bound,
not a fixed speedup multiplier. Report median-latency speedup over the
current SGLang baseline as the geometric mean of per-shape speedups
across the configured shape table below, but treat that value as an
outcome metric rather than a pass/fail threshold.

## Workload Cases (Production Shapes)

These workload cases are empirical-only. They are the unique kernel call
signatures observed from successful `status=ok` runs while sweeping every
preset listed by the current `bench_diffusion_denoise.py --list-models`
source under the SGLang diffusion benchmark skill. Do not add
model-config-derived or analytical shapes to this table.

| Preset | Model | Kernel | dtype | x shape | modulation tensors | flags | Evidence |
|---|---|---|---|---|---|---|---|
| firered-edit-1.0 | FireRedTeam/FireRed-Image-Edit-1.0 | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 8424, 3072]/bfloat16C` | arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 8424, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |
| hunyuanvideo | hunyuanvideo-community/HunyuanVideo | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 27030, 3072]/bfloat16C` | arg1=`[1, 3072]/bfloat16C` ; arg2=`[1, 27030, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |
| hunyuanvideo | hunyuanvideo-community/HunyuanVideo | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 55, 3072]/bfloat16C` | arg1=`[1, 3072]/bfloat16C` ; arg2=`[1, 55, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 2 |
| hunyuanvideo | hunyuanvideo-community/HunyuanVideo | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 27085, 3072]/bfloat16C` | arg1=`[1, 3072]/bfloat16C` ; arg2=`[1, 27085, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 41 |
| qwen | Qwen/Qwen-Image-2512 | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 4096, 3072]/bfloat16C` | arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 4096, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |
| qwen | Qwen/Qwen-Image-2512 | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 19, 3072]/bfloat16C` | arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 19, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 2 |
| qwen | Qwen/Qwen-Image-2512 | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 47, 3072]/bfloat16C` | arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 47, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 122 |
| qwen-edit | Qwen/Qwen-Image-Edit-2511 | `scale_shift.fuse_layernorm_scale_shift_gate_select01_kernel` | bfloat16 | arg0=`[1, 8424, 3072]/bfloat16C` | scale0=`[1, 3072]/bfloat16C` ; shift0=`[1, 3072]/bfloat16C` ; gate0=`[1, 3072]/bfloat16C` ; scale1=`[1, 3072]/bfloat16C` ; shift1=`[1, 3072]/bfloat16C` ; gate1=`[1, 3072]/bfloat16C` ; index=`[1, 8424]/int32C` | weight=`None` ; bias=`None` ; eps=`1e-06` | ion8-h200 call 1 |
| qwen-edit | Qwen/Qwen-Image-Edit-2511 | `scale_shift.fuse_residual_layernorm_scale_shift_gate_select01_kernel` | bfloat16 | arg0=`[1, 8424, 3072]/bfloat16C` | residual=`[1, 8424, 3072]/bfloat16C` ; residual_gate=`[1, 8424, 3072]/bfloat16C` ; scale0=`[1, 3072]/bfloat16C` ; shift0=`[1, 3072]/bfloat16C` ; gate0=`[1, 3072]/bfloat16C` ; scale1=`[1, 3072]/bfloat16C` ; shift1=`[1, 3072]/bfloat16C` ; gate1=`[1, 3072]/bfloat16C` ; index=`[1, 8424]/int32C` | weight=`None` ; bias=`None` ; eps=`1e-06` | ion8-h200 call 1 |
| qwen-edit | Qwen/Qwen-Image-Edit-2511 | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 8424, 3072]/bfloat16C` | arg1=`[1, 8424, 3072]/bfloat16C` ; arg2=`[1, 8424, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |
| qwen-edit | Qwen/Qwen-Image-Edit-2511 | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 195, 3072]/bfloat16C` | arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 195, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 2 |
| qwen-edit | Qwen/Qwen-Image-Edit-2511 | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 189, 3072]/bfloat16C` | arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 189, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 122 |
| wan-i2v | Wan-AI/Wan2.2-I2V-A14B-Diffusers | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 37044, 5120]/bfloat16C` | arg1=`[1, 1, 5120]/float32C` ; arg2=`[1, 37044, 5120]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |
| wan-t2v | Wan-AI/Wan2.2-T2V-A14B-Diffusers | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 37800, 5120]/bfloat16C` | arg1=`[1, 1, 5120]/float32C` ; arg2=`[1, 37800, 5120]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |
| wan-ti2v | Wan-AI/Wan2.2-TI2V-5B-Diffusers | `scale_shift.fuse_scale_shift_kernel` | bfloat16 | arg0=`[1, 18144, 3072]/bfloat16C` | arg1=`[1, 18144, 3072]/float32NC` ; arg2=`[1, 18144, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |

Shape collection methodology: all entries above come directly from
`kernel_shape_capture.py` JSONL records collected while running the
full SGLang diffusion benchmark preset list on `ion-b200`, `ion8-h200`,
and/or `ion9-h200`. Each accepted preset had `status=ok`, a valid
denoise/refinement perf dump, and more than install-only capture lines.
Each preset run used `--backend=sglang` through the benchmark helper and
model weights were deleted from the Hugging Face cache immediately after
that preset completed.

- Captured presets for this task/arch: `['firered-edit-1.0', 'hunyuanvideo', 'qwen', 'qwen-edit', 'wan-i2v', 'wan-t2v', 'wan-ti2v']`
- Capture hosts for this task/arch: `['ion8-h200']`
- Raw evidence: `docs/captured_shapes_h200.jsonl`
- Summary: `docs/captured_shapes_h200.md`

Humanize/RLCR instruction: do not determine, derive, broaden, or
reinterpret optimization shapes during plan generation. The workload
shape set is exactly the rows in this prompt and the matching
`docs/captured_shapes_h200.jsonl`; use those shapes verbatim.

## Canonical Regression Shapes (from SGLang test)

Source: `python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py` (covers all three
scale-shift Triton entry points: `fuse_scale_shift_kernel`, the `select01` variant and the
residual `select01` variant).

- `batch_size`: `[1, 2, 4]` (CI subset `[1, 2]`).
- `seq_len`: `[6, 33, 128, 257]` (CI subset `[6, 128]`).
- `hidden_size`: `[512, 1024, 1536, 3072]` (CI subset `[512, 3072]`).
- `dtype`: `[float16, bfloat16, float32]` (CI subset `[fp16, bf16]`).
- `eps`: `1e-6`.
- `scale0/shift0/gate0/scale1/shift1/gate1`: each shaped `(B, C)`.
- `index`: shaped `(B, L)`, bool / int — required by the `select01` dispatch path.
- Residual / residual_gate path tested on the same grid via
  `fuse_residual_layernorm_scale_shift_gate_select01_kernel`.
- Tolerance: `(atol=5e-2, rtol=5e-2)` non-fp32; `1e-5` fp32.

The simple `fuse_scale_shift_kernel` accepts both 2D `(B,C)` scale/shift and 4D `(B,F,1,C)` scale/shift
(video frames). Cover both layouts during regression.

## Configurable Optimization Axes

Each candidate kernel/family may need different code paths or autotune
configs for different points in this axis space:

- x shape: B in [1,2] * L in [4096..75600] * C in [2048..5120]
- scale/shift layout: (B,C) / (1,C) / (B,F,1,C) / scalar
- dual-modulation index path (Qwen-Image-Edit / Z-Image)
- residual+gate path (Z-Image residual block)
- BLOCK_L / BLOCK_C / num_warps / num_stages choice
- dtype (bfloat16 / float16 / float32)

The promotion target is per-shape correctness plus hardware-bound
performance evidence across **all** configured shapes. A candidate is
target-complete when benchmarks and profiler data show that each important
shape bucket is close to its active bound (memory bandwidth, compute
throughput, launch overhead, occupancy, or dependency/latency limit), or
when a well-supported no-go explains why the remaining gap is not
reachable inside this task boundary. Per-shape specialization is allowed
and encouraged when profiler or benchmark evidence shows that one kernel
cannot cover the whole axis space. See the Shape Specialization Policy
below.

## Required Claude Code Skill

This task talks to the remote GPU box exclusively through the local
Claude Code skills `~/.claude/skills/ion8-h200/SKILL.md` (primary)
and `~/.claude/skills/ion9-h200/SKILL.md` (interchangeable backup
with the same H200 topology and the same `sglang_bbuf` container).
Either skill owns the SSH alias, container lifecycle (privileged
+ Nsight Compute access), idle-GPU selection rule, and the
`kill-idle` shortcut.

Pick whichever skill currently has idle H200 GPUs available; the
remote workspace path, container name, and benchmark commands in
the next section apply to both. If neither skill is loaded, fetch
them before starting the loop; do not paraphrase the SSH pattern by
hand.

## Environment And Remote Rule

Use the `ion8-h200 (or ion9-h200 as backup)` remote GPU environment for all NVIDIA H200
work. All CUDA, Python, pip, nvcc, build, test, benchmark, and Nsight Compute
commands must run inside the existing `sglang_bbuf` Docker container on
`ion8-h200`, with an idle NVIDIA H200 GPU selected.

Before running GPU work, inspect `nvidia-smi` and choose a GPU with no active
compute processes and no meaningful memory occupancy. Export that id as
`REMOTE_GPU_ID` and use it consistently for the baseline, candidate,
benchmark, profiler, and NCU commands in the current run.

Use this command pattern for remote execution:

```bash
ssh ion8-h200 'REMOTE_GPU_ID=<idle-gpu-id>; docker exec sglang_bbuf bash -lc "CUDA_VISIBLE_DEVICES=${REMOTE_GPU_ID} <command>"'
```

Do not run Python, pip, nvcc, builds, tests, benchmarks, or profiling
directly on the `ion8-h200` host.

When multiple sessions share the same remote container, create a task-owned
remote workspace under:

```text
/home/sglang-omni/bbuf/kda_runs/h200_diffusion_fuse_scale_shift__multi_shape/<timestamp-or-session-id>
```

Export it as `REMOTE_KDA_DIR`. Keep build outputs, profiler traces, NCU
reports, captured tensors, and benchmark logs inside that directory.

Before and after every benchmark or profile run, check GPU state and record
the selected host, GPU id, and GPU model in `benchmark.csv` or
`docs/draft.md`.

## Workspace Rule

All work for this kernel task must happen inside the current prompt folder,
the folder that contains this `prompt.md`.

Required local files:

- `src/`: optimized wrapper, native sources (CUDA `.cu`/`.cuh`/`.cpp` for the
CUDA family, Triton/CuTe-DSL Python for the others), dispatcher code, and
registration entrypoint.
- `tests/`: correctness tests adapted from the SGLang reference test under
`python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py`.
- `docs/draft.md`: implementation-plan draft written before code changes.
- `docs/captured_shapes_h200.jsonl`: captured shape JSONL from the diffusion
benchmark sweep, copied into this folder.
- `benchmark.csv`: every measured baseline vs candidate comparison.
- `solutions.jsonl`: every candidate implementation, parent link, status,
and evidence pointer.
- `profile/`: profiler traces and summaries.
- `ncu/`: Nsight Compute reports when collected.

Keep SGLang checkouts as dependencies to inspect, run, or patch
temporarily. The optimized implementation and evidence for this task stay
local to this folder unless intentionally promoted later.

## Baseline Recovery And Correctness Harness

Recover the baseline before writing optimized code:

1. Inspect the SGLang baseline implementation file(s) corresponding to each
wrapped entry point in `sglang/jit_kernel/diffusion/triton/scale_shift.py`.
2. Build a reproducible baseline harness for every shape in the shape table.
3. Adapt the SGLang reference correctness test `python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py` into
`tests/test_correctness.py` of this folder, parameterized over the
configured shape buckets.
4. Capture or generate baseline inputs covering the relevant dtypes and
layouts above.
5. Preserve explicit NaN/Inf checks in every validator.
6. Use dynamic numerical tolerances where applicable
(SGLang-style: candidate error must not exceed a small multiple of the
reference BF16/FP16 quantization noise vs FP32).

The final candidate must pass correctness for every configured shape
before benchmark claims count.

## Benchmark Requirements

- Use warmup and repeated timing.
- Report median latency, mean latency, std, min, p10, and p90 per shape.
- Compare every candidate against the SGLang baseline from the same selected
idle NVIDIA H200 GPU and container environment.
- Keep benchmark scripts and raw result logs in this folder.
- Every claimed improvement must identify the candidate commit or file
version and the exact command used to produce the result.
- Use Nsight Compute when a correct candidate is not clearly target-complete
or when profiler evidence would change the next edit.
- Final claim must be the geometric mean of per-shape speedups across the
full shape table, not the best-case shape alone.
- Final promotion or no-go must include a roofline-style bound analysis:
  estimate the effective bytes moved and useful scalar/vector operations
  for each representative shape bucket, report achieved bandwidth and/or
  FLOP/s, and use profiler metrics to identify the active limiting resource.
  Do not continue RLCR solely to hit a fixed speedup number once the
  evidence shows the candidate is already near the attainable bound.

## Prior Art Research Scope

Before choosing an implementation strategy, inspect SGLang, CUTLASS/CuTe,
CUDA samples, PyTorch, vLLM, TensorRT-LLM, FlashInfer, DeepGEMM, and
public Blackwell or Hopper kernels for directly relevant ideas. Use
KernelWiki when prior SM90, CUTLASS, SGLang, or normalization /
modulation / RoPE / group-norm evidence can guide a design choice.

Record reviewed source paths, commits or installed versions, and which
ideas were kept or rejected in `docs/draft.md` and `solutions.jsonl`.

## Implementation Language Policy

**The optimized candidate must be a native CUDA kernel built from
workspace-owned `.cu` / `.cuh` / `.cpp` / `.h` sources compiled with
`nvcc` (via a CUDA extension build or torch JIT), regardless of
whether the SGLang baseline is CUDA, Triton, or CuTe-DSL.** Python
is allowed for the wrapper, the dispatcher, build glue, harnesses,
and benchmark scripts, but not as the primary kernel.

The SGLang baseline — whatever language it is written in — is a
first-class **reference** for the CUDA candidate. Read its tile and
block choices, vectorization width, fast paths, fusion patterns,
numerical-stability tricks, dispatcher shape guards, and dtype
handling; the CUDA candidate is free to port any of those ideas
directly, replace them with a better algorithm, or mix them with
ideas pulled from KernelWiki PRs, CUTLASS / CuTe SM100 examples,
FlashAttention-4, DeepGEMM, FlashMLA, FlashInfer, or Hopper →
Blackwell migration notes. The baseline is one reference among
many — not a ceiling and not a required porting target. Record
every source whose idea ended up in the candidate in
`solutions.jsonl` with its file path / PR url / wiki page id.

After promotion, the export tool copies the CUDA sources into
`kda_kernels/diffusion/<family>/` so the shippable overlay stays
CUDA-only end-to-end. See the `## Promotion: Export Into
kda_kernels` section below for the export contract.

## External Reference Skills

Two repo-vendored skills live under `../../external/` (they are git
submodules; if either folder is empty, run
`git submodule update --init --recursive` from the repo root before
starting RLCR).

### KernelWiki (`../../external/KernelWiki/`)

Searchable knowledge base of 2,179 merged PRs across CUTLASS, SGLang,
vLLM, FlashInfer, PyTorch, Triton (Blackwell / SM100 + Hopper / SM90),
plus 48 wiki pages, 7 competitions, and 20 blog summaries. Read
`../../external/KernelWiki/SKILL.md` first for the full query syntax.

Treat KernelWiki as a **reference the agent consults at its own
discretion** — when designing the first candidate, when choosing
between two implementation directions, after any focused attempt
comes back slower than the SGLang baseline, when an ncu profile
surfaces a stall the playbook can't fully explain, or any time a
prior-art PR would unblock the next edit. The wiki is never
mandatory; skip it when the candidate direction is obvious and the
profiler evidence is clean.

Suggested targeted queries for this kernel family (fused scale-shift modulation including the Z-Image / Qwen-Image-Edit `select01` dual-modulation path):

  - `python3 ../../external/KernelWiki/scripts/query.py "adaLN modulation fused scale shift gate"`
  - `python3 ../../external/KernelWiki/scripts/query.py "DiT modulation kernel sm100"`
  - `python3 ../../external/KernelWiki/scripts/query.py --tag modulation --type kernel`
  - `python3 ../../external/KernelWiki/scripts/query.py --repo sglang --tag modulation --limit 20`

Record any PR / wiki page that influenced a design decision in
`docs/draft.md` and `solutions.jsonl` with its KernelWiki page id
or upstream PR URL.

### ncu-report-skill (`../../external/ncu-report-skill/`)

Nsight Compute B200 / SM100 workflow. Read
`../../external/ncu-report-skill/SKILL.md` first; the
`reference/` subdirectory has the directory layout, harness guide,
collection options, Python API, six analysis dimensions, diagnosis
playbook, and report template.

Profile **whenever profiler evidence would change the next edit** —
that is, after any benchmark result you do not fully understand,
whether the candidate got *faster* or *slower* than the baseline.
A speedup that comes from an unexpected dimension is just as worth
diagnosing as a regression: the active hardware bound from the
winning candidate tells you the next direction, and the bound from
a losing candidate tells you why the attempted edit didn't pay off.
Skip ncu only when both the result and the cause are already
obvious from code review or microbenchmark.

The mandatory pattern in this repo when you do profile:

  1. Create `profile/<run_name>/{harness,reports,analysis}/` — one
     dir per run, never reuse.
  2. Build a standalone harness under `profile/<run_name>/harness/`.
     Build the harness from your `src/` `.cu` / `.cuh` sources with
  `-lineinfo` so SASS maps back to source. Match the exact captured
  shape from `docs/captured_shapes_h200.jsonl` for the slice you
  are profiling.
  3. Run two profiles into `profile/<run_name>/reports/`:

     ```bash
     ncu --set full --target-processes all \
       -o profile/<run_name>/reports/full \
       <harness binary or python entrypoint>

     ncu --set source --section SourceCounters \
       -o profile/<run_name>/reports/source \
       <harness binary or python entrypoint>
     ```

  4. Parse with the `ncu_report` Python module via the helpers in
     `../../external/ncu-report-skill/helpers/`; write parsed CSVs
     into `profile/<run_name>/analysis/`.
  5. Walk the six analysis dimensions (compute / memory / occupancy
     / latency-hiding / launch-overhead / tail-effect) listed in
     `../../external/ncu-report-skill/reference/05-analysis-dimensions.md`.
  6. Match the dominant signal to
     `../../external/ncu-report-skill/reference/06-diagnosis-playbook.md`
     and write `profile/<run_name>/REPORT.md` using
     `reference/07-report-template.md`.

Record the matched diagnosis, before/after metric, and the resulting
design change in `solutions.jsonl` together with the report path.

## Optimization Exploration Policy

Use the KDA-style exploration loop:

- list candidate optimization directions in `docs/draft.md`;
- rank them by expected benefit, implementation risk, and how directly
they attack the measured bottleneck;
- try each direction for a bounded number of focused iterations;
- keep, revise, or reject each direction with correctness, benchmark, and
NCU evidence;
- maintain parent links in `solutions.jsonl` so later runs can reconstruct
the search DAG.

Consider SM90-specific optimization paths:

- `tcgen05` instructions or warp-specialized cooperative MMA where the
kernel touches a small inner matmul,
- TMEM / TMA / cluster shapes when the working set exceeds shared memory,
- persistent or split scheduling along (rows, hidden, frames, groups),
- vectorized loads/stores (LDG.128 / STG.128) keyed to dtype and stride,
- shared-memory staging vs register-file pressure tradeoffs,
- fused-epilogue patterns when the kernel chains norm + scale-shift +
gate + residual.

## Shape Specialization Policy

Shape-specialized kernels, template/config variants, and a dispatcher or
autotune table are allowed when measured evidence shows that different
shape buckets need different CTA, warpgroup, TMEM, or register-pressure
tradeoffs.

Record the dispatcher decision table with per-bucket baseline, candidate,
latency, speedup, and promote/reject reason in `benchmark.csv` and a
`docs/dispatch.md` note. Do not force a single universal kernel if
evidence shows that different shape buckets need different tradeoffs.

The shape buckets to consider include but are not limited to:

- small image (B*S in 4096..6144, D in 2048..3072) - FLUX/Qwen-Image/Z-Image
- large video (B*S in 33000..75600, D in 2048..5120) - Wan2.2/HunyuanVideo/MOVA/LTX-2
- small video (B*S in 8000..16000, D in 2048..3072) - Helios
- high-channel low-token (Wan A14B with D=5120) vs low-channel high-token (LTX-2 D=2048)

## Interface Contract

Add the candidate under `src/` and expose:

```text
src/register.py
```

with:

```python
KERNEL_SLUG = "h200_diffusion_fuse_scale_shift__multi_shape"
OP_TYPE = "fuse_scale_shift"

def optimized_wrapper(*args, **kwargs):
...

def register() -> dict:
return {
"name": KERNEL_SLUG,
"op_type": OP_TYPE,
"callable": optimized_wrapper,
"version": "dev",
"source": __file__,
}
```

`optimized_wrapper` must preserve the recovered SGLang callsite contract and
fall back to the baseline implementation for unsupported shapes, dtypes,
layouts, devices, normalization types, or feature flags. See
`interface.md` for the exact signature contract to be recovered from the
baseline.

## Required Workflow

1. Confirm the current directory is this kernel folder.
2. Read `../../external/KernelWiki/SKILL.md` and
`../../external/ncu-report-skill/SKILL.md` from this kernel folder.
3. Recover the SGLang baseline path, tensor contract, and exact benchmark
command for every shape in the shape table.
4. Copy the captured shape JSONL into `docs/captured_shapes_h200.jsonl`.
5. Write an implementation-plan draft to `docs/draft.md`.
6. Run official Humanize plan generation on that draft.
7. Start official Humanize RLCR from this kernel folder.
8. Do not implement kernels, run long benchmarks, or collect NCU evidence
before RLCR is active.
9. Record every candidate in `solutions.jsonl` and every performance result
in `benchmark.csv`.

## Promotion: Export Into kda_kernels

When the candidate is correct on every configured shape, beats the
promotion bar, and the dispatcher decision table is recorded, run
the export tool to promote the optimized wrapper into the
shippable `kda_kernels/` overlay:

```bash
python3 scripts/export_kda_kernels/export.py h200_diffusion_fuse_scale_shift__multi_shape
```

That copies this task's `src/` into
`kda_kernels/_impls/h200_diffusion_fuse_scale_shift__multi_shape/`, rewires the matching
kda_kernels stub for `fuse_scale_shift_kernel`, `fuse_layernorm_scale_shift_gate_select01_kernel`, `fuse_residual_layernorm_scale_shift_gate_select01_kernel` to import from there, and flips
`KDA_OPTIMIZED_<fn> = True` on each listed function.

For the export to know which functions to promote, `src/register.py`
must expose an `EXPORTS` dict alongside the existing `register()` /
`optimized_wrapper()` entries:

```python
# kernels/h200_diffusion_fuse_scale_shift__multi_shape/src/register.py

# ... optimized implementations of the wrapped functions live here ...

EXPORTS = {
        "fuse_scale_shift_kernel": fuse_scale_shift_kernel,
        "fuse_layernorm_scale_shift_gate_select01_kernel": fuse_layernorm_scale_shift_gate_select01_kernel,
        "fuse_residual_layernorm_scale_shift_gate_select01_kernel": fuse_residual_layernorm_scale_shift_gate_select01_kernel,
}
```

Functions not present in `EXPORTS` keep their kda_kernels stub on
the SGLang baseline. Partial promotion is safe; rerun export.py
after each additional function is ready, or run
`scripts/export_kda_kernels/export.py --revert h200_diffusion_fuse_scale_shift__multi_shape` to roll back.

After export, end-to-end activation inside an sglang checkout is:

```bash
export PYTHONPATH=/path/to/kernel-pilot:$PYTHONPATH
cd /path/to/sglang
git apply /path/to/kernel-pilot/patches/sglang_kda_kernels.patch
python3 -c 'import sglang; import kda_kernels; print(kda_kernels.status())'
```

and `kda_kernels.uninstall()` restores the SGLang baseline at runtime
without touching the patch.

See `kda_kernels/README.md`, `patches/README.md`, and
`scripts/export_kda_kernels/README.md` for the full contract.

## Completion Bar

The work is complete only when:

- correctness tests pass for every configured shape;
- every dispatched variant is correct for its assigned shape bucket;
- NVIDIA H200 benchmark evidence reports geometric-mean median-latency
speedup over the SGLang baseline across all configured shape buckets;
- roofline-style analysis and NCU evidence explain the improvement,
blocker, active hardware bound, and why the final candidate is close to
the attainable performance limit for the important shape buckets, or a
well-supported no-go explains why no defensible path remains under the
available workspace;
- `prompt.md`, `interface.md`, `benchmark.csv`, and `solutions.jsonl` are
updated with the final result.
