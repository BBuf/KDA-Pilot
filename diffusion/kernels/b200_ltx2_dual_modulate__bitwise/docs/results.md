# Results — b200_ltx2_dual_modulate__bitwise

## Outcome: PROMOTE (bit-exact + faster on every production row)

The candidate is **bit-for-bit equal** (`torch.equal`, atol=rtol=0) to an independent
PyTorch eager oracle (and to the eager baseline) across all production rows, the
canonical regression grid crossed with uniform AND every independent mix of the
[B,D]/[B,1,D]/[B,S,D] param layouts, the CA grid crossed with table dtype {bf16,fp32}
and `temb_seq∈{1,S}`, padded (non-compact, last-dim-contiguous) tables, the D=8192
boundary, and a multi-GPU case (x on a non-current device), and is **faster on all 8
production workloads** (equal-weight geometric-mean speedup **2.65×**). Measured under
the full-operation TVM-FFI CUDA ABI (both baseline and candidate take `x`,
params/temb/table, scalar `double eps`, compact outputs last; the candidate sets a
CUDA device guard to `x`'s device).

## Environment / Provenance (matches bench/results.jsonl exactly)
- Host `innomatrix-us-adc-smb200-0003` (ion-b200); container `sglang_bbuf_pr29315`.
- GPU: NVIDIA B200. The benchmark is pinned to a single GPU, `REMOTE_GPU_ID=5`
  (`CUDA_VISIBLE_DEVICES=5`); correctness was run with `CUDA_VISIBLE_DEVICES=5,6`
  (both idle) to also exercise the multi-GPU device-guard path. Per the benchmark
  artifact, GPU 5 was idle **before** (`0 %, 4 MiB / 183359 MiB`) and **after**
  (`0 %, 4 MiB / 183359 MiB`) — 0 % utilization, no compute processes (the 4 MiB is
  the idle CUDA context).
- Toolchain: torch `2.11.0+cu130`, CUDA runtime `13.0`, nvcc `13.0.88`,
  tvm-ffi `0.1.9`, Python `3.12.3`.
- Baseline source: SGLang `main` @ `aaa31eb0a11e09f9511bade5e815907ec0b91fa0`
  (eager `F.rms_norm` via `RMSNormNoWeight`; see `docs/baseline_source.md`).
- Source hashes (sha256):
  - `solution/kernel.cu` `ba65c199035c409bd36238db2b32c720c91759ea1b9a9d3e92e3eb157e2cea25`
  - `baseline/kernel.cu` `2bf63b76bcc0d6cf2fadc2d8cb124335e770f354e460e6cab932eacf04f66b13`
  - `ltx2_dual_modulate_common.cuh` `61ccae354215df569f0ee93bf2e2b2b088250568d6be3203c0f2164bc12ce01d`
- Compile flags (symmetric, no `--use_fast_math`): `-std=c++17 -O3`,
  `-gencode=arch=compute_100,code=sm_100`; both built via `tvm_ffi.cpp.load`.
- Raw benchmark artifact: `bench/results.jsonl` (gitignored; present locally for
  audit) — 10 lines (1 provenance + 8 result + 1 summary), sha256
  `d2bd989edbc8adfc5310b847cfea78ed9017ce9aec6faf9d79bb3254089a7c23`.

## Correctness
`CUDA_VISIBLE_DEVICES=5,6 python bench/correctness.py` → **1767 passed, 0 failed**.
Covers: production rows; regression grid (B∈[1,2,4] × S∈[6,33,128,257] ×
D∈[512,1024,1536,3072]) × uniform {[B,D],[B,1,D],[B,S,D]}; the 81 independent
mixed-layout combinations (+ a production-sized mixed row); CA grid × table
{bf16,fp32} × `temb_seq∈{1,S}`; padded bf16/fp32 tables; D=8192; reproducibility;
NaN-poison self-test; a **multi-GPU** case (x/params on a non-current device, verifying
the candidate's `CUDAGuard`) + cross-device-output rejection; and the unsupported-row
rejection matrix (non-CUDA, non-bf16 x, non-contiguous last dim, D%256≠0, D>8192,
hidden mismatch, rank-1 param, wrong batch, wrong seq, bad table/temb shape,
non-compact temb, non-compact y0/y1) on BOTH baseline and candidate. Candidate and
baseline are each compared to the independent oracle. The RMS-only diagnostic (AC-4)
holds by construction: both sides compute `normed` via the same `at::rms_norm`.

## Per-shape performance (CUDA-event GPU time, 7 trials, inner-loop amplified)

| Workload | baseline median (µs) | candidate median (µs) | speedup |
|---|---|---|---|
| stage1 video explicit [2,1536,4096] | 171.49 | 109.54 | 1.57× |
| stage1 audio explicit [2,126,2048] | 65.14 | 15.70 | 4.15× |
| stage2 video explicit [1,6144,4096] | 287.74 | 188.19 | 1.53× |
| stage2 audio explicit [1,126,2048] | 65.26 | 15.92 | 4.10× |
| stage1 video temb [2,1536,4096] | 175.40 | 110.13 | 1.59× |
| stage1 audio temb [2,126,2048] | 76.76 | 14.82 | 5.18× |
| stage2 video temb [1,6144,4096] | 294.68 | 194.40 | 1.52× |
| stage2 audio temb [1,126,2048] | 46.27 | 9.62 | 4.81× |

- Equal-weight geometric-mean speedup **2.65×**; arithmetic mean 3.06×;
  min 1.52×; max 5.18×. Matched ratio 8/8 = 1.0. (Small audio rows are latency-bound
  and show more run-to-run baseline variance; the geomean is stable across reruns.)

### Full distribution per workload (µs: median / mean / std / min / p10 / p90)
```
stage1 video explicit  BL 171.49/171.49/0.11/171.35/171.37/171.60  CAND 109.54/109.54/0.10/109.42/109.43/109.64
stage1 audio explicit  BL  65.14/ 66.22/2.21/ 64.48/ 64.51/ 69.39  CAND  15.70/ 15.81/0.28/ 15.53/ 15.55/ 16.18
stage2 video explicit  BL 287.74/287.59/1.02/286.28/286.29/288.70  CAND 188.19/188.34/0.29/188.02/188.08/188.71
stage2 audio explicit  BL  65.26/ 65.76/1.52/ 64.54/ 64.54/ 67.86  CAND  15.92/ 16.04/0.37/ 15.68/ 15.69/ 16.49
stage1 video temb      BL 175.40/175.69/0.55/175.22/175.31/176.28  CAND 110.13/110.23/0.49/109.50/109.74/110.84
stage1 audio temb      BL  76.76/ 77.24/2.17/ 74.75/ 74.83/ 79.57  CAND  14.82/ 14.87/0.12/ 14.73/ 14.77/ 15.04
stage2 video temb      BL 294.68/294.96/1.22/293.50/293.61/296.21  CAND 194.40/194.51/0.33/194.07/194.20/194.92
stage2 audio temb      BL  46.27/ 46.27/0.25/ 45.92/ 46.03/ 46.55  CAND   9.62/  9.65/0.46/  9.18/  9.18/ 10.21
```
Raw per-trial samples are in `bench/results.jsonl` (present locally for audit;
gitignored for PR scope).

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
  ATen elementwise kernels; the candidate collapses the affine to one → **4.1–5.2×**.
- Large video rows (`S∈{1536,6144}`, D=4096): bandwidth-bound. Both are dominated by
  the shared RMS pass plus HBM traffic; the candidate saves the affine intermediates
  → **1.52–1.59×**. The largest row [1,6144,4096] (~25.2M elements) fused affine moves
  ≈150 MB (read `normed` + write `y0`,`y1`), a few tens of µs at B200 HBM bandwidth,
  consistent with the ~188–194 µs candidate totals that also include the shared RMS pass.

Strategy B (a single kernel that also performs the RMS reduction) was assessed and
**not pursued**: `docs/rms_norm_numerics.md` shows PyTorch's vectorized fused RMS
reduction is not reproducible bit-for-bit by a naive kernel reduction, so folding RMS
into the kernel would jeopardize the bitwise contract for, at best, eliminating one
shared RMS pass. Strategy A already wins on every row.

## Exact commands
```bash
# correctness (run with 2 visible GPUs to exercise the multi-GPU device-guard path)
CUDA_VISIBLE_DEVICES=5,6 python bench/correctness.py
# benchmark (single pinned GPU for clean timing)
CUDA_VISIBLE_DEVICES=5 python bench/benchmark.py \
  --workloads bench/workloads.json --out bench/results.jsonl \
  --num-trials 7 --warmup-runs 10 --inner-iterations-min 1 \
  --inner-iterations-max 2048 --target-sample-us 1000 \
  --timeout-seconds 900 --atol 0 --rtol 0
```
