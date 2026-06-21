# KDA Prompt: comm__comm__a12cdaa5b4

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `stepfun-ai/Step-3.7-Flash-NVFP4`
- Model folder: `llm/step_37_flash/b200`
- Kernel category: `comm`
- Max observed GPU share: `38.59%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 36.73% GPU, calls=6552, mean=68.92 us
- `random_mid`: 23.47% GPU, calls=5824, mean=108.70 us
- `sharegpt_low`: 38.59% GPU, calls=6552, mean=82.09 us
- `sharegpt_mid`: 21.40% GPU, calls=5096, mean=145.54 us
- `sharegpt_high`: 27.51% GPU, calls=1456, mean=780.53 us

## Promoted Shape Samples

1. `sglang::outplace_all_reduce` via `external_id=8433`: `{"Concrete Inputs":["","",""],"Input Dims":[[56,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","",""]}`
2. `aten::bitwise_or` via `external_id=60348`: `{"Concrete Inputs":["",""],"Input Dims":[[16,8],[16,8]],"Input Strides":[[8,1],[8,1]],"Input type":["int","int"]}`
3. `sglang::outplace_all_reduce` via `external_id=60866`: `{"Concrete Inputs":["","",""],"Input Dims":[[16,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","",""]}`
4. `aten::_reshape_alias` via `external_id=69468`: `{"Concrete Inputs":["","[16, 128]","[1280, 1]"],"Input Dims":[[16,128],[],[]],"Input Strides":[[1280,1],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
