# KDA Prompt: gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__64c6383c7f

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`
- Model folder: `llm/nemotron3_nano/b200`
- Kernel category: `gemm`
- Max observed GPU share: `2.11%`
- Kernel name: `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10collective13CollectiveMmaINS1_35MainloopSm100TmaUmmaWarpSpecializedILi13ELi2ELi4ENS5_IJNS4_1CILi1EEESB_SB_EEEEENS5_IJNSA_ILi64EEESE_NSA_ILi128EEEEEENS_12float_e4m3_tENS5_IJlSB_lEEESH_SI_NS4_8TiledMMAINS4_8MMA_AtomIJNS4_10MMA_TraitsINS4_19SM100_MMA_F8F6F4_SSEJSH_SH_fSE_SE_NS4_17integral_constantINS4_4UMMA5MajorELSP_0EEESQ_NSN_INSO_7ScaleInELSR_0EEESS_EEEEEENS4_6LayoutISC_NS5_IJNSA_ILi0EEESW_SW_EEEEENS5_IJNS4_10UnderscoreESZ_SZ_EEEEENS4_13SM90_TMA_LOADENS4_14ComposedLayoutINS4_7SwizzleILi3ELi4ELi3EEENS4_18smem_ptr_flag_bitsILi8EEENSV_INS5_IJNSA_ILi8EEESF_EEENS5_IJSF_SB_EEEEEEEvNS4_8identityES12_S1C_vS1D_EENS_8epilogue10collective18CollectiveEpilogueINS1F_23Sm100TmaWarpSpecializedILi1ELi1ELi32ELb0ELb1EEEJSG_NS5_IJNSV_ISE_SB_EES1K_EEEvSI_NS_10bfloat16_tESI_NS1F_6fusion15Sm90TreeVisitorINS1N_11Sm90ComputeINS_10multipliesES1M_fLNS_15FloatRoundStyleE2EvEEJNS1N_16Sm90ColBroadcastILi0ESG_ffNS5_IJSB_SW_SW_EEELi4ELb1EEENS1O_INS1P_IS1Q_ffLS1R_2EvEEJNS1N_16Sm90RowBroadcastILi0ESG_ffNS5_IJSW_SB_SW_EEELi4ELb1EEENS1N_12Sm90AccFetchEEEEEEENS4_5SM1004TMEM4LOAD26SM100_TMEM_LOAD_16dp256b8xES12_NS13_IS15_NS16_ILi16EEENSV_INS5_IJS18_SE_EEENS5_IJSE_SB_EEEEEEENS4_17SM75_U32x4_LDSM_NENS4_14SM90_TMA_STOREES2B_NS4_17SM90_U32x4_STSM_NENS4_39AutoVectorizingCopyWithAssumedAlignmentILi128EEEEEEvvEEEEvNT_6ParamsE`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_low`: 2.11% GPU, calls=80, mean=7.26 us

## Promoted Shape Samples

1. `sgl_kernel::fp8_scaled_mm` via `external_id=50055`: `{"Concrete Inputs":["","","","","15",""],"Input Dims":[[18,2688],[2688,10304],[18,1],[10304,1],[],[]],"Input Strides":[[2688,1],[1,2688],[1,1],[1,1],[],[]],"Input type":["c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","float","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
