# KDA Prompt: moe_comm__notify_dispatch__4a6d3ee17e

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe_comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `zai-org/GLM-5.2-FP8`
- Model folder: `llm/glm_52/b200`
- Kernel category: `moe_comm`
- Max observed GPU share: `32.86%`
- Kernel name: `void deep_ep::intranode::notify_dispatch<8>(int const*, int*, int const*, int*, int, int, int, bool const*, int*, int*, int, int, void**, int**, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 32.86% GPU, calls=608, mean=1315.92 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=1083`: `{"Concrete Inputs":["","[7]","[1]","0"],"Input Dims":[[8,7],[],[],[]],"Input Strides":[[7,1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
