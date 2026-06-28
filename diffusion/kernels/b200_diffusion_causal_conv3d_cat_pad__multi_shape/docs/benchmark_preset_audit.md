# Benchmark Preset / Workload Audit

## Preset
- Preset: `cosmos3-nano-t2v`; model `nvidia/Cosmos3-Nano`; 832x480, 9 frames, 4 denoise steps.
- Entry point: `causal_conv3d_pad.fused_causal_conv3d_cat_pad` (`_fused_cat_pad_5d_kernel`).
- Original capture audit: 2026-06-24 (recorded in `../../docs/sglang_recent_diffusion_b200_profile_audit_2026-06-24.md` and `../../docs/diffusion_benchmark_shape_coverage.md`).

## Capture availability (re-checked 2026-06-25 on ion-b200)
- The capture file `/tmp/sglang_profile_b200/outputs/shape_captures/cosmos3-nano-t2v_no_compile_v2.jsonl` is **no longer present** on `ion-b200` (host `ion-b200`); `/tmp` was cleared since the 2026-06-24 audit. A recursive search under `/tmp` and `/home/sglang-omni` found no `cosmos3-nano-t2v_no_compile*.jsonl`.
- Consequence: the exact captured regression-row tensor metadata (cache-null / no-pad / non-contiguous) cannot be freshly extracted from the original capture.

## Production (headline) rows — retained
The 8 bf16 contiguous production rows in `bench/workloads.json` are retained verbatim from
`../../docs/diffusion_benchmark_shape_coverage.md` (section `diffusion_causal_conv3d_cat_pad__multi_shape`),
which were derived from the 2026-06-24 capture. These remain the frozen headline rows; the
geometric mean is computed over them only.

## Regression rows — synthesized (production:false, low-weight)
Because the original capture is unavailable and a fresh live capture requires running the full
Cosmos3-Nano T2V pipeline (model gated/heavy; disproportionate for low-weight regression coverage),
the regression rows are synthesized from the production shapes to exercise the kernel's branches:
- `reg_cache_null`: depth-0 cache tensor (`cache_t = 0`) — exercises the cache-null path.
- `reg_no_pad_cat_only`: `padding = [0,0,0,0,1,0]` with `cache_t = 1` (effective `depth_left = 0`, no spatial pad) — exercises the cat-only path.
These are `production:false` and excluded from the headline geometric mean.

## Non-contiguous contract decision (evidence-based)
The shape-coverage doc suggests including "captured non-contiguous rows." Resolution for this task:
- The upstream `_fused_cat_pad_5d_kernel` computes `x`/`cache` read offsets with **hardcoded
  C-contiguous stride formulas** and does not read tensor strides; the upstream wrapper does not
  call `.contiguous()`. The kernel therefore has **no correct non-contiguous behavior** — it would
  read the wrong elements (and potentially out of bounds) for a non-contiguous input.
- In a standalone A/B task where correctness is defined as "candidate bitwise-equals the copied
  baseline," a non-contiguous input has **no well-defined correct answer**: the baseline mis-reads it.
- No captured non-contiguous rows are available to define an alternative contract.

Therefore the supported contract is **contiguous-only**: the candidate (`solution/kernel.cu`) and the
correctness harness reject non-contiguous `x`/`cache` with a clear error (safer than replicating the
upstream's silent mis-read). `bench/correctness.py` keeps a non-contiguous **rejection** test. All 8
production rows are bf16 contiguous, so this does not affect the headline. If a future live capture
proves non-contiguous calls occur for this entry point, revisit with a stride-aware path and remeasure.
