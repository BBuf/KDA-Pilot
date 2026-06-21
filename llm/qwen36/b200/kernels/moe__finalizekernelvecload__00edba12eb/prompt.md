# KDA Prompt: moe__finalizekernelvecload__00edba12eb

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `Qwen/Qwen3.6-35B-A3B-FP8`
- Model folder: `llm/qwen36/b200`
- Kernel category: `moe`
- Max observed GPU share: `2.14%`
- Kernel name: `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.14% GPU, calls=328, mean=23.80 us

## Promoted Shape Samples

1. `sglang::trtllm_fp8_block_scale_moe_wrapper` via `external_id=55139`: `{"Concrete Inputs":["","","","","","","","","256","8","","","512","0","256","1.","4","False","0","","16384","1","3"],"Input Dims":[[15434,256],[],[15434,2048],[16,15434],[256,1024,2048],[256,8,16],[256,2048,512],[256,16,4],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[256,1],[],[2048,1],[15434,1],[2097152,2048,1],[128,16,1],[1048576,512,1],[64,4,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","Scalar","Scalar","","","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
