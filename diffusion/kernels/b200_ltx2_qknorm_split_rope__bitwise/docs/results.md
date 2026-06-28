# Results — b200_ltx2_qknorm_split_rope__bitwise

## Outcome

**Bit-exact net improvement.** The candidate (reused `torch.nn.RMSNorm` + a single
fused split-RoPE CUDA kernel) is byte-for-byte equal (`torch.equal`, zero
tolerance) to the PyTorch eager baseline on all eight production rows, a regression
grid, and adversarial rounding-boundary inputs, while delivering an **equal-weight
geometric-mean speedup of ~2.56×** over the eager fallback on B200, faster on every
production row.

## Correctness gate (no tolerance; `torch.equal` on int16 bitcast) — `failures=0, skipped=0`

- Production rows (Section 1): **8/8 bit-equal** (q_out and k_out).
- Regression grid (Section 2): **12/12 bit-equal** (`head_dim∈{64,128}`, `num_heads=32`, `B∈{1,2}`, seq ∈ {129,126,257,1536}, cross-attn unequal Q/K).
- Adversarial rounding-boundary, stage-level (Section 3): **bit-equal**, with a
  sensitivity guard that tripped on **3419 elements** — a deliberately-wrong
  single-fp32-expression reference (no intermediate bf16 round of `first*cos`)
  differs from the eager fallback on those elements, proving the boundary data
  actually exercises the round-first-then-`addcmul` distinction, and the candidate
  matches the *correct* eager value.
- Candidate reject path, via `adapter.call_candidate` on mutated real cases
  (Section 4): **12/12** — base case accepted; TP≠1, non-`RMSNorm`, eps mismatch,
  fp32 weights, non-bf16 q, non-contiguous q, `head_dim` mismatch, 3-D cos,
  last-dim stride≠1, bad output shape, bad output dtype all raise `ValueError`
  before any kernel launch.
- Support-helper unit tests (Section 5): **7/7**.
- The runner is fail-closed: in normal mode any FAIL **or SKIP** in the CUDA
  sections (or CUDA unavailable) exits non-zero.

## Per-shape performance (B200, GPU 5, CUDA events, median over 7 trials)

| Workload | baseline med (µs) | candidate med (µs) | speedup | candidate p10–p90 |
|----------|------------------:|-------------------:|--------:|-------------------|
| stage1 video self q1536 k1536 d128 | 216.91 | 157.32 | 1.379× | 157.05–157.62 |
| stage1 audio self q126 k126 d64 | 128.51 | 26.47 | 4.854× | 23.47–28.57 |
| stage1 audio→video q1536 k126 d64 | 127.66 | 52.25 | 2.443× | 52.16–52.63 |
| stage1 video→audio q126 k1536 d64 | 183.91 | 53.02 | 3.468× | 52.55–54.70 |
| stage2 video self q6144 k6144 d128 | 410.42 | 291.81 | 1.406× | 290.97–292.35 |
| stage2 audio self q126 k126 d64 | 180.08 | 36.86 | 4.886× | 36.55–37.46 |
| stage2 audio→video q6144 k126 d64 | 193.51 | 87.91 | 2.201× | 87.60–88.29 |
| stage2 video→audio q126 k6144 d64 | 187.58 | 88.19 | 2.127× | 87.87–88.32 |

**Headline:** geomean **2.557×**, arithmetic mean 2.846×, min 1.379×, max 4.886× (8/8 production rows passed).

### Measurement note (honest variability)

The candidate is faster on every row in every run. The **geomean varies run-to-run
(~2.56×–2.71× observed)** because the eager baseline's small/cross rows are
launch/host-overhead-bound (their ~130–220 µs is dominated by per-launch CPU
overhead, not tensor size) and therefore sensitive to host-CPU contention from
other jobs on the shared box; the candidate (single GPU-bound kernel) is stable
(its p10–p90 spread is tight). The reported numbers are from the final candidate
(with validate-once; see `docs/benchmark_method.md`). The win is robust: min
per-row ≥ 1.38× even on the worst row, under contention.

## Roofline-style rationale (active bound)

Memory-bound elementwise + small-reduction op. The eager baseline runs split-RoPE
as a chain of separate ATen ops (`reshape/swapaxes` → `split_x*cos` → two
`addcmul_` → `reshape/swapaxes`), each a kernel launch reading/writing bf16
intermediates through HBM plus fixed launch overhead.
- **Small / cross rows (S=126):** dominated by fixed per-launch overhead, so
  collapsing the chain into one fused kernel yields 2.4–4.9×.
- **Large video-self rows (S=1536/6144, d=128):** HBM traffic + the shared
  (`torch`) RMSNorm dominate, so the gain is ~1.40×; the fused kernel reads
  `q_normed`+`cos`+`sin` once and writes `out` once — near the memory-bound floor
  for the RoPE stage. The remaining headroom is the shared RMSNorm.

## Optimization directions (Codex `analyze`; for a future upper-bound round)

Ranked by benefit-vs-risk for pushing the large d128 rows past 1.40× while keeping
strict bit-exactness:
1. **Vectorized 128-bit bf16 load/store** for the RoPE fast path — 5–15% on large
   rows, low bit-exactness risk (arithmetic order/round points unchanged), medium effort.
2. **Shape specialization d64 vs d128** — 5–12%, low–medium risk, medium effort.
3. **Fuse RMSNorm into the kernel** (eliminate the `q_normed` HBM round-trip) —
   highest benefit (~15–35% on large rows) but **high bit-exactness risk** and high
   effort: must clone torch RMSNorm's fp32 reduction order/tree, eps placement in
   `rsqrt(mean(x*x)+eps)`, rsqrt-vs-sqrt+reciprocal, weight-multiply order, and the
   exact bf16 downcast point. First-try bit-exact probability ~20–35%. De-risk by
   first building a standalone RMSNorm that is bit-exact vs torch on all
   production/regression/adversarial rows, then composing, then removing the intermediate.
4. Occupancy/block-size tuning — NCU-gated, 0–10%.

**NCU decision:** a roofline rationale is sufficient to ACCEPT the staged candidate
(bit-exact, clear win). NCU is warranted only for the next edit targeting the large
rows; a short pass on one large video-self row should answer: (a) is DRAM/L2
throughput near roofline or is there memory-instruction inefficiency (→ vectorize
first)?; (b) are bytes/sector and load/store transactions clean for the strided
cos/sin, or is alignment wasting traffic?; (c) do eligible-warps/occupancy/stalls
point to latency/occupancy tuning instead of HBM-byte reduction? NCU was NOT run
this round (not required for acceptance).

## How the bit-exactness is achieved

- **RMSNorm:** reused `torch.nn.RMSNorm(H, eps)` unchanged (bit-exact by construction).
- **Split RoPE:** the CUDA kernel rounds `first*cos`/`second*cos` to bf16 first
  (matching `split_x*cos`), then adds the sine term via fp32 `__fmaf_rn` + one bf16
  round (`__float2bfloat16_rn`), matching PyTorch `addcmul_` (fp32 opmath). No
  `--use_fast_math`; cos/sin indexed via real strides. The hypothesis was confirmed
  bit-exact on B200 on the first attempt.

## Provenance

- Baseline source: SGLang `main` @ `aaa31eb0a11e09f9511bade5e815907ec0b91fa0`
  (`apply_split_rotary_emb` eager fallback). See `docs/baseline_source.md`.
- Candidate source hash (AC-9): `solution/kernel.cu` sha256
  `01d105cf0b9540b120e1ebe334e4a2d29d37ea94249e1d29ce182ed8008f8f09`; built via
  `tvm_ffi.cpp.load` (sm_100 gencode, `-std=c++17 -O3 -lineinfo`, no fast-math).
- Host: `ion-b200` (`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf_pr29315`,
  task workspace `/tmp/ltx2_task`.
- GPU: NVIDIA B200, **id 5**, used consistently for build + correctness + benchmark.
  Idle throughout: a separate pre-benchmark `nvidia-smi -i 5` read `0% util, 0 MiB`;
  the benchmark's own captured `nvidia_smi_before/after` read `0% util` with ≤4 MiB
  residual on GPU 5 (other GPUs were busy — id 5 was the idle card selected).
- Env: torch 2.11.0+cu130, CUDA 13.0, tvm_ffi 0.1.9.
- Benchmark settings: warmup 10, trials 7, inner-loop amplification to ≥1000 µs
  (CUDA events, A/B interleave, isolated subprocess). See `docs/benchmark_method.md`.

## Exact commands

```bash
# pinned to the idle B200 (GPU 5):
ssh ion-b200 'docker exec -e CUDA_VISIBLE_DEVICES=5 sglang_bbuf_pr29315 \
  bash -lc "cd /tmp/ltx2_task && python bench/correctness.py"'   # -> failures=0 skipped=0
ssh ion-b200 'docker exec -e CUDA_VISIBLE_DEVICES=5 sglang_bbuf_pr29315 \
  bash -lc "cd /tmp/ltx2_task && python bench/benchmark.py"'      # -> geomean 2.56x
```

Raw `bench/results.jsonl` is kept locally as evidence (git-ignored; excluded from the PR).
