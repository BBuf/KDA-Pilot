# KDA Prompt: moe__activationdeepseekkernel__b7453c53aa

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`moe` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `deepseek-ai/DeepSeek-Math-V2`
- Model folder: `llm/deepseek_math_v2/b200`
- Kernel category: `moe`
- Max observed GPU share: `4.80%`
- Kernel name: `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 4, true> >(moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 4, true>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_mid`: 4.80% GPU, calls=928, mean=221.14 us

## Promoted Shape Samples

1. `sglang::trtllm_fp8_block_scale_moe_wrapper` via `external_id=93686`: `{"Concrete Inputs":["","","","","","","","","256","8","8","4","2048","32","32","2.5","2","False","0","","16384","1","3"],"Input Dims":[[8661,256],[256],[8661,7168],[56,8661],[32,4096,7168],[32,32,56],[32,7168,2048],[32,56,16],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[256,1],[1],[7168,1],[8661,1],[29360128,7168,1],[1792,56,1],[14680064,2048,1],[896,16,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`
2. `sglang::trtllm_fp8_block_scale_moe_wrapper` via `external_id=1117835`: `{"Concrete Inputs":["","","","","","","","","256","8","8","4","2048","0","32","2.5","2","False","0","","16384","1","3"],"Input Dims":[[8661,256],[256],[8661,7168],[56,8661],[32,4096,7168],[32,32,56],[32,7168,2048],[32,56,16],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input Strides":[[256,1],[1],[7168,1],[8661,1],[29360128,7168,1],[1792,56,1],[14680064,2048,1],[896,16,1],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","c10::Float8_e4m3fn","float","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar","","Scalar","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
