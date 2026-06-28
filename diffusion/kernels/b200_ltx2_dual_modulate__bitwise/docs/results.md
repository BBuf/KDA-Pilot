# Results — b200_ltx2_dual_modulate__bitwise

## Outcome: PROMOTE (bit-exact + faster on every production row)

The candidate is **bit-for-bit equal** (`torch.equal`, atol=rtol=0) to an independent
PyTorch eager oracle (and to the eager baseline) across all production rows, the
canonical regression grid crossed with the [B,D]/[B,1,D]/[B,S,D] param layouts, the
CA grid crossed with table dtype {bf16,fp32} and `temb_seq in {1,S}`, and the D=8192
boundary, and is **faster on all 8 production workloads** (equal-weight geometric-mean
speedup **2.54×**). Measured under the full-operation TVM-FFI CUDA ABI (both baseline
and candidate take `x`, params/temb/table, scalar `double eps`, outputs last).

## Environment / Provenance
- Host `innomatrix-us-adc-smb200-0003` (ion-b200); container `sglang_bbuf_pr29315`.
- GPU: NVIDIA B200, `REMOTE_GPU_ID=5` (pinned via `CUDA_VISIBLE_DEVICES=5` for build,
  correctness, and benchmark). Idle before (util 0 %, mem 0 MiB) and after
  (util 0 %, mem 4 MiB).
- Toolchain: torch `2.11.0+cu130`, CUDA runtime `13.0`, nvcc `13.0.88`,
  tvm-ffi `0.1.9`, Python `3.12.3`.
- Baseline source: SGLang `main` @ `aaa31eb0a11e09f9511bade5e815907ec0b91fa0`
  (eager `F.rms_norm` via `RMSNormNoWeight`; see `docs/baseline_source.md`).
- Candidate / baseline source hashes (sha256, first 16 hex):
  - `solution/kernel.cu` `49ebc74c9481919f`
  - `baseline/kernel.cu` `c55166119a3bec31`
  - `ltx2_dual_modulate_common.cuh` `e02566064bf820a0`
- Compile flags (symmetric, no `--use_fast_math`): `-std=c++17 -O3`,
  `-gencode=arch=compute_100,code=sm_100`; both built via `tvm_ffi.cpp.load`.

## Correctness
`CUDA_VISIBLE_DEVICES=5 python bench/correctness.py` → **1408 passed, 0 failed**.
Covers: production rows; regression grid (B∈[1,2,4] × S∈[6,33,128,257] ×
D∈[512,1024,1536,3072]) × {[B,D],[B,1,D],[B,S,D]}; CA grid × table {bf16,fp32} ×
`temb_seq∈{1,S}`; D=8192; fixed-seed reproducibility; NaN-poison self-test; and the
unsupported-row rejection matrix (non-CUDA, non-bf16 x, non-contiguous last dim,
D%256≠0, D>8192, hidden mismatch, rank-1 param, wrong batch, wrong seq, bad
table/temb shape) on BOTH baseline and candidate. Candidate and baseline are each
compared to the independent oracle. RMS-only diagnostic (AC-4) holds by construction:
both sides compute `normed` via the same `at::rms_norm` / `F.rms_norm`.

## Per-shape performance (CUDA-event GPU time, 7 trials, inner-loop amplified)

| Workload | baseline median (µs) | candidate median (µs) | speedup |
|---|---|---|---|
| stage1 video explicit [2,1536,4096] | 170.96 | 105.11 | 1.63× |
| stage1 audio explicit [2,126,2048] | 40.75 | 11.33 | 3.60× |
| stage2 video explicit [1,6144,4096] | 286.21 | 180.12 | 1.59× |
| stage2 audio explicit [1,126,2048] | 39.88 | 9.68 | 4.12× |
| stage1 video temb [2,1536,4096] | 175.65 | 109.26 | 1.61× |
| stage1 audio temb [2,126,2048] | 46.41 | 12.34 | 3.76× |
| stage2 video temb [1,6144,4096] | 295.19 | 194.36 | 1.52× |
| stage2 audio temb [1,126,2048] | 74.24 | 14.84 | 5.00× |

- Equal-weight geometric-mean speedup **2.54×**; arithmetic mean 2.85×;
  min 1.52×; max 5.00×. Matched ratio 8/8 = 1.0.

### Full distribution per workload (µs: median / mean / std / min / p10 / p90)
```
stage1 video explicit  BL 170.96/170.80/0.28/170.37/170.42/171.02  CAND 105.11/105.14/0.09/105.02/105.03/105.25
stage1 audio explicit  BL  40.75/ 40.99/0.72/ 40.55/ 40.55/ 41.61  CAND  11.33/ 11.33/0.01/ 11.33/ 11.33/ 11.34
stage2 video explicit  BL 286.21/285.93/1.22/284.54/284.54/287.20  CAND 180.12/179.98/0.27/179.46/179.66/180.20
stage2 audio explicit  BL  39.88/ 40.23/0.87/ 39.73/ 39.76/ 41.04  CAND   9.68/  9.70/0.09/  9.58/  9.61/  9.81
stage1 video temb      BL 175.65/175.65/0.15/175.37/175.52/175.79  CAND 109.26/109.21/0.14/109.01/109.04/109.33
stage1 audio temb      BL  46.41/ 46.61/0.47/ 46.21/ 46.25/ 47.24  CAND  12.34/ 12.34/0.01/ 12.32/ 12.33/ 12.35
stage2 video temb      BL 295.19/294.84/1.04/293.42/293.55/295.89  CAND 194.36/194.51/0.22/194.31/194.33/194.74
stage2 audio temb      BL  74.24/ 74.91/1.58/ 73.34/ 73.73/ 77.17  CAND  14.84/ 14.80/0.21/ 14.44/ 14.56/ 14.99
```
Raw samples are in `bench/results.jsonl` (kept local as evidence; excluded from the PR).

## Roofline-style explanation (why it wins; NCU not required — clear win)
The operation is memory-bound bf16 elementwise. Both sides compute the same
`at::rms_norm` (the shared RMS pass); the eager baseline then materializes several
full `[B,S,D]` intermediates (`1+scale`, `normed*…`, `+shift`, ×2 outputs) across
separate ATen elementwise launches, while the candidate fuses the dual affine (and,
for the temb path, the scale/shift derivation) into a single pass that reads `normed`
once and writes both outputs — eliminating the intermediate read/write traffic and
the extra launches.

Two regimes:
- Small audio rows (`S=126`): launch/latency-bound. The baseline issues several small
  ATen elementwise kernels; the candidate collapses the affine to one → **3.6–5.0×**.
- Large video rows (`S∈{1536,6144}`, D=4096): bandwidth-bound. Both are dominated by
  the shared RMS pass plus HBM traffic; the candidate saves the affine intermediates
  → **1.52–1.63×**. The largest row [1,6144,4096] (~25.2M elements) fused affine moves
  ≈150 MB (read `normed` + write `y0`,`y1`), a few tens of µs at B200 HBM bandwidth,
  consistent with the 180–194 µs candidate totals that also include the shared RMS pass.

Strategy B (a single kernel that also performs the RMS reduction) was assessed and
**not pursued**: `docs/rms_norm_numerics.md` shows PyTorch's vectorized fused RMS
reduction is not reproducible bit-for-bit by a naive kernel reduction, so folding RMS
into the kernel would jeopardize the bitwise contract for, at best, eliminating one
shared RMS pass. Strategy A already wins on every row.

## Exact commands
```bash
CUDA_VISIBLE_DEVICES=5 python bench/correctness.py
CUDA_VISIBLE_DEVICES=5 python bench/benchmark.py \
  --workloads bench/workloads.json --out bench/results.jsonl \
  --num-trials 7 --warmup-runs 10 --inner-iterations-min 1 \
  --inner-iterations-max 2048 --target-sample-us 1000 \
  --timeout-seconds 900 --atol 0 --rtol 0
```
