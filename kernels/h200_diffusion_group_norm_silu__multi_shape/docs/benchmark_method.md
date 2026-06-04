# Benchmark Method

Status: final (promotion record; `docs/run_log.md` carries the run-by-run
evidence, `docs/results.md` the final numbers; the DEC-6 amendment at the
bottom of this file supersedes earlier ABI wording where noted).

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

- Symmetric timed glue (revised per the pre-freeze review): BOTH sides
  allocate their output per timed call and rebind it into the output
  container. The copied baseline does so internally (its public entry returns
  a fresh tensor — upstream behavior, unmodified); the candidate wrapper
  mirrors it with one `torch.empty_like` per call before the
  destination-passing FFI kernel. One caching-allocator allocation per call
  on each side; no device-to-device copies in either timed path.
- Poison semantics: with per-call rebinding, the template's poison fill lands
  on replaced tensors for both sides equally; the authoritative
  stale-output/skipped-kernel poison checks drive the candidate's
  destination-passing ABI directly in `bench/correctness.py`
  (`method_poison_*` cases).
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

## Amendment (promotion decision DEC-6, before the final runs)

- The candidate's public entry became allocate-and-return
  (`group_norm_silu_candidate(...) -> Tensor`), exactly mirroring the
  baseline's contract; the adapter glue is now literally identical on both
  sides (call → rebind). The destination-passing form survives as
  `group_norm_silu_candidate_into` for the correctness suite's poison checks.
- The shipped candidate routes two measured regimes to the LOCAL copied
  Triton baseline (rule table + evidence in docs/dispatch.md). Fallback rows
  therefore time device-identical code on both sides; their 0.97-1.00
  readings bound the dispatcher's host-side routing tax (cross-checked by
  the A/A validation at 1.0037).
- Final numbers come from back-to-back full frozen runs (geomean stable to
  ±0.1%; the last complete run is the promotion record; all runs retained in
  docs/run_log.md). No workload, tolerance, or timing-policy field changed
  after the freeze.
