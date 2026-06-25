# Results — b200_diffusion_residual_gate_add__multi_shape

## Conclusion: GO
The fused candidate is correctness-clean on B200 and faster than the faithful
PyTorch-eager production path on every production row. Headline equal-weight
geomean **2.199x** (all rows >= 1.20x). NCU + roofline confirm the result is
bandwidth/launch-bound as expected for elementwise traffic, and the analyze pass
(task3/task7/task10) accepts the baseline/numerics/layout and ranks remaining
optimization as modest, conditional upside — so the generic vectorized candidate
is accepted as the final implementation for this task.

## Environment
- Host `ion-b200` (`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf`
  (`lmsysorg/sglang:dev`); torch 2.11.0+cu130, CUDA 13.0, tvm-ffi 0.1.9, nvcc 13.0.
- NVIDIA B200 (192 GB HBM3e, 148 SMs, ~8 TB/s nominal; NCU sustained ref ~7.2 TB/s).
- Pinned idle GPU: benchmark on GPU 2, correctness+NCU reruns on GPU 0 (each pinned
  via `REMOTE_GPU_ID=<id> CUDA_VISIBLE_DEVICES=<id>`, fail-closed guard
  `KDA_REQUIRE_PINNED_GPU=1`; idle before/after 0%/0MiB). Details in `run_log.md`.
- Baseline source: sgl-project/sglang `main` @ `8314247d9de0fa2c58e34756b3e1dbc6cf815dfd`
  (`docs/baseline_source.md`); candidate `solution/kernel.cu` sha256 `a450f863…`.

## Final commands
```bash
# correctness (strict-pinned)
KDA_REQUIRE_PINNED_GPU=1 REMOTE_GPU_ID=0 CUDA_VISIBLE_DEVICES=0 \
  python bench/correctness.py --impl both --rows all --report /tmp/rga_correctness_final.json
# benchmark (strict-pinned)
KDA_REQUIRE_PINNED_GPU=1 REMOTE_GPU_ID=<id> CUDA_VISIBLE_DEVICES=<id> \
  python bench/benchmark.py --out bench/results.jsonl
# NCU (per representative row)
ncu --set basic --launch-skip 6 --launch-count 1 --target-processes all python /tmp/rga_profile.py <row>
```

## Correctness (AC-3 / AC-4)
`bench/correctness.py --impl both --rows all`: **67/67 PASS** on B200. Covers the 8
production rows (candidate vs fp32 one-round oracle AND vs faithful eager baseline,
bf16 atol=rtol=5e-2), the regression grid (full/broadcast gate; bf16/fp16/fp32;
odd-D / non-vec-aligned-D / small-L tails; deterministic zero/sign rows; repeated
randomized seeds; 4D over multiple frame counts), a poison self-test, and both-side
rejection (full-gate-noncontig, bad-gate-2d, gate-leaddim-not1, dtype-mismatch,
alias, non-contiguous, 4D batch>1).

## Performance (AC-5) — candidate vs faithful eager two-op baseline
Baseline = the profiled production path (`torch.mul(update,gate,out=scratch)` then
`torch.add(residual,scratch,out=out)`, two launches + one temp + two dispatches;
single `torch.add` for the 4D row). Candidate = one fused CUDA pass. CUDA-event
median per call (matched ratio 1.0).

| Workload | gate | speedup | baseline us | candidate us |
|---|---|---:|---:|---:|
| ltx2_full_s8160_c4096 | full | 1.6016 | 66.328 | 41.413 |
| ltx2_bcast_s32640_c4096 | bcast | 2.9638 | 419.032 | 141.384 |
| ltx2_full_s126_c2048 | full | 1.7970 | 17.661 | 9.828 |
| ideogram4_bcast_s4096_c4608 | bcast | 2.8252 | 64.350 | 22.777 |
| flux2_bcast_s4608_c3072 | bcast | 3.2763 | 47.488 | 14.495 |
| flux2_bcast_s4096_c3072 | bcast | 3.3356 | 41.568 | 12.462 |
| flux2_bcast_s512_c3072 | bcast | 1.7261 | 19.546 | 11.324 |
| ltx2_broadcast_add_4d | - | 1.2028 | 11.510 | 9.569 |

Headline and secondary views (the row mix weights broadcast-gate cases heavily, so
secondary views are reported per the analyze caveat):
- **All-8 equal-weight geomean: 2.199x** (the contract headline). Arith mean 2.341x,
  min 1.203x, max 3.336x.
- Residual-gate-only (7 rows) geomean: **2.397x**.
- Call-count-weighted geomean (documented profile call-counts, 6-row subset,
  82,134 calls): **1.699x** — lower because the highest-frequency rows are the tiny
  full-gate `[1,126,2048]` (33,123 calls, 1.80x) and the 4D add (13,392 calls,
  1.20x), which have the smallest per-call speedups.

The win is "fused single CUDA kernel vs the faithful eager two-op production path"
— it removes one kernel launch, the intermediate temp's full write+read, and one
Python dispatch; it is not a single-kernel-vs-single-kernel algorithmic speedup.

## Roofline / speed-of-light (AC-7)
Candidate byte model (bf16, 2 B/elem): full gate ~8 B/elem (r+u+g read, out write);
broadcast gate ~6 B/elem (r+u read, out write; gate cached); 4D add ~4 B/elem
(b read, out write; a cached). Achieved BW from the CUDA-event median above;
DRAM%/SM% from NCU (`--set basic`) for the three profiled rows.

| Workload | elems | cand B/elem | cand us | achieved GB/s | % of ~8 TB/s | NCU DRAM% | NCU SM% | named bound |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| ltx2_full_s8160_c4096 | 33.42M | 8 | 41.41 | 6457 | 80.7 | 72.1 | 55.8 | DRAM-bound (near roofline) |
| ltx2_bcast_s32640_c4096 | 133.69M | 6 | 141.38 | 5674 | 70.9 | 59.5 | 69.8 | SM/occupancy-leaning (modulo+ldg; occ 50.6%) |
| ltx2_full_s126_c2048 | 0.258M | 8 | 9.83 | 210 | 2.6 | 3.7 | 3.1 | launch/grid-bound (grid 126 < 148 SMs) |
| ideogram4_bcast_s4096_c4608 | 18.87M | 6 | 22.78 | 4972 | 62.1 | - | - | DRAM-bound (bandwidth) |
| flux2_bcast_s4608_c3072 | 14.16M | 6 | 14.50 | 5860 | 73.2 | - | - | DRAM-bound (bandwidth) |
| flux2_bcast_s4096_c3072 | 12.58M | 6 | 12.46 | 6058 | 75.7 | - | - | DRAM-bound (bandwidth) |
| flux2_bcast_s512_c3072 | 1.57M | 6 | 11.32 | 833 | 10.4 | - | - | launch/occupancy-leaning (small) |
| ltx2_broadcast_add_4d | 0.774M | 4 | 9.57 | 324 | 4.0 | - | - | launch/low-fusion (inferred, not NCU-profiled) |

NCU bound interpretation (task10, Codex-confirmed):
- Large full-gate (`ltx2_full_s8160`): DRAM-bound near roofline (NCU 72.1% DRAM,
  "DRAM bottleneck"; ~6.46 TB/s effective at benchmark speed).
- Large broadcast-gate (`ltx2_bcast_s32640`): SM/occupancy-leaning, DRAM headroom
  (NCU SM 69.8% > DRAM 59.5%, occupancy 50.6%) — the per-vector `v % row_vec`
  modulo + `__ldg` indexing is the plausible instruction-side limiter.
- Small (`ltx2_full_s126`): launch/grid-bound (NCU: grid 126 blocks < 148 SMs,
  occupancy 12.8%) — the win is collapsing two launches into one.
- 4D add: launch/low-fusion bound, **inferred** from the byte model + 1.20x speedup
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
(67/67 correctness; positive geomean 2.199x on every row; bounds explained by
NCU/roofline); the one ranked edit (broadcast-gate modulo / occupancy) is, per NCU
and the analyze pass, modest and conditional upside for rows that already win
2.83-3.34x, and the natural implementation (row-shaped launch) carries multi-shape
load-imbalance risk; and a single generic fused kernel is explicitly within the
plan's lower-bound path boundary. No `docs/dispatch.md` is written because no
shape-bucket specialization landed.

### Ranked future optimization (not pursued for this deliverable)
1. Broadcast-gate: eliminate the per-vector `v % row_vec` modulo (grid-stride
   row-offset tracking, or a one-block-per-row launch) to lift `ltx2_bcast_s32640`
   from SM/occupancy-leaning (NCU SM 69.8%, occ 50.6%) toward its DRAM roofline.
   Requires re-running strict-pinned correctness + benchmark after the edit.
