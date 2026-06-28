# Results — b200_ltx2_dual_modulate__bitwise

## Outcome: PROMOTE (bit-exact + faster on every production row)

The candidate is **bit-for-bit equal** (`torch.equal`, atol=rtol=0) to an independent
PyTorch eager oracle (and to the eager baseline) across all production rows, the
canonical regression grid crossed with uniform AND every independent mix of the
[B,D]/[B,1,D]/[B,S,D] param layouts, the CA grid crossed with table dtype {bf16,fp32}
and `temb_seq∈{1,S}`, padded (non-compact, last-dim-contiguous) tables, and the
D=8192 boundary, and is **faster on all 8 production workloads** (equal-weight
geometric-mean speedup **2.66×**). Measured under the full-operation TVM-FFI CUDA ABI
(both baseline and candidate take `x`, params/temb/table, scalar `double eps`,
compact outputs last).

## Environment / Provenance (matches bench/results.jsonl exactly)
- Host `innomatrix-us-adc-smb200-0003` (ion-b200); container `sglang_bbuf_pr29315`.
- GPU: NVIDIA B200, `REMOTE_GPU_ID=5` (pinned via `CUDA_VISIBLE_DEVICES=5` for build,
  correctness, and benchmark). Per the recorded artifact, GPU 5 was idle both
  **before** the run (`0 %, 4 MiB / 183359 MiB`) and **after** (`0 %, 4 MiB /
  183359 MiB`) — 0 % utilization, no compute processes (the 4 MiB is the idle CUDA
  context).
- Toolchain: torch `2.11.0+cu130`, CUDA runtime `13.0`, nvcc `13.0.88`,
  tvm-ffi `0.1.9`, Python `3.12.3`.
- Baseline source: SGLang `main` @ `aaa31eb0a11e09f9511bade5e815907ec0b91fa0`
  (eager `F.rms_norm` via `RMSNormNoWeight`; see `docs/baseline_source.md`).
- Candidate / baseline source hashes (sha256):
  - `solution/kernel.cu` `551758b5473eff80526fc2b62373b46d85e0524085d039a1e2c4ff66dfd777d2`
  - `baseline/kernel.cu` `2bf63b76bcc0d6cf2fadc2d8cb124335e770f354e460e6cab932eacf04f66b13`
  - `ltx2_dual_modulate_common.cuh` `b74d0617960cb3c11470b334f69fc90539a28cdd5d81e0de2967dead0ad74ba7`
- Compile flags (symmetric, no `--use_fast_math`): `-std=c++17 -O3`,
  `-gencode=arch=compute_100,code=sm_100`; both built via `tvm_ffi.cpp.load`.
- Raw benchmark artifact: `bench/results.jsonl` (gitignored; present locally for
  audit) — 10 lines (1 provenance + 8 result + 1 summary), sha256
  `f620923a6b3eb1ae975292a58e56399de669f605325f02676005bcbabfe2270c`.

## Correctness
`CUDA_VISIBLE_DEVICES=5 python bench/correctness.py` → **1762 passed, 0 failed**.
Covers: production rows; regression grid (B∈[1,2,4] × S∈[6,33,128,257] ×
D∈[512,1024,1536,3072]) × uniform {[B,D],[B,1,D],[B,S,D]}; the 81 independent
mixed-layout combinations (+ a production-sized mixed row); CA grid × table
{bf16,fp32} × `temb_seq∈{1,S}`; padded (non-compact, last-dim-contiguous) bf16/fp32
tables; D=8192; fixed-seed reproducibility; NaN-poison self-test; and the
unsupported-row rejection matrix (non-CUDA, non-bf16 x, non-contiguous last dim,
D%256≠0, D>8192, hidden mismatch, rank-1 param, wrong batch, wrong seq, bad
table/temb shape, non-compact temb, **non-compact y0/y1**) on BOTH baseline and
candidate. Candidate and baseline are each compared to the independent oracle. The
RMS-only diagnostic (AC-4) holds by construction: both sides compute `normed` via the
same `at::rms_norm` / `F.rms_norm`.

## Per-shape performance (CUDA-event GPU time, 7 trials, inner-loop amplified)

| Workload | baseline median (µs) | candidate median (µs) | speedup |
|---|---|---|---|
| stage1 video explicit [2,1536,4096] | 171.68 | 109.63 | 1.57× |
| stage1 audio explicit [2,126,2048] | 65.64 | 15.76 | 4.16× |
| stage2 video explicit [1,6144,4096] | 287.30 | 188.54 | 1.52× |
| stage2 audio explicit [1,126,2048] | 39.94 | 9.72 | 4.11× |
| stage1 video temb [2,1536,4096] | 177.41 | 110.58 | 1.60× |
| stage1 audio temb [2,126,2048] | 75.54 | 14.97 | 5.05× |
| stage2 video temb [1,6144,4096] | 291.48 | 193.63 | 1.51× |
| stage2 audio temb [1,126,2048] | 74.51 | 14.63 | 5.09× |

- Equal-weight geometric-mean speedup **2.66×**; arithmetic mean 3.08×;
  min 1.51×; max 5.09×. Matched ratio 8/8 = 1.0.

### Full distribution per workload (µs: median / mean / std / min / p10 / p90)
```
stage1 video explicit  BL 171.68/171.69/0.23/171.30/171.47/171.96  CAND 109.63/109.60/0.12/109.43/109.49/109.73
stage1 audio explicit  BL  65.64/ 66.71/1.84/ 65.42/ 65.49/ 68.76  CAND  15.76/ 15.83/0.19/ 15.70/ 15.71/ 16.00
stage2 video explicit  BL 287.30/287.34/1.29/285.64/285.88/288.72  CAND 188.54/188.48/0.17/188.25/188.27/188.65
stage2 audio explicit  BL  39.94/ 40.25/1.08/ 39.60/ 39.66/ 41.12  CAND   9.72/  9.70/0.08/  9.60/  9.60/  9.78
stage1 video temb      BL 177.41/177.45/0.50/176.86/176.89/177.97  CAND 110.58/110.69/0.40/110.22/110.27/111.17
stage1 audio temb      BL  75.54/ 76.58/2.00/ 74.51/ 74.76/ 78.86  CAND  14.97/ 15.04/0.25/ 14.78/ 14.80/ 15.32
stage2 video temb      BL 291.48/291.86/1.45/290.53/290.73/293.59  CAND 193.63/193.67/0.18/193.44/193.48/193.86
stage2 audio temb      BL  74.51/ 74.78/1.25/ 73.68/ 73.75/ 76.12  CAND  14.63/ 14.66/0.29/ 14.39/ 14.41/ 14.98
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
  ATen elementwise kernels; the candidate collapses the affine to one → **4.1–5.1×**.
- Large video rows (`S∈{1536,6144}`, D=4096): bandwidth-bound. Both are dominated by
  the shared RMS pass plus HBM traffic; the candidate saves the affine intermediates
  → **1.51–1.60×**. The largest row [1,6144,4096] (~25.2M elements) fused affine moves
  ≈150 MB (read `normed` + write `y0`,`y1`), a few tens of µs at B200 HBM bandwidth,
  consistent with the ~189–194 µs candidate totals that also include the shared RMS pass.

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
