# KDA Prompt: quant_gemm__per_token_group_quant_8bit_kernel__cd3c819d72

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `moonshotai/Kimi-K2-Instruct`
- Model folder: `llm/kimi_k2/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `12.64%`
- Kernel name: `void per_token_group_quant_8bit_kernel<NaiveScheduler, 128, 8, __nv_bfloat16, c10::Float8_e4m3fn, true, true, false, unsigned int>(__nv_bfloat16 const*, c10::Float8_e4m3fn*, unsigned int*, int const*, int, int, int, int, int)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 12.64% GPU, calls=21960, mean=4.72 us
- `random_mid`: 2.42% GPU, calls=23424, mean=7.23 us
- `sharegpt_mid`: 6.30% GPU, calls=22936, mean=8.17 us

## Promoted Shape Samples

1. `aten::narrow` via `external_id=252`: `{"Concrete Inputs":["","0","1","1"],"Input Dims":[[2],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","Scalar","Scalar","Scalar"]}`
2. `aten::as_strided` via `external_id=5034`: `{"Concrete Inputs":["","[38]","[1]","0"],"Input Dims":[[2048],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`
3. `sgl_kernel::sgl_per_token_group_quant_8bit_v2` via `external_id=9842`: `{"Concrete Inputs":["","","","128","1e-10","-448.","448.","True","False",""],"Input Dims":[[8084,7168],[8084,7168],[8084,14],[],[],[],[],[],[],[]],"Input Strides":[[7168,1],[7168,1],[1,8084],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","int","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar",""]}`
4. `sgl_kernel::sgl_per_token_group_quant_8bit_v2` via `external_id=71051`: `{"Concrete Inputs":["","","","128","1e-10","-448.","448.","True","False",""],"Input Dims":[[7407,2304],[7407,2304],[7407,5],[],[],[],[],[],[],[]],"Input Strides":[[2304,1],[2304,1],[1,7408],[],[],[],[],[],[],[]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","int","Scalar","Scalar","Scalar","Scalar","Scalar","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
