# Results: b200_diffusion_cutedsl_norm_scale_shift__multi_shape

## Headline (run_id=r6-final, shipped configuration, idle-gated)

- **Geometric-mean median-latency speedup over the SGLang CuTe-DSL baseline,
  39 unique captured signatures: 1.3022x end-to-end / 1.2878x device-events**
  (outcome metric per DEC-1/DEC-4; per-case table in `benchmark.csv`,
  aggregation via `python benchmark.py --report --run-id r6-final`).
- Every unique signature >= 1.094x end-to-end (max 1.48x); device-mode range
  0.98x (per-token fp32, at the operand-stream bound — see below) to 1.64x.
- Idle proof (locally auditable, AC-5.1): the harness itself gates the run —
  before: device util/mem 0/0 and no compute processes; after: util 0 after a
  settle period and no OTHER compute process (its own CUDA context memory is
  expected in-process; `bench/benchmark.py::_other_compute_apps`). The
  r6-final rows record `idle_before=0/0` and `idle_after_util=0`; the
  committed external pre/post-exit all-GPU snapshots
  (`bench/evidence/r6-final/allgpu_{before,after}.txt`) show GPU 1 at
  **0% util / 0 MiB with zero compute apps both times** (GPUs 2-7 carried
  unrelated jobs throughout).
- Environment: ion-b200, container
  sglang_bbuf, GPU 1, torch 2.11.0+cu130, CUDA 13.0, SGLang baseline commit
  edb1b3f8f5. `candidate_src_hash=d0f645a016cb` in every r6 row = the joint
  hash of the CURRENT `src/csrc/norm_scale_shift.cuh` + `src/wrapper.py` +
  `src/register.py` (including the review-phase arity-routing fix in
  register.py); correctness (122 tests, incl. the new registered-callable
  routing test) re-passed at the same source.
- Method: candidate and baseline interleaved in one process on identical
  pre-built inputs; candidate behind the kda_nss custom-op layer so both
  sides carry the same host registration/dispatch stack (AC-5.4).
- Audit lineage: r0-v1 (1.70x) demoted — candidate side lacked the custom-op
  layer (host-stack asymmetry); r3-final discarded — GPU-0 contamination
  visible in its own idle columns; r4-final superseded — its idle_after
  columns sampled in-process and its hash predates a comment-only source
  edit. r5-final superseded by r6-final after the review-phase register.py arity-routing fix changed the joint hash (full re-validation, numbers within run-to-run noise). r6-final is the only headline promotion run.

## In-SGLang drop-in confirmation (the promotion arbiter)

`docs/sglang_jit_export.md`: official upstream test grid **147 passed** on
the patched checkout; symmetric same-op A/B (in-body toggle) shows
1.116x-1.463x on six representative buckets (current-source re-run), corroborating the kernel-folder
numbers on the true shipping path; rms fallback probe bitwise-identical.

## Device-vs-host decomposition

- "device" mode = CUDA-event stream-span per call; for stream-saturated
  (large) cases this approximates kernel duration; for host-starved tiny
  cases it includes launch-issue latency — final-config NCU
  (profile/r4f-*/REPORT.md) carries the kernel-duration ground truth.
- Tiny/small rows (S 19..1004): end-to-end 1.39-1.49x comes from the leaner
  host path (stride-classified dispatch + one tvm-ffi call vs einops
  broadcast + hash + 9 dlpack conversions + CuTe-DSL call layer), measured
  through IDENTICAL custom-op layers — an admissible production win.
- Large rows: end-to-end and device speedups agree (1.10-1.35x) — device
  kernel wins, host effects negligible.

## Roofline per bucket (r6-final device medians, boost clocks; peak ~8 TB/s)

| Bucket | Traffic model | Candidate | BW | % peak | Active bound | Verdict |
|---|---|---|---|---|---|---|
| nss bf16 row-bcast huge (176400x5120) | 4 B/elem = 3.61 GB | 787.9us | 4.58 TB/s | ~57% | mixed instruction-issue + DRAM (NCU r4f: see REPORT.md) | 1.35x over baseline (3.40 TB/s); packed-cvt lever recorded for future rounds |
| nss bf16 row-bcast d3072 (27085) | 4 B/elem = 333 MB | 70.0us | 4.76 TB/s | ~59% | same | 1.56x device |
| srnss bf16 gnone huge (44100x5120) | 8 B/elem = 1.81 GB | 272.8us | 6.62 TB/s | ~83% | DRAM | near bound; 1.17x |
| srnss wan affine (37800x5120) | 8 B/elem + row streams = 1.55 GB | 264.7us | 5.85 TB/s | ~73% | DRAM + fp32 operand latency | 1.33x |
| srnss gnone fp32 row (37800x5120) | 8 B/elem = 1.55 GB | 256.4us | 6.04 TB/s | ~75% | DRAM | 1.06x (baseline already near bound) |
| nss per-token fp32 (18144x3072) | 12 B/elem = 669 MB | 102.8us | 6.51 TB/s | ~81% | DRAM (operand streams dominate) | **parity (0.994x device) — evidence-backed: at the operand-stream bound** |
| srnss per-token fp32 gnone (18144x3072) | 16 B/elem = 892 MB | 129.2us | 6.90 TB/s | ~86% | DRAM | 1.02x, at bound |
| nss per-token bf16 (8640x5120) | 8 B/elem = 354 MB | 61.9us | 5.72 TB/s | ~72% | DRAM + partial fill | 1.65x device |
| tiny rows (19..1004) | <= 25 MB | n/a | n/a | n/a | host/launch issue floor (e2e ~63-66us candidate vs ~91-96us baseline, both sides custom-op-wrapped); kernel 7.3us locked clocks (NCU r4f-tiny-s47) | 1.39-1.48x e2e via host path; device-side no-go (floor is the host) |

## Iteration history (full DAG in solutions.jsonl)

1. cand-0001 (v1): 256-bit row-per-CTA port, single-pass E[x^2] stats —
   1.70x e2e but INADMISSIBLE (host-stack asymmetry) + contract deviation.
2. cand-0002 (v2): audit fixes + two-pass variance + per-combo vec width
   (NCU r0v1) + symmetric custom-op layer -> 1.31x admissible.
3. cand-0003 (Welford single-round): REJECTED on r2-v3 (1.16x geomean).
4. cand-0004 (shipped config) validated repeatedly: r4-final (superseded —
   in-process idle sampling + pre-comment-edit hash), r5-final (superseded —
   hash predates the review-phase register.py arity-routing fix), and
   **r6-final** (the headline: idle-gated harness, committed external
   snapshots, current joint hash d0f645a016cb, 1.3022x e2e / 1.2878x device)
   + in-SGLang drop-in arbiter (147 upstream tests, 1.116-1.463x same-op
   A/B at the re-run).

## Caveats (recorded at final audit)

- Native coverage is intentionally production-first (DEC-2): the 10 verified
  combos cover every captured signature; all other layouts/dtypes/norm types
  rely on the fail-closed fallback to the baseline path (tested, including
  inside the in-tree integration).
- The benchmark CSV's per-row `idle_after_mem_mib` necessarily includes the
  process's own CUDA context; the harness gate therefore checks util==0 plus
  zero OTHER compute processes, and the committed post-exit snapshot
  (`bench/evidence/r6-final/allgpu_after.txt`) provides the true 0/0 proof.
- An upstream SGLang PR should land the integration as a normal reviewed
  diff (the hash-guarded body-insertion script is an arbiter mechanism, not
  the PR format).

## Completion statement

Every bucket either improves over the baseline through the shipping-shaped
path, or is shown at its operand-stream DRAM bound with parity (per-token
fp32 family) — satisfying the bound-or-no-go completion bar. The
~57-60%-of-peak ceiling on the nss bf16 broadcast family is the one
non-DRAM-bound gap, attributed by NCU to per-element convert/epilogue
instruction pressure; the packed-conversion lever is recorded in
docs/draft.md and deprioritized after three measured kernel iterations
(bounded-iteration policy).
