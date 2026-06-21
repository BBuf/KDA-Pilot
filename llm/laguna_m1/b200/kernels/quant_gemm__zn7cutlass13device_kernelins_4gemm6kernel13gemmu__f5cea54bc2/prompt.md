# KDA Prompt: quant_gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__f5cea54bc2

Develop an optimized SGLang kernel or wrapper path for the profiler-backed
`quant_gemm` opportunity below on NVIDIA B200. This task is
seeded only from external-id-bound torch-profiler shape samples collected
during real SGLang serving runs.

## Evidence

- Model: `poolside/Laguna-M.1-NVFP4`
- Model folder: `llm/laguna_m1/b200`
- Kernel category: `quant_gemm`
- Max observed GPU share: `29.53%`
- Kernel name: `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalINS1_17GroupProblemShapeIN4cute5tupleIJiiiEEEEENS1_10collective13CollectiveMmaINS1_51MainloopSm100ArrayTmaUmmaWarpSpecializedBlockScaledILi9ELi8ELi2ENS6_IJNS5_1CILi1EEESD_SD_EEENS_4arch5Sm100EEENS6_IJNSC_ILi128EEESI_SI_EEENS6_IJNS_12float_e2m1_tENS_13float_ue4m3_tEEEENS6_IJPNS6_IJlSD_NSC_ILi0EEEEEEPNS5_6LayoutINS6_IJNS6_IJNS6_IJNSC_ILi32EEENSC_ILi4EEEEEEiEEENS6_IJNS6_IJNSC_ILi16EEESS_EEEiEEENS6_IJSD_iEEEEEENS6_IJSX_NS6_IJNS6_IJSN_SD_EEENSC_ILi512EEEEEENS6_IJSN_iEEEEEEEEEEESM_S17_NS5_8TiledMMAINS5_8MMA_AtomIJNS5_17SM100_MMA_MXF4_SSISK_SK_fSL_Li128ELi128ELi16ELNS5_4UMMA5MajorE0ELS1C_0ELNS1B_7ScaleInE0ELS1D_0EEEEEENSQ_ISE_NS6_IJSN_SN_SN_EEEEENS6_IJNS5_10UnderscoreES1I_S1I_EEEEENS6_IJNS5_13SM90_TMA_LOADES1L_EEENS6_IJNS5_14ComposedLayoutINS5_7SwizzleILi2ELi4ELi3EEENS5_18smem_ptr_flag_bitsILi4EEENSQ_INS6_IJNSC_ILi8EEESI_EEENS6_IJSI_SD_EEEEEEENSQ_INS6_IJNS6_IJNS6_IJST_SD_EEESW_EEESD_NS6_IJSD_NSC_ILi2EEEEEEEEENS6_IJNS6_IJNS6_IJSW_S11_EEES10_EEESN_NS6_IJSS_S11_EEEEEEEEEEEvNS5_8identityES1M_S27_vS28_EENS_8epilogue10collective18CollectiveEpilogueINS2A_31Sm100PtrArrayTmaWarpSpecializedILi3ELi2ELi64ELb1ELb0EEEJSJ_NS6_IJSI_NSC_ILi64EEEEEENS_10bfloat16_tESP_S2H_SP_NS2A_6fusion15FusionCallbacksIS2E_NS2I_17LinearCombinationIS2H_fS2H_fLNS_15FloatRoundStyleE2EEESJ_S2G_JEEENS5_5SM1004TMEM4LOAD26SM100_TMEM_LOAD_32dp32b64xES1L_NS1N_INS1O_ILi3ELi4ELi3EEENS1Q_ILi16EEENSQ_INS6_IJS1S_S2F_EEENS6_IJS2F_SD_EEEEEEENS5_39AutoVectorizingCopyWithAssumedAlignmentILi128EEENS5_14SM90_TMA_STOREES2X_S2Z_S2Z_EEEvvEEEEvNT_6ParamsE`
- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.
- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.

## Workload Appearances

- `random_low`: 17.91% GPU, calls=9648, mean=19.04 us
- `random_mid`: 23.10% GPU, calls=9648, mean=90.71 us
- `random_high`: 29.53% GPU, calls=9648, mean=81.15 us
- `sharegpt_low`: 18.17% GPU, calls=9648, mean=19.64 us
- `sharegpt_mid`: 19.88% GPU, calls=9648, mean=105.50 us
- `sharegpt_high`: 29.36% GPU, calls=9648, mean=76.93 us

## Promoted Shape Samples

1. `aten::empty` via `external_id=236`: `{"Concrete Inputs":["[2]","3","0","","","0"],"Input Dims":[[],[],[],[],[],[]],"Input Strides":[[],[],[],[],[],[]],"Input type":["ScalarList","Scalar","Scalar","","","Scalar"]}`
2. `aten::to` via `external_id=12227`: `{"Concrete Inputs":["","","6","False","False",""],"Input Dims":[[17],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[]],"Input type":["float","","Scalar","Scalar","Scalar",""]}`
3. `aten::as_strided` via `external_id=28070`: `{"Concrete Inputs":["","[2774, 1, 128]","[1280, 128, 1]","0"],"Input Dims":[[2816,1,128],[],[],[]],"Input Strides":[[1280,128,1],[],[],[]],"Input type":["c10::BFloat16","ScalarList","ScalarList","Scalar"]}`
4. `aten::_to_copy` via `external_id=35130`: `{"Concrete Inputs":["","3","","","","False",""],"Input Dims":[[1],[],[],[],[],[],[]],"Input Strides":[[1],[],[],[],[],[],[]],"Input type":["long int","Scalar","","","","Scalar",""]}`

The complete evidence bundle is in `docs/evidence.json`. Recover the current
SGLang baseline before writing optimized code, then build a local correctness
and benchmark harness under this task folder. Use the same ABI for baseline
and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.

## Completion Bar

- Correctness passes for every promoted shape sample and relevant dtype/layout.
- Benchmark compares candidate against the current SGLang baseline on an idle B200.
- NCU or benchmark evidence explains the bottleneck and the final design.
- Unsupported shapes must fall back to the recovered SGLang baseline.
