# Diffusion Kernel Optimization Rules

These rules apply to every standalone diffusion kernel task. They restore the
important guardrails from the original long task prompts while keeping each
task prompt short.

## Baseline And Candidate Pairing

Each task must end with two local implementations:

- `baseline/`: copied upstream SGLang kernel source plus a local callable
  exposed through the task benchmark ABI.
- `solution/`: the optimized implementation exposed through the exact same
  task benchmark ABI.

Before copying baseline code, resolve the latest commit on upstream SGLang
`main` and use the diffusion kernel source from that exact commit. Do not use a
stale pinned SGLang commit, a local production checkout with unknown drift, or
copied kernel code from a previous KernelPilot task. Record the SGLang
repository URL, branch (`main`), resolved commit SHA, resolution time, and copied
file list in `docs/baseline_source.md`.

If the SGLang baseline kernel is CUDA/C++ CUDA, the copied baseline and the
optimized candidate must use the same local registration/export/build style.
For example, do not expose the baseline through one Python/JIT wrapper and the
candidate through a lighter direct CUDA path. If one side uses direct
`TVM_FFI_DLL_EXPORT_TYPED_FUNC` registration with output tensors passed last,
the other side must use the same pattern.

If the copied SGLang implementation is Triton, CuTe DSL, or Python, keep it
inside `baseline/` and build a local adapter that has the same call signature,
argument ordering, stream behavior, and output allocation policy as the
candidate adapter.

Every CUDA launch must use PyTorch's current stream, for example
`at::cuda::getCurrentCUDAStream()`.

## Compile Flags

Compile flags must be symmetric between baseline and candidate whenever they can
change numerics or code generation.

Do not pass `--use_fast_math` unless the copied upstream SGLang kernel already
uses it and the candidate uses the exact same flag. The default is no fast math.

Do not add extra `nvcc` flags, architecture-specific toggles, or math-mode flags
to only one side. Record all compile flags in `docs/benchmark_method.md`.

Avoid comparing different builder paths. In particular, do not make one side use
`torch.utils.cpp_extension` while the other side uses direct local registration
unless both sides are rebuilt and timed through an equivalent wrapper path.

PDL may be tested when the copied SGLang kernel has a comparable PDL path, but
it is optional and must be kept only if it wins on the task's actual production
workloads.

## Remote GPU Rule

B200 tasks must validate and benchmark on B200. H200 tasks must validate and
benchmark on H200.

Before GPU work, inspect `nvidia-smi` and choose a GPU with no active compute
processes and no meaningful memory occupancy. Use the selected GPU consistently
for baseline, candidate, correctness, benchmark, profiling, and NCU commands in
the current run.

Record the host, GPU id, GPU model, and before/after GPU state in the task's
`docs/run_log.md` or `docs/results.md`.

Use a task-owned remote workspace for builds, benchmark logs, profiler traces,
and NCU reports. Do not write artifacts into another task's workspace.

## Correctness Before Performance

Before optimization, recover:

- the upstream SGLang baseline source file(s);
- the public callable arguments and scalar parameters;
- the production workload rows from
  `docs/diffusion_benchmark_shape_coverage.md`;
- the canonical regression grid from
  `docs/diffusion_correctness_contract.md`.

The final candidate must pass the production workload correctness checks and the
canonical regression grid before any benchmark result counts.

Preserve explicit NaN/Inf checks. Use tolerances from
`docs/diffusion_correctness_contract.md` unless the task records a stricter
task-local tolerance in `docs/benchmark_method.md`.

## Benchmark And Evidence

Use `docs/standalone_diffusion_benchmark_template.py` as the timing harness
starting point. Do not change workloads, tolerances, score aggregation, or timing
rules after tuning starts unless both baseline and candidate are remeasured.

Every RLCR iteration must refresh its kernel-optimization context before
choosing the next edit, benchmark run, profiling run, or no-go conclusion. That
refresh includes this document, the task prompt, current benchmark evidence,
`external/KernelWiki/SKILL.md`, and `external/ncu-report-skill/SKILL.md` when
those files are available.

When NCU profiling is needed, follow `external/ncu-report-skill/SKILL.md`. Keep
the profile harness, reports, analysis, and summary in a task-owned directory,
and use the resulting evidence to choose the next edit instead of guessing.

A final performance claim must report:

- median, mean, std, min, p10, and p90 latency per workload;
- equal-weight geometric mean speedup over production workloads;
- exact command lines;
- baseline source commit and candidate source hash;
- GPU host/id/model and idle-state evidence.

Use Nsight Compute when a correct candidate is not clearly target-complete or
when profiler evidence would change the next edit. A final improvement or no-go
must include a roofline-style explanation: estimated bytes moved, useful scalar
or vector operations, achieved bandwidth and/or FLOP/s when relevant, and the
active bound or blocker.

Do not finalize a no-go because the first candidate loses. A no-go needs
baseline numbers, at least one reasoned candidate attempt, correctness status,
benchmark evidence, and a named active bound or blocker.

## PR Scope

After a kernel is optimized, the final PR must include only:

- the kernel-related source needed for the copied baseline, optimized solution,
  local ABI, benchmark adapter, and correctness/benchmark harness;
- the per-shape baseline-vs-candidate performance comparison and final
  conclusion, normally in `docs/results.md`;
- small method/provenance notes needed to reproduce the result.

Do not commit intermediate optimization artifacts such as raw NCU reports,
Nsight traces, profiler run directories, temporary harness binaries, build
outputs, scratch logs, failed experiment dumps, or large benchmark JSONL files
unless the user explicitly asks for them in the PR. Keep those artifacts local
to the task workspace or remote workspace for audit/debugging, then leave them
unstaged before opening the PR.

## Shape Specialization

Shape-specialized kernels, template variants, autotune tables, and dispatchers
are allowed when benchmark or profiler evidence shows that different workload
buckets need different block sizes, vector widths, memory layouts, or register
pressure tradeoffs.

When specialization is used, write `docs/dispatch.md` with:

- the bucket condition;
- the selected baseline and candidate entry point;
- per-bucket latency and speedup;
- the reason that bucket uses this implementation.

Do not force one universal kernel when evidence shows multiple shape buckets
need different implementations.

## Prior Art And Exploration

Before settling on an implementation strategy in any RLCR iteration, read or
query `external/KernelWiki/SKILL.md` when it is available, then inspect relevant
upstream code or knowledge sources when they could change the design: SGLang,
CUTLASS/CuTe, CUDA samples, PyTorch, vLLM, TensorRT-LLM, FlashInfer, DeepGEMM,
KernelWiki, and task-local NCU evidence.

Record kept/rejected ideas in `docs/draft.md`, `docs/results.md`, or
`docs/research.md`. Keep optimization attempts bounded and evidence-backed.

## Completion Bar

A diffusion task is complete only when:

- `baseline/`, `solution/`, `bench/`, and `docs/` contain the required local
  artifacts;
- production workload correctness passes;
- canonical regression correctness passes;
- the benchmark result uses the standard standalone timing rules;
- NCU or a clear roofline-style analysis explains the final result or blocker;
- `docs/results.md` summarizes the final command, per-shape performance
  comparison, result, and conclusion;
- the staged PR diff excludes raw profiling, NCU, temporary build, and scratch
  artifacts.
