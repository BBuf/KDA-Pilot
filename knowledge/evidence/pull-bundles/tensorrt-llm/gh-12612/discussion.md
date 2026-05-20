# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12612](https://github.com/NVIDIA/TensorRT-LLM/pull/12612)
- Source page: `sources/prs/tensorrt-llm/PR-12612.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12612`
- Generated at: `2026-05-20T15:18:12.875708+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-31T06:40:54Z`
- Merged: `2026-04-07T02:48:16Z`

## Discussion Counts

- Issue comments: 27
- Review submissions: 8 (approved=3, commented=5)
- Inline review comments: 11
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=4
- Human participants with discussion text: coderabbitai, mzweilz, niukuo, pengbowang-nv, tensorrt-cicd, yunruis, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-31T06:57:14Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 7 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#pullrequestreview-4035128109)
- `2026-03-31T15:58:50Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#pullrequestreview-4038437120)
- `2026-04-01T04:36:17Z` `COMMENTED` by `yunruis` (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#pullrequestreview-4041607573)
- `2026-04-01T05:11:57Z` `COMMENTED` by `pengbowang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#pullrequestreview-4041711309)
- `2026-04-01T05:58:20Z` `APPROVED` by `niukuo` - jenkins/: LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#pullrequestreview-4041852968)
- `2026-04-01T07:05:32Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#pullrequestreview-4042145635)
- `2026-04-01T08:33:53Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#pullrequestreview-4042581343)
- `2026-04-07T02:45:35Z` `APPROVED` by `mzweilz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#pullrequestreview-4065486506)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/CMakeLists.txt`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/indexerTopK.cu`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QE4m3KvE2m1OE4m3H256PagedKvSlidingOrChunkedCausalP32VarSeqQ8Kv128PersistentSwapsAbForGen_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QE4m3KvE2m1OE4m3H64PagedKvDenseP32VarSeqQ16Kv128StaticSwapsAbForGen_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP32MultiCtasKvCgaVarSeqSkipsSoftmaxQ128Kv128StaticKeepsAbForGen_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP32MultiCtasKvVarSeqSkipsSoftmaxQ128Kv128StaticKeepsAbForGen_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP32VarSeqSkipsSoftmaxQ8Kv128PersistentSwapsAbForGen_cubin.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`: 1 inline comment(s)
- `.pre-commit-config.yaml`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-31T06:57:12Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/CMakeLists.txt`:27; signals: benchmark, compile, cuda, cute, hopper, kernel, ptx, race; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 126 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#discussion_r3013907340)
- `2026-03-31T06:57:09Z` `issue` by `coderabbitai`; signals: attention, compile, cuda, hang, kernel, layout, nan, ptx; excerpt: "📝 Walkthrough Walkthrough Pre-commit configuration adds exclusion rules for FMHA kernel output directories. FmhaDispatcher populates additional runner parameters including processor count and layout-dependent settings. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#issuecomment-4160372961)
- `2026-03-31T06:57:12Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/CMakeLists.txt`:42; signals: benchmark, cute, hang, kernel, layout, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 126 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#discussion_r3013907368)
- `2026-03-31T06:57:12Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QE4m3KvE2m1OE4m3H64PagedKvDenseP32VarSeqQ16Kv128StaticSwapsAbForGen_cubin.cpp`:3; signals: compile, cute, kernel, pipeline, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50376 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#discussion_r3013907385)
- `2026-03-31T06:57:12Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP32MultiCtasKvVarSeqSkipsSoftmaxQ128Kv128StaticKeepsAbForGen_cubin.cpp`:3; signals: cute, kernel, pipeline, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 50376 --- Ensure Git LFS materialization happens before ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#discussion_r3013907394)
- `2026-03-31T06:57:13Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP32VarSeqSkipsSoftmaxQ8Kv128PersistentSwapsAbForGen_cubin.cpp`:3; signals: cute, kernel, pipeline, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 7637 --- Ensure Git LFS objects are materialized ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#discussion_r3013907399)
- `2026-03-31T06:57:14Z` `review` `COMMENTED` by `coderabbitai`; signals: block, kernel, sm100, tensorrt, tma; excerpt: "Actionable comments posted: 7 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#pullrequestreview-4035128109)
- `2026-03-31T06:57:12Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP32MultiCtasKvCgaVarSeqSkipsSoftmaxQ128Kv128StaticKeepsAbForGen_cubin.cpp`:3; signals: cute, kernel, sm100, tensorrt, tma; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 2997 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#discussion_r3013907389)
- `2026-03-31T06:57:12Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/cubin/FmhaSm100aKernel_QE4m3KvE2m1OE4m3H256PagedKvSlidingOrChunkedCausalP32VarSeqQ8Kv128PersistentSwapsAbForGen_cubin.cpp`:3; signals: cute, kernel, sm100, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 10841 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#discussion_r3013907375)
- `2026-04-01T04:36:16Z` `inline` by `yunruis` `cpp/tensorrt_llm/kernels/indexerTopK.cu`:23; signals: compile, hang, kernel, tensorrt; excerpt: "\ is needed because this file uses FLT MAX. Without the direct include, FLT MAX might still compile if some other header pulled in ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#discussion_r3019711120)
- `2026-03-31T15:58:47Z` `inline` by `yuxianq` `cpp/tensorrt_llm/kernels/indexerTopK.cu`:23; signals: kernel, tensorrt; excerpt: "Is it necessary?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#discussion_r3016839680)
- `2026-04-01T05:11:52Z` `inline` by `pengbowang-nv` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`:401; signals: kernel, tensorrt; excerpt: "Obsolete comment" (https://github.com/NVIDIA/TensorRT-LLM/pull/12612#discussion_r3019803857)
