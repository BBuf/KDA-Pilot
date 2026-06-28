# Results — b200_diffusion_residual_gate_add__multi_shape

> **⚠️ SUPERSEDED — baseline changed, re-benchmark required.** The numbers below
> were measured against the faithful PyTorch-**eager** `mul`+`add` baseline. The
> `residual_gate_add` baseline has since been replaced with SGLang's **Triton**
> `fuse_scale_shift_kernel` (the production serving path; see
> `docs/baseline_source.md` and SGLang PR #29361). The Triton kernel is far faster
> than eager, so the eager-relative geomean (~2.19x) below no longer reflects the
> GO margin — SGLang PR #29361 measures the native-CUDA fast path at ≈1.11x over
> this Triton kernel on the LTX-2 broadcast row. Both gates (correctness +
> benchmark) must be re-run on idle B200 against the new baseline before this
> verdict stands. `broadcast_add_4d` (eager `torch.add`) is unaffected.

## Conclusion: GO (against the old eager baseline; pending re-benchmark vs Triton)
The fused candidate is correctness-clean on B200 and faster than the faithful
PyTorch-eager production path on every production row. Headline equal-weight
geomean **2.193x** (all rows >= 1.18x). NCU + roofline confirm the result is
bandwidth/launch-bound as expected for elementwise traffic, and the analyze pass
(task3/task7/task10) accepts the baseline/numerics/layout and ranks remaining
optimization as modest, conditional upside — so the generic vectorized candidate
is accepted as the final implementation for this task.

Scope: the ABI is batch-1 (every frozen production row is B=1). Full gate
`[1,L,D]`, row-broadcast gate `[1,1,D]`, and 4D `a=[1,1,P,D]`/`b=[1,S,P,D]` are
supported; a true B>1 broadcast is deliberately out of scope and is rejected
symmetrically on both the candidate and the eager baseline (shared
`bench/adapter.py::_validate`), with `rga-gate-leaddim-not1` and `bcast-batch-gt1`
rejection tests. See `docs/baseline_source.md` for the contract rationale.

## Environment
- Host `ion-b200`, container `sglang_bbuf`
  (`lmsysorg/sglang:dev`); torch 2.11.0+cu130, CUDA 13.0, tvm-ffi 0.1.9, nvcc 13.0.
- NVIDIA B200 (192 GB HBM3e, 148 SMs, ~8 TB/s nominal; NCU sustained ref ~7.2 TB/s).
- **All final evidence is on ONE pinned idle GPU: physical GPU 7**
  (`REMOTE_GPU_ID=7 CUDA_VISIBLE_DEVICES=7`, fail-closed guard
  `KDA_REQUIRE_PINNED_GPU=1`); correctness, benchmark, and NCU were all collected
  on GPU 7, idle before/after (0%/0MiB). See `docs/run_log.md`. (Earlier rounds
  also ran on GPU 2/GPU 0; those are superseded by this unified GPU-7 chain.)
- Baseline source: sgl-project/sglang `main` @ `8314247d9de0fa2c58e34756b3e1dbc6cf815dfd`
  (`docs/baseline_source.md`). Candidate `solution/kernel.cu` sha256: the Round-4
  benchmark was measured on `a450f863…`; subsequent review fixes are host-side and
  compute-neutral on the timed single-GPU path — R5 added a `out.ndim()==4` reject
  (`27f67c5f…`), R7 added same-device validation + a `CUDAGuard` (no-op when the
  tensor device is already current) giving the current source `a6ab9c86…` (R6 was
  adapter-only, kernel unchanged). The device kernels and the valid-input timed
  path are identical across these, so the measured geomean stands; correctness was
  re-confirmed 67/67 on each rebuild (see `docs/run_log.md`). R8 was harness-only
  (`bench/benchmark.py` now sets the selected CUDA device before collecting
  provenance, so a non-default `--device` records the right GPU/SM/flags); the
  candidate hash is unchanged and both gates were re-run fresh on idle GPU 7
  (67/67, geomean 2.186x).

## Final commands (all on GPU 7)
```bash
export KDA_REQUIRE_PINNED_GPU=1 REMOTE_GPU_ID=7 CUDA_VISIBLE_DEVICES=7
python bench/correctness.py --impl both --rows all --report /tmp/rga_correctness_final.json
python bench/benchmark.py --out bench/results.jsonl
ncu --set basic --launch-skip 6 --launch-count 1 --target-processes all -o /tmp/ncu_<row> python /tmp/rga_profile.py <row>
```

## Correctness (AC-3 / AC-4)
`bench/correctness.py --impl both --rows all` (GPU 7): **67/67 PASS**. Covers the 8
production rows (candidate vs fp32 one-round oracle AND vs faithful eager baseline,
bf16 atol=rtol=5e-2), the regression grid (full/broadcast gate; bf16/fp16/fp32;
odd-D / non-vec-aligned-D / small-L tails; deterministic zero/sign rows; repeated
randomized seeds; 4D over multiple frame counts), a poison self-test, and both-side
rejection (full-gate-noncontig, bad-gate-2d, gate-leaddim-not1, dtype-mismatch,
alias, non-contiguous, 4D batch>1).

## Performance (AC-5) — candidate vs faithful eager two-op baseline (GPU 7)
Baseline = the profiled production path (`torch.mul(update,gate,out=scratch)` then
`torch.add(residual,scratch,out=out)`, two launches + one temp + two dispatches;
single `torch.add` for the 4D row). Candidate = one fused CUDA pass. CUDA-event
median per call (matched ratio 1.0).

| Workload | gate | speedup | baseline us | candidate us |
|---|---|---:|---:|---:|
| ltx2_full_s8160_c4096 | full | 1.5977 | 66.180 | 41.421 |
| ltx2_bcast_s32640_c4096 | bcast | 2.9781 | 420.216 | 141.104 |
| ltx2_full_s126_c2048 | full | 1.7535 | 10.590 | 6.039 |
| ideogram4_bcast_s4096_c4608 | bcast | 2.8348 | 64.616 | 22.793 |
| flux2_bcast_s4608_c3072 | bcast | 3.2779 | 47.492 | 14.489 |
| flux2_bcast_s4096_c3072 | bcast | 3.3286 | 41.456 | 12.455 |
| flux2_bcast_s512_c3072 | bcast | 1.7542 | 19.622 | 11.186 |
| ltx2_broadcast_add_4d | - | 1.1805 | 11.716 | 9.925 |

Headline and secondary views (the row mix weights broadcast-gate cases heavily, so
secondary views are reported):
- **All-8 equal-weight geomean: 2.193x** (the contract headline). Min 1.18x, max 3.33x.
- Residual-gate-only (7 rows) geomean: **2.396x**.
- Call-count-weighted geomean (documented profile call-counts, 6-row subset,
  82,134 calls): **1.676x** — lower because the highest-frequency rows are the tiny
  full-gate `[1,126,2048]` (33,123 calls, 1.75x) and the 4D add (13,392 calls,
  1.18x), which have the smallest per-call speedups.

The win is "fused single CUDA kernel vs the faithful eager two-op production path"
— it removes one kernel launch, the intermediate temp's full write+read, and one
Python dispatch; it is not a single-kernel-vs-single-kernel algorithmic speedup.
(Run-to-run the headline geomean is stable: 2.199x on GPU 2, 2.193x on GPU 7, and
2.186x on a fresh GPU-7 re-run after the Round-8 benchmark-provenance fix — all
within run-to-run noise, per-row deltas < 1%.)

## Roofline / speed-of-light (AC-7), GPU 7
Candidate byte model (bf16, 2 B/elem): full gate ~8 B/elem (r+u+g read, out write);
broadcast gate ~6 B/elem (r+u read, out write; gate cached); 4D add ~4 B/elem
(b read, out write; a cached). Achieved BW from the CUDA-event median above;
DRAM%/SM% from NCU (`--set basic`, GPU 7) for the three profiled rows.

| Workload | elems | cand B/elem | cand us | achieved GB/s | % of ~8 TB/s | NCU DRAM% | NCU SM% | named bound |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| ltx2_full_s8160_c4096 | 33.42M | 8 | 41.42 | 6455 | 80.7 | 72.5 | 55.7 | DRAM-bound (near roofline) |
| ltx2_bcast_s32640_c4096 | 133.69M | 6 | 141.10 | 5685 | 71.1 | 59.5 | 69.7 | SM/occupancy-leaning (modulo+ldg; occ 50.5%) |
| ltx2_full_s126_c2048 | 0.258M | 8 | 6.04 | 342 | 4.3 | 3.8 | 3.1 | launch/grid-bound (grid 126 < 148 SMs) |
| ideogram4_bcast_s4096_c4608 | 18.87M | 6 | 22.79 | 4968 | 62.1 | - | - | DRAM-bound (bandwidth) |
| flux2_bcast_s4608_c3072 | 14.16M | 6 | 14.49 | 5862 | 73.3 | - | - | DRAM-bound (bandwidth) |
| flux2_bcast_s4096_c3072 | 12.58M | 6 | 12.46 | 6062 | 75.8 | - | - | DRAM-bound (bandwidth) |
| flux2_bcast_s512_c3072 | 1.57M | 6 | 11.19 | 844 | 10.5 | - | - | launch/occupancy-leaning (small) |
| ltx2_broadcast_add_4d | 0.774M | 4 | 9.93 | 312 | 3.9 | - | - | launch/low-fusion (inferred, not NCU-profiled) |

NCU bound interpretation (task10, Codex-confirmed; GPU 7 `.ncu-rep` retained under
the ignored remote `/tmp`):
- Large full-gate (`ltx2_full_s8160`): DRAM-bound near roofline (NCU 72.5% DRAM,
  "DRAM bottleneck"; ~6.46 TB/s effective at benchmark speed).
- Large broadcast-gate (`ltx2_bcast_s32640`): SM/occupancy-leaning, DRAM headroom
  (NCU SM 69.7% > DRAM 59.5%, occupancy 50.5%) — the per-vector `v % row_vec`
  modulo + `__ldg` indexing is the plausible instruction-side limiter.
- Small (`ltx2_full_s126`): launch/grid-bound (NCU: grid 126 blocks < 148 SMs,
  occupancy 12.7%) — the win is collapsing two launches into one.
- 4D add: launch/low-fusion bound, **inferred** from the byte model + 1.18x speedup
  (this row was not separately NCU-profiled).

## Analyze pass (task3 / task7 / task10, via Codex)
- task3 — baseline faithfulness ACCEPT, fp32 one-round numerics + bf16 5e-2 oracle
  ACCEPT, out-of-place + contiguous-only alias/layout ACCEPT. No unfair/illusory
  win once framed as fused-vs-eager (above) with secondary views.
- task7 — ranked optimization directions: (1) highest-value = remove the
  broadcast-gate per-vector modulo (bcast_big SM-leaning), "modest but real,
  moderate risk, worth a bounded experiment if more work is allowed"; (2) full-gate
  large already ~roofline (low headroom); (3) small rows launch-bound (per-row CTA
  split risks hurting large rows unless separately dispatched); (4) 4D low priority.
- task10 — confirmed the per-row bound characterization above (4D marked inferred).

## Optimization decision (task7 -> task8)
Accept the current generic grid-stride fused candidate as the final implementation
for this task. Rationale (evidence-backed): the success bar is decisively met
(67/67 correctness; positive geomean 2.193x on every row; bounds explained by
NCU/roofline); the one ranked edit (broadcast-gate modulo / occupancy) is, per NCU
and the analyze pass, modest and conditional upside for rows that already win
2.83-3.33x, and the natural implementation (row-shaped launch) carries multi-shape
load-imbalance risk; and a single generic fused kernel is explicitly within the
plan's lower-bound path boundary. No `docs/dispatch.md` is written because no
shape-bucket specialization landed.

### Ranked future optimization (not pursued for this deliverable)
1. Broadcast-gate: eliminate the per-vector `v % row_vec` modulo (grid-stride
   row-offset tracking, or a one-block-per-row launch) to lift `ltx2_bcast_s32640`
   from SM/occupancy-leaning (NCU SM 69.7%, occ 50.5%) toward its DRAM roofline.
   Requires re-running strict-pinned correctness + benchmark after the edit.
