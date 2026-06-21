# KDA Prompt: gemm__kernel_cutlass_kernel_flashinfergemmkernelsdense__dcb59f24e5

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Model folder: `llm/deepseek_v32/b200`
- Kernel category: `gemm`
- Max observed GPU share: `2.61%`
- Kernel name: `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK21111000_PermutationMNK____MMAAtom_ThrID2_0`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.39% GPU, calls=3706, mean=11.36 us
- `sharegpt_high`: 2.61% GPU, calls=3587, mean=10.64 us

## Promoted Shape Samples

1. `sglang::fp4_gemm` via `external_id=53932`: `{"Concrete Inputs":["","","","","","15","9216"],"Input Dims":[[2121,3584],[3584,9216],[2176,448],[448,9216],[],[],[]],"Input Strides":[[3584,1],[1,3584],[448,1],[1,448],[],[],[]],"Input type":["unsigned char","unsigned char","unsigned char","c10::Float8_e4m3fn","float","Scalar","Scalar"]}`
2. `aten::empty` via `external_id=54130`: `{"Concrete Inputs":["[2121, 9216]","15","","","False",""],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","","","Scalar",""]}`
3. `aten::as_strided` via `external_id=140515`: `{"Concrete Inputs":["","[]","[]","16"],"Input Dims":[[65],[],[],[]],"Input Strides":[[1],[],[],[]],"Input type":["long int","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
