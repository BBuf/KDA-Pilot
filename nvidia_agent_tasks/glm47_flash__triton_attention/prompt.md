# Triton unified attention, extend + decode (GLM-4.7-Flash)

**Task:** `glm47_flash__triton_attention`

**Model:** `zai-org/GLM-4.7-Flash`
**Serving command this workload came from (SGLang cookbook recipe):**

```bash
python -m sglang.launch_server --model zai-org/GLM-4.7-Flash --reasoning-parser glm45 --tool-call-parser glm47 --attention-backend triton --tp 1 --host 0.0.0.0 --port 8000
```

**Measured share:** **75.3%** of total serving GPU time (cookbook-aligned profiler sweep, peak scenario ShareGPT at concurrency 32). Tonight's capture confirms the call counts on the same recipe, and the same kernels are **50.8%** of Qwen3-Next at 32k input.

## Kernels in scope

- `triton_decode_attention`
- `triton_decode_attention_grouped`
- `triton_extend_attention`

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang, editable install) - the same
implementation the deployment above runs. Do not benchmark against a naive
PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- Highest single-kernel share we have ever measured in this sweep - and `--attention-
  backend triton` is not a fallback here, it is what the SGLang cookbook recipe for
  GLM-4.7-Flash prescribes, so every user of this model runs this kernel.
- No FlashAttention / FlashInfer / TRT-LLM path covers this model's attention shape
  today, so there is no vendor kernel to fall back on: the Triton kernel IS the
  production kernel.

## Correctness gate

- Stateless: exact-shape output comparison against the copied Triton baseline on every
  workload row, plus the paged-KV gather semantics (`kv_indptr` / `kv_indices`)
  preserved for ragged batches.
- Rows include the padded / mixed-length decode batches that the real scheduler
  produced; a candidate that only handles uniform batches fails.

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic
call counts, and `tensors/` (where present) holds real input/output/state payloads
captured from the running model. `docs/capture_provenance.md` records exactly how
they were produced, including the GSM8K accuracy of the serving run they came from.

Selection rule, restated: shapes are real, ranked by production call count, split
into real-traffic vs warmup-only, and cover the full (sequence length x
concurrency x dataset) matrix - not a single shape.

## Notes

- The KV pool is multi-GB, so the payload stores the *gathered* rows the call actually
  reads (`in_k_buffer__gathered` + `in_k_buffer__rows`) instead of the whole pool.
  Rebuild a compact pool from those rows.
- GLM-4.7-Flash also drives the Triton fused-MoE path (223k calls in this capture) -
  that data is in the A4 task.

## Deliverable

1. Kernel source in `solution/`, buildable standalone against the copied baseline
   ABI (`baseline/`).
2. Benchmark output per workload row: baseline vs candidate, CUDA-graph timed,
   interleaved A/B - see `../docs/measurement_contract.md`.
3. Correctness-gate output as defined above.
4. If you used Nsight Compute, the report and the bottleneck it identified.
