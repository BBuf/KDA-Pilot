# Implementation Draft: b200_diffusion_cutedsl_norm_scale_shift__multi_shape

Working notes for the native CUDA candidate. Updated every optimization round
with the context refresh (KernelWiki / ncu evidence) that drives the next edit.

## Workload structure (39 unique signatures, docs/captured_shapes_unique.md)

Buckets by rows `R = B*S` (B==1 in every captured row) and `D`:

| Bucket | Rows R | D | Signatures | Regime |
|---|---|---|---|---|
| huge-video | 27030..176400 | 3072/5120 | mova 176400/44100×5120, wan 74088/75600×5120, wan 37044/37800×5120 (nss fp32-bcast, srnss gate+w/b fp32, srnss gnone fp32), hunyuan 27030/27085×3072 (+srnss) | HBM-bandwidth-bound |
| mid-image | 4096..18144 | 3072/4096/5120 | firered 8424×3072 (+srnss), helios 11040×5120 **per-token fp32**, helios 8640×5120 per-token bf16, joyai 7904×4096, qwen 4096×3072 (+srnss), wan-ti2v 18144×3072 (per-token fp32/bf16, srnss variants) | BW-bound w/ tail effects; per-token rows operand-stream-bound |
| small | 997..1004 | 4096 | joyai 997/1004×4096 | partial fill, latency-sensitive |
| tiny | 19..195 | 1536/3072 | qwen 19/47 (+srnss), hunyuan 55 (+srnss), mova 101×1536 (+srnss gnone), qwen-edit 189/195 (+srnss) | launch/host-overhead-bound |

Bytes model (per element of x; bf16 x):
- nss broadcast scale/shift: read 2B (x) + ~0 (operands L2-resident) + write 2B → **4B/elem**. mova 176400×5120: ~3.6 GB total → HBM-floor ≈ traffic/peak-BW; baseline should already be close.
- nss per-token fp32 scale/shift (helios 11040×5120, wan-ti2v 18144×3072): 2B + 4B + 4B + 2B = **12B/elem** → scale/shift streams dominate (2/3 of traffic). Improvement ceiling is tiny; bound statement required.
- srnss broadcast (qwen/hunyuan/firered/mova): read x+residual 4B + write res_out+y 4B = **8B/elem**.
- srnss wan variant (gate [1,1,D] fp32, w/b [D] fp32, scalar scale/shift): same 8B/elem stream + L2-resident operands.

## Baseline structure (recovered; interface.md has the contract)

One CTA per row; `D//256` warps; one 128-bit copy per thread per operand
(8×bf16 or 4×fp32); fp32 reductions; layer = TWO full passes (mean reduction,
then variance reduction; each = warp shuffle tree + smem round + 2 syncs);
scale/shift loads issued AFTER the norm completes (serial epilogue latency);
host path = einops rearrange/expand + hash-key dict + CuTe-DSL tvm-ffi call
(9 dlpack conversions per call).

## Ranked candidate directions

| # | Direction | Attacks | Expected benefit | Risk | Status |
|---|---|---|---|---|---|
| D1 | Native CUDA port, row-per-CTA, 128-bit vec, fp32 reduce, all production layout classes; lean `load_jit` wrapper (no einops, no per-call rearrange; stride-classified dispatch) | host overhead (tiny/mid buckets end-to-end), foundation for everything | high (host) / parity (device) | low | round 0 target |
| D2 | Single-pass layer stats (fused sum+sumsq, ONE reduction round, E[x²]−mean² with clamp; two-pass kept as compile-time fallback) + prefetch scale/shift/gate/weight DURING reduction | reduction latency on small/mid R; epilogue serialization | med on R≤~16k; hidden on huge R | numerics: verify vs fp32 ref + dynamic tol | round 0 (flagged) |
| D3 | Small-R specialization: row-per-warpgroup (128 lanes, D/128 elems/lane) + multi-row CTA; dispatch on (R, D) | tiny/small bucket underfill (19..1004 CTAs on 148 SMs) | med device-side; end-to-end capped by launch floor (~3-5µs) | med | after v1 benchmark |
| D4 | Large-R tuning: rows-per-CTA=2/4 (fewer CTAs, reused operand registers), wave-quantization trim, L2 ldg hints | huge-video tail/issue overhead | small-med | med | after ncu |
| D5 | PDL (`enable_pdl` like qknorm_rope.cuh) | back-to-back launch gaps in production graphs | unknown; pilot showed isolated-latency HARM | low (flag) | validate-only |
| D6 | 256-bit loads/stores on sm_100 (paired uint4 / b256 PTX) if profitable | instruction issue on BW-bound rows | small | low | after ncu |

Non-directions (recorded): tcgen05/TMEM/cluster (no matmul in this op);
smem staging of x (register path already minimal); persistent grid for huge R
(CTA-per-row already saturates; revisit only on ncu evidence).

## KernelWiki context (round 0)

- `pr-sglang-14717` — upstream PR that introduced this exact kernel family
  (motivation: GPU bubbles → fusion for Qwen-Image/WAN/HunyuanVideo). Confirms
  production intent; no further optimization in-tree since.
- `pr-flashinfer-3008` — PDL added to CuTe-DSL rmsnorm variants (precedent for
  D5; PDL is a flag, validate on real workload per task policy).
- `pr-flashinfer-2233` — fused RMSNorm + FP4 quant in CuTe-DSL (epilogue-fusion
  pattern reference; quant epilogue not applicable here).
- Queries run: `"CuTe DSL norm scale shift fused"`, `"fused norm residual gate
  adaLN"`, `--tag modulation --architecture sm100` (no matches for the last).

## Numerics decisions

- Match baseline contract: pre-norm value cast to x.dtype before norm; fp32
  statistics; norm output cast to x.dtype before scale/shift; scale/shift
  applied in their own dtype (fp32 promotes); final cast to y.dtype.
- D2 single-pass variance deviates from baseline's two-pass internally but must
  stay within the fp32-reference dynamic tolerance; if any configured case
  exceeds the bound, ship the two-pass template instantiation instead.

## Round log

- Round 0 / step 1: baseline recovered (commit edb1b3f8f5, parity 39/39
  bitwise), 39 unique signatures mapped, directions ranked.
- Round 0 / step 2 (D1+D2 implemented): candidate v1 = row-per-CTA, 256-bit
  vectors (16xbf16/thread, block=D/16), fp32 single-pass fused sum+sumsq with
  clamp (two-pass behind a flag), operand classes scalar/row/per-token, fp32
  [D] affine path, fused residual+gate, fail-closed dispatcher. Correctness:
  117 passed candidate-mode, zero fallbacks on production. Benchmark r0-v1:
  geomean over 39 unique signatures **1.7037x endtoend / 1.5985x
  device-events**. Real device wins on stream-saturated huge rows (mova
  176400x5120: 1061->733us ≈ 4.9 TB/s vs baseline 3.4); tiny rows are
  host-issue-bound (95->39us end-to-end dominated by wrapper path, device-event
  numbers there measure stream-span incl. issue starvation, not kernel time).
  Surprises queued for ncu: (a) per-token fp32 scale/shift rows
  (helios 11040x5120: candidate device-events 113.1 vs baseline 104.8us);
  (b) huge-row bandwidth at ~61% of peak — what limits?
  Context refresh: no new KernelWiki query needed (direction list unchanged);
  ncu round 1 launched per the skill workflow (profile/r0v1-*).
- Round 0 / step 3 (Codex audit + ncu round 1 -> v2): Codex audit verdicts and
  dispositions — (1) single-pass variance contract deviation: ACCEPTED, flipped
  TWO_PASS_VARIANCE=True (contract-exact; fused form kept as documented A/B
  lever only); (2) missing is_cuda/device guards in operand classification:
  ACCEPTED, added same-device checks; (3) S=0 reaching native: ACCEPTED, added
  numel()>0; (4) srnss scale=None AttributeError: ACCEPTED, non-tensor
  scale/shift now falls back so the baseline raises its own validation error;
  (5) custom-op registration "not preserved": CLARIFIED — the in-tree export
  (the promotion arbiter) keeps SGLang's own registration; ADDITIONALLY added a
  local `kda_nss::*` custom-op layer (shipping_entry_points) so the local A/B
  compares candidate and baseline through IDENTICAL host stacks (the benchmark
  now defaults to it); (6) srnss reference missing pre-norm cast: ACCEPTED,
  reference now contract-exact; (7) adversarial high-mean + cpu-operand +
  empty-rows + scale-None probes: ADDED (correctness v2: 121 passed).
  NCU round 1 findings -> v2 edit: fp32-operand combos now build with
  kVecBytes=16 (8 elems/thread, block=D/8) after candidate occupancy 41% /
  long_scoreboard 16.4 vs baseline occ 82% on the token-fp32 case; bf16-only
  combos keep kVecBytes=32. Reports: profile/r0v1-*/REPORT.md.
- Round 0 / step 4 (evidence audit -> r4 re-validation): Codex evidence audit
  flagged: (1) r3-final ran on a CONTAMINATED GPU0 (1576 MiB before / 58%
  util + 2292 MiB after, visible in benchmark.csv idle columns) while
  docs/results.md claimed clean — ACCEPTED, full re-run as r4-final on
  verified-idle GPU1 with all-GPU before/after logs; (2) candidate_src_hash
  bound only the .cuh so r2-v3 and r3-final shared a hash across different
  wrapper configs — ACCEPTED, hash now spans .cuh+wrapper.py+register.py;
  (3) bench/benchmark.py overstated "device execution only" — ACCEPTED,
  docstring corrected to stream-span semantics; (4) dispatch.md nss_row_bf16
  e2e range omitted the 1.09x s27030 outlier — to recompute from clean r4
  data (the outlier itself looks like the GPU contamination); (5) tiny-row
  kernel-time claim and final-config bound claims lacked NCU on the SHIPPED
  build — ACCEPTED, final-config ncu round queued for huge-bf16 + token-fp32
  + one tiny row; (6) in-SGLang drop-in still pending — running now (export/
  run_export_test.sh: task-owned clone at the pinned commit, .cuh under
  csrc/diffusion/, native glue module, minimal op-body patch with
  registration untouched, official pytest grid + symmetric same-op A/B smoke
  + rms fallback probe).
