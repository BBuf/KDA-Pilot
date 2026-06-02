# KDA Prompt: b200_diffusion_norm_infer__multi_shape

Optimize the SGLang diffusion `Inference-only LN/RMSN 2-pass kernel` kernel(s) for the full set of
production diffusion-model shapes captured from the SGLang diffusion benchmark
skill on NVIDIA B200. This prompt follows the Kernel Design Agents workflow
with official Humanize, KernelWiki, and `ncu-report-skill` available.

This is a multi-shape KDA prompt in the style of
`BBuf/kernel-design-agents`: first recover the baseline and correctness
contract, then run profiling-guided optimization, then specialize per shape
bucket with a dispatcher when measured evidence justifies it.

## Kernel Information

- Kernel folder: `b200_diffusion_norm_infer__multi_shape`
- Source project: SGLang (`python/sglang/jit_kernel/diffusion/`)
- Description: Optimize the two SGLang diffusion inference-only norm kernels: `norm_infer` (2-pass LN/RMSN baseline) and `triton_one_pass_rms_norm` (tiled one-pass RMSN). Both consume 2D row tensors and run pure forward on the diffusion path.
- Hardware target: NVIDIA B200
- Wrapped baseline entry points:
- `sglang.jit_kernel.diffusion.triton.norm:norm_infer`
- `sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm`
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

| Preset | Model | Kernel | dtype | x shape | weight/bias | flags | Evidence |
|---|---|---|---|---|---|---|---|
| helios | BestWishYsh/Helios-Base | `norm.norm_infer` | float32 | arg0=`[8640, 5120]/float32C` | arg1=`[5120]/float32C` ; arg2=`[5120]/float32C` | eps=`1e-06` ; is_rms_norm=`False` | ion-b200 call 1 |
| hunyuanvideo | hunyuanvideo-community/HunyuanVideo | `rmsnorm_onepass.triton_one_pass_rms_norm` | bfloat16 | arg0=`[648720, 128]/bfloat16C` | arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 1 |
| hunyuanvideo | hunyuanvideo-community/HunyuanVideo | `rmsnorm_onepass.triton_one_pass_rms_norm` | bfloat16 | arg0=`[1320, 128]/bfloat16C` | arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 3 |
| hunyuanvideo | hunyuanvideo-community/HunyuanVideo | `rmsnorm_onepass.triton_one_pass_rms_norm` | bfloat16 | arg0=`[650040, 128]/bfloat16C` | arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 81 |
| zimage | Tongyi-MAI/Z-Image-Turbo | `rmsnorm_onepass.triton_one_pass_rms_norm` | bfloat16 | arg0=`[16384, 128]/bfloat16C` | arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 1 |
| zimage | Tongyi-MAI/Z-Image-Turbo | `rmsnorm_onepass.triton_one_pass_rms_norm` | bfloat16 | arg0=`[4096, 128]/bfloat16C` | arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 2 |

Shape collection methodology: all entries above come directly from
`kernel_shape_capture.py` JSONL records collected while running the
full SGLang diffusion benchmark preset list on `ion-b200`, `ion8-h200`,
and/or `ion9-h200`. Each accepted preset had `status=ok`, a valid
denoise/refinement perf dump, and more than install-only capture lines.
Each preset run used `--backend=sglang` through the benchmark helper and
model weights were deleted from the Hugging Face cache immediately after
that preset completed.

- Captured presets for this task/arch: `['helios', 'hunyuanvideo', 'zimage']`
- Capture hosts for this task/arch: `['ion-b200']`
- Raw evidence: `docs/captured_shapes_b200.jsonl`
- Summary: `docs/captured_shapes_b200.md`

Humanize/RLCR instruction: do not determine, derive, broaden, or
reinterpret optimization shapes during plan generation. The workload
shape set is exactly the rows in this prompt and the matching
`docs/captured_shapes_b200.jsonl`; use those shapes verbatim.

## Canonical Regression Shapes (from SGLang test)

Source: `python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py`
(this is the file that exercises `norm_infer` end-to-end as part of the Z-Image / Qwen-Image
select01 dual-modulation baseline).

- `batch_size`: `[1, 2, 4]` (CI subset `[1, 2]`).
- `seq_len`: `[6, 33, 128, 257]` (CI subset `[6, 128]`).
- `hidden_size`: `[512, 1024, 1536, 3072]` (CI subset `[512, 3072]`).
- `dtype`: `[torch.float16, torch.bfloat16, torch.float32]` (CI subset `[fp16, bf16]`).
- `eps`: `1e-6`.
- `is_rms_norm`: explicit kernel argument; the test uses `False` (LayerNorm).
- Tolerance: `(atol=5e-2, rtol=5e-2)` for non-fp32, `1e-5` for fp32.

Cross-validate `triton_one_pass_rms_norm` on the same row counts (`M = B*S`) and on per-head tiles
`(4096, 128)` / `(16384, 128)` (the live captures from Z-Image).

## Configurable Optimization Axes

Each candidate kernel/family may need different code paths or autotune
configs for different points in this axis space:

- M (rows) in 1024..100000
- N (hidden) in 1024..8192
- norm_type (layer/rms)
- has_weight / has_bias
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
Claude Code skill `~/.claude/skills/ion-b200/SKILL.md`. The skill
owns the SSH alias `ion-b200`, the `sglang_bbuf` Docker container
lifecycle (the create command keeps `--privileged --cap-add=SYS_ADMIN
--security-opt seccomp=unconfined` so `ncu --set basic` can collect
counters), the idle-GPU selection rule (`nvidia-smi` 0% util + low
memory), and the `kill-idle` shortcut.

If the skill is missing on the box that launches Humanize/RLCR, fetch
it before starting the loop; do not paraphrase the SSH pattern by
hand. The skill's SKILL.md is the single source of truth for `ion-b200`
host conventions; this prompt only consumes them.

## Environment And Remote Rule

Use the `ion-b200` remote GPU environment for all NVIDIA B200
work. All CUDA, Python, pip, nvcc, build, test, benchmark, and Nsight Compute
commands must run inside the existing `sglang_bbuf` Docker container on
`ion-b200`, with an idle NVIDIA B200 GPU selected.

Before running GPU work, inspect `nvidia-smi` and choose a GPU with no active
compute processes and no meaningful memory occupancy. Export that id as
`REMOTE_GPU_ID` and use it consistently for the baseline, candidate,
benchmark, profiler, and NCU commands in the current run.

Use this command pattern for remote execution:

```bash
ssh ion-b200 'REMOTE_GPU_ID=<idle-gpu-id>; docker exec sglang_bbuf bash -lc "CUDA_VISIBLE_DEVICES=${REMOTE_GPU_ID} <command>"'
```

Do not run Python, pip, nvcc, builds, tests, benchmarks, or profiling
directly on the `ion-b200` host.

When multiple sessions share the same remote container, create a task-owned
remote workspace under:

```text
/home/sglang-omni/bbuf/kda_runs/b200_diffusion_norm_infer__multi_shape/<timestamp-or-session-id>
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
- `docs/captured_shapes_b200.jsonl`: captured shape JSONL from the diffusion
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
wrapped entry point in `sglang/jit_kernel/diffusion/triton/norm.py`.
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
idle NVIDIA B200 GPU and container environment.
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
- Benchmark the SHIPPING integration, symmetrically. The promotion number must
  come from the exact path the kernel will ship in, with the candidate and the
  baseline going through an IDENTICAL wrapper / dispatch / registration layer —
  only the device kernel may differ. Prefer the in-SGLang drop-in (candidate
  `.cuh` under the real, unchanged public op); never benchmark a side overlay
  that replaces or bypasses the public op against a baseline that keeps it.
- Preserve every production requirement of the public entry point. If the SGLang
  op is a registered custom op (`@register_custom_op`, for torch.compile /
  CUDA-graph compatibility), the shipped integration MUST keep that registration.
  An integration that drops it (e.g. monkey-patching the public symbol with a
  plain Python callable) is NOT a valid promotion arbiter — it changes the
  production contract, so its number is not comparable to the baseline's.
- Decompose every speedup into DEVICE vs HOST. Split the measured delta into the
  device-kernel change (admissible) and the host/integration-layer change
  (wrapper, dispatch, registration). A "win" that comes from removing a
  production-required host layer (e.g. dropping custom-op registration) is a
  FALSE ECONOMY, not a kernel improvement, and must not be claimed. Cross-check
  with a symmetric, same-process, interleaved A/B that isolates the device kernel.

## Prior Art Research Scope

Before choosing an implementation strategy, inspect SGLang, CUTLASS/CuTe,
CUDA samples, PyTorch, vLLM, TensorRT-LLM, FlashInfer, DeepGEMM, and
public Blackwell or Hopper kernels for directly relevant ideas. Use
KernelWiki when prior SM100, CUTLASS, SGLang, or normalization /
modulation / RoPE / group-norm evidence can guide a design choice.

Record reviewed source paths, commits or installed versions, and which
ideas were kept or rejected in `docs/draft.md` and `solutions.jsonl`.

## Implementation Language & Build Policy

**The optimized candidate must be a native CUDA kernel built from
workspace-owned `.cu` / `.cuh` sources, regardless of whether the SGLang
baseline is CUDA, Triton, or CuTe-DSL.** Python is allowed for the wrapper,
the dispatcher, build glue, harnesses, and benchmark scripts, but not as the
primary kernel.

**Build + export the kernel through SGLang's own `jit_kernel` / tvm-ffi
stack — NOT `torch.utils.cpp_extension`.** Concretely:

- Expose the device code as a templated
  `XxxKernel<...>::run(tvm::ffi::TensorView ..., float eps)` launcher in a
  `.cuh`, validating inputs with `host::TensorMatcher` / `SymbolicSize` and
  launching on the current stream with `host::LaunchKernel(...)`. Mirror an
  existing kernel such as
  `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh`.
- Drive it from Python with `sglang.jit_kernel.utils.load_jit` +
  `make_cpp_args` + `cache_once`, preserving the public SGLang callable
  name(s) and falling back to the SGLang baseline for unsupported signatures.

**Compile flags MUST match the corresponding SGLang `jit_kernel` kernel's
options. In particular, do NOT pass `--use_fast_math`** — SGLang's
`jit_kernel` build does not use it, so adding it diverges from the baseline's
numerics and is not a fair/consistent comparison. Add an extra `nvcc` flag
only if the matching SGLang kernel also uses it.

**PDL may be tried** (the SGLang baseline templates `enable_pdl` via
`is_arch_support_pdl()`), but it is OPTIONAL: validate it on the real workload
before keeping it. In the qknorm pilot, enabling PDL *hurt* isolated-launch
latency, so do not assume it helps — keep it only if it wins on this task's
actual benchmark.

The SGLang baseline — whatever language it is written in — is a first-class
**reference** for the CUDA candidate. Read its tile/block choices,
vectorization width, fast paths, fusion patterns, numerical-stability tricks,
dispatcher shape guards, and dtype handling; the candidate may port any of
those, replace them with a better algorithm, or mix in ideas from KernelWiki
PRs, CUTLASS / CuTe SM100 examples, FlashAttention-4, DeepGEMM, FlashMLA, or
FlashInfer. The baseline is one reference among many — not a ceiling. Record
every source whose idea ended up in the candidate in `solutions.jsonl`.

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

Suggested targeted queries for this kernel family (inference-only 2-pass LayerNorm / RMSNorm and tiled one-pass RMSNorm baselines):

  - `python3 ../../external/KernelWiki/scripts/query.py "layer norm 2-pass inference sm100"`
  - `python3 ../../external/KernelWiki/scripts/query.py "one pass rmsnorm tiled per head"`
  - `python3 ../../external/KernelWiki/scripts/query.py --tag rms-norm --architecture sm100 --limit 20`
  - `python3 ../../external/KernelWiki/scripts/query.py --tag layer-norm --architecture sm100 --limit 20`

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
  shape from `docs/captured_shapes_b200.jsonl` for the slice you
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

Consider SM100-specific optimization paths:

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
KERNEL_SLUG = "b200_diffusion_norm_infer__multi_shape"
OP_TYPE = "layer_or_rms_norm_infer"

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
4. Copy the captured shape JSONL into `docs/captured_shapes_b200.jsonl`.
5. Write an implementation-plan draft to `docs/draft.md`.
6. Run official Humanize plan generation on that draft.
7. Start official Humanize RLCR from this kernel folder.
8. Do not implement kernels, run long benchmarks, or collect NCU evidence
before RLCR is active.
9. Record every candidate in `solutions.jsonl` and every performance result
in `benchmark.csv`.
10. After the RLCR loop fully finishes (correctness + benchmark landed), export the Python interface via SGLang `jit_kernel` / tvm-ffi and test in-SGLang drop-in replacement (see *Export & Replacement Test*). Do not export before the loop is done.

## Export & Replacement Test (final step — after the RLCR loop finishes)

Run this ONLY after the RLCR loop is fully done: correctness passes on every
configured shape and the benchmark evidence is recorded. Export is not part of
the optimization rounds — it is the final packaging + sanity step.

1. **Export the Python interface through SGLang `jit_kernel` / tvm-ffi.** Place
   the candidate `.cuh` under `python/sglang/jit_kernel/csrc/...` and expose it
   via `load_jit` / `make_cpp_args` / `cache_once`, preserving the exact public
   SGLang callable name(s) listed in this task's **Kernel Information** section.
   Compile flags match the SGLang baseline (no `--use_fast_math`; see the
   Implementation Language & Build Policy).

2. **Test that it drop-in replaces the kernel inside SGLang and runs.** In an
   editable SGLang checkout, make the public entry point resolve to the
   candidate, then:
   - run the task's correctness oracle inside SGLang and confirm it passes;
   - run a smoke benchmark inside SGLang and confirm parity-or-speedup vs the
     original SGLang kernel on the production shapes;
   - confirm unsupported signatures still fall back to the SGLang baseline.

   This in-tree drop-in — candidate under SGLang's OWN, unchanged public op, so
   any `@register_custom_op` / torch.compile registration is preserved — is THE
   promotion arbiter. Do NOT substitute a comparison where only one side carries
   the production wrapper/registration (e.g. an overlay that monkey-patches the
   public symbol with a plain Python callable): that changes the production
   contract, so its speedup is not comparable to the baseline's.

Record the SGLang files touched, the preserved entry points, the template args
/ wrapper names passed to `load_jit`, and the in-SGLang correctness + benchmark
results in `docs/sglang_jit_export.md` and `solutions.jsonl`. See
`docs/sglang_jit_kernel_export.md` for the full export contract.

## Completion Bar

The work is complete only when:

- correctness tests pass for every configured shape;
- every dispatched variant is correct for its assigned shape bucket;
- NVIDIA B200 benchmark evidence reports geometric-mean median-latency
speedup over the SGLang baseline across all configured shape buckets;
- roofline-style analysis and NCU evidence explain the improvement,
blocker, active hardware bound, and why the final candidate is close to
the attainable performance limit for the important shape buckets, or a
well-supported no-go explains why no defensible path remains under the
available workspace;
- `prompt.md`, `interface.md`, `benchmark.csv`, and `solutions.jsonl` are
updated with the final result.
