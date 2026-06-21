# Kernel Shape Inventory — sharegpt_low

- Model: `inclusionAI/Ring-2.5-1T`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2446.8 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 30.75 | 11592 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::sub` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 27.44 | 11520 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o819281921_tensorptrbf16gmemalign128o819281921_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[44, 8192], [], []], "Input Strides": [[8192, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 13.29 | 10944 | moe | ok | True | `fused_moe_kernel` | external_id=125156: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "True", "False", "False", "False", "True", "", "", "", "", "", "", "", "2.5", "", "", "False", ""], "Input ... |
| 7.52 | 25600 | gemm | ok | True | `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10collective13CollectiveMmaINS1_35MainloopSm100TmaUmmaWarpSpecializedILi13ELi2ELi4ENS5_IJNS4_1CILi1EEENSA_ILi4EEESB_EEEEENS5_IJNSA_ILi64EEESF_NSA_ILi128EEEEEENS_12float_e4m3_tENS5_IJlSB_lEEESI_SJ_NS4_8TiledMMAINS4_8MMA_AtomIJNS4_10MMA_TraitsINS4_19SM100_MMA_F8F6F4_SSEJSI_SI_fSF_SF_NS4_17integral_constantINS4_4UMMA5MajorELSQ_0EEESR_NSO_INSP_7ScaleInELSS_0EEEST_EEEEEENS4_6LayoutINS5_IJSB_SB_SB_EEENS5_IJNSA_ILi0EEESY_SY_EEEEENS5_IJNS4_10UnderscoreES11_S11_EEEEENS4_23SM90_TMA_LOAD_MULTICASTENS4_14ComposedLayoutINS4_7SwizzleILi3ELi4ELi3EEENS4_18smem_ptr_flag_bitsILi8EEENSW_INS5_IJNSA_ILi8EEESG_EEENS5_IJSG_SB_EEEEEEEvNS4_8identityENS4_13SM90_TMA_LOADES1E_vS1F_EENS_8epilogue10collective18CollectiveEpilogueINS1I_23Sm100TmaWarpSpecializedILi1ELi1ELi32ELb0ELb1EEEJSH_NS5_IJNSW_ISF_SB_EES1N_EEEvSJ_NS_10bfloat16_tESJ_NS1I_6fusion15Sm90TreeVisitorINS1Q_11Sm90ComputeINS_10multipliesES1P_fLNS_15FloatRoundStyleE2EvEEJNS1Q_16Sm90ColBroadcastILi0ESH_ffNS5_IJSB_SY_SY_EEELi4ELb1EEENS1R_INS1S_IS1T_ffLS1U_2EvEEJNS1Q_16Sm90RowBroadcastILi0ESH_ffNS5_IJSY_SB_SY_EEELi4ELb1EEENS1Q_12Sm90AccFetchEEEEEEENS4_5SM1004TMEM4LOAD26SM100_TMEM_LOAD_16dp256b8xES1G_NS15_IS17_NS18_ILi16EEENSW_INS5_IJS1A_SF_EEENS5_IJSF_SB_EEEEEEENS4_17SM75_U32x4_LDSM_NENS4_14SM90_TMA_STOREES2E_NS4_17SM90_U32x4_STSM_NENS4_39AutoVectorizingCopyWithAssumedAlignmentILi128EEEEEEvvEEEEvNT_6ParamsE` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 4.19 | 39744 | quant_gemm | ok | True | `void per_token_quant_fp8_small_batch_kernel<__nv_bfloat16, __nv_fp8_e4m3, 16>(__nv_bfloat16 const*, __nv_fp8_e4m3*, float*, long, long)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
