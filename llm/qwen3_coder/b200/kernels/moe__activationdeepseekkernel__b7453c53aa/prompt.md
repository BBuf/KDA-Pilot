# KDA Prompt: moe__activationdeepseekkernel__b7453c53aa

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
- Model folder: `llm/qwen3_coder/b200`
- Kernel category: `moe`
- Max observed GPU share: `10.56%`
- Kernel name: `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 4, true> >(moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 4, true>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 10.56% GPU, calls=3968, mean=91.81 us
- `random_high`: 5.43% GPU, calls=3968, mean=24.29 us
- `sharegpt_mid`: 8.56% GPU, calls=3472, mean=47.01 us

## Promoted Shape Samples

1. `sglang::trtllm_fp8_block_scale_moe_wrapper` via `external_id=13473`: `{"Concrete Inputs":["","","","","","","","","160","8","","","2560","80","20","1.","1","False","0","","16384","1","3"],"Input Dims":[[11011,160],[],[11011,6144],[48,11011],[20,5120,6144],[20,40,48],[20,6144,2560],[20,48,20],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[160,1],[],[6144,1],[11011,1],[31457280,6144,1],[1920,48,1],[15728640,2560,1],[960,20,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","Scalar","Scalar","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `aten::as_strided` via `external_id=28954`: `{"Concrete Inputs":["","[1]","[1]","447"],"Input Dims":[[448],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`
3. `aten::lift_fresh` via `external_id=43593`: `{"Concrete Inputs":[""],"Input Dims":[[]],"Input Strides":[[]],"Input type":["int"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
