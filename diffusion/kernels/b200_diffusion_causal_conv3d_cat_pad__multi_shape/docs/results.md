# Results

> **Status: PROMOTABLE WIN.** The optimized CUDA candidate is bitwise-exact on B200
> and beats the copied SGLang Triton baseline on every production shape:
> **production-row geometric-mean speedup ≈ 2.07×** (two clean runs: 2.06× and 2.09×;
> per-row 1.55×–2.44×). NCU shows the win is real and the kernel is compute/instruction-
> bound (not bandwidth-bound), so memory headroom remains for a future round.

## Setup / provenance
- GPU: NVIDIA B200, host `ion-b200` (`innomatrix-us-adc-smb200-0003`), **GPU 0**, pinned with `CUDA_VISIBLE_DEVICES=0`.
  - Idle proof: no compute processes on GPU 0 before or after the canonical run; 0% utilization throughout (see `docs/run_log.md`).
- Baseline: copied SGLang Triton `_fused_cat_pad_5d_kernel` @ `67b2a9e` via destination-passing `baseline/binding.py`.
- Candidate: flat-chunk 16-byte-vectorized-store CUDA kernel (`solution/kernel.cu`, `cat_pad_flat_kernel`), built via tvm-ffi (`-std=c++17 -O3`, native `sm_100`, no fast math).
- Tolerance: bitwise exact (`atol=0, rtol=0`); all 11 workloads pass the A/B correctness gate; full `bench/correctness.py` PASS (13 value cases + non-contiguous positive + poison + rejection). Timing: CUDA events, inner-loop amplification, interleaved A/B (template).

## Per-shape results (baseline vs optimized candidate; canonical idle-GPU run)

| Workload | Headline | baseline µs | candidate µs | speedup | candidate GB/s |
|----------|:--------:|------------:|-------------:|--------:|---------------:|
| `prod_c1024_t1_h30_w52__cache1`  | ✅ | 30.15  | 14.41  | 2.09 | ~1180 |
| `prod_c1024_t1_h30_w52__cache2`  | ✅ | 25.53  | 16.51  | 1.55 | ~1224 |
| `prod_c1024_t2_h60_w104__cache1` | ✅ | 109.52 | 53.54  | 2.05 | ~1722 |
| `prod_c1024_t2_h60_w104__cache2` | ✅ | 109.02 | 57.47  | 1.90 | ~1826 |
| `prod_c512_t4_h120_w208__cache1` | ✅ | 313.18 | 136.81 | 2.29 | ~2085 |
| `prod_c512_t4_h120_w208__cache2` | ✅ | 315.18 | 142.70 | 2.21 | ~2178 |
| `prod_c256_t4_h240_w416__cache1` | ✅ | 616.05 | 252.02 | 2.44 | ~2247 |
| `prod_c256_t4_h240_w416__cache2` | ✅ | 615.55 | 262.84 | 2.34 | ~2349 |
| `reg_cache_null` (non-headline)            | — | 26.59 | 14.40 | 1.85 | — |
| `reg_no_pad_cat_only` (non-headline)       | — | 25.56 | 10.30 | 2.48 | — |
| `reg_noncontig_x_hw_transposed` (non-headline) | — | 36.66 | 4.13 | 8.89 | — |

**Production headline:** equal-weight geometric-mean speedup **≈ 2.07×** (run A 2.057×, run B 2.090×; arith mean ≈ 2.09×, min 1.55×, max 2.44×).

## Roofline / NCU evidence (active bound)
- Bytes moved per row = read(x + cache) + write(full output), bf16. Largest row (`c256…cache1`): ~566 MB → candidate ~2.25 TB/s; per-row candidate bandwidth ranges ~1.18–2.35 TB/s vs baseline ~0.66–1.00 TB/s.
- B200 HBM peak ≈ 8 TB/s, so the candidate runs at ~15–29% of peak bandwidth.
- **Nsight Compute** (`cat_pad_flat_kernel<uint16,8>`, largest shape, `ncu --set basic`): **Compute (SM) throughput 81.2%**, DRAM throughput 17.9%, Memory throughput 27.7%, achieved occupancy 54.2%.
- **Named active bound: instruction/compute-bound**, not memory bandwidth. The per-output-element index arithmetic + predication (interior test, `iw` range check, per-lane row-wrap handling) saturates the SMs while DRAM is far from peak. This is why the kernel wins ~2× yet stays well under bandwidth roofline.

## Conclusion
Promotable win: correct (bitwise-exact across production + regression + non-contiguous, with poison/rejection coverage) and a reproducible ~2.07× production geometric-mean speedup over the frozen baseline on an idle B200, with full provenance. The flat-chunk 16-byte-store design fixed both the per-element 64-bit index math (vs the scalar transliteration) and the small-shape thread-utilization problem (vs an intermediate row-per-block attempt).

## Headroom / future optimization (documented, not required by the success bar)
NCU shows the kernel is instruction-bound with ~3–5× memory headroom. The highest-value next step is a branch-light fast path: detect chunks that are fully interior with no spatial border and no row wrap, and copy them with minimal per-lane predication (and a realignment-aware vectorized read, since the `W_l=1` shift makes the source-to-output mapping offset by one element). Cache-streaming hints (`L1::no_allocate`) and launch-bound/occupancy tuning are second-order per KernelWiki. These are candidate Round 3 work; the current candidate already satisfies the promotion bar.
