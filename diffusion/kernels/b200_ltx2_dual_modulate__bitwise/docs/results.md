# Results — LTX2 Dual Modulation Bit-Exact B200 Kernel Pair

## Headline

- **12/12 production workloads bit-wise equal** to the PyTorch eager baseline
  (`torch.equal`, atol=rtol=0).
- **Equal-weight geometric mean speedup: 3.54×** over the 12 production rows.
- Arithmetic mean 3.65×, **min 2.42×** (no production shape regresses), max 5.18×.
- Independent-oracle correctness gate: **1819 checks passed, 0 failed** on B200.

## Provenance

- Task: `b200_ltx2_dual_modulate__bitwise` (target NVIDIA B200).
- Host: `innomatrix-us-adc-smb200-0003` (reached via `ion-b200`), container
  `sglang_bbuf_pr29315`.
- GPU: NVIDIA B200, `REMOTE_GPU_ID=5`; **idle before and after** (0% util, 0 MiB used
  before; 0% / 0 MiB after). GPU 6 (also idle) was used only for the multi-GPU
  device-honoring correctness check.
- Toolchain: torch `2.11.0+cu130`, CUDA runtime `13.0`, nvcc `13.0.88`,
  tvm-ffi `0.1.9`, Python `3.12.3`.
- Baseline source: upstream SGLang `main`; the production normalization is
  `torch.nn.functional.rms_norm` (`RMSNormNoWeight.forward_native`). Recovery commit
  `aaa31eb0a11e09f9511bade5e815907ec0b91fa0` (2026-06-28); re-verified unchanged at
  `bb74ed4a8da02b4f142191eedac824471cfb1ec6` (2026-06-29). See `docs/baseline_source.md`.
- Candidate source hash (sha256 of `solution/kernel.cu`):
  `e0d07d4bf06760b5090313b78fdf3dc075bf72d373cd4cd66cac898e7d32716a`.
- Build: `tvm_ffi.cpp.load`, flags `-std=c++17 -O3 -gencode=arch=compute_100,code=sm_100`,
  no `--use_fast_math`; identical builder/flags on baseline and candidate.
- Exact commands (run inside the container, `CUDA_VISIBLE_DEVICES` pins the GPU):
  - Correctness: `CUDA_VISIBLE_DEVICES=5,6 python bench/correctness.py`
  - Benchmark: `CUDA_VISIBLE_DEVICES=5 python bench/benchmark.py --out bench/results.jsonl`
- Raw per-trial samples and full environment provenance are in `bench/results.jsonl`
  (kept local; excluded from the PR per the diffusion artifact rules).

## Per-shape performance (median µs, GPU-event timing)

| Workload | op | x shape | base med | cand med | speedup |
|---|---|---|---|---|---|
| stage1 video | explicit | [2,1536,4096] | 171.73 | 43.56 | 3.94× |
| stage1 audio | explicit | [2,126,2048] | 69.07 | 16.56 | 4.17× |
| stage2 video | explicit | [1,6144,4096] | 287.34 | 79.02 | 3.64× |
| stage2 audio | explicit | [1,126,2048] | 68.60 | 16.90 | 4.06× |
| stage1 video | CA-from-temb | [2,1536,4096] | 177.16 | 66.55 | 2.66× |
| stage1 audio | CA-from-temb | [2,126,2048] | 81.15 | 15.66 | 5.18× |
| stage2 video | CA-from-temb | [1,6144,4096] | 296.13 | 122.24 | 2.42× |
| stage2 audio | CA-from-temb | [1,126,2048] | 77.70 | 15.62 | 4.97× |
| HQ stage1 video | explicit | [1,8160,4096] | 393.74 | 101.68 | 3.87× |
| HQ stage2 video | explicit | [1,32640,4096] | 1471.42 | 373.28 | 3.94× |
| HQ stage1 video | CA-from-temb | [1,8160,4096] | 402.75 | 160.58 | 2.51× |
| HQ stage2 video | CA-from-temb | [1,32640,4096] | 1504.77 | 608.10 | 2.47× |

Geomean **3.54×**, arithmetic mean 3.65×, min 2.42×, max 5.18×. No production shape
family regresses; a single generic kernel pair wins on every bucket, so no per-shape
dispatch is required (the only fallback is alignment-based — see `docs/dispatch.md`).

### Full distribution (µs; b=baseline, c=candidate: median/mean/std/min/p10/p90)

| Workload | baseline med/mean/std/min/p10/p90 | candidate med/mean/std/min/p10/p90 |
|---|---|---|
| s1536 video explicit | 171.73/171.95/0.59/171.49/171.56/172.58 | 43.56/43.58/0.07/43.49/43.51/43.66 |
| s126 audio explicit | 69.07/70.25/2.92/67.62/67.65/74.15 | 16.56/17.02/1.59/15.99/16.01/18.56 |
| s6144 video explicit | 287.34/288.04/1.53/285.96/286.62/289.85 | 79.02/79.15/0.25/78.89/78.92/79.42 |
| s126 audio explicit (st2) | 68.60/69.61/2.30/67.28/67.60/72.64 | 16.90/16.87/0.33/16.48/16.48/17.23 |
| s1536 video temb | 177.16/177.65/1.03/176.76/176.88/179.09 | 66.55/66.58/0.16/66.32/66.45/66.79 |
| s126 audio temb | 81.15/81.67/2.21/79.05/79.40/83.98 | 15.66/15.73/0.25/15.47/15.49/15.99 |
| s6144 video temb | 296.13/296.25/2.55/292.53/293.80/298.52 | 122.24/122.23/0.32/121.92/121.93/122.63 |
| s126 audio temb (st2) | 77.70/79.10/2.41/76.88/77.22/82.24 | 15.62/15.80/0.47/15.35/15.42/16.43 |
| s8160 video explicit | 393.74/394.03/1.39/392.49/392.59/395.82 | 101.68/101.55/0.25/101.23/101.28/101.77 |
| s32640 video explicit | 1471.42/1477.48/12.48/1468.16/1469.31/1491.69 | 373.28/373.15/1.63/370.11/371.51/374.76 |
| s8160 video temb | 402.75/403.59/3.40/400.73/401.32/406.83 | 160.58/160.45/0.43/159.84/159.87/160.86 |
| s32640 video temb | 1504.77/1502.71/9.88/1488.51/1489.51/1512.43 | 608.10/612.13/8.13/604.29/605.78/623.50 |

## Correctness

`bench/correctness.py` (independent pure-PyTorch oracle, not imported from `baseline/`)
passes **1819/0** on B200, covering: all 12 production rows built with their exact frozen
shapes AND strides (including the non-compact `[B,1,D]` batch stride `4·D` and the HQ
`S=8160`/`S=32640` rows); the canonical regression grid `B∈{1,2,4} × S∈{6,33,128,257} ×
D∈{512,1024,1536,3072}` crossed with uniform and all 81 independent mixed
`{[B,D],[B,1,D],[B,S,D]}` param layouts; the CA grid crossed with table dtype
`{bf16,fp32}` and `temb_seq∈{1,S}`; padded (non-compact) tables; the `D=8192` boundary;
same-seed reproducibility; NaN-poison skipped-kernel detection; identical rejection
(non-CUDA / non-bf16 / non-contiguous / `D` not ÷256 / `D>8192` / param mismatch /
non-compact outputs / non-contiguous temb — both baseline and candidate raise); the
multi-GPU device-guard test (candidate correct on a non-current device, raises on a
cross-device output); and the alignment-based scalar fallback (forced with a deliberately
misaligned non-16-byte compact output, so both the vectorized and scalar paths are
verified bit-exact).

## Design and numerics

Strategy A: reuse ATen `at::rms_norm` for the normalization so `normed` is bit-identical
to the eager `F.rms_norm` by construction, then a single fused CUDA kernel applies both
affines in one pass over `normed`, writing `y0` and `y1`. The affine reproduces the three
PyTorch-visible bf16 rounding points (`1+scale` → bf16, `·normed` → bf16, `+shift` → bf16)
with explicit `__fadd_rn`/`__fmul_rn`/`__float2bfloat16_rn` (no FMA contraction, no
single-shot fp32 collapse, no native bf16 operators). The CA path derives scale/shift
inline from `scale_shift_table.to(bf16)` (fp32 table rounded to bf16 first) `+ temb`,
honoring the table row stride and `temb_seq∈{1,S}`. The dominant compact traffic
(`normed` read, `y0`/`y1` writes) moves in 16-byte vectors (8 bf16/thread); the
per-element arithmetic is unchanged, so the vectorized and scalar paths are bit-identical.
Independent numerics review (Codex `gpt-5.5:xhigh`) confirmed exact eager parity on all
points; see `docs/rms_norm_numerics.md`.

## Roofline / NCU analysis (active bound)

The candidate call is `at::rms_norm` (shared with the baseline) + the fused affine kernel.
GPU-event split on the huge `S=32640` explicit row (boost clocks):

- `rms_norm`: 82 µs, ≈6510 GB/s ≈ **81% of HBM peak** — already near the memory roofline;
  Strategy A cannot improve it (it is the shared, ATen-optimal path).
- fused affine (vectorized): 285 µs, ≈2817 GB/s ≈ 35% of HBM peak — moves
  `normed`(read) + `y0`,`y1`(write) = 6 B/element.

Nsight Compute (`--set basic`) on the vectorized `explicit_affine_kernel_vec`:

- huge video `S=32640`: Memory(L1TEX) Throughput **95.5%**, DRAM Throughput 22.6%,
  Compute(SM) 55.7%, Achieved Occupancy 64.8% → **L1TEX-bound on the scalar broadcast
  param-load instructions** (the params are cached, so DRAM stays low; the load-issue
  rate saturates the memory pipe).
- audio `S=126` (stage1, `[2,126,2048]`): Memory 18.9%, DRAM 2.0%, Occupancy 19.9% →
  **launch/latency-bound** (~0.5M elements). The 4–5× win here comes from collapsing the
  eager path's many kernel launches into `rms_norm` + one fused kernel.

**Conclusion:** correct and target-complete. A single bit-exact kernel pair beats the
eager baseline on every production shape (geomean 3.54×, no regression). The remaining
video headroom (DRAM ~23%) is bounded by L1TEX from the scalar broadcast param loads, not
DRAM bandwidth.

### Documented future direction (not pursued this round)

- Vectorize the broadcast param loads (16-byte `int4`, guarded by a host-side
  stride/alignment check) to relieve the L1TEX bound and convert the video affine toward
  the DRAM roofline. Expected to lift the explicit video rows further; left as a bounded
  follow-up because the current result already exceeds the bar with no regression.
- Strategy B (a fully custom fused RMS+affine) was evaluated and **not pursued**: the gate
  (Strategy A leaving a per-shape gap) is not met — every row already wins ≥2.42× — and a
  custom RMS reduction risks `rstd` bit-exactness (torch-version-sensitive). The RMS-only
  `torch.equal` + `rstd` ULP gate recipe is recorded for any future attempt.
