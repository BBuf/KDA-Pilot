# Benchmark Method

Status: scaffold draft — finalized after the remote H200 baseline lock
(`docs/run_log.md` carries the run-by-run evidence).

## Harness

- `bench/benchmark.py` is a byte-identical copy of
  `../../docs/standalone_diffusion_benchmark_template.py` (verified with
  `diff` at copy time; any future deviation must be recorded here with both
  sides remeasured). Timing policy is therefore the standard one: per-workload
  spawn isolation, fresh random inputs per trial, correctness-before-timing
  with output poisoning, deterministic interleaved A/B order per trial, CUDA
  events with inner-loop amplification (target sample ~1000 us, inner 1..4096),
  median/mean/std/min/p10/p90 per side, equal-weight geomean over
  `production=true` PASSED rows.
- Benchmark constants come from `config.toml` `[benchmark]` (warmup 10,
  iterations 200 per the template's trial structure, trials 7, timeout 600 s,
  isolated runner). The harness invocation pins them via CLI defaults.
- `bench/workloads.json` is a generated artifact (`bench/gen_workloads.py`)
  from the retained capture JSONL in pre-reset git history; provenance in
  `bench/workloads_meta.json`. 48 production rows (triton entry, fp16,
  `num_groups=32`, `eps=1e-6`) + diagnostic wrapper rows (`production=false`).
  Frozen before tuning; LTX capture-derived diagnostic rows (DEC-5) may be
  appended only BEFORE the baseline numbers freeze.

## ABI and calling convention

- Baseline: the copied SGLang callables (`baseline/binding.py`) allocate and
  return their output per call — upstream production behavior, kept verbatim.
  The adapter uses a rebind container for baseline outputs; no extra
  device-to-device copy is added to the timed path.
- Candidate: destination-passing tvm-ffi CUDA (`solution/`), output
  preallocated in `make_case`; the template's poison check is fully effective
  on the candidate side.
- Wrapper rows (`apply_group_norm_silu`): `torch.nn.GroupNorm`/`nn.SiLU`
  modules are constructed in `make_case` (outside timing); module-attribute
  extraction happens inside BOTH timed calls (the baseline wrapper unpacks
  attributes per call; the candidate wrapper path mirrors it).
- Scratch policy: each side keeps its natural per-call behavior — the
  baseline's chunked path allocates its partial-sum scratch internally
  (upstream code, unmodified); the candidate allocates its reduction scratch
  via the caching allocator inside its Python binding per call. Neither side
  preallocates scratch out of band.
- Grad mode: the worker runs `torch.set_grad_enabled(False)` (template);
  `make_case` asserts it. Rationale: the upstream baseline silently routes to
  eager `F.silu(F.group_norm(...))` under grad mode (gate
  `_can_use_triton_group_norm_silu`), which would corrupt the comparison.
- Baseline-path authenticity: `make_case` refuses production rows where the
  upstream gate would route to eager; a one-time profiler-based kernel-name
  verification on representative shapes is recorded in `docs/run_log.md`.

## Compile flags (symmetry)

- Baseline Triton kernels: upstream `@triton.jit` defaults — no extra flags.
- Candidate CUDA: `-O3 -std=c++20` + the target SM arch for H200; **no
  `--use_fast_math`** (the upstream baseline does not use it), no asymmetric
  math/arch toggles. Full nvcc command recorded here after the first remote
  build.

## Harness validation (pre-freeze, one-time)

- A/A run: `GNS_BENCH_CANDIDATE=baseline` wires the candidate side to the
  baseline callable; both sides time identical code. Acceptance: geomean in
  [0.98, 1.02] on a representative subset. Result recorded in
  `docs/run_log.md` before the baseline numbers freeze.
- Poison check: a deliberately skipped candidate kernel must be caught by the
  template's NaN-poisoned outputs (exercised in `bench/correctness.py`).

## Deviation log

- `config.toml` `[build].baseline_entry` corrected from the template-generated
  `baseline/kernel.cu::group_norm_silu_baseline` to
  `baseline/binding.py::group_norm_silu_baseline`: the upstream baseline for
  this family is Triton (no CUDA baseline file exists). Recorded at scaffold
  time, before any measurement.
