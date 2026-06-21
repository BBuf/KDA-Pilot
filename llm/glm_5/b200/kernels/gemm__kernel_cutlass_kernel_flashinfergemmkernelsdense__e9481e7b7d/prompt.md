# KDA Prompt: gemm__kernel_cutlass_kernel_flashinfergemmkernelsdense__e9481e7b7d

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/GLM-5-NVFP4`
- Model folder: `llm/glm_5/b200`
- Kernel category: `gemm`
- Max observed GPU share: `2.26%`
- Kernel name: `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK11110000_PermutationMNK____MMAAtom_ThrID1_0`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 2.03% GPU, calls=2652, mean=18.56 us
- `random_high`: 2.26% GPU, calls=3063, mean=38.97 us

## Promoted Shape Samples

1. `sglang::fp4_gemm` via `external_id=20168`: `{"Concrete Inputs":["","","","","","15","6144"],"Input Dims":[[16873,3072],[3072,6144],[16896,384],[384,6144],[],[],[]],"Input Strides":[[3072,1],[1,3072],[384,1],[1,384],[],[],[]],"Input type":["unsigned char","unsigned char","unsigned char","c10::Float8_e4m3fn","float","Scalar","Scalar"]}`
2. `aten::view` via `external_id=20128`: `{"Concrete Inputs":["","[-1, 16, 256]"],"Input Dims":[[16873,16,256],[]],"Input Strides":[[4096,256,1],[]],"Input type":["c10::BFloat16","ScalarList"]}`
3. `sglang::fp4_gemm` via `external_id=71714`: `{"Concrete Inputs":["","","","","","15","6144"],"Input Dims":[[30796,3072],[3072,6144],[30848,384],[384,6144],[],[],[]],"Input Strides":[[3072,1],[1,3072],[384,1],[1,384],[],[],[]],"Input type":["unsigned char","unsigned char","unsigned char","c10::Float8_e4m3fn","float","Scalar","Scalar"]}`
4. `aten::as_strided` via `external_id=71426`: `{"Concrete Inputs":["","[30796, 16, 192]","[4096, 256, 1]","0"],"Input Dims":[[30796,16,256],[],[],[]],"Input Strides":[[4096,256,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
