# KDA Prompt: attention__fmhasm100fkernel_qkve4m3obfloat16hqk576hv512page__ff06b37547

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`attention` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Model folder: `llm/deepseek_v32/b200`
- Kernel category: `attention`
- Max observed GPU share: `6.49%`
- Kernel name: `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512PagedKvDenseStaticTokenSparseP1VarSeqQ32Kv128PersistentSwapsAbForGen`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_high`: 2.84% GPU, calls=1708, mean=29.22 us
- `sharegpt_high`: 6.49% GPU, calls=1952, mean=48.51 us

## Promoted Shape Samples

1. `aten::copy_` via `external_id=44448`: `{"Concrete Inputs":["","","True"],"Input Dims":[[31],[31],[]],"Input Strides":[[1],[1],[]],"Input type":["int","int","Scalar"]}`
2. `sglang::unified_attention_with_output` via `external_id=47556`: `{"Concrete Inputs":["","","","","True","26","","","","","False","",""],"Input Dims":[[896,32,512],[896,1,512],[896,1,512],[896,16384],[],[],[896,32,64],[896,1,64],[],[164096,64],[],[],[896,2048]],"Input Strides":[[512,458752,1],[512,512,1],[512,512,1],[16384,1],[],[],[6144,192,1],[2112,64,1],[],[64,1],[],[],[2048,1]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","c10::BFloat16","c10::BFloat16","","float","Scalar","","int"]}`
3. `sglang::unified_attention_with_output` via `external_id=45190`: `{"Concrete Inputs":["","","","","True","0","","","","","False","",""],"Input Dims":[[896,32,512],[896,1,512],[896,1,512],[896,16384],[],[],[896,32,64],[896,1,64],[],[164096,64],[],[],[896,2048]],"Input Strides":[[512,458752,1],[512,512,1],[512,512,1],[16384,1],[],[],[6144,192,1],[2112,64,1],[],[64,1],[],[],[2048,1]],"Input type":["c10::BFloat16","c10::BFloat16","c10::BFloat16","c10::BFloat16","Scalar","Scalar","c10::BFloat16","c10::BFloat16","","float","Scalar","","int"]}`
4. `aten::as_strided` via `external_id=46723`: `{"Concrete Inputs":["","[894, 64, 128]","[8192, 128, 1]","0"],"Input Dims":[[894,64,128],[],[],[]],"Input Strides":[[8192,128,1],[],[],[]],"Input type":["c10::Float8_e4m3fn","ScalarList","ScalarList","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
