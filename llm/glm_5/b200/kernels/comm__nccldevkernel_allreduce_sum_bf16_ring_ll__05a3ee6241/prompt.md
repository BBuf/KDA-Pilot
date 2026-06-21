# KDA Prompt: comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/GLM-5-NVFP4`
- Model folder: `llm/glm_5/b200`
- Kernel category: `comm`
- Max observed GPU share: `14.65%`
- Kernel name: `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_mid`: 14.65% GPU, calls=628, mean=548.45 us

## Promoted Shape Samples

1. `record_param_comms` via `external_id=124329`: `{"Concrete Inputs":["","","","3","","[]","[]","0","1","4"],"Input Dims":[[[9962,6144]],[],[],[],[],[],[],[],[],[]],"Input Strides":[[[6144,1]],[],[],[],[],[],[],[],[],[]],"Input type":["TensorList","","","Scalar","","ScalarList","ScalarList","Scalar","Scalar","Scalar"]}`
2. `aten::empty_strided` via `external_id=123779`: `{"Concrete Inputs":["[318784]","[1]","6","0","",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","ScalarList","Scalar","Scalar","",""]}`
3. `aten::resize_` via `external_id=118600`: `{"Concrete Inputs":["","[231]",""],"Input Dims":[[0],[],[]],"Input Strides":[[1],[],[]],"Input type":["int","ScalarList",""]}`
4. `triton_poi_fused_mul_unsqueeze_0` via `external_id=124040`: `{"Concrete Inputs":["","","0.088388347648318447","318784"],"Input Dims":[[9962,32,1],[9962,32,1],[],[]],"Input Strides":[[32,1,1],[32,1,1],[],[]],"Input type":["float","float","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
