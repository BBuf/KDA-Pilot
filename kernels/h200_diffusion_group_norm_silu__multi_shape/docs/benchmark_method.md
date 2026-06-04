# Benchmark Method

Status: final (promotion record = the round-2 frozen run; `docs/run_log.md`
carries the run-by-run evidence, `docs/results.md` the final numbers and the
explicit AC-5 per-row-floor no-go record).

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

- Template contract (final): `make_case` preallocates one output tensor per
  side; `call_baseline`/`call_candidate` write into those buffers through
  destination-passing local ABIs and never allocate output tensors in a
  timed path. The baseline side replicates the copied Triton launcher bodies
  verbatim with the caller's buffer (internal scratch untouched; verified
  bit-identical to the upstream allocate-and-return entries) and refuses the
  upstream eager fallback. The template's output-poisoning check is fully
  effective on both sides every trial.
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

## Amendment (round 1 — template contract restored per the round-0 review)

The round-0 implementation timed allocate-and-return glue on both sides; the
round-0 review correctly held that this deviates from the template contract
("outputs preallocated; call_* must not allocate output tensors"). Round 1
restored the contract exactly:

- BOTH sides write into harness-preallocated buffers
  (`{"y": torch.empty_like(x)}` per side in `make_case`). The candidate side
  is `solution/binding.py::group_norm_silu_candidate_into`; the baseline side
  is `baseline/binding.py::group_norm_silu_baseline_into` /
  `group_norm_silu_baseline_apply_into` — destination-passing wrappers that
  replicate the copied launchers' bodies verbatim except for the output
  buffer (internal partials/stats scratch unchanged; verified bit-identical
  to the allocate-and-return entries). The baseline wrapper REFUSES the
  upstream eager fallback so it can never be timed silently.
- The template's output-poisoning check is fully effective on both sides
  every trial. No timed path allocates an output tensor.
- A/A validation under this exact contract: geomean 0.9990 (8 spread rows,
  0.9854–1.0076).
- The shipped candidate contains no baseline routing (round-0's DEC-6
  dispatch experiment was removed per the review; measurement record kept in
  docs/dispatch.md history). Final numbers come from the round-2 frozen run
  (the round-1 run with the generic giant route is retained in
  docs/run_log.md for the cross-run band); no workload, tolerance, or
  timing-policy field changed after the freeze.
