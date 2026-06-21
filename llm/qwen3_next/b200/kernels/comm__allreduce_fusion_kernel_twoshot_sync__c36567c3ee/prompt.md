# KDA Prompt: comm__allreduce_fusion_kernel_twoshot_sync__c36567c3ee

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`comm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3-Next-80B-A3B-Instruct`
- Model folder: `llm/qwen3_next/b200`
- Kernel category: `comm`
- Max observed GPU share: `16.11%`
- Kernel name: `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>, std::array<int, 8>, std::array<int, 8>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 16.11% GPU, calls=760, mean=901.81 us
- `sharegpt_high`: 10.72% GPU, calls=760, mean=1177.73 us

## Promoted Shape Samples

1. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=30455`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","True"],"Input Dims":[[687,2048],[687,2048],[2048],[],[],[],[],[],[]],"Input Strides":[[2048,1],[2048,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `sglang::store_cache` via `external_id=30439`: `{"Concrete Inputs":["","","","","","512","0","4959741"],"Input Dims":[[687,256],[687,256],[4959741,256],[4959741,256],[687],[],[],[]],"Input Strides":[[256,1],[1536,1],[256,1],[256,1],[1],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","long int","Scalar","Scalar","Scalar"]}`
3. `sglang::flashinfer_allreduce_residual_rmsnorm` via `external_id=160474`: `{"Concrete Inputs":["","","","9.9999999999999995e-07","2048","","False","False","True"],"Input Dims":[[785,2048],[785,2048],[2048],[],[],[],[],[],[]],"Input Strides":[[2048,1],[2048,1],[1],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
4. `aten::mm` via `external_id=160444`: `{"Concrete Inputs":["",""],"Input Dims":[[785,2048],[2048,1]],"Input Strides":[[2048,1],[1,2048]],"Input type":["c10::BFloat16","c10::BFloat16"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
