# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#9175](https://github.com/NVIDIA/TensorRT-LLM/pull/9175)
- Source page: `sources/prs/tensorrt-llm/PR-9175.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-9175`
- Generated at: `2026-05-20T15:19:24.854085+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-14T12:57:09Z`
- Merged: `2025-11-21T14:35:00Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 8
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: ChristinaZ, coderabbitai, nekorobov, rosenrodt, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-14T13:07:27Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#pullrequestreview-3464860727)
- `2025-11-14T14:38:27Z` `COMMENTED` by `rosenrodt` - Thanks! I have left a quesiton inline around perf considerations. Otherwise looks good to me. Tagging @ChristinaZ for ... (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#pullrequestreview-3465225588)
- `2025-11-21T09:38:43Z` `COMMENTED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#pullrequestreview-3491921292)
- `2025-11-21T10:31:21Z` `COMMENTED` by `ChristinaZ` (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#pullrequestreview-3471300565)
- `2025-11-21T10:34:11Z` `APPROVED` by `ChristinaZ` (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#pullrequestreview-3492149711)
- `2025-11-21T10:55:52Z` `COMMENTED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#pullrequestreview-3492233086)
- `2025-11-21T11:31:24Z` `COMMENTED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#pullrequestreview-3492360829)
- `2025-11-21T11:31:38Z` `COMMENTED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#pullrequestreview-3492361454)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`: 8 inline comment(s)

## High-Signal Discussion

- `2025-11-14T13:07:27Z` `review` `COMMENTED` by `coderabbitai`; signals: benchmark, block, compile, cuda, deadlock, dtype, hang, kernel; excerpt: "Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#pullrequestreview-3464860727)
- `2025-11-14T13:07:24Z` `issue` by `coderabbitai`; signals: block, compile, correctness, dtype, fp8, hang, kernel, moe; excerpt: "📝 Walkthrough Walkthrough The PR introduces vectorized processing utilities (Float4Max, Float2Max functors, type-packing functions) and a KernelTraits template for adaptive operations based on token ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#issuecomment-3532646611)
- `2025-11-17T07:14:50Z` `inline` by `ChristinaZ` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`:314; signals: block, kernel, moe, register, tensorrt; excerpt: "Do we need to add some initialization operations for the register arrays? Because if (permutedIdx == -1) seems to leave some registers unwritten. And ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#discussion_r2532957152)
- `2025-11-21T11:31:38Z` `inline` by `nekorobov` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`:314; signals: block, flashinfer, kernel, moe, tensorrt; excerpt: "Fixed, also will submit to flashinfer" (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#discussion_r2549465549)
- `2025-11-14T14:31:45Z` `inline` by `rosenrodt` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`:276; signals: block, kernel, moe, tensorrt; excerpt: "Wonder if we considered looping tokenIdxCtaIdx first, followed by hiddenIdx? This way we check for if (permutedIdx == -1) before entering hiddenIdx loop" (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#discussion_r2527721918)
- `2025-11-17T07:27:33Z` `inline` by `ChristinaZ` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`:227; signals: block, kernel, moe, tensorrt; excerpt: "It seems that 128 is an important constant and shouldn’t be modified. How about making it a constexpr variable within the namespace so that ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#discussion_r2532986211)
- `2025-11-21T09:38:43Z` `inline` by `nekorobov` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`:276; signals: block, kernel, moe, tensorrt; excerpt: "Then we can't store scaleArr and dataArr by tokenIdxCta since they are different for each hiddenIdx" (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#discussion_r2549126224)
- `2025-11-21T10:53:36Z` `inline` by `nekorobov` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`:227; signals: block, kernel, moe, tensorrt; excerpt: "Agree, we should" (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#discussion_r2549365152)
- `2025-11-21T10:55:45Z` `inline` by `nekorobov` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`:314; signals: block, kernel, moe, tensorrt; excerpt: "You are right, I missed this, this is important" (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#discussion_r2549370947)
- `2025-11-21T11:31:24Z` `inline` by `nekorobov` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.cu`:227; signals: block, kernel, moe, tensorrt; excerpt: "Added" (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#discussion_r2549465046)
- `2025-11-14T14:38:27Z` `review` `COMMENTED` by `rosenrodt`; signals: kernel, perf; excerpt: "Thanks! I have left a quesiton inline around perf considerations. Otherwise looks good to me. Tagging @ChristinaZ for insights for past work on finalize ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#pullrequestreview-3465225588)
- `2025-11-14T17:28:40Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 24595]( [ run ] completed with state SUCCESS. Commit: cede79a [/LLM/main/L0 MergeRequest PR pipeline 18565]( completed with status: 'SUCCESS'" (https://github.com/NVIDIA/TensorRT-LLM/pull/9175#issuecomment-3533817875)
