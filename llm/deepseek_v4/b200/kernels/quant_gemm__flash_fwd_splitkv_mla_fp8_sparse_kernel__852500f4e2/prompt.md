# KDA Prompt: quant_gemm__flash_fwd_splitkv_mla_fp8_sparse_kernel__852500f4e2

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `deepseek-ai/DeepSeek-V4-Flash`
- Model folder: `llm/deepseek_v4/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `4.11%`
- Kernel name: `void sm100::decode::head64::flash_fwd_splitkv_mla_fp8_sparse_kernel<sm100::decode::head64::KernelTemplate<(ModelType)1>, sm100::decode::head64::KernelTemplate<(ModelType)1>::TmaParams<cute::tuple<int, int, int, int>, cute::TiledCopy<cute::Copy_Atom<cute::Copy_Traits<cute::SM90_TMA_LOAD, cute::C<65536>, cute::AuxTmaParams<cute::tuple<cute::ScaledBasis<cute::C<1>, 1>, cute::ScaledBasis<cute::C<1>, 0>, cute::ScaledBasis<cute::C<1>, 2>, cute::ScaledBasis<cute::C<1>, 3> >, cute::Layout<cute::tuple<cute::C<64>, cute::C<64>, cute::C<1>, cute::C<1> >, cute::tuple<cute::ScaledBasis<cute::C<1>, 1>, cute::ScaledBasis<cute::C<1>, 0>, cute::ScaledBasis<cute::C<1>, 2>, cute::ScaledBasis<cute::C<1>, 3> > > const&, cute::Swizzle<3, 4, 3> const&> >, cutlass::bfloat16_t>, cute::Layout<cute::tuple<cute::C<1>, cute::tuple<cute::tuple<cute::tuple<cute::C<64>, cute::C<64> >, cute::C<8> > > >, cute::tuple<cute::C<0>, cute::tuple<cute::tuple<cute::tuple<cute::C<64>, cute::C<1> >, cute::C<4096> > > > >, cute::tuple<cute::C<64>, cute::C<512> > >, cute::tuple<int, int, int, int>, cute::TiledCopy<cute::Copy_Atom<cute::Copy_Traits<cute::SM90_TMA_STORE, cute::C<65536>, cute::AuxTmaParams<cute::tuple<cute::ScaledBasis<cute::C<1>, 1>, cute::ScaledBasis<cute::C<1>, 0>, cute::ScaledBasis<cute::C<1>, 2>, cute::ScaledBasis<cute::C<1>, 3> >, cute::Layout<cute::tuple<cute::C<64>, cute::C<64>, cute::C<1>, cute::C<1> >, cute::tuple<cute::ScaledBasis<cute::C<1>, 1>, cute::ScaledBasis<cute::C<1>, 0>, cute::ScaledBasis<cute::C<1>, 2>, cute::ScaledBasis<cute::C<1>, 3> > > const&, cute::Swizzle<3, 4, 3> const&> >, cutlass::bfloat16_t>, cute::Layout<cute::tuple<cute::C<1>, cute::tuple<cute::tuple<cute::tuple<cute::C<64>, cute::C<64> >, cute::C<1> > > >, cute::tuple<cute::C<0>, cute::tuple<cute::tuple<cute::tuple<cute::C<64>, cute::C<1> >, cute::C<0> > > > >, cute::tuple<cute::C<64>, cute::C<64> > > > >(SparseAttnDecodeParams, sm100::decode::head64::KernelTemplate<(ModelType)1>::TmaParams<cute::tuple<int, int, int, int>, cute::TiledCopy<cute::Copy_Atom<cute::Copy_Traits<cute::SM90_TMA_LOAD, cute::C<65536>, cute::AuxTmaParams<cute::tuple<cute::ScaledBasis<cute::C<1>, 1>, cute::ScaledBasis<cute::C<1>, 0>, cute::ScaledBasis<cute::C<1>, 2>, cute::ScaledBasis<cute::C<1>, 3> >, cute::Layout<cute::tuple<cute::C<64>, cute::C<64>, cute::C<1>, cute::C<1> >, cute::tuple<cute::ScaledBasis<cute::C<1>, 1>, cute::ScaledBasis<cute::C<1>, 0>, cute::ScaledBasis<cute::C<1>, 2>, cute::ScaledBasis<cute::C<1>, 3> > > const&, cute::Swizzle<3, 4, 3> const&> >, cutlass::bfloat16_t>, cute::Layout<cute::tuple<cute::C<1>, cute::tuple<cute::tuple<cute::tuple<cute::C<64>, cute::C<64> >, cute::C<8> > > >, cute::tuple<cute::C<0>, cute::tuple<cute::tuple<cute::tuple<cute::C<64>, cute::C<1> >, cute::C<4096> > > > >, cute::tuple<cute::C<64>, cute::C<512> > >, cute::tuple<int, int, int, int>, cute::TiledCopy<cute::Copy_Atom<cute::Copy_Traits<cute::SM90_TMA_STORE, cute::C<65536>, cute::AuxTmaParams<cute::tuple<cute::ScaledBasis<cute::C<1>, 1>, cute::ScaledBasis<cute::C<1>, 0>, cute::ScaledBasis<cute::C<1>, 2>, cute::ScaledBasis<cute::C<1>, 3> >, cute::Layout<cute::tuple<cute::C<64>, cute::C<64>, cute::C<1>, cute::C<1> >, cute::tuple<cute::ScaledBasis<cute::C<1>, 1>, cute::ScaledBasis<cute::C<1>, 0>, cute::ScaledBasis<cute::C<1>, 2>, cute::ScaledBasis<cute::C<1>, 3> > > const&, cute::Swizzle<3, 4, 3> const&> >, cutlass::bfloat16_t>, cute::Layout<cute::tuple<cute::C<1>, cute::tuple<cute::tuple<cute::tuple<cute::C<64>, cute::C<64> >, cute::C<1> > > >, cute::tuple<cute::C<0>, cute::tuple<cute::tuple<cute::tuple<cute::C<64>, cute::C<1> >, cute::C<0> > > > >, cute::tuple<cute::C<64>, cute::C<64> > > >)`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_mid`: 4.11% GPU, calls=1616, mean=86.09 us
- `sharegpt_high`: 2.70% GPU, calls=1592, mean=89.29 us

## Promoted Shape Samples

1. `sgl_kernel::sparse_decode_fwd` via `external_id=478971`: `{"Concrete Inputs":["","","","","","","","","","","512","0.044194173824159223"],"Input Dims":[[3286,1,64,512],[1988,256,1,584],[3286,1,128],[3286],[64],[148,8],[3287],[19873,64,1,584],[3286,1,512],[3286],[],[]],"Input Strides":[[32768,32768,512,1],[149760,584,584,1],[128,128,1],[1],[1],[8,1],[1],[37440,584,584,1],[512,512,1],[1],[],[]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","int","int","float","int","int","c10::Float8_e4m3fn","int","int","Scalar","Scalar"]}`
2. `sgl_kernel::sparse_decode_fwd` via `external_id=467569`: `{"Concrete Inputs":["","","","","","","","","","","512","0.044194173824159223"],"Input Dims":[[3286,1,64,512],[1988,256,1,584],[3286,1,128],[3286],[64],[],[],[19873,64,1,584],[3286,1,512],[3286],[],[]],"Input Strides":[[32768,32768,512,1],[149760,584,584,1],[128,128,1],[1],[1],[],[],[37440,584,584,1],[512,512,1],[1],[],[]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","int","int","float","","","c10::Float8_e4m3fn","int","int","Scalar","Scalar"]}`
3. `sgl_kernel::sparse_decode_fwd` via `external_id=600545`: `{"Concrete Inputs":["","","","","","","","","","","512","0.044194173824159223"],"Input Dims":[[1741,1,64,512],[1988,256,1,584],[1741,1,128],[1741],[64],[148,8],[1742],[19873,64,1,584],[1741,1,512],[1741],[],[]],"Input Strides":[[32768,32768,512,1],[149760,584,584,1],[128,128,1],[1],[1],[8,1],[1],[37440,584,584,1],[512,512,1],[1],[],[]],"Input type":["c10::BFloat16","c10::Float8_e4m3fn","int","int","float","int","int","c10::Float8_e4m3fn","int","int","Scalar","Scalar"]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
