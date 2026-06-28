# Results — b200_ltx2_dual_modulate__bitwise

## Outcome: PROMOTE (bit-exact + faster on every production row)

The candidate is **bit-for-bit equal** (`torch.equal`, atol=rtol=0) to an independent
PyTorch eager oracle (and to the eager baseline) across all production rows, the
canonical regression grid crossed with uniform AND every independent mix of the
[B,D]/[B,1,D]/[B,S,D] param layouts, the CA grid crossed with table dtype {bf16,fp32}
and `temb_seq∈{1,S}`, padded (non-compact, last-dim-contiguous) tables, and the
D=8192 boundary, and is **faster on all 8 production workloads** (equal-weight
geometric-mean speedup **2.69×**). Measured under the full-operation TVM-FFI CUDA ABI
(both baseline and candidate take `x`, params/temb/table, scalar `double eps`,
outputs last).

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
  - `solution/kernel.cu` `551758b5473eff80`
  - `baseline/kernel.cu` `2bf63b76bcc0d6cf`
  - `ltx2_dual_modulate_common.cuh` `3bcbdf2eadf8d4a0`
- Compile flags (symmetric, no `--use_fast_math`): `-std=c++17 -O3`,
  `-gencode=arch=compute_100,code=sm_100`; both built via `tvm_ffi.cpp.load`.
- Raw benchmark artifact: `bench/results.jsonl` (gitignored; present locally for
  audit) — 10 lines (1 provenance + 8 result + 1 summary), sha256
  `22184da0c16cc5eb…`.

## Correctness
`CUDA_VISIBLE_DEVICES=5 python bench/correctness.py` → **1754 passed, 0 failed**.
Covers: production rows; regression grid (B∈[1,2,4] × S∈[6,33,128,257] ×
D∈[512,1024,1536,3072]) × uniform {[B,D],[B,1,D],[B,S,D]}; the 81 independent
mixed-layout combinations (+ a production-sized mixed row); CA grid × table
{bf16,fp32} × `temb_seq∈{1,S}`; padded (non-compact, last-dim-contiguous) bf16/fp32
tables; D=8192; fixed-seed reproducibility; NaN-poison self-test; and the
unsupported-row rejection matrix (non-CUDA, non-bf16 x, non-contiguous last dim,
D%256≠0, D>8192, hidden mismatch, rank-1 param, wrong batch, wrong seq, bad
table/temb shape, **non-compact temb**) on BOTH baseline and candidate. Candidate and
baseline are each compared to the independent oracle. RMS-only diagnostic (AC-4)
holds by construction: both sides compute `normed` via the same `at::rms_norm` /
`F.rms_norm`.

## Per-shape performance (CUDA-event GPU time, 7 trials, inner-loop amplified)

| Workload | baseline median (µs) | candidate median (µs) | speedup |
|---|---|---|---|
| stage1 video explicit [2,1536,4096] | 171.50 | 109.59 | 1.57× |
| stage1 audio explicit [2,126,2048] | 65.37 | 15.48 | 4.22× |
| stage2 video explicit [1,6144,4096] | 287.46 | 188.28 | 1.53× |
| stage2 audio explicit [1,126,2048] | 39.88 | 9.60 | 4.15× |
| stage1 video temb [2,1536,4096] | 176.79 | 110.43 | 1.60× |
| stage1 audio temb [2,126,2048] | 78.40 | 14.89 | 5.27× |
| stage2 video temb [1,6144,4096] | 294.23 | 194.41 | 1.51× |
| stage2 audio temb [1,126,2048] | 75.45 | 14.85 | 5.08× |

- Equal-weight geometric-mean speedup **2.69×**; arithmetic mean 3.12×;
  min 1.51×; max 5.27×. Matched ratio 8/8 = 1.0.

### Full distribution per workload (µs: median / mean / std / min / p10 / p90)
```
stage1 video explicit  BL 171.50/171.57/0.28/171.19/171.31/171.86  CAND 109.59/109.59/0.08/109.45/109.51/109.69
stage1 audio explicit  BL  65.37/ 65.39/0.30/ 65.00/ 65.04/ 65.74  CAND  15.48/ 15.53/0.21/ 15.33/ 15.34/ 15.78
stage2 video explicit  BL 287.46/286.98/1.56/284.59/284.89/288.35  CAND 188.28/188.32/0.27/187.98/188.06/188.60
stage2 audio explicit  BL  39.88/ 40.04/0.79/ 39.43/ 39.51/ 40.67  CAND   9.60/  9.58/0.07/  9.45/  9.50/  9.66
stage1 video temb      BL 176.79/176.80/0.31/176.38/176.47/177.18  CAND 110.43/110.49/0.47/109.80/110.03/111.07
stage1 audio temb      BL  78.40/ 77.53/1.98/ 74.31/ 74.91/ 79.23  CAND  14.89/ 15.08/0.55/ 14.50/ 14.58/ 15.67
stage2 video temb      BL 294.23/294.47/1.37/292.79/292.98/296.16  CAND 194.41/194.43/0.23/194.06/194.21/194.68
stage2 audio temb      BL  75.45/ 76.31/1.49/ 74.83/ 75.08/ 78.31  CAND  14.85/ 14.83/0.24/ 14.48/ 14.57/ 15.08
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
  ATen elementwise kernels; the candidate collapses the affine to one → **4.2–5.3×**.
- Large video rows (`S∈{1536,6144}`, D=4096): bandwidth-bound. Both are dominated by
  the shared RMS pass plus HBM traffic; the candidate saves the affine intermediates
  → **1.51–1.60×**. The largest row [1,6144,4096] (~25.2M elements) fused affine moves
  ≈150 MB (read `normed` + write `y0`,`y1`), a few tens of µs at B200 HBM bandwidth,
  consistent with the ~188–194 µs candidate totals that also include the shared RMS pass.

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
