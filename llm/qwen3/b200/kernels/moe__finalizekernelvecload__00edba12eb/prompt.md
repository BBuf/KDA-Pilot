# KDA Prompt: moe__finalizekernelvecload__00edba12eb

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-235B-A22B-Instruct-2507`
- Model folder: `llm/qwen3/b200`
- Kernel category: `moe`
- Max observed GPU share: `4.08%`
- Kernel name: `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 4.08% GPU, calls=1504, mean=70.33 us
- `random_high`: 3.12% GPU, calls=6016, mean=10.67 us
- `sharegpt_mid`: 2.85% GPU, calls=1504, mean=35.64 us

## Promoted Shape Samples

1. `aten::floor_divide` via `external_id=13394`: `{"Concrete Inputs":["",""],"Input Dims":[[20],[]],"Input Strides":[[1],[]],"Input type":["long int","long int"]}`
2. `aten::as_strided` via `external_id=30441`: `{"Concrete Inputs":["","[2358, 1, 128]","[1280, 128, 1]","0"],"Input Dims":[[2560,1,128],[],[],[]],"Input Strides":[[1280,128,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
3. `aten::lift_fresh` via `external_id=47523`: `{"Concrete Inputs":[""],"Input Dims":[[14]],"Input Strides":[[1]],"Input type":["int"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
