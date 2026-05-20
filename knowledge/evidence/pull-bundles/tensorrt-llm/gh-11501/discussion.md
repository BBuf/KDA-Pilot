# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11501](https://github.com/NVIDIA/TensorRT-LLM/pull/11501)
- Source page: `sources/prs/tensorrt-llm/PR-11501.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11501`
- Generated at: `2026-05-20T15:17:42.570876+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-13T03:21:44Z`
- Merged: `2026-03-01T15:45:22Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: coderabbitai, longlee0622, nekorobov, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-13T03:27:36Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11501#pullrequestreview-3794834023)
- `2026-02-24T00:56:37Z` `APPROVED` by `longlee0622` (https://github.com/NVIDIA/TensorRT-LLM/pull/11501#pullrequestreview-3844368673)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-13T03:27:33Z` `issue` by `coderabbitai`; signals: block, cuda, cute, cutlass, deepgemm, gemm, hang, kernel; excerpt: "📝 Walkthrough Walkthrough The changes enhance block-scale MOE kernel launching by introducing block-count adjustment macros and block-indexed vectorized loading. A new hiddenDimPerBlock parameter enables ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11501#issuecomment-3894606322)
- `2026-02-13T03:27:36Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/DevKernel.h`:134; signals: benchmark, block, hang, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Copy-paste inconsistency: true should be false in the non-PDL branch. Line 133 uses KernelParams ::Type inside the !data.mUsePdl branch. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11501#discussion_r2802083467)
- `2026-02-13T03:27:36Z` `review` `COMMENTED` by `coderabbitai`; signals: block, kernel, moe, tensorrt; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11501#pullrequestreview-3794834023)
- `2026-02-13T07:20:32Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 35867]( [ run ] completed with state SUCCESS. Commit: 3ed1d78 [/LLM/main/L0 MergeRequest PR pipeline 27699]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11501#issuecomment-3895326608)
- `2026-02-13T13:37:04Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 35907]( [ run ] completed with state SUCCESS. Commit: 3ed1d78 [/LLM/main/L0 MergeRequest PR pipeline 27726]( completed with status: 'SUCCESS' Pipeline passed with ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11501#issuecomment-3897295289)
