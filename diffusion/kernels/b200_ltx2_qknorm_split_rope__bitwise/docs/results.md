# Results — b200_ltx2_qknorm_split_rope__bitwise

## Outcome

**Bit-exact net improvement.** The candidate (reused `torch.nn.RMSNorm` + a single
fused split-RoPE CUDA kernel) is byte-for-byte equal (`torch.equal`, zero
tolerance) to the PyTorch eager baseline on all eight production rows, the
regression grid, and adversarial rounding-boundary inputs, while delivering an
**equal-weight geometric-mean speedup of 2.71×** over the eager fallback on B200.

## Correctness gate (no tolerance; `torch.equal` on int16 bitcast)

- Production rows: **8/8 bit-equal** (q_out and k_out).
- Regression grid (`head_dim∈{64,128}`, `num_heads=32`, `B∈{1,2}`, seq ∈ {129,126,257,1536}, cross-attn unequal Q/K): **12/12 bit-equal**.
- Adversarial rounding-boundary (`d128`, S=257): **bit-equal**.
- Reject/negative tests (TP≠1, non-bf16, non-contiguous x, interleaved/3-D cos, cos last-dim stride≠1): **6/6 reject as expected**.
- `failures=0, skipped=0`.

## Per-shape performance (B200, GPU 5, CUDA events, median over 7 trials)

| Workload | baseline med (µs) | candidate med (µs) | speedup | baseline p10–p90 | candidate p10–p90 |
|----------|------------------:|-------------------:|--------:|------------------|-------------------|
| stage1 video self q1536 k1536 d128 | 221.18 | 158.19 | 1.398× | 219.56–225.40 | 157.94–158.82 |
| stage1 audio self q126 k126 d64 | 182.91 | 37.09 | 4.932× | 181.50–187.06 | 36.63–38.00 |
| stage1 audio→video q1536 k126 d64 | 191.96 | 52.84 | 3.633× | 183.16–194.59 | 52.76–53.01 |
| stage1 video→audio q126 k1536 d64 | 186.18 | 52.81 | 3.526× | 183.14–194.00 | 52.72–52.97 |
| stage2 video self q6144 k6144 d128 | 408.42 | 291.87 | 1.399× | 406.77–412.01 | 290.91–292.53 |
| stage2 audio self q126 k126 d64 | 189.33 | 37.15 | 5.096× | 188.29–199.41 | 36.56–38.27 |
| stage2 audio→video q6144 k126 d64 | 185.93 | 87.86 | 2.116× | 178.42–191.01 | 87.32–88.27 |
| stage2 video→audio q126 k6144 d64 | 189.72 | 88.01 | 2.156× | 185.88–192.40 | 87.75–88.38 |

**Headline:** geomean **2.706×**, arithmetic mean 3.032×, min 1.398×, max 5.096× (8/8 production rows passed).

## Roofline-style rationale (active bound)

This is a memory-bound elementwise + small-reduction op. The eager baseline runs
the split-RoPE as a chain of separate ATen ops — `reshape/swapaxes` →
`split_x*cos` → two `addcmul_` → `reshape/swapaxes` — each a separate kernel
launch that reads/writes bf16 intermediates through HBM, plus fixed per-launch
overhead.

- **Small / cross rows (S=126):** total time is dominated by fixed per-launch
  overhead (~180–190 µs regardless of the tiny tensor), so collapsing the RoPE
  chain into one fused kernel yields 3.5–5.1×.
- **Large video-self rows (S=1536/6144, d=128):** HBM traffic dominates and the
  RMSNorm (shared, `torch`) is a large fixed cost on both sides, so the gain is
  ~1.40×; the fused kernel still removes the `split_x*cos` intermediate write/read
  and extra launches. The candidate reads `q_normed`+`cos`+`sin` once and writes
  `out` once — near the memory-bound floor for the RoPE stage. The remaining
  headroom is the shared RMSNorm, which a future fused RMSNorm+RoPE kernel
  (upper bound) could attack.

## How the bit-exactness is achieved

- **RMSNorm:** reused `torch.nn.RMSNorm(H, eps)` unchanged (bit-exact by construction).
- **Split RoPE:** the CUDA kernel rounds `first*cos` / `second*cos` to bf16 first
  (matching the standalone `split_x*cos_u`), then adds the sine term with an fp32
  fused-multiply-add and a single bf16 round (`__fmaf_rn` + `__float2bfloat16_rn`),
  matching PyTorch's `addcmul_` (fp32 opmath). No `--use_fast_math`; cos/sin
  indexed via real strides (non-contiguous production layout). The fp32-fma
  hypothesis was confirmed bit-exact on B200 on the first attempt.

## Provenance

- Baseline source: SGLang `main` @ `aaa31eb0a11e09f9511bade5e815907ec0b91fa0`
  (`apply_split_rotary_emb` eager fallback). See `docs/baseline_source.md`.
- Candidate: `solution/kernel.cu` (committed at `62f511a84`), built via
  `tvm_ffi.cpp.load` (sm_100 gencode, `-std=c++17 -O3 -lineinfo`, no fast-math).
- Host: `ion-b200` (`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf_pr29315`,
  task workspace `/tmp/ltx2_task`.
- GPU: NVIDIA B200, **id 5**, idle before (0% util, 0 MiB) and after (0% util, 4 MiB);
  other GPUs busy — id 5 used consistently for build + correctness + benchmark.
- Env: torch 2.11.0+cu130, CUDA 13.0, tvm_ffi 0.1.9.
- Benchmark settings: warmup 10, trials 7, inner-loop amplification to ≥1000 µs
  (CUDA events, A/B interleave, isolated subprocess). See `docs/benchmark_method.md`.

## Exact commands

```bash
# build + correctness + benchmark, pinned to the idle B200 (GPU 5):
ssh ion-b200 'docker exec -e CUDA_VISIBLE_DEVICES=5 sglang_bbuf_pr29315 \
  bash -lc "cd /tmp/ltx2_task && python -c \"from solution.build import load_candidate_module; load_candidate_module()\""'
ssh ion-b200 'docker exec -e CUDA_VISIBLE_DEVICES=5 sglang_bbuf_pr29315 \
  bash -lc "cd /tmp/ltx2_task && python bench/correctness.py"'
ssh ion-b200 'docker exec -e CUDA_VISIBLE_DEVICES=5 sglang_bbuf_pr29315 \
  bash -lc "cd /tmp/ltx2_task && python bench/benchmark.py"'
```

Raw `bench/results.jsonl` is kept locally as evidence (git-ignored; excluded from the PR).
