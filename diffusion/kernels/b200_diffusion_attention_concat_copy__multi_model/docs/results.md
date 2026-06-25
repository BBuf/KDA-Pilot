# Results — b200_diffusion_attention_concat_copy__multi_model

## Outcome

**Evidence-backed WIN** on the immutable AC-4 grid. Candidate CUDA kernels beat the PyTorch/ATen baseline by an **equal-weight geometric-mean speedup of 1.409×** over the 7 production workloads on an idle NVIDIA B200, with **100% bit-exact correctness** (`required_matched_ratio = 1.0`; all 22 workloads, atol=rtol=0, NaN/Inf preserved) and a passing negative-test matrix.

Measured on the **corrected slice grid** (AC-4 head contract: model `h_full = 24` FLUX.2 / `32` JoyAI, sliced to `h_local = h_full/sp_size = 12 / 16` at `sp_size=2`), replacing the Round 0 48/64-head synthetic grid (now retained only as regression).

## Promotion Gate
- Correctness: **PASS** — 44/44 (baseline + candidate × 22) bit-exact vs an independent PyTorch oracle; poison + negative-control OK.
- Negative-test matrix: **PASS** — invalid order, pre-sliced prefix, `h_start % h_local != 0`, out-of-range `h_start`, and contiguous copy source are all rejected loudly (validator + candidate kernel).
- A/A harness validity: **PASS** — baseline-vs-baseline geomean 1.0023.
- Performance: **PASS** — production geomean 1.409× > 1.0.
- GPU discipline: **PASS** — single idle B200 (id 0), idle before (`0 %, 4 MiB`) and after (`0 %, 4 MiB`), `REMOTE_GPU_ID=0` constant.

## Per-Row Results (production, headline geomean)

| Workload | op | h_full→h_local | speedup | baseline (µs) | candidate (µs) |
|----------|----|----------------|---------|---------------|----------------|
| flux_concat_512_4096_h24 | concat | 24 | 0.950 | 9.795 | 10.310 |
| joyai_concat_8048_1004_h32 | concat | 32 | 0.868 | 25.019 | 28.814 |
| flux_copy_4608_h24 | copy | 48→24 view | 1.814 | 22.858 | 12.602 |
| joyai_copy_8048_h32 | copy | 64→32 view | 2.616 | 74.476 | 28.464 |
| joyai_copy_1004_h32 | copy | 64→32 view | 1.385 | 8.549 | 6.173 |
| flux_slice_concat_512_4096_hf24_hl12_r0_AB | slice+concat | 24→12 | 1.998 | 20.599 | 10.312 |
| joyai_slice_concat_1004_8048_hf32_hl16_r0_BA | slice+concat | 32→16 | 1.019 | 20.960 | 20.567 |
| **production geomean** | | | **1.409** | | |

Regression rows (15, not in headline) all pass correctness; speedups corroborate the pattern (slice both orders/ranks, the 48/64 synthetic variant, copy variants, NaN/Inf, degenerate, fp16/fp32). Arithmetic mean 1.52×; min 0.868; max 2.616.

## Where the speedup comes from (per-op bytes / achieved bandwidth)

B200 HBM3e peak ≈ 8 TB/s. All ops are pure memory movement; bytes moved and achieved bandwidth decide.

- **copy_contiguous — WIN (1.39–2.62×).** Source is a non-contiguous head-sliced view (models `x[:, :, h0:h1, :].contiguous()`); ATen's generic strided `copy_` under-utilizes bandwidth. `joyai_copy_8048`: ~132 MB / 28.5 µs → **4.64 TB/s** candidate vs 74.5 µs → **1.77 TB/s** baseline.
- **slice_heads_then_concat — WIN (1.02–2.00×).** Two compounding effects: (1) fusion removes the intermediate contiguous-prefix scratch round-trip; (2) on the AC-4 grid the prefix slice is a *strided* head gather (12 of 24 / 16 of 32 heads), so the baseline's `.contiguous()` step is the same slow strided copy ATen does poorly. FLUX (`hf24→hl12`) hits **2.00×** (baseline 20.6 µs strided-contiguous + cat vs candidate 10.3 µs single fused pass). JoyAI (`hf32→hl16`) is **1.02×** — the large 8048 shard copy dominates and dilutes the small-prefix savings.
- **concat_sequence — PARITY (0.950 / 0.868).** Both sides are one bandwidth-bound pass over identical bytes; ATen `CatArrayBatchedCopy` is near roofline (`joyai_concat` baseline 5.92 TB/s vs candidate 5.14 TB/s). Expected near-parity (research.md); does not threaten the headline.

## Candidate design (final, hardened)
Single exported selector; output decomposed into sequence regions written once: pitched 16 B block gather for head-sliced copy/prefix, single coalesced pass for plain concat, flat copy for the shard. Contract checks reject invalid `order`, `h_local<=0`, `h_start % h_local != 0`, out-of-range `h_start`, pre-sliced prefix, and shape/stride mismatches before any copy. General per-output-vector kernel retained as B>1 / non-16 B-aligned fallback. Optimization trajectory: v1 generic 0.96 → v2 region-based 1.235 → v3 single-launch concat 1.322 (48/64 grid) → v4 corrected AC-4 grid + hardened **1.409**.

## Environment and provenance
- Host: `ion-b200` (`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf`, workspace `/home/sglang-omni/bbuf/kda/attn_concat_copy`.
- GPU: NVIDIA B200 (sm_100), id 0; idle before `0 %, 4 MiB`, after `0 %, 4 MiB`.
- Toolchain: torch 2.11.0+cu130, CUDA 13.0, nvcc 13.0, Python 3.12.3, Linux 6.8.
- Baseline source: SGLang `main` @ `67b2a9ed0cfba8ec625d3f26548e502646fd914d` (`docs/baseline_source.md`).
- Candidate source hash: `solution/kernel.cu` sha256 `364faf8afcaf8992ee8afa238e489a68b5a0efb1e2c51082ebff38df33562b0a`.
- Compile flags: `-std=c++17 -O3 -gencode=arch=compute_100,code=sm_100 -lineinfo`; no `--use_fast_math`.
- Benchmark settings (config.toml): warmup 10, trials 7, inner-iterations max 2048, target 1000 µs, isolated subprocess; CUDA-event interleaved A/B; bit-exact compare.

## Reproduction
On `ion-b200`, container `sglang_bbuf`, `/home/sglang-omni/bbuf/kda/attn_concat_copy`, idle GPU 0:
```bash
python bench/gen_workloads.py --check                      # freeze + schema guard
CUDA_VISIBLE_DEVICES=0 python bench/correctness.py --impl both --device cuda   # 44/44 + negatives
CUDA_VISIBLE_DEVICES=0 KDA_AA=1 python bench/benchmark.py --out bench/results_aa.jsonl --device cuda:0 --inner-iterations-max 2048 --timeout-seconds 900 --atol 0 --rtol 0
CUDA_VISIBLE_DEVICES=0 python bench/benchmark.py --out bench/results.jsonl --device cuda:0 --inner-iterations-max 2048 --timeout-seconds 900 --atol 0 --rtol 0
```
