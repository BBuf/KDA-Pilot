# KDA Prompt: comm__comm__0821f7c6e6

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `poolside/Laguna-XS.2-FP8`
- Model folder: `llm/poolside_laguna_xs2/b200`
- Kernel category: `comm`
- Max observed GPU share: `9.03%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 9.03% GPU, calls=2916, mean=6.79 us
- `random_mid`: 6.05% GPU, calls=2592, mean=13.08 us
- `sharegpt_mid`: 6.55% GPU, calls=2592, mean=12.88 us
- `sharegpt_high`: 8.85% GPU, calls=2268, mean=17.38 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=392`: `{"Concrete Inputs":["","[4097, 38]","[262148, 1]","0"],"Input Dims":[[4097,262148],[],[],[]],"Input Strides":[[262148,1],[],[],[]],"Input type":["int","ScalarList","ScalarList","Scalar"]}`
2. `aten::as_strided` via `external_id=3616`: `{"Concrete Inputs":["","[1, 1]","[0, 0]",""],"Input Dims":[[4097,262148],[],[],[]],"Input Strides":[[262148,1],[],[],[]],"Input type":["int","ScalarList","ScalarList",""]}`
3. `aten::permute` via `external_id=6398`: `{"Concrete Inputs":["","[0, 2, 1, 3]"],"Input Dims":[[54601,64,2,128],[]],"Input Strides":[[16384,256,128,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
4. `aten::empty_strided` via `external_id=8110`: `{"Concrete Inputs":["[140, 16, 128]","[2048, 128, 1]","15","0","","False"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
