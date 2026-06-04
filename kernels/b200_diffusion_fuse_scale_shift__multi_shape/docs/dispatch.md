# Dispatch — b200_diffusion_fuse_scale_shift__multi_shape

The candidate is one CUDA module with a host-side dispatch inside each
exported entry point. Both sides expose the same three entry points; the
baseline (copied Triton) keeps the upstream wrapper's own internal dispatch
(3D blc-opt kernel / 4D autotuned kernel / scalar fast path), so the dispatch
boundary is symmetric: one call per entry point on each side. No per-shape
fallback to the baseline is used — the candidate wins every production row.

## fuse_scale_shift buckets (candidate-internal)

| bucket condition | kernel | why | evidence (production rows, final run) |
|---|---|---|---|
| 4D scale `[B,F,1,C]` | `scale_shift_frame_kernel` (strided, no compaction copies) | upstream semantics preserved without the wrapper's `.contiguous()` copies | correctness-only class (no retained 4D row); rider reg_ep1_4d 7.05x |
| both scale and shift 0D/1-element scalar, both zero | device-to-device copy (matches the reference copy fast path exactly, incl. ignoring `scale_constant`) | reference parity | correctness-only class |
| 16B-vectorizable (C % vec == 0; x/out/scale/shift bases 16B-aligned; unit channel stride; row strides 16B multiples) and rows >= 512 | `scale_shift_rowgrid_kernel` — one block per token row, 16B vectors, `__ldcs/__stcs` for streams, `__ldg` for token-shared (sl==0) modulation rows | no per-element division; streaming rows cannot thrash L2; reused rows stay cached | s4096 3.14x; s8424 bcast rows 1.63-1.70x (5.0 TB/s); full3d 1.39x (7.6 TB/s); hunyuanvideo 27k 1.16x (5.4 TB/s); wan-ti2v chunk2 fp32 1.25x (6.55 TB/s); wan-t2v/i2v fp32-bcast 1.89-1.91x (5.6 TB/s) |
| 16B-vectorizable and rows < 512 | `scale_shift_flatvec_kernel` — flat vectorized grid, 32-bit indexing | one block per row would underfill 148 SMs at S=19..195 | S in {19,47,189,195,55}: 7.55-9.05x (host-path bound; candidate floor ~4.3-4.5us vs baseline ~33-40us) |
| anything else (odd C, exotic strides, non-zero scalars) | `scale_shift_strided_kernel` (generic, fp32 math) | always-correct fallback | correctness grid only |

## Gated LayerNorm buckets (candidate-internal, both entry points)

| bucket condition | kernel | why | evidence |
|---|---|---|---|
| 16B-vectorizable (C % vec == 0; all bases aligned; mod rows unit-stride with 16B-multiple batch strides) and rounds = ceil((C/vec)/threads) <= 4 | `ln_select01_vec_kernel` / `residual_ln_select01_vec_kernel` — one block per row, threads picked per C (C=3072 bf16 -> 384 threads, 1 round), fp32 register cache of the row, statistics by dtype (bf16/fp16: shifted-data one-pass moments, single fused reduction, 2 barriers; fp32: reference centered two-pass), `__ldg` modulation rows, raw-dtype 16B gate pass-through | exact-C (no 25% masked-lane waste at Triton's BLOCK_N=4096); x read once; minimal barriers | qwen-edit gated 1.04x (3.09 TB/s), resgated 1.05x (4.90 TB/s) on S=8424; riders with affine/int64/fp32 7.6-8.0x |
| otherwise | `ln_select01_kernel` / `residual_ln_select01_kernel` (generic two-pass scalar) | always-correct fallback | correctness grid only |

## Named remaining bound

The gated EP2 row is barrier/launch-pipeline-limited at one block per token
row (8424 blocks), not DRAM-limited: it achieves 3.09 TB/s while the same
kernel family streams at 4.9-7.6 TB/s elsewhere, and the baseline shares the
same structural bound (2.97 TB/s). Multi-row blocks or
a split stats/apply scheme could raise it further; not pursued after the
promotion gate was met on every row (bounded-attempts policy) — recorded as
the active bound for this row class. (All bucket evidence numbers above are
from the canonical final run; NCU SOL details in docs/run_log.md.)
