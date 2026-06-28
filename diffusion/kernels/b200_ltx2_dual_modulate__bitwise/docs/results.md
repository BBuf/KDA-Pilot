# Results — b200_ltx2_dual_modulate__bitwise

## Outcome: PROMOTE (bit-exact + faster on every production row)

The candidate is **bit-for-bit equal** (`torch.equal`, atol=rtol=0) to the PyTorch
eager baseline across all production rows, the canonical regression grid, the fp32
`scale_shift_table` path, `temb_seq in {1, S}`, and all explicit param layouts, and
is **faster on all 8 production workloads** (equal-weight geometric-mean speedup
**2.55×**).

## Environment / Provenance
- Host: `innomatrix-us-adc-smb200-0003` (ion-b200); container `sglang_bbuf_pr29315`
  (the same container that captured `bench/workloads.json`).
- GPU: NVIDIA B200, `REMOTE_GPU_ID=5` (pinned via `CUDA_VISIBLE_DEVICES=5` for build,
  correctness, and benchmark). Idle before (util 0 %, mem 0 MiB) and after
  (util 0 %, mem 4 MiB).
- Toolchain: torch `2.11.0+cu130`, CUDA runtime `13.0`, nvcc `13.0.88`,
  tvm-ffi `0.1.9`, Python `3.12.3`.
- Baseline source: SGLang `main` @ `aaa31eb0a11e09f9511bade5e815907ec0b91fa0`
  (eager `F.rms_norm` via `RMSNormNoWeight`; see `docs/baseline_source.md`).
- Candidate source: `solution/kernel.cu` (fused affine) + PyTorch `F.rms_norm`.
- Compile flags (symmetric, no `--use_fast_math`): `-std=c++17 -O3`,
  `-gencode=arch=compute_100,code=sm_100`.

## Correctness
`CUDA_VISIBLE_DEVICES=5 python bench/correctness.py` → **227 passed, 0 failed**.
Covers: 8 production rows, regression grid (B∈[1,2,4] × S∈[6,33,128,257] ×
D∈[512,1024,1536,3072]), explicit param layouts ([B,D]/[B,1,D]/[B,S,D]), fp32 and
bf16 `scale_shift_table`, `temb_seq ∈ {1, S}`, NaN-poison self-test (skipped-kernel
detection), and unsupported-row rejection (non-bf16 x, D%256≠0, D>8192, param hidden
mismatch). RMS-only diagnostic (AC-4) holds by construction: the candidate computes
`normed` with the same `F.rms_norm` as the baseline.

## Per-shape performance (CUDA-event GPU time, 7 trials, inner-loop amplified)

| Workload | baseline median (µs) | candidate median (µs) | speedup | bl p10/p90 | cand p10/p90 |
|---|---|---|---|---|---|
| stage1 video explicit [2,1536,4096] | 152.42 | 105.30 | 1.45× | 152.26/152.60 | 105.21/105.33 |
| stage1 audio explicit [2,126,2048] | 72.34 | 17.55 | 4.12× | 71.27/72.51 | 17.36/18.19 |
| stage2 video explicit [1,6144,4096] | 268.94 | 180.39 | 1.49× | 268.11/269.54 | 179.95/180.76 |
| stage2 audio explicit [1,126,2048] | 71.98 | 17.48 | 4.12× | 70.73/73.13 | 17.29/17.63 |
| stage1 video temb [2,1536,4096] | 157.00 | 109.58 | 1.43× | 156.33/157.78 | 109.41/109.67 |
| stage1 audio temb [2,126,2048] | 80.80 | 16.00 | 5.05× | 78.41/83.31 | 15.87/16.61 |
| stage2 video temb [1,6144,4096] | 265.46 | 194.56 | 1.36× | 264.24/266.47 | 194.16/194.98 |
| stage2 audio temb [1,126,2048] | 84.80 | 17.38 | 4.88× | 79.22/93.10 | 15.69/18.94 |

- Equal-weight geometric-mean speedup: **2.546×**; arithmetic mean 2.99×;
  min 1.36×; max 5.05×. Matched ratio 8/8 = 1.0.
- Full median/mean/std/min/p10/p90 and raw samples are in `bench/results.jsonl`
  (kept local as evidence; excluded from the PR).

## Roofline-style explanation (why it wins; NCU not required — clear win)
The operation is memory-bound bf16 elementwise: per output element the affine reads
`normed` (2 B) + broadcast params and writes `y0`+`y1` (4 B). The eager baseline
materializes many full `[B,S,D]` intermediates (`1+scale`, `normed*…`, `+shift`, ×2
outputs) across separate kernel launches; the candidate fuses the dual affine (and,
for the temb path, the scale/shift derivation) into a single pass that reads
`normed` once and writes both outputs, eliminating the intermediate read/write
traffic and the extra launches. RMS (`F.rms_norm`) is shared by both sides.

Two regimes are visible:
- Small audio rows (`S=126`): launch/latency-bound. The baseline issues ~6+ small
  elementwise kernels; the candidate collapses them to one → **4.1–5.1×**.
- Large video rows (`S∈{1536,6144}`, D=4096): bandwidth-bound. Both sides are
  dominated by the shared `F.rms_norm` plus HBM traffic; the candidate saves the
  affine intermediates → **1.36–1.49×**. For the largest row [1,6144,4096] (~25.2M
  elements) the fused affine moves ≈150 MB (read `normed` + write `y0`,`y1`), a few
  tens of µs at B200 HBM bandwidth, consistent with the 180–195 µs candidate total
  that also includes the shared RMS pass.

Strategy B (a single kernel that also performs the RMS reduction) was assessed and
**not pursued**: `docs/rms_norm_numerics.md` shows PyTorch's vectorized fused RMS
reduction is not reproducible bit-for-bit by a naive kernel reduction, so folding
RMS into the kernel would jeopardize the bitwise contract for, at best, the
elimination of one shared RMS pass. Strategy A already wins on every row.

## Exact commands
```bash
# build + correctness (GPU 5)
CUDA_VISIBLE_DEVICES=5 python bench/correctness.py
# benchmark (GPU 5)
CUDA_VISIBLE_DEVICES=5 python bench/benchmark.py \
  --workloads bench/workloads.json --out bench/results.jsonl \
  --num-trials 7 --warmup-runs 10 --inner-iterations-min 1 \
  --inner-iterations-max 2048 --target-sample-us 1000 \
  --timeout-seconds 900 --atol 0 --rtol 0
```
