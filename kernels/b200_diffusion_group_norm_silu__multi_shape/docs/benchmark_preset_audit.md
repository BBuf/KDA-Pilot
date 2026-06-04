# Benchmark Preset Audit — `b200_diffusion_group_norm_silu__multi_shape`

Family entry points: `group_norm_silu.apply_group_norm_silu`,
`group_norm_silu.triton_group_norm_silu`.

Authority: `../../docs/diffusion_benchmark_shape_coverage.md` (the union of
retained pre-reset captures and the fresh 2026-06-03 B200/H200 capture audit).
The current SGLang diffusion benchmark helper defines 20 presets; each is
audited below for this family. Per the task prompt, optimization is not ready
until every preset has a fresh capture row, a live no-call note, or an explicit
blocked status (blocked presets cannot be treated as no-call proof).

| # | Preset | Status for this family | Evidence |
|---|--------|------------------------|----------|
| 1 | `hunyuanvideo` | COVERED — all 160 retained live VAE rows in `bench/workloads.json` come from this preset | Retained capture `git show 35bc2c6b4~1:kernels/b200_diffusion_group_norm_silu__multi_shape/docs/captured_shapes_b200.jsonl` (host ion-b200, fp16, num_groups=32, eps=1e-6); regenerate/verify via `bench/gen_workloads.py --check` |
| 2 | `zimage` | LIVE NO-CALL — native B200 run completed without exercising these entry points | 2026-06-03 fresh-capture audit, `docs/diffusion_benchmark_shape_coverage.md` ("zimage ... live no-call for these entry points") |
| 3 | `firered-edit-1.1` | LIVE NO-CALL — native H200 run completed (64 target rows for other families), none for group_norm_silu | 2026-06-03 fresh-capture audit, same doc |
| 4 | `helios` | LIVE NO-CALL — native H200 run completed (LayerNorm/norm_scale_shift rows only) | 2026-06-03 fresh-capture audit, same doc |
| 5 | `ltx23-one-stage` | LIVE NO-CALL — native H200 run completed (split-RoPE rows only) | 2026-06-03 fresh-capture audit, same doc |
| 6 | `flux` | BLOCKED — Hugging Face 403 gated-repo access; run also fell back to diffusers backend, so no native shape evidence | 2026-06-03 audit; NOT usable as no-call proof |
| 7 | `flux2` | BLOCKED — same gated-access failure as `flux` | 2026-06-03 audit; NOT usable as no-call proof |
| 8 | `ltx23-two-stage-cfg-parallel` | BLOCKED — H200 OOM while loading the two-stage transformer; B200 retry stopped with incomplete `Lightricks/LTX-2.3` snapshot cache | 2026-06-03 audit; NOT usable as no-call proof |
| 9 | `hunyuan3d-shape` | RUNTIME-BLOCKED — fails at denoise step 0 (`cfg_policy` kwarg error); B200 retry reached no target rows | 2026-06-03 audit; explicitly "treat as runtime-blocked, not as a no-call proof" |
| 10 | `qwen` | RETAINED NO-CALL — retained captures show only QKNorm+RoPE / norm-scale-shift / scale-shift rows; group_norm_silu retained rows are hunyuanvideo-only | `docs/diffusion_benchmark_shape_coverage.md` family sections (required rows: "hunyuanvideo VAE shapes only") |
| 11 | `qwen-edit` | RETAINED NO-CALL — same basis as `qwen` | Same doc |
| 12 | `wan-t2v` | RETAINED NO-CALL — retained rows for this preset hit scale-shift/norm families only | Same doc |
| 13 | `wan-ti2v` | RETAINED NO-CALL — same basis | Same doc |
| 14 | `wan-i2v` | RETAINED NO-CALL — same basis | Same doc |
| 15 | `ltx2` | RETAINED NO-CALL — retained rows are split-RoPE only | Same doc |
| 16 | `ltx23-ti2v-two-stage` | RETAINED NO-CALL — retained rows are split-RoPE only | Same doc |
| 17 | `ltx23-two-stage` | RETAINED NO-CALL — retained rows are split-RoPE only | Same doc |
| 18 | `mova-720p` | RETAINED NO-CALL — retained rows hit norm-scale-shift family only | Same doc |
| 19 | `joyai-edit` | RETAINED NO-CALL — retained rows hit QKNorm+RoPE / norm-scale-shift families only | Same doc |
| 20 | `firered-edit-1.0` | RETAINED NO-CALL — retained rows hit scale-shift/norm families only | Same doc |

## Readiness Conclusion

- Every retained live shape row for this family/arch (160 rows, hunyuanvideo,
  B200 host) is present in `bench/workloads.json` (verified by
  `bench/gen_workloads.py --check`).
- Every current preset missing from the retained rows has a live no-call note
  (4 presets, 2026-06-03 audit), a retained no-call basis citing the shape
  coverage authority (11 presets), or an explicit blocked status (4 presets:
  `flux`, `flux2`, `ltx23-two-stage-cfg-parallel`, `hunyuan3d-shape`).
- Blocked presets are recorded as blocked, not as no-call proof. If any of
  them is later unblocked and captures group_norm_silu rows on B200, the
  workload set must be re-frozen and both sides remeasured before further
  tuning claims.
- Gate result: the task is READY for optimization under this audit.
