# KDA Prompt: comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ring-2.6-1T`
- Model folder: `llm/inclusion_ring26/b200`
- Kernel category: `comm`
- Max observed GPU share: `10.10%`
- Kernel name: `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 10.10% GPU, calls=1288, mean=784.24 us

## Promoted Shape Samples

1. `record_param_comms` via `external_id=33722`: `{"Concrete Inputs":["","","","7","","[]","[]","0","1","8"],"Input Dims":[[[16384,8192]],[],[],[],[],[],[],[],[],[]],"Input Strides":[[[8192,1]],[],[],[],[],[],[],[],[],[]],"Input type":["TensorList","","","Scalar","","ScalarList","ScalarList","Scalar","Scalar","Scalar"]}`
2. `sglang::_run_activation_inplace` via `external_id=33128`: `{"Concrete Inputs":["","",""],"Input Dims":[[],[16384,4608],[16384,2304]],"Input Strides":[[],[4608,1],[2304,1]],"Input type":["","c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
