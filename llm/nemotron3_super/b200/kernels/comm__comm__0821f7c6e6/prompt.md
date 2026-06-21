# KDA Prompt: comm__comm__0821f7c6e6

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Model folder: `llm/nemotron3_super/b200`
- Kernel category: `comm`
- Max observed GPU share: `35.59%`
- Kernel name: `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 32.11% GPU, calls=3204, mean=37.14 us
- `random_mid`: 7.62% GPU, calls=2492, mean=52.36 us
- `random_high`: 3.54% GPU, calls=1780, mean=76.38 us
- `sharegpt_low`: 35.59% GPU, calls=3204, mean=42.68 us
- `sharegpt_mid`: 7.80% GPU, calls=2492, mean=43.35 us
- `sharegpt_high`: 2.05% GPU, calls=1424, mean=45.64 us

## Promoted Shape Samples

1. `sglang::outplace_all_reduce` via `external_id=4704`: `{"Concrete Inputs":["","",""],"Input Dims":[[38,4096],[],[]],"Input Strides":[[4096,1],[],[]],"Input type":["c10::BFloat16","",""]}`
2. `aten::reshape` via `external_id=5281`: `{"Concrete Inputs":["","[38, 2048]"],"Input Dims":[[38,2048],[]],"Input Strides":[[2048,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
3. `aten::as_strided` via `external_id=13380`: `{"Concrete Inputs":["","[38, 32]","[4640, 1]","4608"],"Input Dims":[[38,32],[],[],[]],"Input Strides":[[4640,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
4. `aten::view` via `external_id=14075`: `{"Concrete Inputs":["","[4, 1, 32768]"],"Input Dims":[[4,32768],[]],"Input Strides":[[32768,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
