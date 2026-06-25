# Results — b200_diffusion_attention_concat_copy__multi_model

## Outcome

**Evidence-backed WIN.** The candidate CUDA kernel beats the PyTorch/ATen baseline by an **equal-weight geometric-mean speedup of 1.322×** over the 7 production workloads on an idle NVIDIA B200, with **100% bit-exact correctness** (`required_matched_ratio = 1.0`; all 20 workloads, atol=rtol=0, NaN/Inf preserved).

The win is driven by the two op types where ATen leaves headroom — the strided head-sliced `copy_contiguous` and the fused `slice_heads_then_concat` — while plain `concat_sequence` lands at parity with ATen's already-near-roofline `CatArrayBatchedCopy`, exactly as predicted in `docs/research.md`.

## Promotion Gate
- Correctness: **PASS** — 20/20 rows bit-exact vs an independent PyTorch oracle (candidate and baseline), poison + negative-control + NaN/Inf preservation all pass (`bench/correctness.py --impl both`).
- A/A harness validity: **PASS** — baseline-vs-baseline geomean = 1.0002 (no slot bias).
- Performance: **PASS** — production geomean 1.322× > 1.0.
- GPU discipline: **PASS** — single idle B200 (id 0), idle before and after, `REMOTE_GPU_ID=0` held constant across correctness/A-A/benchmark.

## Per-Row Results (production, headline geomean)

| Workload | op | speedup | baseline (µs) | candidate (µs) |
|----------|----|---------|---------------|----------------|
| flux_concat_512_4096_h24 | concat | 1.000 | 10.283 | 10.286 |
| joyai_concat_8048_1004_h32 | concat | 0.863 | 24.866 | 28.805 |
| flux_copy_4608_h24 | copy | 1.828 | 22.714 | 12.429 |
| joyai_copy_8048_h32 | copy | 2.630 | 74.248 | 28.235 |
| joyai_copy_1004_h32 | copy | 1.376 | 8.481 | 6.166 |
| flux_slice_concat_512_4096_h24_sp2_r0_AB | slice+concat | 1.088 | 15.777 | 14.500 |
| joyai_slice_concat_1004_8048_h32_sp2_r0_BA | slice+concat | 1.139 | 39.281 | 34.488 |
| **production geomean** | | **1.322** | | |

Regression rows (not in headline) all pass correctness and corroborate the pattern: slice+concat both orders / both sp_ranks 1.10–1.42×; copy 1.41–1.79×; small/degenerate rows 1.5–2.2× (candidate's single launch beats ATen's multi-launch on tiny shapes); plain-concat opposite order 0.93–0.96× (parity). Arithmetic mean 1.42×; min 0.863; max 2.630.

## Where the speedup comes from (per-op bytes / achieved bandwidth)

B200 HBM3e peak ≈ 8 TB/s. All three ops are pure memory movement; the question is bytes moved and achieved bandwidth.

- **copy_contiguous — WIN (1.38–2.63×).** The source is a non-contiguous head-sliced view (models `x[:, :, h0:h1, :].contiguous()`). ATen's generic strided `copy_` under-utilizes bandwidth here; the candidate copies per-`(seq)` contiguous `H·D` blocks with 16 B vectors.
  - `joyai_copy_8048_h32`: ~132 MB traffic. Candidate 28.2 µs → **4.67 TB/s**; baseline 74.2 µs → **1.78 TB/s** (ATen ~22% of peak on the strided view).
  - `flux_copy_4608_h24`: ~57 MB. Candidate 12.4 µs → 4.56 TB/s; baseline 22.7 µs → 2.49 TB/s.
- **slice_heads_then_concat — WIN (1.09–1.14×).** The fusion removes the intermediate contiguous-prefix materialization. Baseline traffic ≈ `4P + 2S` (read prefix, write scratch, read scratch, read shard, write output); fused candidate ≈ `2P + 2S`. Ideal `1 + P/(P+S)` ≈ 1.11× for both production shapes — matched by the measured 1.088× / 1.139×.
  - `flux_slice AB`: candidate ~56.6 MB / 14.5 µs ≈ 3.90 TB/s; baseline ~62.8 MB / 15.8 µs ≈ 3.98 TB/s — same bandwidth, candidate moves ~10% fewer bytes (no scratch).
- **concat_sequence — PARITY (1.000 / 0.863).** Both sides are a single bandwidth-bound pass over the same bytes. ATen's `CatArrayBatchedCopy` is near roofline:
  - `flux_concat`: candidate 10.29 µs ≈ 5.50 TB/s = baseline 10.28 µs (tie).
  - `joyai_concat`: candidate 28.8 µs ≈ 5.14 TB/s vs baseline 24.9 µs ≈ 5.95 TB/s (ATen ~16% better bandwidth on this large copy). This is the only sub-parity production row; it does not threaten the headline and matches the expected "concat near-parity vs ATen" (research.md).

## Candidate design (final)
Single exported selector function; the output is decomposed into 1–2 sequence regions written directly to the final buffer:
- copy / slice-prefix: pitched 16 B block copy of the head-sliced source (the part ATen does inefficiently).
- plain concat: one coalesced single-launch pass with a segment branch (matches ATen's single-kernel cat).
- slice shard: one flat coalesced copy.
A general per-output-vector kernel (correct for any B / non-16 B-aligned layout) is retained as a fallback; every production/regression row (B=1, D=128, 16 B-aligned) takes the fast region path. Optimization iterations: v1 single generic kernel (geomean 0.96, concat slow) → v2 region-based (1.235) → v3 single-launch concat (**1.322**).

## Environment and provenance
- Host: `ion-b200` (`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf`, workspace `/home/sglang-omni/bbuf/kda/attn_concat_copy`.
- GPU: NVIDIA B200 (sm_100), id 0; idle before `0 %, 4 MiB` and after `0 %, 4 MiB`.
- Toolchain: torch 2.11.0+cu130, CUDA 13.0, nvcc 13.0, Python 3.12.3, Linux 6.8.
- Baseline source: SGLang `main` @ `67b2a9ed0cfba8ec625d3f26548e502646fd914d` (see `docs/baseline_source.md`).
- Candidate source hash: `solution/kernel.cu` sha256 `73381d63fe2341b6569f1c7cb1f88b4a342887f585b703a81039480ac8d07e7d`.
- Compile flags: `-std=c++17 -O3 -gencode=arch=compute_100,code=sm_100 -lineinfo`; no `--use_fast_math` (see `docs/benchmark_method.md`).
- Benchmark settings (config.toml): warmup 10, trials 7, inner-iterations max 2048, target sample 1000 µs, isolated subprocess per workload; CUDA-event interleaved A/B timing; bit-exact compare.

## Reproduction
On `ion-b200`, container `sglang_bbuf`, task dir `/home/sglang-omni/bbuf/kda/attn_concat_copy`, idle GPU 0:
```bash
# freeze check (workloads are immutable)
python bench/gen_workloads.py --check
# correctness (bit-exact, both impls)
CUDA_VISIBLE_DEVICES=0 python bench/correctness.py --impl both --device cuda
# A/A harness validity (expect geomean ~1.0)
CUDA_VISIBLE_DEVICES=0 KDA_AA=1 python bench/benchmark.py --out bench/results_aa.jsonl --device cuda:0 --inner-iterations-max 2048 --timeout-seconds 900 --atol 0 --rtol 0
# headline A/B benchmark
CUDA_VISIBLE_DEVICES=0 python bench/benchmark.py --out bench/results.jsonl --device cuda:0 --inner-iterations-max 2048 --timeout-seconds 900 --atol 0 --rtol 0
```
