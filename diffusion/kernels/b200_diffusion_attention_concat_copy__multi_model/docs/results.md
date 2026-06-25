# Results — b200_diffusion_attention_concat_copy__multi_model

## Outcome

**Evidence-backed WIN.** On the committed kernel (sha256 `4f102e04…`), the candidate beats the PyTorch/ATen baseline with an **equal-weight production geometric-mean speedup of 1.30× (recorded clean run; robust range 1.30–1.39 across repeats)** on an idle NVIDIA B200, with **100% bit-exact correctness** (all 24 workloads, atol=rtol=0, NaN/Inf preserved) and a passing negative-test matrix.

The win is robust (geomean > 1.0 in every clean run) and is dominated by the stable, large `copy_contiguous` advantage; `concat_sequence` and `slice_heads_then_concat` sit near parity. See "Measurement variance" below.

## Promotion Gate
- Correctness: **PASS** — 48/48 (baseline + candidate × 24) bit-exact vs an independent PyTorch oracle; poison + negative-control OK.
- Negative-test matrix: **PASS** — rejected loudly (validator + candidate kernel): invalid order, `h_local<=0`, `h_start % h_local != 0`, out-of-range `h_start`, pre-sliced prefix, contiguous copy source, sequence-strided concat source, non-dense slice shard/prefix, dtype mismatch, shape mismatch, source batch mismatch, non-dense (padded) output batch stride, and cross-CUDA-device inputs.
- A/A harness validity: **PASS** — baseline-vs-baseline geomean ≈ 1.0 (0.9996–1.0023 across rounds).
- Performance: **PASS** — production geomean > 1.0 in every clean run (1.296 / 1.316 / 1.391).
- GPU discipline: **PASS** — single idle B200 (id 0), idle before (`0 %, 4 MiB`) and after (`0 %, 4 MiB`), `REMOTE_GPU_ID=0` constant.

## Per-Row Results (production, recorded clean run; geomean 1.296)

| Workload | op | h_full→h_local | speedup | baseline (µs) | candidate (µs) |
|----------|----|----------------|---------|---------------|----------------|
| flux_concat_512_4096_h24 | concat | 24 | 0.991 | 10.219 | 10.310 |
| joyai_concat_8048_1004_h32 | concat | 32 | 0.866 | 24.974 | 28.845 |
| flux_copy_4608_h24 | copy | 48→24 view | 1.820 | 22.778 | 12.519 |
| joyai_copy_8048_h32 | copy | 64→32 view | 2.610 | 74.456 | 28.528 |
| joyai_copy_1004_h32 | copy | 64→32 view | 1.388 | 8.564 | 6.170 |
| flux_slice_concat_512_4096_hf24_hl12_r0_AB | slice+concat | 24→12 | 1.193 | 12.277 | 10.290 |
| joyai_slice_concat_1004_8048_hf32_hl16_r0_BA | slice+concat | 32→16 | 0.907 | 18.624 | 20.526 |
| **production geomean** | | | **1.296** | | |

Arithmetic mean 1.396. The 17 regression rows (full slice order×rank matrix, 48/64 synthetic variant, copy variants, NaN/Inf, degenerate, fp16/fp32) all pass correctness.

## Measurement variance (important for honest interpretation)
Across 3 back-to-back clean idle-GPU-0 runs the production geomean was **1.296, 1.316, 1.391** (median 1.316). The candidate kernels are stable run-to-run (e.g. flux_slice candidate 10.29–10.31 µs). The variance comes entirely from the **ATen baseline for the slice rows**: ATen's strided `.contiguous()`+`cat` for `flux_slice` measures **bimodally** at ~12.3 µs or ~19.4 µs, so that row's speedup swings 1.19×↔1.88× and `joyai_slice` 0.91×↔1.01×. `copy` (1.39–2.61×) and `concat` (0.87–0.99×) are stable. The win (geomean > 1.0) holds in every run; the headline conservatively reports the lowest observed clean run.

## Where the speedup comes from (per-op)
- **copy_contiguous — WIN (1.39–2.61×, stable).** The dominant, reproducible win. Source is a non-contiguous head-sliced view (models `x[:, :, h0:h1, :].contiguous()`); ATen's generic strided `copy_` under-utilizes bandwidth (`joyai_copy_8048`: ~132 MB / 28.5 µs → **4.6 TB/s** candidate vs 74.5 µs → **1.8 TB/s** baseline), while the candidate's pitched 16 B block gather is near bandwidth.
- **slice_heads_then_concat — WIN-to-PARITY (≈0.9–1.9×).** The fused candidate writes the output once (no intermediate contiguous-prefix scratch) and is stable; the realized speedup is gated by ATen's bimodal slice baseline (above). The candidate is never slower than ~parity and is often faster.
- **concat_sequence — PARITY (0.87–0.99×).** Both sides are one bandwidth-bound pass over identical bytes; ATen `CatArrayBatchedCopy` is near roofline. Expected near-parity; does not threaten the geomean (carried by copy).

## Candidate design (final, hardened)
Single exported selector; output decomposed into sequence regions written once: pitched 16 B block gather for head-sliced copy/prefix, single coalesced pass for plain concat, flat copy for the shard. Before any copy the candidate validates the exact supported layout and rejects otherwise: `order ∈ {0,1}`, `h_local>0`, `h_full>h_local` (no pre-sliced prefix), `h_start % h_local == 0`, in-range `h_start`, dense strides for concat/shard/output (incl. a dense output batch stride for `B>1`) and the full-head prefix, a genuinely non-contiguous head-sliced copy source, every source dimension (batch/seq/head/head_dim) matching the output, matching dtype, and every source tensor on the same CUDA device as the output. A general per-output-vector kernel is retained as the B>1 / non-16 B-aligned fallback. Optimization trajectory: v1 0.96 → v2 region-based 1.235 → v3 single-launch concat ≈1.3–1.4.

## Environment and provenance
- Host: `ion-b200` (`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf`, workspace `/home/sglang-omni/bbuf/kda/attn_concat_copy`.
- GPU: NVIDIA B200 (sm_100), id 0; idle before `0 %, 4 MiB`, after `0 %, 4 MiB`.
- Toolchain: torch 2.11.0+cu130, CUDA 13.0, nvcc 13.0, Python 3.12.3, Linux 6.8.
- Baseline source: SGLang `main` @ `67b2a9ed0cfba8ec625d3f26548e502646fd914d` (`docs/baseline_source.md`).
- Candidate source hash: `solution/kernel.cu` sha256 `4f102e045d6fa595679d51a0b2f25605fab740df77ce6527987dba389eeb9c44` (the committed kernel).
- Compile flags: `-std=c++17 -O3 -gencode=arch=compute_100,code=sm_100 -lineinfo`; no `--use_fast_math`.
- Benchmark settings (config.toml): warmup 10, trials 7, inner-iterations max 2048, target 1000 µs, isolated subprocess; CUDA-event interleaved A/B; bit-exact compare.

## Reproduction
On `ion-b200`, container `sglang_bbuf`, `/home/sglang-omni/bbuf/kda/attn_concat_copy`, idle GPU 0:
```bash
python bench/gen_workloads.py --check                      # freeze + schema + contract guard
CUDA_VISIBLE_DEVICES=0,2 python bench/correctness.py --impl both --device cuda   # 48/48 + negatives (incl. cross-device)
CUDA_VISIBLE_DEVICES=0 KDA_AA=1 python bench/benchmark.py --out bench/results_aa.jsonl --device cuda:0 --inner-iterations-max 2048 --timeout-seconds 900 --atol 0 --rtol 0
CUDA_VISIBLE_DEVICES=0 python bench/benchmark.py --out bench/results.jsonl --device cuda:0 --inner-iterations-max 2048 --timeout-seconds 900 --atol 0 --rtol 0
```
