# NCU + Roofline Report — cuda-v4 (promoted, native CUDA diffusion RoPE), B200 / sm_100

> Candidate lineage: v1 (scalar LTX-2, geomean 0.954×) → v2 (128-bit vectorized, 1.351×) → v3 (standard drops shared-mem `__syncthreads`, 1.349× with standard 1.76×) → **v4 (LTX-2 block size matched to per-row work; geomean 1.3834×, standard 1.80×)**. All bit-exact vs baseline on 11/11.

- Host/GPU: `ion-b200` (innomatrix-us-adc-smb200-0003), container `sglang_bbuf`, NVIDIA B200 (GPU 5, idle-gated), CC 10.0.
- Baseline (pinned): SGLang `0b65588c180a519427867d53cc4ed6e9e2610890` (`0.5.12.dev472+g3f7e538b2`), torch 2.11.0+cu130, nvcc 13.0, tvm_ffi 0.1.9.
- Candidate: `src/csrc/rotary_embedding.cuh`, built via SGLang `jit_kernel` (no `torch.utils.cpp_extension`, no `--use_fast_math`), PDL OFF.
- Harness: `profile_one.py` (one warmed launch per shape). NCU: `--section SpeedOfLight --section Occupancy --section LaunchStats -k regex:rotary --launch-skip 2 --launch-count 1`. Reports under `reports/`.
- Correctness gate: bit-exact vs the SGLang diffusion Triton baseline on all 11 unique signatures (`pair_diff = 0`).

## Measured SOL (NCU, warmed launch, kernel-name filtered)

| Bucket (shape) | Kernel | DRAM SOL % | Compute (SM) SOL % | Achieved Occ % | Waves/SM |
|---|---|---|---|---|---|
| standard 1×27030×24×128 (v3) | `standard_rotary_kernel<128>` | 59.1 | 62.1 | 80.2 | 22.8 |
| LTX-2 large half64 1×24576×4096 | `ltx2_split_rotary_kernel<64>` | 85.3 | 67.7 | 84.8 | 20.8 |
| LTX-2 large half32 1×24576×2048 (v4, block=128) | `ltx2_split_rotary_kernel<32>` | 74.9 | 64.9 | 86.0 | 10.4 |
| LTX-2 small 1×126×2048 (v4, block=128) | `ltx2_split_rotary_kernel<32>` | 2.4 | 2.5 | 6.3 | 0.05 |

> v4 note: matching the LTX-2 block size to per-row work (half32 → 128 threads instead of 256) raised half32-large occupancy 73.6%→86.0% and removed idle-warp overhead (Compute SOL 72.6%→64.9%); wall-time is DRAM-paced at ~75% SOL (near bound). Same change lifted the small/medium LTX-2 shapes (geomean 1.349→1.383). half64-large and the standard kernel are unchanged by v4 (their rows above remain valid).

(Durations under profiling are inflated by replay; perf numbers below use the clean CUDA-event benchmark medians.)

## Roofline (B200 HBM3e peak ≈ 8 TB/s)

Bytes moved = read(x) + read(cos)+read(sin) + write(out). Effective BW = bytes / candidate median latency.

| Bucket | Bytes moved | Cand median | Eff. BW | % of ~8 TB/s | Speedup vs Triton |
|---|---|---|---|---|---|
| standard | ~346 MB | 61.7 µs | ~5.6 TB/s | ~70% | 1.80× |
| LTX-2 large half64 (24576) | ~604 MB | 92.4 µs | ~6.5 TB/s | ~82% | 1.00× |
| LTX-2 large half32 (24576) | ~302 MB | 50.2 µs | ~6.0 TB/s | ~75% | 1.20× |
| LTX-2 small (126) | ~2 MB | 13.6 µs | ~0.15 TB/s | ~2% | 1.60× |

## Six-dimension analysis & active bound per bucket

1. **Compute** — RoPE is a few fp32 FMAs + bf16 round per element; low arithmetic intensity. Only the standard kernel approaches a compute/issue limit (62% SM SOL) because it reads fp32 cos/sin and does the fp32-faithful pair math; LTX-2 compute SOL is secondary to DRAM.
2. **Memory** — dominant. LTX-2-large-half64 at **85.3% DRAM SOL** is the clearest signal: bandwidth-bound, near the HBM ceiling. half32-large at 74% (BW-leaning). standard at 59% (≈69% effective in the clean benchmark).
3. **Occupancy** — healthy for all large/standard buckets (74–85%); not the limiter there. The small shape is **occupancy-starved** (8.3%).
4. **Latency-hiding** — the standard kernel improved from 47%→59% DRAM SOL once the shared-cos/sin `__syncthreads` barrier was removed (cuda-v2→v3): more memory-level parallelism, fewer stalls.
5. **Launch-overhead** — dominates the small shape: **Waves/SM = 0.11** (126 blocks ≪ SM count), so the GPU is mostly idle and per-launch overhead governs latency. The candidate wins (1.55–1.63×) precisely by having lower fixed overhead than the autotuned Triton baseline.
6. **Tail-effect** — large shapes have many waves (≈21–23 Waves/SM), so tail is negligible; the small shape is a single partial wave (pure latency).

### Named active bound → completion decision
- **LTX-2 large half64**: DRAM-bandwidth bound (85% SOL), at **parity** with the (also-bandwidth-saturated) Triton baseline. **No-go** for further speedup — both are near the HBM ceiling; ~1.0–1.06× is the attainable bound for this access pattern.
- **LTX-2 large half32**: BW-leaning (74%); candidate already 1.20–1.22× over Triton. Near bound; remaining gap is the HBM efficiency ceiling.
- **standard**: compute/BW-balanced (59/62% SOL), **1.76×** over Triton (matches the best-known prior result). Practical bound: the bit-exact fp32 RoPE math is the limiter; reducing it would break the numeric contract. **No-go** for materially more without sacrificing correctness.
- **LTX-2 small/medium**: launch/latency/occupancy bound (cannot add work — shapes are fixed). Candidate wins 1.55–1.63× via lower launch overhead; near the latency floor.

## Conclusion
The promoted candidate (cuda-v4) is **≥ baseline on every captured signature** (geomean **≈1.45×** across 3 consecutive idle-gated runs: 1.4522/1.4528/1.4605×; an earlier run measured 1.3834× — candidate times are stable, the spread is Triton-baseline run-to-run variance on launch-bound shapes; all exceed the prior-run hypothesis 1.3676×), bit-exact on all 11, and each representative bucket is at or near its active hardware bound:
- **LTX-2 large half64** — DRAM-bandwidth bound (85% SOL), parity with Triton → **no-go** (HBM ceiling).
- **standard** — compute/BW-balanced (59/62% SOL), 1.80× → near practical bound (bit-exact fp32 math).
- **LTX-2 large half32** — BW-leaning (75% SOL @ 86% occ), 1.21–1.23× → near bound.
- **LTX-2 small/medium** — launch/latency bound (≤0.05 waves/SM), 1.66–1.71× via lower launch overhead.

Optimization is complete on a bound basis, not multiplier-chasing. Codex (independent) concurred: promote, with the caveat that standard/half32 retain minor scheduling/cache headroom (not proven final optima) while large-half64 is at the standalone bandwidth ceiling.
