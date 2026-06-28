# Results — b200_ltx2_qknorm_split_rope__bitwise

## Outcome

**Bit-exact net improvement.** The candidate (reused `torch.nn.RMSNorm` + a single
fused split-RoPE CUDA kernel) is byte-for-byte equal (`torch.equal`, zero
tolerance) to the PyTorch eager baseline on all eight production rows, a regression
grid, and adversarial rounding-boundary inputs, while running faster than the eager
fallback on every production row. As-shipped end-to-end geomean **~1.96×**
(includes the candidate's per-call safety validation); **kernel-only ~2.56×** with
that validation hoisted to setup as a production integration would (see "Validation
cost" below).

## Correctness gate (no tolerance; `torch.equal` on int16 bitcast) — `failures=0, skipped=0`

- Production rows (Section 1): **8/8 bit-equal** (q_out and k_out).
- Regression grid (Section 2): **12/12 bit-equal** (`head_dim∈{64,128}`, `num_heads=32`, `B∈{1,2}`, seq ∈ {129,126,257,1536}, cross-attn unequal Q/K).
- Adversarial rounding-boundary, stage-level (Section 3): **bit-equal**, sensitivity
  guard tripped on **3419 elements** (a single-fp32-expression reference without the
  intermediate bf16 round differs from the eager fallback there, proving the data
  exercises the round-first-then-`addcmul` distinction; the candidate matches the
  *correct* eager value).
- Candidate reject path, via `adapter.call_candidate` on mutated real cases
  (Section 4): **21/21** — base accepted; rejects (all raise `ValueError` before any
  kernel launch) for TP≠1, non-`RMSNorm` and `RMSNorm` subclass, eps mismatch, fp32
  weights, non-bf16 q AND k, non-contiguous q AND k, `head_dim` mismatch, q_cos 3-D,
  q_cos/k_sin dtype, q_cos last-stride≠1, q_sin shape, **CPU cos / CPU output
  (wrong-device)**, bad output shape/dtype/contiguity, and a **mutate-after-accept**
  case (the same inputs object mutated in place into an unsupported config still
  rejects — no validation-cache bypass).
- Support-helper unit tests (Section 5): **9/9** (includes two added rejects for cos/sin whose batch or sequence length does not match `x`).
- Fail-closed: in normal mode any FAIL **or SKIP** in the CUDA sections (or CUDA
  unavailable) exits non-zero.

## Per-shape performance (B200, GPU 5, CUDA events, median over 7 trials; as-shipped, per-call validation)

| Workload | baseline med (µs) | candidate med (µs) | speedup | candidate p10–p90 |
|----------|------------------:|-------------------:|--------:|-------------------|
| stage1 video self q1536 k1536 d128 | 217.29 | 160.21 | 1.356× | 160.01–160.58 |
| stage1 audio self q126 k126 d64 | 114.79 | 42.92 | 2.674× | 39.35–45.63 |
| stage1 audio→video q1536 k126 d64 | 178.48 | 66.75 | 2.674× | 56.60–69.38 |
| stage1 video→audio q126 k1536 d64 | 131.77 | 53.21 | 2.476× | 53.04–53.37 |
| stage2 video self q6144 k6144 d128 | 404.46 | 295.81 | 1.367× | 295.21–297.49 |
| stage2 audio self q126 k126 d64 | 139.80 | 50.13 | 2.789× | 44.21–52.19 |
| stage2 audio→video q6144 k126 d64 | 133.26 | 89.20 | 1.494× | 88.31–89.35 |
| stage2 video→audio q126 k6144 d64 | 138.63 | 88.75 | 1.562× | 88.37–89.21 |

**Headline (as-shipped):** geomean **1.955×**, arithmetic mean 2.049×, min 1.356×, max 2.789× (8/8 production rows passed).

### Validation cost (as-shipped vs kernel-only)

For safety (AC-7), `run_candidate` validates its inputs on EVERY call and rejects
unsupported configs before any kernel launch (it can never be bypassed by in-place
mutation). That validation is ~15 µs of CPU metadata checks per call. In a
production integration the shapes/configs are static, so validation is a one-time
setup gate, not a per-token-batch cost. Two measurements bracket this:
- **As-shipped, per-call validation in the timed path:** geomean **1.955×** (table above).
- **Kernel-only (validation hoisted/cached to setup):** geomean **~2.56×**
  (measured in a validate-once configuration; per-row the candidate medians drop to
  ~26–37 µs on the small audio rows). This reflects the production-representative
  cost of the kernel itself.

Either way the candidate is bit-exact and faster on every row.

### Measurement variability (honest)

The candidate is faster on every row in every run, but the geomean varies run-to-run
because the eager baseline's small/cross rows are launch/host-overhead-bound
(~115–220 µs dominated by per-launch CPU overhead, not tensor size) and thus
sensitive to host-CPU contention from other jobs on the shared box. The candidate
(one GPU-bound kernel) is stable (tight p10–p90). Both sides are measured under
identical settings in the same run, so each A/B ratio is fair.

## Roofline-style rationale (active bound)

Memory-bound elementwise + small-reduction op. The eager baseline runs split-RoPE
as a chain of separate ATen ops (`reshape/swapaxes` → `split_x*cos` → two
`addcmul_` → `reshape/swapaxes`), each a kernel launch reading/writing bf16
intermediates through HBM plus fixed launch overhead. Small/cross rows (S=126) are
launch-overhead-bound, so collapsing the chain into one fused kernel yields the
large speedups; large video-self rows (S=1536/6144, d=128) are HBM- + shared-RMSNorm-
bound, so the gain is ~1.36×. The fused kernel reads `q_normed`+`cos`+`sin` once and
writes `out` once — near the memory-bound floor for the RoPE stage; the remaining
headroom is the shared RMSNorm.

## Optimization directions (Codex `analyze`; for a future upper-bound round)

Ranked by benefit-vs-risk for pushing the large d128 rows past ~1.36× while keeping
strict bit-exactness:
1. **Vectorized 128-bit bf16 load/store** for the RoPE fast path — 5–15% on large rows, low bit-exactness risk, medium effort.
2. **Shape specialization d64 vs d128** — 5–12%, low–medium risk, medium effort.
3. **Fuse RMSNorm into the kernel** (eliminate the `q_normed` HBM round-trip) — highest benefit (~15–35% on large rows) but **high bit-exactness risk** (must clone torch RMSNorm's fp32 reduction order/tree, eps placement, rsqrt-vs-sqrt+reciprocal, weight-multiply order, exact downcast point; ~20–35% first-try) and high effort. De-risk via a standalone bit-exact RMSNorm first, then compose, then remove the intermediate.
4. Occupancy/block-size tuning — NCU-gated, 0–10%.

**NCU decision:** a roofline rationale is sufficient to ACCEPT the staged candidate
(bit-exact, clear win). NCU is warranted only for a future edit targeting the large
rows; a short pass on one large video-self row should answer: DRAM/L2 throughput vs
roofline; bytes/sector for the strided cos/sin; eligible-warps/occupancy/stalls.
NCU was NOT run this round (not required for acceptance).

## How the bit-exactness is achieved

- **RMSNorm:** reused `torch.nn.RMSNorm(H, eps)` unchanged (bit-exact by construction).
- **Split RoPE:** the CUDA kernel rounds `first*cos`/`second*cos` to bf16 first
  (matching `split_x*cos`), then adds the sine term via fp32 `__fmaf_rn` + one bf16
  round (`__float2bfloat16_rn`), matching PyTorch `addcmul_` (fp32 opmath). No
  `--use_fast_math`; cos/sin indexed via real strides.

## Provenance

- Baseline source: SGLang `main` @ `aaa31eb0a11e09f9511bade5e815907ec0b91fa0`
  (`apply_split_rotary_emb` eager fallback). See `docs/baseline_source.md`.
- Candidate source hash (AC-9): `solution/kernel.cu` sha256
  `983fb2791b9343f141a0332c303e9ef3ef53aaffc22d49f7aefe8b0ff7788024`. The compiled
  code is unchanged since the kernel was first written (it was bit-exact from the
  start); later rounds hardened the Python validation/reject path, and this round
  edited only `kernel.cu` comments — the B200 correctness re-run confirms it stays
  bit-exact. Built via `tvm_ffi.cpp.load` (sm_100 gencode, `-std=c++17 -O3 -lineinfo`,
  no fast-math).
- Host: `ion-b200` (`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf_pr29315`,
  task workspace `/tmp/ltx2_task`.
- GPU: NVIDIA B200, **id 5** (only GPU visible under `CUDA_VISIBLE_DEVICES=5`),
  used consistently for build + correctness + benchmark; idle throughout (a separate
  `nvidia-smi -i 5` pre-check read 0% util / 0 MiB; the benchmark's captured
  before/after read 0% util with ≤4 MiB residual).
- Env: torch 2.11.0+cu130, CUDA 13.0, tvm_ffi 0.1.9.
- Benchmark settings: warmup 10, trials 7, inner-loop amplification to ≥1000 µs
  (CUDA events, A/B interleave, isolated subprocess). See `docs/benchmark_method.md`.

## Exact commands

```bash
# pinned to the idle B200 (GPU 5):
ssh ion-b200 'docker exec -e CUDA_VISIBLE_DEVICES=5 sglang_bbuf_pr29315 \
  bash -lc "cd /tmp/ltx2_task && python bench/correctness.py"'   # -> failures=0 skipped=0
ssh ion-b200 'docker exec -e CUDA_VISIBLE_DEVICES=5 sglang_bbuf_pr29315 \
  bash -lc "cd /tmp/ltx2_task && python bench/benchmark.py"'      # -> geomean 1.96x (as-shipped)
```

Raw `bench/results.jsonl` is kept locally as evidence (git-ignored; excluded from the PR).
