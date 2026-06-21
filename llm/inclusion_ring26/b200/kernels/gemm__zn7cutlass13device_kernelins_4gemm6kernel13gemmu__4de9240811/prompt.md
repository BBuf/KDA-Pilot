# KDA Prompt: gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__4de9240811

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `inclusionAI/Ring-2.6-1T`
- Model folder: `llm/inclusion_ring26/b200`
- Kernel category: `gemm`
- Max observed GPU share: `6.88%`
- Kernel name: `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10collective13CollectiveMmaINS1_35MainloopSm100TmaUmmaWarpSpecializedILi17ELi2ELi4ENS5_IJNS4_1CILi2EEESB_NSA_ILi1EEEEEEEENS5_IJNSA_ILi256EEENSA_ILi128EEENSA_ILi64EEEEEENS_12float_e4m3_tENS5_IJlSC_lEEESJ_SK_NS4_8TiledMMAINS4_8MMA_AtomIJNS4_10MMA_TraitsINS4_25SM100_MMA_F8F6F4_2x1SM_SSEJSJ_SJ_fSF_SG_NS4_17integral_constantINS4_4UMMA5MajorELSR_0EEESS_NSP_INSQ_7ScaleInELST_0EEESU_EEEEEENS4_6LayoutINS5_IJSC_SC_SC_EEENS5_IJNSA_ILi0EEESZ_SZ_EEEEENS5_IJNS4_10UnderscoreES12_S12_EEEEENS4_28SM100_TMA_2SM_LOAD_MULTICASTENS4_14ComposedLayoutINS4_7SwizzleILi2ELi4ELi3EEENS4_18smem_ptr_flag_bitsILi8EEENSX_INS5_IJNSA_ILi8EEESH_EEENS5_IJSH_SC_EEEEEEEvNS4_8identityENS4_18SM100_TMA_2SM_LOADES1F_vS1G_EENS_8epilogue10collective18CollectiveEpilogueINS1J_23Sm100TmaWarpSpecializedILi4ELi2ELi32ELb0ELb1EEEJNS5_IJSG_SG_SH_EEENS5_IJNSX_ISG_SC_EENSX_INSA_ILi32EEESC_EEEEEvSK_NS_10bfloat16_tESK_NS1J_6fusion15Sm90TreeVisitorINS1U_11Sm90ComputeINS_10multipliesES1T_fLNS_15FloatRoundStyleE2EvEEJNS1U_16Sm90ColBroadcastILi0ESI_ffNS5_IJSC_SZ_SZ_EEELi4ELb1EEENS1V_INS1W_IS1X_ffLS1Y_2EvEEJNS1U_16Sm90RowBroadcastILi0ESI_ffNS5_IJSZ_SC_SZ_EEELi4ELb1EEENS1U_12Sm90AccFetchEEEEEEENS4_5SM1004TMEM4LOAD26SM100_TMEM_LOAD_32dp32b32xENS4_13SM90_TMA_LOADENS16_IS18_NS19_ILi16EEENSX_INS5_IJS1B_S1Q_EEENS5_IJS1Q_SC_EEEEEEENS4_39AutoVectorizingCopyWithAssumedAlignmentILi128EEENS4_14SM90_TMA_STOREES2J_S2L_S2L_EEEvvEEEEvNT_6ParamsE`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_mid`: 4.92% GPU, calls=6480, mean=75.88 us
- `random_high`: 6.88% GPU, calls=9680, mean=130.43 us
- `sharegpt_mid`: 3.89% GPU, calls=6480, mean=52.25 us
- `sharegpt_high`: 5.63% GPU, calls=9680, mean=98.71 us

## Promoted Shape Samples

1. `sgl_kernel::fp8_scaled_mm` via `external_id=33123`: `{"Concrete Inputs":["","","","","15",""],"Input Dims":[[16384,8192],[8192,4608],[16384,1],[4608,1],[],[]],"Input Strides":[[8192,1],[1,8192],[1,1],[1,1],[],[]],"Input type":["c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","float","Scalar",""]}`
2. `sgl_kernel::fp8_scaled_mm` via `external_id=166890`: `{"Concrete Inputs":["","","","","15",""],"Input Dims":[[10556,8192],[8192,4608],[10556,1],[4608,1],[],[]],"Input Strides":[[8192,1],[1,8192],[1,1],[1,1],[],[]],"Input type":["c10::Float8_e4m3fn","c10::Float8_e4m3fn","float","float","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
