# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12440](https://github.com/NVIDIA/TensorRT-LLM/pull/12440)
- Source page: `sources/prs/tensorrt-llm/PR-12440.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12440`
- Generated at: `2026-05-20T15:18:08.027516+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-23T06:20:51Z`
- Merged: `2026-05-06T07:18:41Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 20
- Review threads observed: 20
- Resolved/outdated thread markers: resolved=20, outdated=4
- Human participants with discussion text: coderabbitai, liji-nv, nekorobov, rosenrodt, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-29T07:22:29Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 20 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#pullrequestreview-4194875366)
- `2026-04-29T07:29:29Z` `APPROVED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#pullrequestreview-4194911210)
- `2026-05-06T06:49:10Z` `APPROVED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#pullrequestreview-4233857189)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/KernelRunner.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x128x256_s6_et128x128_m256x128x64_c2x1x1_rN_TN_schPd2x1x2x3_biasFp32N_bM_rgTma_clmp_dynB_sm100f_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x32x256_s9_et128x32_m128x32x64_c1x1x1_rM_TN_transOut_schedS_biasFp32M_bN_rgTma_clmp_dynB_sm100f_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schedS_biasFp32M_bN_rgTma_clmp_dynB_sm100f_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x8x512u2_s4_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schedS_biasFp32M_bN_rgTma_clmp_sm100f_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E4m3_castE4m3_Fp32_Ab32_t128x64x256_s4_et128x64_m128x64x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100a_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E4m3_castE4m3_Fp32_Ab32_t128x8x256_s5_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schedS_biasFp32M_bN_rgTma_clmp_dynB_sm103a_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E4m3_castE4m3_Fp32_Ab32_t128x8x512_s3_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100a_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E4m3_castE4m3_Fp32_Ab32_t128x8x512u2_s3_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schedS_biasFp32M_bN_rgTma_clmp_dynB_sm100a_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E4m3_castE4m3_Fp32_Ab32_t128x8x512u2_s3_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100a_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E4m3_castE4m3_Fp32_Ab32_t128x8x512u2_s3_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm103a_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E4m3E4m3_Fp32_t128x128x128_s5_et64x128_m64x128x32_c1x1x1_rM_TN_transOut_noShflA_dsFp8_schedS_bN_rgTma_clmp_dynB_sm100f_cubin.cpp`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-29T07:22:29Z` `review` `COMMENTED` by `coderabbitai`; signals: epilogue, fp4, gemm, hang, kernel, layout, tensorrt, throughput; excerpt: "Actionable comments posted: 20 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#pullrequestreview-4194875366)
- `2026-04-29T07:22:25Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x8x512u2_s4_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schedS_biasFp32M_bN_rgTma_clmp_sm100f_cubin.cpp`:3; signals: block, compile, cute, gemm, kernel, moe, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50377 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#discussion_r3159230722)
- `2026-04-29T07:22:25Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E4m3_castE4m3_Fp32_Ab32_t128x8x512u2_s3_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schedS_biasFp32M_bN_rgTma_clmp_dynB_sm100a_cubin.cpp`:3; signals: compile, cuda, cute, gemm, kernel, pipeline, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50376 --- Ensure CI resolves Git LFS objects ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#discussion_r3159230745)
- `2026-04-29T07:22:25Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E4m3E4m3_Fp32_t128x128x128_s5_et64x128_m64x128x32_c1x1x1_rM_TN_transOut_noShflA_dsFp8_schedS_bN_rgTma_clmp_dynB_sm100f_cubin.cpp`:3; signals: cute, fp8, gemm, kernel, pipeline, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50376 --- Git LFS pointer stored as .cpp ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#discussion_r3159230758)
- `2026-04-29T07:22:25Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShflA_dsFp8_schedS_bN_rgTma_clmp_dynB_sm100f_cubin.cpp`:3; signals: compile, cuda, cute, fp8, gemm, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50377 --- Unresolved Git LFS pointers across 100+ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#discussion_r3159230770)
- `2026-04-29T07:22:25Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128_s4_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShflA_dsFp8_schedS_bN_rgTma_clmp_sm100f_cubin.cpp`:3; signals: compile, cuda, cute, fp8, gemm, kernel, pipeline, ptx; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50376 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#discussion_r3159230779)
- `2026-04-29T07:22:21Z` `issue` by `coderabbitai`; signals: blackwell, block, cuda, dtype, epilogue, fp4, fp8, gemm; excerpt: "📝 Walkthrough Walkthrough Refactors kernel selection logic in batched GEMM runner, introduces new bias/scheduling parameters and hybrid slice K optimization (Blackwell-only), adds bias row ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#issuecomment-4341661253)
- `2026-04-29T07:22:24Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x128x256_s6_et128x128_m256x128x64_c2x1x1_rN_TN_schPd2x1x2x3_biasFp32N_bM_rgTma_clmp_dynB_sm100f_cubin.cpp`:3; signals: cute, gemm, hang, kernel, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 261 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#discussion_r3159230696)
- `2026-04-29T07:22:25Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E4m3_castE4m3_Fp32_Ab32_t128x8x512u2_s3_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100a_cubin.cpp`:3; signals: cute, gemm, kernel, pipeline, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50377 --- Unresolved Git LFS pointers in cubin ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#discussion_r3159230751)
- `2026-04-29T07:22:25Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x256u2_s6_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f_cubin.cpp`:3; signals: compile, cute, gemm, kernel, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50376 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#discussion_r3159230786)
- `2026-04-29T07:22:24Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x32x256_s9_et128x32_m128x32x64_c1x1x1_rM_TN_transOut_schedS_biasFp32M_bN_rgTma_clmp_dynB_sm100f_cubin.cpp`:3; signals: cute, gemm, kernel, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50377 --- Exclude Git LFS pointer stubs from ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#discussion_r3159230707)
- `2026-04-29T07:22:25Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/batchedGemm/trtllmGen_bmm_export/cubins/Bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schedS_biasFp32M_bN_rgTma_clmp_dynB_sm100f_cubin.cpp`:3; signals: cute, gemm, kernel, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 4074 --- Add Git LFS tracking rule to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12440#discussion_r3159230715)
