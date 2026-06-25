# Results — b200_diffusion_attention_concat_copy__multi_model

## Outcome

**Evidence-backed WIN.** Candidate CUDA kernels beat the PyTorch/ATen baseline by an **equal-weight geometric-mean speedup of 1.406×** over the 7 production workloads on an idle NVIDIA B200, with **100% bit-exact correctness** (`required_matched_ratio = 1.0`; all 24 workloads, atol=rtol=0, NaN/Inf preserved) and a passing negative-test matrix (validator + kernel level).

Measured on the model-head AC grid (FLUX.2 `h_full=24 → h_local=12`, JoyAI `h_full=32 → h_local=16` at `sp_size=2`), with the candidate enforcing exact supported layouts.

## Promotion Gate
- Correctness: **PASS** — 48/48 (baseline + candidate × 24) bit-exact vs an independent PyTorch oracle; poison + negative-control OK.
- Negative-test matrix: **PASS** — rejected loudly (validator + candidate kernel): invalid order, `h_local<=0`, `h_start % h_local != 0`, out-of-range `h_start`, pre-sliced prefix, contiguous copy source, sequence-strided concat source, non-dense slice shard/prefix, dtype mismatch, and shape mismatch.
- A/A harness validity: **PASS** — baseline-vs-baseline geomean 0.9996.
- Performance: **PASS** — production geomean 1.406× > 1.0.
- GPU discipline: **PASS** — single idle B200 (id 0), idle before (`0 %, 4 MiB`) and after (`0 %, 4 MiB`), `REMOTE_GPU_ID=0` constant.

## Per-Row Results (production, headline geomean)

| Workload | op | h_full→h_local | speedup | baseline (µs) | candidate (µs) |
|----------|----|----------------|---------|---------------|----------------|
| flux_concat_512_4096_h24 | concat | 24 | 0.999 | 10.293 | 10.308 |
| joyai_concat_8048_1004_h32 | concat | 32 | 0.866 | 24.946 | 28.803 |
| flux_copy_4608_h24 | copy | 48→24 view | 1.815 | 22.762 | 12.542 |
| joyai_copy_8048_h32 | copy | 64→32 view | 2.625 | 74.432 | 28.352 |
| joyai_copy_1004_h32 | copy | 64→32 view | 1.379 | 8.511 | 6.173 |
| flux_slice_concat_512_4096_hf24_hl12_r0_AB | slice+concat | 24→12 | 1.900 | 19.596 | 10.312 |
| joyai_slice_concat_1004_8048_hf32_hl16_r0_BA | slice+concat | 32→16 | 1.004 | 20.657 | 20.577 |
| **production geomean** | | | **1.406** | | |

Regression rows (17, not in headline) all pass correctness; they cover the full slice order×rank cross product (both orders × {rank0, rank1} per model), the 48/64-head synthetic variant, copy variants, NaN/Inf, degenerate, and fp16/fp32. Arithmetic mean 1.51×; min 0.866; max 2.625.

## Where the speedup comes from (per-op bytes / achieved bandwidth)

B200 HBM3e peak ≈ 8 TB/s. All ops are pure memory movement.

- **copy_contiguous — WIN (1.38–2.62×).** Source is a non-contiguous head-sliced view (models `x[:, :, h0:h1, :].contiguous()`); ATen's generic strided `copy_` under-utilizes bandwidth. `joyai_copy_8048`: ~132 MB / 28.4 µs → **4.66 TB/s** candidate vs 74.4 µs → **1.77 TB/s** baseline.
- **slice_heads_then_concat — WIN (1.00–1.90×).** Two compounding effects: fusion removes the intermediate contiguous-prefix scratch round-trip, and on this grid the prefix slice is a strided head gather (12 of 24 / 16 of 32 heads) so the baseline's `.contiguous()` step is the same slow strided copy ATen does poorly. FLUX (`hf24→hl12`) hits **1.90×** (baseline 19.6 µs strided-contiguous + cat vs candidate 10.3 µs single fused pass). JoyAI (`hf32→hl16`) is **1.00×** — the large 8048 shard copy dominates and dilutes the small-prefix savings.
- **concat_sequence — PARITY (0.999 / 0.866).** Both sides are one bandwidth-bound pass over identical bytes; ATen `CatArrayBatchedCopy` is near roofline. Expected near-parity; does not threaten the headline.

## Candidate design (final, hardened)
Single exported selector; output decomposed into sequence regions written once: pitched 16 B block gather for head-sliced copy/prefix, single coalesced pass for plain concat, flat copy for the shard. Before any copy the candidate validates the exact supported layout and rejects otherwise: `order ∈ {0,1}`, `h_local>0`, `h_full>h_local` (no pre-sliced prefix), `h_start % h_local == 0`, in-range `h_start`, dense strides for concat/shard/output and the full-head prefix, a genuinely non-contiguous head-sliced copy source, and matching head-dim/shape/dtype. A general per-output-vector kernel is retained as the B>1 / non-16 B-aligned fallback. Optimization trajectory: v1 0.96 → v2 region-based 1.235 → v3 single-launch concat 1.322 → corrected AC grid + hardening **1.406**.

## Environment and provenance
- Host: `ion-b200` (`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf`, workspace `/home/sglang-omni/bbuf/kda/attn_concat_copy`.
- GPU: NVIDIA B200 (sm_100), id 0; idle before `0 %, 4 MiB`, after `0 %, 4 MiB`.
- Toolchain: torch 2.11.0+cu130, CUDA 13.0, nvcc 13.0, Python 3.12.3, Linux 6.8.
- Baseline source: SGLang `main` @ `67b2a9ed0cfba8ec625d3f26548e502646fd914d` (`docs/baseline_source.md`).
- Candidate source hash: `solution/kernel.cu` sha256 `5e04227361c8226e7e307bc6f69d55e5511cce18023dff0c2ab5fd85cf653ad5`.
- Compile flags: `-std=c++17 -O3 -gencode=arch=compute_100,code=sm_100 -lineinfo`; no `--use_fast_math`.
- Benchmark settings (config.toml): warmup 10, trials 7, inner-iterations max 2048, target 1000 µs, isolated subprocess; CUDA-event interleaved A/B; bit-exact compare.

## Reproduction
On `ion-b200`, container `sglang_bbuf`, `/home/sglang-omni/bbuf/kda/attn_concat_copy`, idle GPU 0:
```bash
python bench/gen_workloads.py --check                      # freeze + schema + contract guard
CUDA_VISIBLE_DEVICES=0 python bench/correctness.py --impl both --device cuda   # 48/48 + negatives
CUDA_VISIBLE_DEVICES=0 KDA_AA=1 python bench/benchmark.py --out bench/results_aa.jsonl --device cuda:0 --inner-iterations-max 2048 --timeout-seconds 900 --atol 0 --rtol 0
CUDA_VISIBLE_DEVICES=0 python bench/benchmark.py --out bench/results.jsonl --device cuda:0 --inner-iterations-max 2048 --timeout-seconds 900 --atol 0 --rtol 0
```
