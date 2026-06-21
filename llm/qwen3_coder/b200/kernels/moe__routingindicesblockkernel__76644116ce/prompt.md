# KDA Prompt: moe__routingindicesblockkernel__76644116ce

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
- Model folder: `llm/qwen3_coder/b200`
- Kernel category: `moe`
- Max observed GPU share: `2.17%`
- Kernel name: `void moe::dev::routing::routingCustom::routingIndicesBlockKernel<moe::dev::routing::routingCustom::KernelParams<__nv_bfloat16, __nv_bfloat16, 160, 8, moe::dev::routing::TopKExpertSelect<moe::dev::routing::NoOpPreprocess, moe::dev::routing::SoftmaxPostprocess> > >(moe::dev::routing::routingCustom::KernelParams<__nv_bfloat16, __nv_bfloat16, 160, 8, moe::dev::routing::TopKExpertSelect<moe::dev::routing::NoOpPreprocess, moe::dev::routing::SoftmaxPostprocess> >)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 2.17% GPU, calls=3968, mean=3.54 us

## Promoted Shape Samples

1. `aten::as_strided` via `external_id=4440`: `{"Concrete Inputs":["","[1]","[1]","0"],"Input Dims":[[512],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
