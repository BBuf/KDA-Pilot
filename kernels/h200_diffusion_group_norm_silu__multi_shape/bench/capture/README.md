# LTX preset shape-capture (audit evidence)

Reduced-step live captures for the LTX two-stage presets, scheduled before the
workload freeze (preset audit, DEC-5). The shim wraps the two GroupNorm+SiLU
entry points at import time inside the capture run's processes; nothing on
disk is patched, and the shim is never active for correctness/benchmark runs.

Usage on the remote H200 box (inside the container, from the SGLang repo):

```bash
export PYTHONPATH=/path/to/task/bench/capture:$PYTHONPATH
export GNS_CAPTURE_OUT=/path/to/task/docs/captured_shapes_ltx_h200.jsonl
export GNS_CAPTURE_MODEL=<preset-name>
export GNS_CAPTURE_ARCH=h200
python python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/scripts/bench_diffusion_denoise.py \
    --preset <preset-name> --num-inference-steps <small>   # upsampler shapes are step-count independent
```

Presets: `ltx2`, `ltx23-ti2v-two-stage`, `ltx23-two-stage` (canonical
resolutions from the preset table; only the step count may be reduced).

Each completed run yields either capture rows (recorded into the audit +
`bench/workloads.json` as `production=false` diagnostics) or a live no-call
proof for `docs/benchmark_preset_audit.md`.
