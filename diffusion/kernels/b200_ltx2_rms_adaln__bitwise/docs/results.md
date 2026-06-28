# Results — b200_ltx2_rms_adaln__bitwise

## Outcome: PROMOTE (bit-exact, ~1.96x geomean speedup over PyTorch eager)

The staged candidate is **bit-wise equal** to the PyTorch eager baseline on every
production row and the full regression grid, and is **~1.96x faster** on all four
production workloads on NVIDIA B200.

## Correctness (zero tolerance)
- `bench/correctness.py --impl both`: **69/69 rows PASS (bitwise)** on NVIDIA B200.
  Comparison = raw `uint16` storage equality + `torch.equal`, `atol=rtol=0`.
  Coverage:
  - 4 production rows;
  - canonical adapted grid (CuTe DSL Norm Scale Shift contract `(1,1024,8,3072)`/`(4,512,16,3072)` flattened to rank-3 `x=[B,S*F,D]` → `[1,8192,3072]`/`[4,8192,3072]`), all supported layouts `[D]`/`[B,D]`/`[B,1,D]`/`[B,S*F,D]` + mixed scale/shift;
  - smoke rows; adversarial bf16 rounding-boundary rows; poison self-test;
  - out-of-gate: fp16/fp32/scalar/`1SD`/`11D`/non-contiguous/CPU/bad-D → eager-fallback bit-exact; **BF1D non-divisible** (`x=[1,1000,3072]`, scale/shift `[1,7,1,3072]`, `S%F!=0`) and **CUDA-x + CPU-scale device mismatch** → controlled rejection; raw kernel fails closed on every out-of-gate row.
- Baseline (ATen eager), candidate, and an independent eager oracle all match bit-for-bit.

## Performance (NVIDIA B200, GPU id 6, idle)

Primary metric: `baseline_median_us / candidate_median_us`; headline = equal-weight geometric mean over the 4 production rows.

| Workload | x shape | baseline median (µs) | candidate median (µs) | candidate std (µs) | speedup |
|----------|---------|----------------------|------------------------|--------------------|---------|
| ltx23_stage1_video_s1536_d4096_full | [2,1536,4096] | 57.584 | 28.994 | 0.023 | 1.986x |
| ltx23_stage1_audio_s126_d2048_full | [2,126,2048] | 37.240 | 19.176 | 0.285 | 1.942x |
| ltx23_stage2_video_s6144_d4096_full | [1,6144,4096] | 106.680 | 54.164 | 0.172 | 1.970x |
| ltx23_stage2_audio_s126_d2048_full | [1,126,2048] | 36.903 | 18.854 | 0.260 | 1.957x |

- **Geometric-mean speedup: 1.964x** (arithmetic mean 1.964x; min 1.942x; max 1.986x). All 4 PASSED the bitwise gate before timing.
- Timing: standalone template, isolated subprocess runner, 7 trials, CUDA-event inner-loop amplification (~1000µs samples), interleaved A/B. Full samples + mean/min/p10/p90 in the result JSON (kept local, not staged). An earlier run measured geomean 2.009x; the ~1.96–2.0x band is run-to-run variance on the shared box (GPU 6 isolated and idle for both).

## NCU-backed analysis (task12 — `profile/staged_20260629/REPORT.md`)

NCU on the candidate's `rms_adaln_modulation_kernel` (the shared `at::rms_norm` step excluded by `-k`):

| | Video `[1,6144,4096]` | Audio `[2,126,2048]` |
|---|---:|---:|
| Modulation-kernel duration | 45.76 µs | 7.26 µs |
| DRAM read / write | 151.0 / 29.3 MB | 3.1 / ~0 MB |
| DRAM throughput (% peak) | **51.4 %** (~3.9 TB/s of ~8 TB/s) | 5.6 % |
| Achieved occupancy | 60.2 % | 20.3 % |

- **Video: memory-bound.** The modulation kernel reads `normed + scale + shift` (≈ 3 × 50.3 MB) and is the dominant cost (~45.8 µs of the ~54 µs candidate). The ~2× end-to-end win comes from collapsing eager's three elementwise modulation launches + two full-size temporaries into this one fused pass. Active bound: HBM bandwidth; ~51 % of peak leaves headroom for an optional future memory-tuning pass (must re-pass the bitwise gate).
- **Audio: launch/latency-bound.** Only 252 blocks on 148 SMs (20 % occupancy, 5.6 % DRAM); the problem is too small to saturate the GPU, so the ~2× there is launch-overhead reduction (1 fused kernel vs 3 elementwise launches).

## Candidate-direction decision (task10 — `docs/dispatch.md`)
- **Selected: staged** (shared `at::rms_norm` + fused modulation) — bit-exact + ~1.96x.
- **NO-GO: fully-fused single kernel.** The `bench/probe_fused.py` bounded attempt shows a custom single-kernel fp32 RMS reduction does **not** reproduce `at::rms_norm`'s `normed` bf16 bits (43–248 elements differ per large row, ~0.0002 %, 1 ULP). A fused kernel therefore cannot be bit-exact; the staged path is the production choice.

## Bit-exactness design (why it is safe)
- Stage 1 reuses the **same** `at::rms_norm(x,{D},{},eps)` as the baseline → `normed` bits identical by construction (no reduction-order matching; see `docs/numerics_notes.md`).
- Stage 2 reproduces eager's three rounding points exactly with `__float2bfloat16_rn` after `1+scale`, after the multiply, after the add (PyTorch fp32-opmath + RNE bf16 store). No `--use_fast_math`; discrete rounds prevent FMA contraction.
- A 2D `[B,D]` scale/shift is applied as `[B,1,D]` (per-(batch,channel) over the sequence) in the kernel (PERBATCH mode), the ATen baseline, and the oracle — see `docs/baseline_source.md`.

## Environment / provenance
- Host `ion-b200` (innomatrix-us-adc-smb200-0003), container `sglang_bbuf`, GPU id **6**, NVIDIA B200. GPU 6 idle before (0% util, ~0 MiB) and after (0% util, ~0 MiB) for both correctness and benchmark — see `docs/run_log.md`.
- torch 2.12.1+cu130, CUDA 13.0, tvm_ffi 0.1.9, nvcc CUDA 13.0, cc (gcc) 13.3.0.
- Compile flags (symmetric, both sides): `-std=c++17 -O3 -gencode=arch=compute_100,code=sm_100`, torch linkage, **no `--use_fast_math`**.
- Baseline upstream commit: `aaa31eb0a11e09f9511bade5e815907ec0b91fa0` (SGLang `main`). Candidate `solution/kernel.cu` sha256: `39e243ed62581364a87f7de2cf86f4a3b47367305963de1853517997520041ef`.

## PR scope
Final staged diff contains kernel code (`baseline/`, `solution/`), local ABI/adapter + correctness/benchmark/probe harness (`bench/`), provenance/results/dispatch/numerics notes + the curated NCU `profile/staged_20260629/REPORT.md`. Raw NCU `.ncu-rep`, benchmark JSON, build dirs, and `__pycache__` are kept local only (`.gitignore`); `.humanize*` is untracked.
