# Dispatch decision table — h200_diffusion_rotary_embedding__multi_shape

Candidate `native_cuda_v2_vectorized` (`src/csrc/rotary_embedding.cuh`). Evidence: `benchmark.csv` (wall-clock, allocation-fair, register cached) + `profile/ncu_v2_20260602_065439/` (NCU). Host `ion-h200-8`, GPU 7 (NVIDIA H200), sglang `c47f0e7cd` (≡ pinned `6965fe0ee`). All 6 production buckets are promoted to the native CUDA route (faster than the autotuned SGLang Triton baseline, near the HBM bandwidth bound).

## Promoted buckets (CUDA route)
| API | Exact gate (shape / dtype / layout) | baseline median µs | candidate median µs | speedup | route | promote reason |
|---|---|---|---|---|---|---|
| `apply_rotary_embedding` | x `(1,27030,24,128)` bf16 contiguous; cos/sin `(27030,64)` fp32 contiguous; `interleaved=False` | 157.68 | 105.68 | **1.492×** | cuda | faster; NCU 90.6µs/75% DRAM (~80% roofline) |
| `apply_ltx2_split_rotary_emb` | x `(1,1536,4096)` bf16; cos/sin `(1,32,1536,64)` bf16 non-contig (last stride 1, head stride 64, seq stride 2048) | 27.23 | 21.57 | **1.263×** | cuda | faster; bandwidth-bound |
| `apply_ltx2_split_rotary_emb` | x `(1,126,2048)`; cos/sin `(1,32,126,32)` bf16 non-contig (head 32, seq 1024) | 24.14 | 16.97 | **1.423×** | cuda | faster (fair harness); kernel ~4µs |
| `apply_ltx2_split_rotary_emb` | x `(1,1536,2048)`; cos/sin `(1,32,1536,32)` bf16 non-contig | 24.49 | 18.74 | **1.306×** | cuda | faster |
| `apply_ltx2_split_rotary_emb` | x `(1,6144,4096)`; cos/sin `(1,32,6144,64)` bf16 non-contig | 59.53 | 53.00 | **1.123×** | cuda | faster; NCU 34.6µs/79% DRAM (~90% roofline) |
| `apply_ltx2_split_rotary_emb` | x `(1,6144,2048)`; cos/sin `(1,32,6144,32)` bf16 non-contig | 40.94 | 34.06 | **1.202×** | cuda | faster |

**Geomean speedup (6 dedup shapes): 1.296× wall-clock; 1.297× GPU-kernel (CUDA events).** Active bound = HBM memory bandwidth (NCU 75–79% DRAM on the large buckets, near the analytical roofline). No further specialization is justified by current evidence — a single standard kernel + a single LTX-2 kernel (templated on dtype) cover all buckets near-bound.

## Fallback (NOT promoted → route to SGLang baseline, else PyTorch reference)
Every signature outside the exact gates above falls back, verified non-recursive + numerically by `tests/test_correctness.py::test_fallback_routing`:

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
