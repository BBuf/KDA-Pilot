# Results

> **Status: PROMOTABLE WIN.** The optimized CUDA candidate is bitwise-exact on B200 and
> beats the copied SGLang Triton baseline on every production shape:
> **production-row geometric-mean speedup ≈ 2.06×** (four runs across two idle GPUs:
> 2.057×, 2.090×, 2.063×, 2.060×; per-row 1.60×–2.45×). NCU shows the kernel is
> compute/instruction-bound (not bandwidth-bound), so memory headroom remains.

## Setup / provenance
- GPU: NVIDIA B200, host `ion-b200` (`innomatrix-us-adc-smb200-0003`). Canonical run on **GPU 7**, pinned with `CUDA_VISIBLE_DEVICES=7`.
  - Idle proof (canonical run): GPU 7 had **no compute processes** before or after, 0% utilization, 0 MiB used. Earlier consistent runs used GPU 0 (see `docs/run_log.md`).
- Baseline: copied SGLang Triton `_fused_cat_pad_5d_kernel` @ `67b2a9e` via destination-passing `baseline/binding.py`.
- Candidate: flat-chunk 16-byte-vectorized-store CUDA kernel (`solution/kernel.cu`, `cat_pad_flat_kernel`) + stride-aware fallback, built via tvm-ffi (`-std=c++17 -O3`, native `sm_100`, no fast math).
- Tolerance: bitwise exact (`atol=0, rtol=0`); all 12 workloads pass the A/B correctness gate; full `bench/correctness.py` PASS (13 value cases + non-contiguous positive + nonzero-storage-offset positive + poison + rejection). Timing: CUDA events, inner-loop amplification, interleaved A/B (template).

## Per-shape results (baseline vs optimized candidate; canonical idle-GPU-7 run)

| Workload | Headline | baseline µs | candidate µs | speedup | candidate GB/s |
|----------|:--------:|------------:|-------------:|--------:|---------------:|
| `prod_c1024_t1_h30_w52__cache1`  | ✅ | 26.32  | 14.40  | 1.83 | ~1180 |
| `prod_c1024_t1_h30_w52__cache2`  | ✅ | 26.48  | 16.52  | 1.60 | ~1224 |
| `prod_c1024_t2_h60_w104__cache1` | ✅ | 108.88 | 53.53  | 2.03 | ~1722 |
| `prod_c1024_t2_h60_w104__cache2` | ✅ | 108.94 | 57.38  | 1.90 | ~1829 |
| `prod_c512_t4_h120_w208__cache1` | ✅ | 311.18 | 136.39 | 2.28 | ~2091 |
| `prod_c512_t4_h120_w208__cache2` | ✅ | 312.90 | 142.44 | 2.20 | ~2182 |
| `prod_c256_t4_h240_w416__cache1` | ✅ | 613.18 | 250.37 | 2.45 | ~2261 |
| `prod_c256_t4_h240_w416__cache2` | ✅ | 612.48 | 262.10 | 2.34 | ~2356 |
| `reg_cache_null` (non-headline)               | — | 26.42 | 14.40 | 1.83 | — |
| `reg_no_pad_cat_only` (non-headline)          | — | 26.14 | 10.29 | 2.54 | — |
| `reg_noncontig_x_hw_transposed` (non-headline)| — | 38.61 | 5.15  | 7.49† | — |
| `reg_noncontig_offset` (non-headline)         | — | 45.18 | 4.38  | 10.33† | — |

**Production headline:** equal-weight geometric-mean speedup **≈ 2.06×** (runs 2.057–2.090×; arith mean ≈ 2.08×, min 1.60×, max 2.45×).

† The two non-contiguous rows' large "speedups" are **not** a meaningful kernel win: the baseline
binding normalizes non-contiguous inputs with `.contiguous()` inside the timed call (the upstream
kernel is contiguous-only), so most of that baseline time is a layout-normalization copy. These
rows are non-headline correctness coverage for the stride-aware fallback (incl. nonzero storage
offset), not a performance claim.

## Roofline / NCU evidence (active bound)
- Bytes moved per row = read(x + cache) + write(full output), bf16. Largest row (`c256…cache1`): ~566 MB → candidate ~2.25 TB/s; per-row candidate bandwidth ~1.18–2.36 TB/s vs baseline ~0.66–1.00 TB/s.
- B200 HBM peak ≈ 8 TB/s, so the candidate runs at ~15–29% of peak bandwidth.
- **Nsight Compute** (`cat_pad_flat_kernel<uint16,8>`, largest shape, `ncu --set basic`): **Compute (SM) throughput 81.2%**, DRAM throughput 17.9%, Memory throughput 27.7%, achieved occupancy 54.2%.
- **Named active bound: instruction/compute-bound**, not memory bandwidth. The per-output-element index arithmetic + predication (interior test, `iw` range check, per-lane row-wrap handling) saturates the SMs while DRAM is far from peak — explaining the ~2× win that stays under the bandwidth roofline.

## Conclusion
Promotable win: bitwise-exact across production + regression (cache-null, no-pad, non-contiguous, nonzero-storage-offset) with poison/rejection coverage, and a reproducible ~2.06× production geometric-mean speedup over the frozen baseline on an idle B200 with full provenance. The flat-chunk 16-byte-store design fixed both the per-element index math (vs the scalar transliteration) and the small-shape thread-utilization problem (vs an intermediate row-per-block attempt).

## Headroom / future optimization (documented; not required by the success bar)
NCU shows the kernel is instruction-bound with ~3–5× memory headroom. The highest-value next step is a branch-light fast path: detect chunks that are fully interior with no spatial border and no row wrap, and copy them with minimal per-lane predication (and a realignment-aware vectorized read, since the `W_l=1` shift makes the source-to-output mapping offset by one element). Cache-streaming hints (`L1::no_allocate`) and launch-bound/occupancy tuning are second-order per KernelWiki. These are optional future work; the current candidate already satisfies the promotion bar.
