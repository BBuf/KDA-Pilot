# Dispatch decision table — b200_diffusion_qknorm_rope__multi_shape

The registered `optimized_wrapper` is an **evidence-gated dispatcher** (no env var):

- Production config (`head_dim=128, rope_dim=128, is_neox=False, bf16, contiguous q/k`):
  - `num_tokens >= 512` (large bucket) → **`QKNormRopeStagedKernel`** (CTA-per-token cos/sin staging)
  - `num_tokens < 512` (small bucket) → **SGLang baseline** (`fused_inplace_qknorm_rope`)
- Any non-production dtype/head_dim/rope_dim/is_neox, non-contiguous layout, or other
  signature → **SGLang baseline** fallback (explicit, before the C++ `TensorMatcher`).

`KDA_CAND_VARIANT={warp,staged}` overrides the route for experiments only. Threshold
512 splits the captured buckets cleanly (production small ≤195, large ≥4096).

## Evidence (device-fair interleaved, B200 GPU 4, commit `69ae5b366`/`e2b54594a`)

Device-fair = both kernels timed through their **direct JIT modules** (symmetric, no
`register_custom_op`); warp-variant sanity geomean **0.9994x** confirms fairness.
Baseline medians from the frozen `benchmark.csv` (commit `68a32061`).

| shape | bucket | route | baseline µs | staged device-fair speedup | promote/reject |
|-------|--------|-------|-------------|----------------------------|----------------|
| joyai-edit B7904/H32 | large | staged | 89.2 | **1.26x** | PROMOTE |
| qwen B4096/H24 | large | staged | 59.3 | **1.18x** | PROMOTE |
| qwen-edit B8424/H24 | large | staged | 95.6 | **1.20x** | PROMOTE |
| zimage B4096/H30 | large | staged | 73.6 | **1.10x** | PROMOTE |
| zimage B4128/H30 | large | staged | 74.0 | **1.10x** | PROMOTE |
| qwen B19/H24 | small | baseline | 60.7 | 1.01x (staged ≈ no win) | REJECT staging → baseline |
| qwen B47/H24 | small | baseline | 60.8 | 1.00x | REJECT staging → baseline |
| qwen-edit B195/H24 | small | baseline | 61.2 | 1.01x | REJECT staging → baseline |
| qwen-edit B189/H24 | small | baseline | 61.2 | 0.99x | REJECT staging → baseline |
| zimage B32/H30 | small | baseline | 61.5 | 1.00x | REJECT staging → baseline |

**Production device-fair geomean = 1.0787x** (large staged win; small unchanged).

## Why small shapes route to baseline (NCU evidence)
`profile/baseline_b200/REPORT.md`: small shapes are **launch/dispatch-bound** — the
device kernel is only ~7.55µs vs ~60µs end-to-end (~88% host dispatch), and the grid is
tiny (114 < 148 SMs, 0.10 waves/SM). Staging needs even more CTAs per token, so it does
not help (device-fair ~1.0x / slightly slower). The device kernel is not the small-shape
bottleneck; routing small → the proven SGLang baseline is the correct, low-risk choice.

## Why large shapes route to staged (NCU evidence)
`profile/staged_b200/REPORT.md`: staging cuts `long_scoreboard` 11.9 → 9.29 and device
time 109.6 → 88.1 µs on B8424 (the float32 cos/sin row is staged once per token and
reused across heads instead of re-read per head).

## Integrated install-path note (AC-4)
A `register_custom_op`-wrapped integrated benchmark (`benchmark.py --integrated`) is
**confounded**: the small/baseline route re-enters the baseline's own `register_custom_op`
inside the candidate's custom op (double wrapping → artificial ~0.72x), and the run hit a
high-variance window. In production, `kda_kernels.install()` **replaces** the public op
with the dispatcher (no double layer), so small → baseline = 1.0x. The clean device-win
evidence is the device-fair comparison above. A faithful integrated validation via the
`kda_kernels` plain-dispatcher install path is deferred to the export milestone (AC-8),
where the export machinery provides it natively.
