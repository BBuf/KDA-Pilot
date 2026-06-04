# Final Results: h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape

**Decision: PROMOTED.** The native CUDA candidate (`src/norm_tanh_mul_add_candidate.cuh`,
anchor configuration) replaces the CuTe-DSL baseline on the captured production fast
path, with fallback to the vendored pinned baseline for every other signature.

## Headline numbers (vs locked pinned baseline, ion8-h200 GPU0, idle, symmetric custom-op layers)

Primary local claim = alternating same-process interleaved A/B (per the round-1 audit
ruling); sequential-vs-locked and device-only decomposition as supporting evidence.
Three independent benchmark sessions agree:

| session | interleaved geomean | sequential geomean | benchmark.csv candidate_version |
|---|---|---|---|
| ab_run2 (round 1) | 1.3621x | 1.4695x | r1-cuda-port-v2 |
| run10 (round 2, post-gates) | 1.3253x | 1.4463x | r2-anchor-gated |
| r3-anchor-control (round 3) | 1.3314x | 1.4637x | r3-anchor-control |

Per-shape (r3-anchor-control session; wall µs, locked baseline → candidate):

| shape | baseline | candidate | interleaved | device (events) | candidate GPU µs | modeled BW |
|---|---|---|---|---|---|---|
| single S=4096 | 82.36 | 56.38 | 1.318x | 1.388x | 41.95 | 2250 GB/s |
| dual S=4096 | 106.80 | 73.08 | 1.348x | 1.405x | 47.44 | 2653 GB/s |
| single S=4128 | 81.40 | 55.97 | 1.317x | 1.382x | 41.04 | 2318 GB/s |
| dual S=4128 | 107.72 | 72.85 | 1.343x | 1.398x | 48.13 | 2636 GB/s |

DEVICE vs HOST decomposition: the win is device-dominated (device-only interleaved
1.38–1.41x vs wall 1.31–1.35x); host overhead is comparable on both sides
(symmetric `torch.library.custom_op` layers; candidate gate cost counted against the
candidate). No claim depends on removing any production-required host layer.

## Correctness

- `tests/test_baseline_parity.py`: vendored pinned baseline ≡ sglang package
  (`torch.equal`, 4 captured signatures) — 6/6.
- `tests/test_correctness.py`: 14/14 on H200 with the candidate active — fp32 tanh
  oracle with storage-dtype mirroring + backward-error model + compositional stage-2
  verification; y and y2 dynamic bounds vs baseline noise; dispatch branch-contract
  tests; default-eps contract; bitwise fallback equality; misaligned-view error
  parity; input-mutation guard; NaN/Inf validators; sensitivity tests proving the
  checker rejects wrong math. Exhaustive grid: 844/844 cases.

## Search summary (all rejections evidence-backed in solutions.jsonl + benchmark.csv)

- Wave 1 (tiling): rows-per-CTA {2,4}, vecs-per-thread {3,5}, upfront operand
  staging — ALL slower (best 1.18x vs anchor 1.33x interleaved). Lesson: keep
  load-after-reduce ordering and one-row-per-CTA on many-row grids.
- Wave 2 (NCU-ranked): dual `__launch_bounds__` register cap 0.999x device;
  2-sync reduction 0.996x; tanh-precompute +2.2% device on dual but 1.3122x vs
  1.3314x anchor at the full wrapper layer → rejected.
- Final bound (profile/ncu_anchor_r2/REPORT.md + FINAL ADDENDUM): not
  DRAM-bandwidth-bound (50–51% memory throughput; 2.1–2.4 TB/s actual DRAM);
  single is memory-latency-bound (long_scoreboard 5.0/issue, ALU 52%/XU 38.6%),
  dual issue/barrier-bound under a 40-register occupancy cap. The anchor is at the
  practical operating point for this dataflow on H200 within the bounded search.

## Reproduction

```bash
# inside sglang_bbuf on an idle H200 (CUDA_VISIBLE_DEVICES pinned)
KDA_RUN_CORRECTNESS=1 python -m pytest tests/test_correctness.py -v
KDA_RUN_CORRECTNESS=1 KDA_EXHAUSTIVE=1 python -m pytest tests/test_correctness.py::test_baseline_matches_oracle
python benchmark.py --lock --host <host>          # once, idle GPU
python benchmark.py --host <host> --candidate-version <git-sha>
```

All evidence files: `benchmark.csv` (every row carries host/GPU id/model, commits,
exact command; the round-1 `ab_run1` rows are marked INVALIDATED at row level —
jit-cache bug; wave-2 sweep rows are labeled SELECTION-ONLY device-level evidence),
`solutions.jsonl` (parent-linked entries), `docs/baseline_locked.json`,
`profile/ncu_anchor_r2/`, remote logs under
`ion8-h200:/home/sglang-omni/bbuf/kda_runs/h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape/2026-06-04_16-05-34/logs/`.

## Dispatch

Single fast-path family (no per-bucket split → no `docs/dispatch.md` needed):
bf16 + rms + D=3840 + `weight=[D]` + `bias=None` + `scale(/scale2)=[1,1,D]` +
`shift=[B,S,D]` + 16B-aligned + contiguous + `B*S ≤ 2^31-1`, any row count;
everything else (including misaligned views, other dtypes/norm types/layouts/D,
CPU, kwargs-style calls) routes to the vendored pinned baseline, preserving its
exact error behavior.
