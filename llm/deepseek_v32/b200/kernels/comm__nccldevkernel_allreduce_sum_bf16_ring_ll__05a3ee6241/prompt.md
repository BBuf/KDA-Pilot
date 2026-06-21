# KDA Prompt: comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Model folder: `llm/deepseek_v32/b200`
- Kernel category: `comm`
- Max observed GPU share: `57.13%`
- Kernel name: `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 57.13% GPU, calls=492, mean=4022.14 us
- `sharegpt_mid`: 15.00% GPU, calls=492, mean=609.76 us

## Promoted Shape Samples

1. `aten::fill_` via `external_id=18471`: `{"Concrete Inputs":["","0"],"Input Dims":[[11136,4096],[]],"Input Strides":[[4096,1],[]],"Input type":["c10::BFloat16","Scalar"]}`
2. `sglang::hadamard_transform` via `external_id=17701`: `{"Concrete Inputs":["","0.088388347648318447"],"Input Dims":[[11134,128],[]],"Input Strides":[[128,1],[]],"Input type":["c10::BFloat16","Scalar"]}`
3. `record_param_comms` via `external_id=17659`: `{"Concrete Inputs":["","","","0","","[]","[]","0","1","4"],"Input Dims":[[[11134,7168]],[],[],[],[],[],[],[],[],[]],"Input Strides":[[[7168,1]],[],[],[],[],[],[],[],[],[]],"Input type":["TensorList","","","Scalar","","ScalarList","ScalarList","Scalar","Scalar","Scalar"]}`
4. `aten::clone` via `external_id=95057`: `{"Concrete Inputs":["",""],"Input Dims":[[552320],[]],"Input Strides":[[1],[]],"Input type":["float",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
