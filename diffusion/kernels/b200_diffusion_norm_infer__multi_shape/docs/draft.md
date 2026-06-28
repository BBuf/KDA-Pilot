# Round-2 continuation draft — b200_diffusion_norm_infer__multi_shape

Written before any round-2 code change. Round 1 (lineage `cand-0001` →
`cand-0006-final`, promoted via repo PR #23) ended with: fp32 LN `[8640,5120]`
1.16×/1.20× (memory-BW ~66% peak), bf16 RMS small/mid 1.5–1.7× (launch/occupancy
bound), large-S RMS `[648720/650040,128]` evidence-backed no-go → Triton baseline
fallback (parity), geomean 1.27× wall / 1.33× kernel (outcome metric). This round
revalidates that state on `ion-b200` and reopens the large-S bucket through its
recorded re-open condition.

## State audit (round-2 entry)

Verified present and intact in this worktree (fresh worktree; submodules
`external/KernelWiki` @ `faed56ce` and `external/ncu-report-skill` @ `d1887948`
initialized via `git submodule update --init --recursive`; both SKILL.md read):

- `src/norm_cuda/diffusion_norm_infer.cuh`, `src/register.py`, `src/__init__.py`
  (`_KERNEL_VERSION = "v2"`, allowlists `_SUPPORTED_LN` / `_SUPPORTED_RMS`)
- `tests/test_correctness.py` (69 cases), `tests/test_fused_substitution.py` (48 cases)
- `benchmark.py` (interleaved per-iteration A/B harness), `benchmark.csv` (round-1 rows
  incl. `cand-0006-final`)
- `solutions.jsonl` — 9 entries, DAG intact: `cand-0001-*` → `cand-0002-ln-opt` →
  `cand-0003-rms-mlp` (nogo) → `cand-0004-dispatch` → `cand-0005-sglang-export`
  (promoted) → `cand-0006-final`
- `docs/captured_shapes_b200.jsonl` + `.md` — exactly 6 unique call signatures,
  matching the prompt's workload table verbatim (no derived shapes)
- `docs/dispatch.md` (per-shape decision table + large-S no-go package + re-open
  condition), `docs/optimization_directions.md` (round-1 ranked directions),
  `docs/schemas.md`, `docs/sglang_jit_export.md` (isolated-worktree export pattern)
- `profile/ac_e_r5/` (per-bucket bounds: LN ~66% peak BW; small/mid RMS occ 15/40/76%),
  `profile/rms_largeS_r4/` (no-go NCU: DRAM 38.5%, long-scoreboard ~56%, occ 77%)

Conditional repo-root docs (`standalone_diffusion_benchmark.md`,
`diffusion_kernel_rules.md`, `diffusion_correctness_contract.md`) do not exist in
this repo → recorded as conditional no-ops. `docs/sglang_jit_kernel_export.md`
exists at repo root and remains the export contract.

## Round-2 environment rules (deltas vs round 1)

- Round-1 numbers came from host `ion-b200`; this round runs on
  `ion-b200` (via the local `ion-b200` skill, container `sglang_bbuf`). Round-1
  numbers are lineage context only — every claim this round is re-measured fresh.
- Baseline pin: container-current sglang commit, recorded in provenance, plus a
  drift check of `python/sglang/jit_kernel/diffusion/triton/norm.py` and
  `python/sglang/jit_kernel/diffusion/triton/rmsnorm_onepass.py` against round-1
  `0b65588c` (local checkout evidence: both files unchanged `0b65588c..0689ba84b8`).
- JIT hygiene: force a fresh tvm-ffi build before any timing (fresh cache dir or
  `_KERNEL_VERSION` bump) so stale `.so` reuse cannot contaminate measurements.
- New-candidate A/B lane: the two Triton baselines get pinned copies under
  `baseline/` (lineage in `docs/baseline_source.md`) exposed through the same local
  entry ABI; one-time parity cross-check vs the installed sglang baseline. The
  promoted round-1 layout (`src/`, `tests/`, root `benchmark.py`) stays canonical.
- kda_kernels overlay promotion is out of scope this round (separate contract).

## Ranked round-2 directions (extends docs/optimization_directions.md)

1. **Tile-based multi-row-per-CTA bf16 RMS for S ∈ {648720, 650040}, D=128** —
   the recorded re-open condition from the round-1 no-go ("multi-row-per-block,
   shared load pipeline"). Baseline: Triton 16-row × 128-col tile at ~4.3–4.7 TB/s
   (~55–59% peak), i.e. not BW-saturated. Design space: R ∈ {8,16,32} rows/CTA via
   256-thread CTAs with 16B vector loads (8 bf16/lane; one CTA-load step covers
   16×128), per-row segmented half-warp reduction in fp32, `w[128]` (256 B) in
   registers/smem, grid-stride vs persistent scheduling, optional cp.async
   double-buffer pipeline. Expected benefit: medium (realistic ceiling ~1.0–1.1×;
   row-norm kernels on this part trend latency/issue-bound, per round-1 NCU and the
   sibling h200 round). Risk: medium — a refreshed evidence-backed no-go is an
   acceptable exit. Forbidden vehicle: warp-per-row family (incl. kUnroll
   grid-stride) — already no-go'd with NCU evidence.
2. **fp32 LN `[8640,5120]` polish — conditional gate** — open only if the round-2
   rebaseline/NCU shows exploitable headroom beyond the round-1 ~66%-peak BW bound.
   Levers if opened: thread-count sweep (128/256/512), streaming vs read-mostly
   cache hints (`x`/`y` stream, `w`/`b` evict-last), PDL A/B (empirical only;
   qknorm pilot showed PDL can hurt isolated-launch latency). Round-1 advice stands:
   avoid split-row/multi-CTA reductions (8640 rows already cover 148 SMs). Expected
   benefit: low-medium (~few % to 1.1×). Risk: low-medium.
3. **Small/mid RMS `[1320/4096/16384,128]`** — no new work: launch/occupancy-bound
   at 1.5–1.7×. Re-verify unregressed only. Expected benefit of new work: ~0.
4. **Protected invariants** — dispatcher fallback semantics (15 routing cases),
   `KDA_REQUIRE_CUDA=1` raise-not-fallback, numerics policy (fp32 accumulation,
   `sum((x-mean)^2)/N`, no `--use_fast_math`), allowlist widening only with
   per-shape evidence.

## KernelWiki / ncu-report-skill context (this iteration)

- Re-read both SKILL.md files (KernelWiki cutoff 2026-04-27; ncu-report-skill
  B200/sm_100 with six analysis dimensions + B200 metric-name caveats).
- Fresh queries: `query.py "one pass rmsnorm tiled per head"` and
  `query.py --tag rms-norm --architecture sm100` → no new directly-relevant tiled
  streaming-RMS prior art beyond round-1's references; top hits are norm-fusion PRs
  (TensorRT-LLM PR-13892 RMSNorm fold-in, sglang PR-24696 fused QKV RMSNorm), which
  exceed this task's public-entry contract → noted, not adopted.
- Round-1 references remain operative: `wiki/patterns/memory-bound.md`,
  `wiki/hardware/pdl-gdc.md`, `sources/docs/nvidia-blackwell-tuning-guide.md`.
- ncu plan for this round: profile only when a result is not fully understood;
  fresh `profile/<run>/{harness,reports,analysis}/` per run, `-lineinfo` harness,
  `--set full` + `--set source`, six-dimension walk, `REPORT.md` per template.

## Round-2 evidence contract (summary)

Every candidate → `solutions.jsonl` with parent link into the round-1 DAG; every
measurement → `benchmark.csv` with full provenance (host, GPU id/model, container,
sglang/cuda/torch, exact command, candidate version); GPU idleness checked before
and after each run; geomean across all six shapes reported as an outcome; final
bound closure per touched bucket (roofline note + named limiting resource) or a
refreshed no-go package.
