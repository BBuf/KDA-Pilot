# Results — b200_ltx2_rms_adaln__bitwise

## Headline

**GO.** The staged candidate is **bit-wise equal** to the PyTorch eager baseline on
every tested row and is **1.91x–2.03x faster** on the six production workloads,
**equal-weight geometric-mean speedup 1.974x**, with **no per-shape regression**.

- Correctness: `bench/correctness.py --impl both --rows all` -> **71/71 bit-wise
  PASS** (torch.equal + raw uint16; tolerance forbidden).
- Benchmark: 6/6 production rows bit-wise matched; geomean **1.974x**.
- Promotion criterion (DEC-1): bit-wise exact on all rows + no production-row
  median regression + equal-weight geomean > 1.0x — **all satisfied**.

**Scope:** finite inputs (the production rows are finite, and the correctness
harness rejects any NaN/Inf output). Bit-exactness of NaN/Inf payload/sign is out
of scope and is not claimed (DEC-4).

## Candidate design

Staged candidate (`solution/kernel.cu::ltx2_rms_adaln_candidate`):

1. **Stage 1** reuses the SAME `at::rms_norm(x, {D}, {}, eps)` as the baseline, so
   the bf16 `normed` is bit-identical by construction (no RMS reduction-order
   reverse-engineering).
2. **Stage 2** is one fused CUDA kernel reproducing the three post-norm bf16
   round-to-nearest-even boundaries exactly:
   `one_plus = rne(1 + scale)`, `mul = rne(normed * one_plus)`, `y = rne(mul + shift)`
   (`__float2bfloat16_rn` / `__fadd_rn` / `__fmul_rn`; no FMA contraction; no
   `--use_fast_math`/FTZ), 16-byte (8×bf16) vectorized loads/stores, per-layout
   broadcast for scale/shift (`[D]`/`[B,D]`/`[B,1,D]`/`[B,S,D]`), fail-closed
   support gate, launched on the current CUDA stream.

Exposed through the same destination-passing tvm-ffi ABI and symmetric compile
flags as `baseline/kernel.cu` (`-std=c++17 -O3` + device `-gencode`, torch linkage,
no fast-math).

## Environment / provenance

- Host `ion-b200` (`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf`.
- GPU: NVIDIA B200 (sm_100), id 5, idle (0% util, 0 MiB before; 4 MiB after),
  pinned `CUDA_VISIBLE_DEVICES=5` for all commands.
- torch 2.12.1+cu130, CUDA 13.0, tvm_ffi 0.1.9, nvcc V13.0.88.
- Baseline upstream: SGLang `main` @ `aaa31eb0…` (re-resolved at loop start to
  `bb74ed4a…`; the two RMS-AdaLN source files are byte-identical). See
  `docs/baseline_source.md`.
- Full command log + idle evidence in `docs/run_log.md`; raw samples in
  `bench/results.jsonl` (kept local, excluded from the PR).

## Per-shape benchmark (headline)

Standard standalone harness: isolated subprocess runner, CUDA-event inner-loop
amplification (~1000us samples), interleaved A/B per trial, equal-weight geomean.
Median latency per side:

| Workload | shape | baseline (us) | candidate (us) | speedup | matched |
|----------|-------|---------------|----------------|---------|---------|
| ltx23_stage1_video  | [2,1536,4096]  | 57.64  | 29.03  | 1.985 | yes |
| ltx23_stage1_audio  | [2,126,2048]   | 37.20  | 19.51  | 1.907 | yes |
| ltx23_stage2_video  | [1,6144,4096]  | 106.58 | 53.94  | 1.976 | yes |
| ltx23_stage2_audio  | [1,126,2048]   | 38.99  | 20.24  | 1.926 | yes |
| ltx23_hq_stage1_video | [1,8160,4096]  | 139.82 | 69.07  | 2.024 | yes |
| ltx23_hq_stage2_video | [1,32640,4096] | 486.09 | 239.70 | 2.028 | yes |

- Equal-weight geometric mean: **1.974x** (arithmetic mean 1.974; min 1.907; max 2.028).
- No production-row regression (every row > 1.0x).

## Why ~2x — decomposition and roofline

Both sides share `at::rms_norm`; the win comes from collapsing the modulation —
the three eager ops `(1+scale)`, `normed*(1+scale)`, `+shift`, plus the final
destination `copy_` the eager baseline issues to land its result in `output` —
into a single fused pass that writes `output` directly. Decomposition (simple
CUDA-event timing; explanatory, not the headline):

| row | rms-only (us) | modulation eager / 3 ops (us) | modulation fused / 1 kernel (us) | fused mod BW |
|-----|---------------|-------------------------------|----------------------------------|--------------|
| s1536_d4096  | 14.6 | 42.4  | 14.2  | ~7115 GB/s |
| s6144_d4096  | 18.4 | 88.0  | 34.9  | ~5768 GB/s |
| hq_s8160_d4096 | 24.9 | 112.5 | 43.1 | ~6209 GB/s |
| hq_s32640_d4096 | 82.5 | 399.6 | 155.2 | ~6890 GB/s |
| audio_d2048  | ~12  | ~30   | ~3-5  | ~0.4-1.2 TB/s |

modulation bytes = read `normed` + read `scale` + read `shift` + write `out`
= `4 * B*S*D * 2` bytes (full layout). B200 HBM3e peak ≈ 8 TB/s.

- **Video rows (D=4096):** the fused modulation kernel is **memory-bandwidth-bound,
  achieving ~72–89% of peak HBM bandwidth (≈5.8–7.1 TB/s)** — near-optimal for a
  pure elementwise streaming kernel. The ~2x overall follows from modulation
  3-passes → 1-pass while `at::rms_norm` is unchanged.
- **Audio rows (S=126, D=2048):** tiny and **launch-/latency-bound** (achieved
  bandwidth far below peak). They still improve (no regression) because fusing
  three kernel launches into one removes ~2 launch overheads per call — fusion
  helps the small rows rather than hurting them, contrary to the usual
  small-row-underfill worry.
- NCU was not required: the bottleneck is an unambiguous memory-bound elementwise
  fusion with no non-obvious behavior, and no further kernel edit is implied by a
  profile. The roofline above is the evidence per the diffusion kernel rules
  ("NCU or a clear roofline-style analysis").

## Shape specialization / dispatch

**None.** A single staged kernel wins all six production rows (1.91–2.03x) with no
per-shape regression, including both the small audio (S=126) and the huge video
(S=32640) extremes. No shape table or dispatcher is warranted, so `docs/dispatch.md`
is intentionally not created (it exists only when specialization is used).

## Fully-fused single kernel — probe gate (NO-GO)

`solution/fused_probe.cu` + `bench/probe_fused.py` test whether a custom
single-kernel fp32 RMS reduction can reproduce `at::rms_norm`'s bf16 `normed`
bit-for-bit (48 cases = 8 shapes × 3 seeds × {randn, wide-magnitude}):

- Video rows (D=4096 and canonical D=3072): **DIFFER** on most seeds/modes (a few
  hundred elements out of 12–134M, ~0.0001–0.0008%, max_abs ~1–2 bf16 ULPs — a
  low-mantissa reduction-order difference).
- Audio rows (D=2048): EQUAL on all seeds/modes (the small reduction happens to
  match ATen for this size, but that does not make the kernel bit-exact on all rows).

**Conclusion:** this custom single-kernel reduction cannot be made bit-exact against
`at::rms_norm` on the video production rows (ATen's fp32 reduction order is not
reproducible bit-for-bit here), so a fully-fused single kernel is a documented
**NO-GO**; the staged candidate is the production path (DEC-2 probe gate).

> Caveat: the probe disproves *this* reduction as a bit-exact replacement; it is
> not a mathematical proof that no version-pinned, ATen-exact reduction could ever
> exist. But reproducing ATen's reduction bit-for-bit across shapes and torch
> versions is exactly the fragility the staged path (reusing `at::rms_norm`) avoids
> by construction.

## Conclusion

**GO — promote the staged candidate.** It is bit-wise exact on all production rows
plus the regression grid and adversarial rows, fails closed on out-of-gate inputs
(public path falls back bit-exact), beats the baseline by an equal-weight geomean of
**1.974x** with no per-shape regression on an idle B200, and the result is explained
by a near-peak-bandwidth memory-bound modulation fusion. The fully-fused single
kernel is a documented no-go.
