# Results — b200_ltx2_rms_adaln__bitwise

## Outcome: PROMOTE (bit-exact, ~2.0x geomean speedup over PyTorch eager)

The staged candidate is **bit-wise equal** to the PyTorch eager baseline on every
production row and the full regression grid, and is **~2.0x faster** on all four
production workloads on NVIDIA B200.

## Correctness (zero tolerance)
- `bench/correctness.py --impl both`: **55/55 rows PASS (bitwise)** on NVIDIA B200.
  Comparison = raw `uint16` storage equality + `torch.equal`, `atol=rtol=0`.
  Coverage: 4 production rows, in-gate grid (all supported layouts `[D]`/`[B,D]`/`[B,1,D]`/`[B,S,D]` + mixed scale/shift), adversarial bf16 rounding-boundary rows, out-of-gate eager-fallback + raw-kernel fail-closed rows, and a poison self-test.
- Both the baseline (ATen eager) and the candidate match an independent PyTorch eager oracle bit-for-bit, and match each other.

## Performance (NVIDIA B200, GPU id 6, idle)

Primary metric: `baseline_median_us / candidate_median_us`. Headline: equal-weight geometric mean over the 4 production rows.

| Workload | x shape | baseline median (µs) | candidate median (µs) | candidate std (µs) | speedup |
|----------|---------|----------------------|------------------------|--------------------|---------|
| ltx23_stage1_video_s1536_d4096_full | [2,1536,4096] | 57.510 | 28.889 | 0.038 | 1.991x |
| ltx23_stage1_audio_s126_d2048_full | [2,126,2048] | 23.083 | 11.191 | 0.219 | 2.063x |
| ltx23_stage2_video_s6144_d4096_full | [1,6144,4096] | 105.810 | 53.863 | 0.148 | 1.964x |
| ltx23_stage2_audio_s126_d2048_full | [1,126,2048] | 37.149 | 18.394 | 0.288 | 2.020x |

- **Geometric-mean speedup: 2.009x** (arithmetic mean 2.009x; min 1.964x; max 2.063x). All 4 PASSED the bitwise gate before timing.
- Timing: standalone template, isolated subprocess runner, 7 trials, CUDA-event inner-loop amplification (~1000µs samples, inner iters 16–128 per side), interleaved A/B. Full samples + mean/min/p10/p90 in the result JSON (kept local, not staged).

## Roofline-style analysis (why ~2x)

The op is memory-bound (pure elementwise + a cheap row reduction). Taking the largest row, stage2 video `[1,6144,4096]` bf16 (one `[B,S,D]` array = 50.33 MB):

- **Baseline** (eager): `rms_norm` (read x + write normed) then three separate elementwise launches `1+scale` (read scale + write t1), `normed*t1` (read normed + read t1 + write t2), `t2+shift` (read t2 + read shift + write y) ≈ **10 array passes ≈ 503 MB**, across **4 kernel launches** plus two full-size temporaries. Achieved ≈ 503 MB / 105.81 µs ≈ **4.76 TB/s**.
- **Candidate** (staged): `at::rms_norm` (read x + write normed) then **one** fused modulation kernel (read normed + read scale + read shift + write y) ≈ **6 array passes ≈ 302 MB**, across **2 kernel launches**, no modulation temporaries. Achieved ≈ 302 MB / 53.86 µs ≈ **5.61 TB/s** (~70% of B200 HBM3e ≈ 8 TB/s).

The ~2x comes from (a) ~1.67x less HBM traffic (3 elementwise passes + 2 temporaries collapsed into 1 fused pass) and (b) higher achieved bandwidth + 2 fewer launches. **Active bound: HBM bandwidth.**

## Bit-exactness design (why it is safe)
- Stage 1 reuses the **same** `at::rms_norm(x,{D},{},eps)` as the baseline, so the fp32 reduction order and the bf16 store of `normed` are identical by construction (no reduction-order reverse-engineering — see `docs/numerics_notes.md`).
- Stage 2 reproduces eager's three rounding points exactly with `__float2bfloat16_rn` after `1+scale`, after the multiply, and after the add (matches PyTorch's fp32-opmath + round-to-nearest-even bf16 store). No `--use_fast_math`; the discrete rounds prevent FMA contraction.

## Environment / provenance
- Host `ion-b200` (innomatrix-us-adc-smb200-0003), container `sglang_bbuf`, GPU id **6**, NVIDIA B200. GPU 6 idle before (0% util, ~0 MiB) and after (0% util, ~0 MiB) — see `docs/run_log.md`.
- torch 2.12.1+cu130, CUDA 13.0, tvm_ffi 0.1.9, nvcc CUDA 13.0, cc (gcc) 13.3.0.
- Compile flags (symmetric, both sides): `-std=c++17 -O3 -gencode=arch=compute_100,code=sm_100`, torch linkage, **no `--use_fast_math`**.
- Baseline upstream commit: `aaa31eb0a11e09f9511bade5e815907ec0b91fa0` (SGLang `main`). Candidate `solution/kernel.cu` sha256: `711459cbab831935733975045465e585c5110e2f1d8ffa599ed9d554796ff0e8`.

## Future opportunity (not required; bounded stretch — task10)
A fully-fused single kernel (RMS reduction + modulation in one pass) would remove the `normed` write+read (~4 array passes instead of 6 for the staged path), potentially pushing toward ~3x. It requires replicating ATen's exact fp32 RMS reduction order to preserve bit-exactness (the staged path deliberately avoids this risk). Recommended only behind a `normed`-uint16-equality gate and NCU evidence; the staged candidate already satisfies the goal with guaranteed bit-exactness.

## PR scope
Final staged diff contains only kernel code (`baseline/`, `solution/`), the local ABI/adapter + correctness/benchmark harness (`bench/`), and provenance/results notes (`docs/`). Raw benchmark JSON, profiler/NCU artifacts, build dirs, and `__pycache__` are kept local only (`.gitignore`); `.humanize*` is untracked.
