# Results: b200_diffusion_cutedsl_norm_scale_shift__multi_shape

## Headline (run_id=r3-final, shipped configuration)

- **Geometric-mean median-latency speedup over the SGLang CuTe-DSL baseline,
  39 unique captured signatures: 1.2987x end-to-end / 1.2896x device-events**
  (outcome metric per DEC-1/DEC-4; per-case table in `benchmark.csv`,
  aggregation via `python benchmark.py --report --run-id r3-final`).
- Every unique signature >= 1.09x end-to-end; device-mode range 1.00x
  (per-token fp32, at bound — see below) to 1.64x.
- Environment: ion-b200 (innomatrix-us-adc-smb200-0003), container
  sglang_bbuf, idle B200 GPU0 (uuid GPU-a4d97fda…, 0% util / 0 MiB before and
  after every run), torch 2.11.0+cu130, CUDA 13.0, SGLang baseline commit
  edb1b3f8f5. Candidate and baseline interleaved in one process on identical
  pre-built inputs; candidate behind the kda_nss custom-op layer so both sides
  carry the same host registration/dispatch stack (admissibility per AC-5.4).

## Device-vs-host decomposition

- "device" mode = CUDA-event stream-span per call; "endtoend" = wall clock
  with per-sample sync. For stream-saturated (large) cases device ~= kernel
  duration; for host-starved tiny cases device includes issue latency, so NCU
  durations are the kernel-truth there (see profile/r0v1-*/REPORT.md).
- Tiny/small rows (S 19..1004): end-to-end 1.27-1.47x comes from the leaner
  host path (stride-classified dispatch + single tvm-ffi call vs the
  baseline's einops broadcast + 9 dlpack conversions + CuTe-DSL call layer),
  measured through IDENTICAL custom-op layers on both sides — an admissible
  production win, not a registration-dropping artifact. True kernel time for
  these rows is a few microseconds either way (launch/host-bound bucket).
- Large rows: end-to-end and device speedups agree (1.10-1.35x) — device
  kernel wins, host effects negligible.

## Roofline per bucket (device medians at boost clocks; peak HBM ~8 TB/s)

| Bucket | Traffic model | Candidate BW | % peak | Active bound | Verdict |
|---|---|---|---|---|---|
| nss bf16 row-bcast, huge (176400x5120) | 4 B/elem (x rd + y wr; operands L2-resident) = 3.61 GB | 788.8us -> 4.58 TB/s | ~57% | mixed: instruction issue (NCU sm_SOL 66% > mem_SOL 45%) + DRAM | 1.35x over baseline (3.40 TB/s). Remaining gap = convert/epilogue instruction pressure; packed-cvt lever recorded, deprioritized after bounded rounds |
| nss bf16 row-bcast, d3072 (27085) | 4 B/elem = 333 MB | 70.0us -> 4.76 TB/s | ~59% | same as above | 1.51x over baseline |
| srnss bf16 (44100x5120 gnone) | 8 B/elem (x+res rd, y+res_out wr) = 1.81 GB | 274.6us -> 6.58 TB/s | ~82% | DRAM bandwidth | near bound; 1.17x |
| srnss wan affine (37800x5120, gate fp32 + w/b fp32 + scalar sc) | 8 B/elem + row streams = 1.55 GB | 265.4us -> 5.83 TB/s | ~73% | DRAM + fp32 operand latency | 1.32x |
| srnss gnone fp32 row (37800x5120) | 8 B/elem = 1.55 GB | 256.4us -> 6.04 TB/s | ~75% | DRAM | 1.06x (baseline already near bound) |
| nss per-token fp32 (18144x3072) | 12 B/elem (x rd 2B + sc 4B + sh 4B + y wr 2B) = 669 MB | 100.9us -> 6.63 TB/s | ~83% | DRAM (operand streams dominate) | **parity (1.00x) — evidence-backed: both implementations sit at the operand-stream bound; no further device headroom in-kernel** |
| srnss per-token fp32 gnone (18144x3072) | 16 B/elem = 892 MB | 129.3us -> 6.90 TB/s | ~86% | DRAM | 1.02x, at bound |
| nss per-token bf16 (8640x5120) | 8 B/elem = 354 MB | 60.8us -> 5.82 TB/s | ~73% | DRAM + partial-fill | 1.64x |
| tiny rows (19..1004) | <= 25 MB | n/a (host-bound) | n/a | launch/host issue floor (~60-80us per call e2e both sides) | candidate 1.27-1.47x e2e via host path; device-side no-go: kernel time ~3-5us, floor is the host |

## Iteration history (full DAG in solutions.jsonl)

1. cand-0001 (v1): 256-bit row-per-CTA port, single-pass E[x^2] stats —
   geomean 1.70x e2e but INADMISSIBLE comparison (candidate lacked the
   custom-op layer) + contract deviation (audit).
2. cand-0002 (v2): audit fixes + two-pass variance + per-combo vec width
   (NCU-driven) + symmetric custom-op layer -> 1.31x e2e admissible.
3. cand-0003 (Welford single-round): REJECTED on r2-v3 evidence (1.16x; merge
   division in the dependent shuffle chain costs more than the saved round).
4. cand-0004 (shipped = v2 config): r3-final 1.2987x e2e / 1.2896x device.

## Completion statement

Per-bucket status: every bucket either improves over the baseline through the
shipping-shaped path, or is shown at its operand-stream DRAM bound with parity
(per-token fp32 family) — satisfying the bound-or-no-go completion bar. The
remaining ~57-60%-of-peak ceiling on the nss bf16 broadcast family is
explained by NCU evidence (instruction-issue pressure from per-element
converts/epilogue on a 4 B/elem kernel); the packed-conversion lever is
recorded in docs/draft.md for future rounds and was deprioritized under the
bounded-iteration policy after three measured kernel iterations.
