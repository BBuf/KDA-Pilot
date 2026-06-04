# Dispatch table + promote/no-go — continuation round (tilev1)

Native-CUDA candidates (built via SGLang jit_kernel/tvm-ffi, no `--use_fast_math`)
behind a zero-overhead dispatcher (`src/norm_dispatch.py`) that preserves the two
public callable names and falls back to the SGLang baseline for any unsupported
signature.

> **Historical note**: the previously promoted decision table (normv5, geomean
> **1.4223x**) was measured through the `kda_kernels.install()` overlay
> (plain-callable monkey-patch) and is **historical overlay evidence — not
> admissible** under the shipping-integration rules added by kernel-pilot
> commit `cc17c1149` (symmetric topology, registration preservation,
> device-vs-host decomposition). It is superseded by the symmetric numbers
> below. Lineage: `solutions.jsonl` ids `continuation_pr25_audit` → `tilev1`.

## Kernels (tilev1)

- `triton_one_pass_rms_norm` → `rms_norm_tile<128,8,128,false,false,bf16>`
  (`src/rms_norm_d128_tile16.cuh`): one 8x128 tile per 128-thread CTA
  (16 lanes/row, one 128-bit chunk per lane), fp32 sum-of-squares per row,
  grid = ceil(M/8) — the Triton baseline's program-grid structure ported to
  CUDA. Replaces the normv5 persistent warp kernel (`src/rms_norm_d128.cuh`,
  retained unrouted) whose capped 1056-block grid starved memory-level
  parallelism at huge M (NCU: 77.54% vs 83% DRAM).
- `norm_infer` → `layer_norm_block<5120,true,false,float>`
  (`src/layer_norm_n5120.cuh`, byte-unchanged from normv5): one CTA per row,
  256x20 float4 tiling, fp32 two-moment block reduce.

## Decision table (ion8-h200 GPU0, NVIDIA H200, idle-gated; symmetric local legs;
## wall = solo-call median, dev = stream-saturated rate; vs copied Triton baseline @ 84e1108312)

| Bucket | shape | variant | base wall | cand wall | wall x | base dev | cand dev | dev x | active bound | decision |
|---|---|---|---|---|---|---|---|---|---|---|
| LN fp32 | [8640,5120] | layer_norm_block | 110.69 | 103.23 | 1.072 | 91.04 | 89.48 | 1.017 | HBM (NCU 79.8% ≈ base 79.7%) | **promote** (device parity at bound + admissible host win) |
| RMS huge | [648720,128] | rms_norm_tile | 104.35 | 94.97 | 1.099 | 82.02 | 81.03 | 1.012 | HBM (NCU cand 82.67% vs base 82.17%; identical 77.66us single-launch) | **promote** (device parity-plus at bound) |
| RMS huge | [650040,128] | rms_norm_tile | 104.21 | 94.77 | 1.100 | 82.19 | 81.28 | 1.011 | HBM | **promote** |
| RMS small | [1320,128] | rms_norm_tile | 25.72 | 16.00 | 1.607 | 19.09 | 9.25 | 2.065 | launch/enqueue rate (kernel ~3.2us, <8% DRAM) | **promote** (host/launcher win, decomposed per DEC-2) |
| RMS small | [16384,128] | rms_norm_tile | 26.12 | 17.03 | 1.534 | 19.08 | 9.24 | 2.064 | launch/enqueue rate | **promote** |
| RMS small | [4096,128] | rms_norm_tile | 25.98 | 16.13 | 1.611 | 18.98 | 9.29 | 2.044 | launch/enqueue rate | **promote** |
| **geomean** | | | | | **1.314** | | | **1.444** | | |

Notes on the columns: `wall` is directly comparable to the locked-baseline
methodology; `dev` is the stream-saturated per-call rate (one CUDA-event pair
around 32 back-to-back enqueues — for long kernels it converges to kernel
duration, for short ones to the enqueue rate limit, i.e. the production
back-to-back throughput view). The copied-baseline leg drops sglang's
custom-op eager shim, so it is LEANER than the production path — these
speedups are conservative (locked real-path small-RMS wall is ~31.5us vs the
copied leg's ~26us). Full per-leg distributions: `benchmark.csv`
(`mode=symmetric_leg`, `candidate_version=tilev1`).

## Roofline (H200 HBM3e 4.8 TB/s peak; ~80-85% practically attainable)

| Bucket | bytes/call | kernel time | achieved BW | % peak | limiter |
|---|---|---|---|---|---|
| LN fp32 [8640,5120] | 354 MB | 85.6us (NCU normv2) | 4.14 TB/s effective (79.8% DRAM sustained) | ~80% | HBM bandwidth (== baseline) |
| RMS huge [648720,128] | 307-309 MB (NCU dram bytes) | 77.66us (NCU, == baseline) | 3.95-3.98 TB/s | 82.2-82.7% | HBM bandwidth (== baseline; prior warp kernel 77.5% closed by tile grid) |
| RMS small [1320..16384,128] | 0.34-8.4 MB | 3.1-3.2us kernel | <8% DRAM | n/a | host launch/enqueue rate (Triton launcher 18.7-19.1us/call saturated vs tvm-ffi 9.2-9.3us/call; solo-call hosts 22.1 vs 10.4us) |

Both legs of every bandwidth-bound bucket sit at the practical HBM bound;
no defensible device headroom remains (the baseline itself caps at ~82-83%).
The launch-bound buckets are limited by the Python/launcher path; the
candidate's tvm-ffi path roughly halves it — claimed as a host win with the
device/host split recorded (DEC-2), never as a kernel-duration win.

## Routing guards (exact; else fall back to SGLang baseline)

- `triton_one_pass_rms_norm` → `rms_norm_tile<128,8,128,false,bf16>` when:
  CUDA, dtype **bf16 only** (fp16 D=128 compiles but is outside the validated
  shape set → baseline), `x.is_contiguous()`, D==128, w is [128] bf16
  contiguous. ALL captured RMS shapes (M 1320..650040) route to the same tile
  kernel — the sweep showed it wins at every captured M, so there is no
  M-threshold split.
- `norm_infer` → `layer_norm_block<5120,true,false,float>` when: CUDA, dtype
  float32, `is_rms_norm=False`, `out is None`, `x.is_contiguous()`, N==5120,
  weight & bias both [N] f32 contiguous.
- The full `x.is_contiguous()` requirement guarantees `reshape(-1,D)` and the
  fresh `empty_like(x)` output are kernel-writable views; merely
  last-dim-contiguous higher-rank inputs fall back to baseline (regression-tested).
- Everything else (CPU/MPS, non-contiguous, other dtype/N/D, `is_rms_norm=True`
  on `norm_infer`, missing weight/bias) → SGLang baseline.

## Promote/no-go rationale (geomean = outcome metric per DEC-4)

- **Promote tilev1.** Per-shape: the three bandwidth-bound buckets are at the
  HBM bound with device parity-or-better (NCU-confirmed identical duration on
  the decision shape); the three launch-bound buckets win 1.53-1.61x wall via
  the leaner launcher (admissible per DEC-2, decomposed). No shape regresses
  on either wall or saturated device rate — the normv5 huge-RMS device
  regression (0.907x) is closed (1.011-1.012x).
- Rejected variants this round (evidence in `solutions.jsonl` id `tilev1` and
  the sweep transcript): tile16x128 / tile16x256 / tile32x256 (slightly slower
  or equal), streaming cache hints `__ldcs/__stcs` (-0.6% device but +1.6%
  wall), PDL (not re-tried: launch-overlap feature with prior negative
  evidence on this family).
- Final promotion arbiter = the in-SGLang dispatch-symmetric env-toggle A/B
  (registration byte-unchanged), recorded in `docs/sglang_jit_export.md`.
