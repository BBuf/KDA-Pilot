# KDA Prompt: moe_comm__cached_notify_combine__3b8f1bd9fe

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe_comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `zai-org/GLM-5.2-FP8`
- Model folder: `llm/glm_52/b200`
- Kernel category: `moe_comm`
- Max observed GPU share: `4.86%`
- Kernel name: `void deep_ep::intranode::cached_notify_combine<8>(void**, int*, int, int, int, int**, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 4.86% GPU, calls=608, mean=194.53 us

## Promoted Shape Samples

1. `aten::record_stream` via `external_id=27211`: `{"Concrete Inputs":["",""],"Input Dims":[[38,8],[]],"Input Strides":[[8,1],[]],"Input type":["float",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
