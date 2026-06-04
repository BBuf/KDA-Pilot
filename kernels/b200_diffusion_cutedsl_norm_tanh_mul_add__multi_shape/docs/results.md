# Results — `b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape`

## FINAL VERDICT — PROMOTE

**Shipping integration (the promotion arbiter — DISPATCH-SYMMETRIC in-SGLang drop-in:
both routes measured in the SAME patched checkout through the identical custom-op
wrapper + dispatch branch, native routes toggled by env, contract-clean idle GPU 1):
geomean 1.493× over the 4 captured zimage shapes** — v1 1.596×/1.621× (geo 1.609×),
v2 1.378×/1.393× (geo 1.385×); public-op wall medians, full stats in
`export/arbiter_runs/*_r4.json` and `benchmark.csv` (mode
`in-sglang-arbiter-dispatch-symmetric`); details `docs/sglang_jit_export.md`. In-SGLang
correctness PASS including the gate-verified fallback (mixed-dtype probe asserted
`native_supported(...) is False` AND its public-op output matched the reference within
production tolerances). Both entry points ship natively (v1 and v2 each clear the
pre-registered parity-or-better rule in the dispatch-symmetric arbiter). Benchmark runs
are admitted only under the enforced GPU contract (`REMOTE_GPU_ID` matching
`CUDA_VISIBLE_DEVICES`; strict mocked-state-self-tested gate: start = no compute apps,
util ≤ 5%, memory ≤ 2 GiB; end = no foreign compute app AND memory ≤ 2 GiB, so
memory-only or unattributable high-memory contamination is rejected, not just extra
apps) — the gate twice refused a foreign-occupied GPU 0 before the final runs moved to
idle GPU 1, whose recorded end state (one app, 1148 MiB) passes the end ceiling.

Honest decomposition (Codex-reviewed framing): raw-callable wall geomean 1.379-1.400×
(final enforced-gate rerun on GPU 1: 1.379×);
device-only kernel deltas v1 **+4%** (41.4 vs 43.0 µs) and v2 **−16%** (78.6 vs 66.0 µs;
≈267 MB/launch register-spill traffic) — the integrated win is dominated by the native
tvm-ffi host path replacing the CuTe-DSL host path inside the unchanged public op,
which is legitimate shipped-path cost on both sides (no production-required layer
removed). Residual device gap to the bytes floor (13.5/18.0 µs) is latency-structural
(barrier-serialized per-row reductions at sub-wave grid); levers measured and
rejected with evidence: prefetch (spills), v2 register budget (occupancy), PDL (A/B),
K∈{2,4,8} sweep. Named out-of-scope blocker: warp-per-row redesign.

Correctness: 33/33 on B200 with the anti-fallback guard across 204 native-path cases
(fp32 oracle with baseline rounding/affine semantics + dynamic noise bound), 22
contract-rejection cases, affine-edge/routing/fallback tests, plus in-SGLang public-op
validation. Command (inside `sglang_bbuf`, workspace root):

```bash
CUDA_VISIBLE_DEVICES=0 KDA_RUN_CORRECTNESS=1 python -m pytest tests/test_correctness.py -q
# => 33 passed, 4 warnings in 240.49s   (re-run after every kernel edit; identical result)
```

NCU evidence: raw `.ncu-rep` files (full set, base+cand, both variants) are retained in
the remote run directory `REMOTE_KDA_DIR/workspace/profile/final_lb_k8_full/reports/`;
the local `profile/final_lb_k8_full/` mirror holds the parsed summaries
(`analysis/metrics_summary.csv`, `analysis/stall_breakdown.csv`) and `REPORT.md`.

---

Living evidence document; chronology below.
Host `innomatrix-us-adc-smb200-0003` (ion-b200), container `sglang_bbuf`, GPU 0
(`GPU-a4d97fda-2684-94c9-4291-c6b291c0eb33`, NVIDIA B200, 148 SMs), SGLang
`main@edb1b3f8f`, torch 2.11.0+cu130, CUDA 13.0.

## Roofline / bytes model (per call)

bf16, D=3840; weight/scale D-vectors (7.5 KB) negligible; B200 HBM3e peak ≈ 8 TB/s,
~7 TB/s effective planning number.

| Variant | Shape | Reads | Writes | Total bytes | Floor @ 7 TB/s |
|---|---|---|---|---|---|
| v1 | [1, 4096, 3840] | x 31.5 MB + shift 31.5 MB | y 31.5 MB | 94.4 MB | ≈ 13.5 µs |
| v1 | [1, 4128, 3840] | ″ ×(4128/4096) | ″ | 95.1 MB | ≈ 13.6 µs |
| v2 | [1, 4096, 3840] | x + shift | y + y2 | 125.8 MB | ≈ 18.0 µs |
| v2 | [1, 4128, 3840] | ″ | ″ | 126.8 MB | ≈ 18.1 µs |

Useful op counts (v1): 1 mul+add per element for modulation + norm (2 flops/elem reduce
+ 2 flops/elem normalize) ≈ 5 flops/elem ≈ 79 MFLOP per call — arithmetic intensity
≈ 0.8 flop/byte, far below the roofline knee ⇒ the op SHOULD be memory-bound.

## Measured timeline (chronological)

### Frozen baseline (commit 3957e12df; CuTe-DSL kernels via raw callables)

| Channel | v1 S=4096 | v1 S=4128 | v2 S=4096 | v2 S=4128 |
|---|---|---|---|---|
| wall-synced median | 81.96 µs | 83.40 µs | 111.57 µs | 112.24 µs |
| event-bracket median (diagnostic) | 73.06 | 72.02 | 86.37 | 88.42 |
| NCU kernel duration (v1 S=4096) | **43.3 µs** | — | — | — |

NCU `--set basic` (launch-skip 25, count 2): Compute(SM) 67-68%, DRAM 24%, Memory 28%,
grid 4096 × 480 thr, 32 regs/thr, occupancy 80.6%.

**Diagnosis**: the baseline kernel is COMPUTE-bound — ~3.2× above its bytes floor —
consistent with per-row re-evaluation of `tanh(scale)` (~15.7 M tanh per call while the
production scale `[1,1,D]` needs only 3840). Additionally the CuTe tvm-ffi host path
serializes inside CUDA-event brackets (73 µs bracket vs 43.3 µs kernel), so event
numbers are diagnostic-only; wall-synced covers end-to-end and NCU covers device-only.

### Candidate v1 (commit acb0b5ef6; native CUDA, K=8 rows/CTA, hoisted tanh)

Correctness: 33/33 with `KDA_REQUIRE_CANDIDATE=1` (all 204 native-eligible cases vs
baseline + fp32 reference + dynamic noise bound; affine-edge, routing, fallback tests).

| Channel | v1 S=4096 | v1 S=4128 | v2 S=4096 | v2 S=4128 | geomean |
|---|---|---|---|---|---|
| wall speedup | 1.309× | 1.326× | 0.935× | 0.936× | **1.110×** |
| event speedup (diagnostic) | 1.219 | 1.209 | 0.735 | 0.622 | 0.906 |

NCU candidate v1 S=4096: duration **52.7 µs** (slower than baseline kernel 43.3 µs!),
Compute(SM) 32.5%, DRAM 19.6%, grid 512 × 480 thr, **48 regs/thr, occupancy 40.5%**.

**Diagnosis**: tanh hoist succeeded (Compute 67→32%) but register growth (48/thr) cut
occupancy to 2 CTAs/SM and K=8 shrank the grid to 512 CTAs → latency-bound; v2 worst
(two serial CTA reductions per row at low occupancy). End-to-end v1 still wins on the
lighter host path; the device kernel itself regressed.

### Round 1 edit: `__launch_bounds__(D/8, ≥4 CTAs/SM)` register cap + K sweep

(commit a9d0d4d7d) Wall-channel speedups vs baseline, per rows-per-CTA K:

| K | v1 S=4096 | v1 S=4128 | v2 S=4096 | v2 S=4128 | geomean wall | geomean event (diag) |
|---|---|---|---|---|---|---|
| 2 | 1.406× | 1.402× | 1.273× | 1.256× | 1.332× | 1.260 |
| 4 | 1.474× | 1.457× | 1.241× | 1.249× | 1.351× | 1.282 |
| 8 | 1.468× | 1.469× | **1.317×** | **1.293×** | **1.384×** | 1.316 |

Register cap restored occupancy; the v2 regression is gone at every K. **K=8 kept as
the default** (best geomean).

NCU `--set basic` (K=8, S=4096, launch-skip 25, count 2):

| Kernel | Duration | Regs | Occupancy | DRAM % | Compute(SM) % | vs bytes floor |
|---|---|---|---|---|---|---|
| candidate v1 | **41.1-41.8 µs** | 32 | 72.5-73.7% | 26.3% | 45.3-46.3% | 3.0× above 13.5 µs |
| candidate v2 | **78.7-78.8 µs** | 32 | 73.5-73.9% | 21.5% | 42.5-43.0% | 4.4× above 18.0 µs |
| baseline v1 (ref) | 43.3 µs | 32 | 80.6% | 24.0% | 67.5% | 3.2× |

Decomposition at this point: device-only v1 ≈ 1.05× (41.1 vs 43.3 µs NCU); the rest of
the 1.47× v1 wall win is host-path (CuTe tvm-ffi dispatch ≈ 38 µs/call vs native ≈ 12 µs).
Both candidate kernels remain latency-bound (DRAM ≈ 21-26%): with K=8 the grid is 512
CTAs ≈ one wave at 4 CTAs/SM, and each row's CTA-wide reduction barriers serialize.
Round 2 edit: software-pipelined next-row x/shift prefetch (issue row r+1 loads before
row r's barriers) — results below.

### Round 2 edit: next-row prefetch pipeline — REJECTED

Correctness held (33/33) but NCU showed v1 126.1 µs / v2 154.4 µs (3.1× / 2.0× worse
than round 1): keeping the prefetched vectors live across the reduction barriers under
the 32-register cap forces local-memory spills inside the row loop. Edit reverted; the
**round-1 launch-bounds K=8 kernel is the final candidate** of this loop.

### Round 3-4: formal NCU comparison + v2 register-budget attempt

Formal `--set full` reports (`profile/final_lb_k8_full/`, parsed in `analysis/`):
baseline v1 **43.0 µs** / v2 **66.0 µs** (zero spills, ALU 52-56% — tanh math), candidate
v1 **41.4 µs** / v2 **78.6 µs** (ALU 29-33%, but waves/SM 0.86, `long_scoreboard` 7.7-7.9,
and local-memory spills: v1 47 MB, v2 267 MB per launch). Device-only: v1 1.04×, v2 0.84×
(v2's end-to-end 1.29× is host-path-carried). PDL A/B: geomean 1.384× ≈ noise-worse →
PDL stays OFF. Round 4 tried a v2-only 3-CTA/SM register budget (regs 40, no-spill
hypothesis): NCU 93.7 µs, occupancy 57.6% — REJECTED (concurrency loss > spill relief);
uniform 4-CTA K=8 build is final. Full six-dimension analysis:
`profile/final_lb_k8_full/REPORT.md`.

### Bound attribution (final-candidate state)

The remaining gap to the bytes floor (v1 41.1 vs 13.5 µs; v2 78.7 vs 18.0 µs) is
latency-structural, not bandwidth or compute: DRAM ≤ 26%, Compute ≤ 46%, occupancy
~73%, and each row requires CTA-wide fp32 reduction barriers (1 for rms, ×2 for the
second norm) that serialize the per-CTA row chain; at K=8 the grid (512 CTAs) is ~one
wave, and smaller K (more waves) does not improve end-to-end (measured K∈{2,4,8}).
Attempted latency-overlap via prefetch is refuted by register-pressure spills (above).
A warp-per-row redesign would need cross-lane-only reductions at 960 elem/warp slices
and a different vectorization contract — outside this loop's bounded scope; recorded as
the named blocker for further device-side gains.

## Device-vs-host decomposition policy

- End-to-end claim: wall-synced medians at the raw-callable layer (both sides carry
  their real host cost; CuTe host ≈ 38 µs/call for v1 = 82.0 wall − 43.3 NCU vs native
  host ≈ 12 µs = 65.0 wall − 52.7 NCU).
- Device-only claim: NCU kernel durations, identical launch-skip/count discipline.
- Promotion arbiter: in-SGLang drop-in with identical custom-op wrapper on both sides.
