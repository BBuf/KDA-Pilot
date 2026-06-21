# KDA Prompt: comm__comm__0821f7c6e6

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `deepseek-ai/DeepSeek-V4-Flash`
- Model folder: `llm/deepseek_v4/b200`
- Kernel category: `comm`
- Max observed GPU share: `36.16%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 34.98% GPU, calls=3432, mean=124.14 us
- `random_mid`: 4.18% GPU, calls=1896, mean=260.56 us
- `random_high`: 4.51% GPU, calls=384, mean=1183.58 us
- `sharegpt_low`: 36.16% GPU, calls=3432, mean=136.59 us
- `sharegpt_mid`: 13.55% GPU, calls=1896, mean=242.13 us
- `sharegpt_high`: 15.95% GPU, calls=744, mean=1127.72 us

## Promoted Shape Samples

1. `sglang::outplace_all_reduce` via `external_id=12013`: `{"Concrete Inputs":["","",""],"Input Dims":[[38,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","",""]}`
2. `aten::transpose` via `external_id=14006`: `{"Concrete Inputs":["","-1","-2"],"Input Dims":[[4,40],[],[]],"Input Strides":[[40,1],[],[]],"Input type":["int","Scalar","Scalar"]}`
3. `aten::slice` via `external_id=34434`: `{"Concrete Inputs":["","1","48","64","1"],"Input Dims":[[38,64,512],[],[],[],[]],"Input Strides":[[32768,512,1],[],[],[],[]],"Input type":["c10::BFloat16","Scalar","Scalar","Scalar","Scalar"]}`
4. `sglang::outplace_all_reduce` via `external_id=228560`: `{"Concrete Inputs":["","",""],"Input Dims":[[15,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
