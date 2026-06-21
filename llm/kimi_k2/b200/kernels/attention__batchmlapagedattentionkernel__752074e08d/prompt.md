# KDA Prompt: attention__batchmlapagedattentionkernel__752074e08d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`attention` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-K2-Instruct`
- Model folder: `llm/kimi_k2/b200`
- Kernel category: `attention`
- Max observed GPU share: `4.70%`
- Kernel name: `void flashinfer::mla::BatchMLAPagedAttentionKernel<flashinfer::mla::KernelTraits<true, 2u, true, 512u, 64u, 64u, 64u, __nv_bfloat16, __nv_bfloat16, __nv_bfloat16, int>, flashinfer::MLAParams<__nv_bfloat16, __nv_bfloat16, __nv_bfloat16, int> >(flashinfer::MLAParams<__nv_bfloat16, __nv_bfloat16, __nv_bfloat16, int>)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_high`: 4.70% GPU, calls=2440, mean=50.46 us

## Promoted Shape Samples

1. `sglang::unified_attention_with_output` via `external_id=97300`: `{"Concrete Inputs":["","","","","True","15","","","","","","",""],"Input Dims":[[1536,8,512],[1536,1,512],[1536,1,512],[1536,4096],[],[],[1536,8,64],[1536,1,64],[],[],[],[],[]],"Input Strides":[[512,786432,1],[512,512,1],[512,512,1],[4096,1],[],[],[1536,192,1],[2112,64,1],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","c10::BFloat16","c10::BFloat16","","","","",""]}`
2. `sglang::unified_attention_with_output` via `external_id=96820`: `{"Concrete Inputs":["","","","","True","0","","","","","","",""],"Input Dims":[[1536,8,512],[1536,1,512],[1536,1,512],[1536,4096],[],[],[1536,8,64],[1536,1,64],[],[],[],[],[]],"Input Strides":[[512,786432,1],[512,512,1],[512,512,1],[4096,1],[],[],[1536,192,1],[2112,64,1],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","c10::BFloat16","c10::BFloat16","","","","",""]}`
3. `sglang::unified_attention_with_output` via `external_id=96852`: `{"Concrete Inputs":["","","","","True","1","","","","","","",""],"Input Dims":[[1536,8,512],[1536,1,512],[1536,1,512],[1536,4096],[],[],[1536,8,64],[1536,1,64],[],[],[],[],[]],"Input Strides":[[512,786432,1],[512,512,1],[512,512,1],[4096,1],[],[],[1536,192,1],[2112,64,1],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","c10::BFloat16","c10::BFloat16","","","","",""]}`
4. `sglang::unified_attention_with_output` via `external_id=97204`: `{"Concrete Inputs":["","","","","True","12","","","","","","",""],"Input Dims":[[1536,8,512],[1536,1,512],[1536,1,512],[1536,4096],[],[],[1536,8,64],[1536,1,64],[],[],[],[],[]],"Input Strides":[[512,786432,1],[512,512,1],[512,512,1],[4096,1],[],[],[1536,192,1],[2112,64,1],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","c10::BFloat16","c10::BFloat16","","","","",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
