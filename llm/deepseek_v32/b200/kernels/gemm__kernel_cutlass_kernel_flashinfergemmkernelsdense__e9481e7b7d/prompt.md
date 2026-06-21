# KDA Prompt: gemm__kernel_cutlass_kernel_flashinfergemmkernelsdense__e9481e7b7d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Model folder: `llm/deepseek_v32/b200`
- Kernel category: `gemm`
- Max observed GPU share: `3.57%`
- Kernel name: `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK11110000_PermutationMNK____MMAAtom_ThrID1_0`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.59% GPU, calls=4705, mean=19.06 us
- `sharegpt_mid`: 3.57% GPU, calls=4211, mean=16.94 us

## Promoted Shape Samples

1. `sglang::fp4_gemm` via `external_id=18043`: `{"Concrete Inputs":["","","","","","15","9216"],"Input Dims":[[11134,3584],[3584,9216],[11136,448],[448,9216],[],[],[]],"Input Strides":[[3584,1],[1,3584],[448,1],[1,448],[],[],[]],"Input type":["unsigned char","unsigned char","unsigned char","c10::Float8_e4m3fn","float","Scalar","Scalar"]}`
2. `aten::copy_` via `external_id=17725`: `{"Concrete Inputs":["","","False"],"Input Dims":[[11134,32,64],[11134,32,64],[]],"Input Strides":[[6144,192,1],[6144,192,1],[]],"Input type":["c10::BFloat16","c10::BFloat16","Scalar"]}`
3. `PythonDispatchMode` via `external_id=95081`: `{"Concrete Inputs":[""],"Input Dims":[[33161216]],"Input Strides":[[1]],"Input type":["int"]}`
4. `sglang::fp4_gemm` via `external_id=95689`: `{"Concrete Inputs":["","","","","","15","9216"],"Input Dims":[[8630,3584],[3584,9216],[8704,448],[448,9216],[],[],[]],"Input Strides":[[3584,1],[1,3584],[448,1],[1,448],[],[],[]],"Input type":["unsigned char","unsigned char","unsigned char","c10::Float8_e4m3fn","float","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
