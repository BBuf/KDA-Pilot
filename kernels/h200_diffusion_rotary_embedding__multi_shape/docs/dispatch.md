# Dispatch decision table — h200_diffusion_rotary_embedding__multi_shape

Current candidate `native_cuda_v3_streamcache` (`src/csrc/rotary_embedding.cuh`: v2 design
+ `__ldcs`/`__stcs` streaming-cache accesses on every read-once/write-once global stream).
Evidence: `benchmark.csv` blocks of 2026-06-04 (symmetric same-process interleaved A/B,
allocation-fair, register cached, pipelined CUDA-event device timing) +
`profile/ncu_v3_20260604/` (NCU full/source/duration sets, both sides). Host `ion-h200-8`,
GPU 0 (NVIDIA H200, idle 0%/0MiB), SGLang `84e110831` (rotary files ≡ pinned `6965fe0ee`).

All 6 production buckets stay promoted to the native CUDA route. Per the tightened
shipping rules every per-bucket claim below is decomposed into DEVICE (kernel-vs-kernel)
vs HOST (launch-path residual); host-path wins are labeled host and are legitimate
shipped wins only because the wrapper preserves the full public contract (plain
functions in SGLang — no custom-op registration exists to drop; functional new-tensor
semantics; non-recursive fallback).

## Promoted buckets (CUDA route) — wall (shipping) + device (kernel) decomposition

| API | Exact gate (shape / dtype / layout) | base wall µs | cand wall µs | wall speedup | device speedup (events) | kernel ratio (NCU) | win source / promote reason |
|---|---|---|---|---|---|---|---|
| `apply_rotary_embedding` | x `(1,27030,24,128)` bf16 contiguous; cos/sin `(27030,64)` fp32 contiguous; `interleaved=False` | 164.34 | 109.79 | **1.497×** | 1.462× (130.81→89.49µs) | 1.72× (153.5→89.4µs) | real kernel win; NCU 89.4µs / 74.4% DRAM (~81% roofline) |
| `apply_ltx2_split_rotary_emb` | x `(1,1536,4096)` bf16; cos/sin `(1,32,1536,64)` bf16 non-contig (last stride 1, head 64, seq 2048) | 29.14 | 23.48 | **1.241×** | 1.505×* | 0.93× (10.65 vs 11.49µs) | host-path win: Triton spends ~29µs wall on a ~10.6µs kernel (launch machinery) vs the tvm-ffi path's ~23.5µs wall on a ~11.5µs kernel — wall is the shipping claim; Triton kernel itself slightly faster |
| `apply_ltx2_split_rotary_emb` | x `(1,126,2048)`; cos/sin `(1,32,126,32)` bf16 non-contig (head 32, seq 1024) | 26.67 | 19.78 | **1.349×** | 1.515×* | 0.75× (2.70 vs 3.58µs) | host-path win; kernel-only deficit from grid undersubscription (126 blocks < 132 SMs) — queued future work |
| `apply_ltx2_split_rotary_emb` | x `(1,1536,2048)`; cos/sin `(1,32,1536,32)` bf16 non-contig | 27.02 | 21.15 | **1.277×** | 1.492×* | 0.85× (6.62 vs 7.81µs) | host-path win; wall is the shipping claim |
| `apply_ltx2_split_rotary_emb` | x `(1,6144,4096)`; cos/sin `(1,32,6144,64)` bf16 non-contig | 62.75 | 53.72 | **1.168×** | 1.023× (40.50→39.59µs) | 0.98× (35.2 vs 35.9µs) | **kernel parity** (device-fair within noise; prior round 1.004×, confirmed); wall win is host-path (Triton launch residual ~22.2µs vs ~14.1µs); kept per the re-measure rule — wall-fair win reproduces |
| `apply_ltx2_split_rotary_emb` | x `(1,6144,2048)`; cos/sin `(1,32,6144,32)` bf16 non-contig | 42.46 | 33.23 | **1.278×** | 1.128× (23.19→20.56µs) | 1.04× (19.5 vs 18.7µs) | small real kernel win + host win, both labeled (prior-round event reading 1.286× downgraded to today's 1.128×/1.04×) |

(*) starvation artifact: the Triton kernel on these buckets is shorter than its own
per-launch host cost, so even pipelined event timing keeps gaps on the baseline side —
the NCU kernel-ratio column is the device arbiter there.

**Shipping outcome (geomean over the 6 dedup shapes): wall 1.2977× interleaved
(legacy-mode headline 1.2775×).** The device geomean 1.3379× is diagnostic only — it
mixes starvation-inflated small-bucket numbers; per-bucket kernel truth is the NCU
column. Active bound = HBM memory bandwidth on the big buckets (NCU 74–76% DRAM,
81–88% of the analytical roofline; `profile/ncu_v3_20260604/REPORT.md`). No further
specialization is justified by current evidence: a single standard kernel + a single
LTX-2 kernel (templated on dtype) cover all buckets, and the remaining kernel-side
levers are each ≲5% with regression risk (the 384-thread launch variant measurably
regressed and was rejected).

## Continuation history (2026-06-04 round)

- v2 `native_cuda_v2_vectorized` re-validated vs SGLang `84e110831` (== pin): 6/6
  correct, legacy geomean 1.2671× (prior-round headline 1.2955× on GPU 7).
- v3a std `__ldcs`/`__stcs`: KEPT (std device-fair 1.40× → 1.46×).
- v3b std 384-thread launch: REJECTED (device-fair 1.41×; occupancy 93.75% < 100% hurts
  this DRAM-bound kernel).
- v3c LTX-2 streaming hints: KEPT (S6144h32 device-fair 1.086× → 1.128×; others within
  noise, no regression) → `native_cuda_v3_streamcache`.
- LTX-2 cos/sin gather rewrite: NOT attempted — NCU shows ~4.2 TB/s (~88% of peak) on
  the target bucket; no provably wasteful gather exists (near-bound stop rule).
- PDL: skipped — optional per the task contract, negative prior evidence on this launch
  pattern (qknorm pilot), and both large buckets are bandwidth-bound, not launch-bound.

## Fallback (NOT promoted → route to SGLang baseline, else PyTorch reference)
Every signature outside the exact gates above falls back, verified non-recursive +
numerically by `tests/test_correctness.py::test_fallback_routing`:

| Signature | Route |
|---|---|
| fp16 standard / fp16 LTX-2 | baseline (then reference) |
| standard `interleaved=True` | baseline |
| standard 3D input `(T,H,D)` | baseline |
| standard non-production head size (e.g. D=64) | baseline |
| LTX-2 contiguous cos/sin (non-captured layout) | baseline |
| LTX-2 non-captured `S`, `B!=1`, `num_heads!=32`, `half∉{32,64}` | baseline |
| CPU tensors / CUDA-x + CPU-cos device mismatch | reference / raises like baseline |

Broadening the CUDA route to any of these requires new benchmark rows + an updated entry here first.
