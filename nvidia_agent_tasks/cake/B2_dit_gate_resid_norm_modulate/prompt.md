# Fused DiT gate + residual + norm + shift/scale (bit-exact)

**Target agent:** CAKE / kernel-design  **Task id:** `B2_dit_gate_resid_norm_modulate`

**Model:** `Qwen-Image, Z-Image, LTX-2, MiniMax-H3 (all DiT blocks with adaLN modulation)`
**Serving command this workload came from (SGLang cookbook recipe):**

```bash
sglang serve <model> (denoise loop)
```

**Measured share:** elementwise residue after our existing fusions is 1-4% of a step (image / short-sequence models at the high end)

## Kernels in scope

- `diffusion_fused_ln_modulate`
- `diffusion_modulate_scale_shift`

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang, editable install) - the same
implementation the deployment above runs. Do not benchmark against a naive
PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- TRT-LLM already ships this kernel as `fusedDiTGateResidNormShiftScale` in `visual_gen`
  (three variants, Apache-2.0). Relative to what SGLang already fuses, the delta is the
  gate multiply, the residual add and the dual output. We would rather have it built and
  validated with you than re-derive it, and the shapes below say which variants are
  worth having.
- Honest framing: this is the smallest item in this handoff. Our elementwise kernels
  already run at 70-88% of achievable bandwidth, so the ceiling is the 1-4% pass-count
  saving, and it only clears our 2% end-to-end bar on the image / short-sequence models.
  Skip it if you are short on cycles - C1/C2/C3 are the load-bearing ones.

## Correctness gate

- Bit-exact. We gate diffusion fusions on md5-identical output frames, and we have done
  this for aten LayerNorm before (Welford order, FFMA, rcp/rsqrtf sequence replicated at
  SASS level) - that is the standard here, because a 1e-6 drift compounds over 50
  denoise steps.

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic
call counts, and `tensors/` (where present) holds real input/output/state payloads
captured from the running model. `docs/capture_provenance.md` records exactly how
they were produced, including the GSM8K accuracy of the serving run they came from.

Selection rule, restated: shapes are real, ranked by production call count, split
into real-traffic vs warmup-only, and cover the full (sequence length x
concurrency x dataset) matrix - not a single shape.

## Notes

- Sequence-packed modulation (per-row indexed adaLN) is the variant we lack and want
  most; see the row set for the packed shapes.

## Deliverable

1. Kernel source in `solution/`, buildable standalone against the copied baseline
   ABI (`baseline/`).
2. Benchmark output per workload row: baseline vs candidate, CUDA-graph timed,
   interleaved A/B - see `../../docs/measurement_contract.md`.
3. Correctness-gate output as defined above.
4. If you used Nsight Compute, the report and the bottleneck it identified.
