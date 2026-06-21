# KDA Prompt: gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__12e4691976

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ring-2.5-1T`
- Model folder: `llm/ring_25_1t/b200`
- Kernel category: `gemm`
- Max observed GPU share: `2.18%`
- Kernel name: `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10collective13CollectiveMmaINS1_35MainloopSm100TmaUmmaWarpSpecializedILi13ELi2ELi4ENS5_IJNS4_1CILi2EEENSA_ILi1EEESC_EEEEENS5_IJNSA_ILi128EEESF_SF_EEENS_12float_e4m3_tENS5_IJlSC_lEEESH_SI_NS4_8TiledMMAINS4_8MMA_AtomIJNS4_10MMA_TraitsINS4_25SM100_MMA_F8F6F4_2x1SM_SSEJSH_SH_fSF_SF_NS4_17integral_constantINS4_4UMMA5MajorELSP_0EEESQ_NSN_INSO_7ScaleInELSR_0EEESS_EEEEEENS4_6LayoutINS5_IJSC_SC_SC_EEENS5_IJNSA_ILi0EEESX_SX_EEEEENS5_IJNS4_10UnderscoreES10_S10_EEEEENS4_18SM100_TMA_2SM_LOADENS4_14ComposedLayoutINS4_7SwizzleILi3ELi4ELi3EEENS4_18smem_ptr_flag_bitsILi8EEENSV_INS5_IJNSA_ILi8EEESF_EEENS5_IJSF_SC_EEEEEEEvNS4_8identityES13_S1D_vS1E_EENS_8epilogue10collective18CollectiveEpilogueINS1G_23Sm100TmaWarpSpecializedILi2ELi2ELi32ELb0ELb1EEEJNS5_IJNSA_ILi64EEESF_SF_EEENS5_IJNSV_IS1L_SC_EENSV_INS5_IJNSA_ILi32EEESB_EEENS5_IJSC_S1L_EEEEEEEEvSI_NS_10bfloat16_tESI_NS1G_6fusion15Sm90TreeVisitorINS1U_11Sm90ComputeINS_10multipliesES1T_fLNS_15FloatRoundStyleE2EvEEJNS1U_16Sm90ColBroadcastILi0ESG_ffNS5_IJSC_SX_SX_EEELi4ELb1EEENS1V_INS1W_IS1X_ffLS1Y_2EvEEJNS1U_16Sm90RowBroadcastILi0ESG_ffNS5_IJSX_SC_SX_EEELi4ELb1EEENS1U_12Sm90AccFetchEEEEEEENS4_5SM1004TMEM4LOAD26SM100_TMEM_LOAD_32dp32b32xENS4_13SM90_TMA_LOADENS14_INS15_ILi2ELi4ELi3EEENS17_ILi16EEENSV_INS5_IJS19_S1O_EEENS5_IJS1O_SC_EEEEEEENS4_39AutoVectorizingCopyWithAssumedAlignmentILi128EEENS4_14SM90_TMA_STOREES2K_S2M_S2M_EEEvvEEEEvNT_6ParamsE`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `sharegpt_high`: 2.18% GPU, calls=19280, mean=7.64 us

## Promoted Shape Samples

1. `sgl_kernel::fp8_scaled_mm` via `external_id=224816`: `{"Concrete Inputs":["","","","","15",""],"Input Dims":[[189,8192],[8192,4608],[189,1],[4608,1],[],[]],"Input Strides":[[8192,1],[1,8192],[1,1],[1,1],[],[]],"Input type":["c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","float","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
