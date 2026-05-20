# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11165](https://github.com/NVIDIA/TensorRT-LLM/pull/11165)
- Source page: `sources/prs/tensorrt-llm/PR-11165.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11165`
- Generated at: `2026-05-20T15:17:42.532724+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-31T15:41:52Z`
- Merged: `2026-02-26T04:16:06Z`

## Discussion Counts

- Issue comments: 39
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: chenfeiz0326, coderabbitai, longlee0622, rosenrodt, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-31T15:49:39Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#pullrequestreview-3732915584)
- `2026-02-26T03:20:36Z` `APPROVED` by `longlee0622` (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#pullrequestreview-3858185924)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-01-31T15:49:39Z` `review` `COMMENTED` by `coderabbitai`; signals: cache, cutlass, gemm, kernel, moe, race, tensorrt; excerpt: "Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#pullrequestreview-3732915584)
- `2026-01-31T15:49:36Z` `issue` by `coderabbitai`; signals: block, compile, correctness, cuda, cutlass, dtype, fp4, gemm; excerpt: "📝 Walkthrough Walkthrough A launch bounds compiler attribute is added to the doActivationKernel CUDA kernel declaration in the MOE GEMM kernels file, specifying occupancy ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#issuecomment-3828741214)
- `2026-02-01T05:44:33Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 34330]( [ run ] completed with state SUCCESS. Commit: c3a255d [/LLM/main/L0 MergeRequest PR pipeline 26479]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#issuecomment-3830421221)
- `2026-02-01T08:43:10Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 34342]( [ run ] completed with state SUCCESS. Commit: c3a255d [/LLM/main/L0 MergeRequest PR pipeline 26491]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#issuecomment-3830629514)
- `2026-02-01T14:15:12Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 34354]( [ run ] completed with state SUCCESS. Commit: c3a255d [/LLM/main/L0 MergeRequest PR pipeline 26502]( completed with status: 'SUCCESS'" (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#issuecomment-3831113384)
- `2026-02-19T04:56:26Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 36200]( [ run ] completed with state SUCCESS. Commit: 1a23931 [/LLM/main/L0 MergeRequest PR pipeline 27981]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#issuecomment-3924692808)
- `2026-02-19T07:40:28Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 36208]( [ run ] completed with state SUCCESS. Commit: 9fca6a0 [/LLM/main/L0 MergeRequest PR pipeline 27989]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#issuecomment-3925186038)
- `2026-02-19T10:32:42Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 36221]( [ run ] completed with state SUCCESS. Commit: 9fca6a0 [/LLM/main/L0 MergeRequest PR pipeline 28001]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#issuecomment-3926316519)
- `2026-02-19T14:39:59Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 36227]( [ run ] completed with state SUCCESS. Commit: 9fca6a0 [/LLM/main/L0 MergeRequest PR pipeline 28007]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#issuecomment-3927712275)
- `2026-02-19T17:37:41Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 36255]( [ run ] completed with state SUCCESS. Commit: 9fca6a0 [/LLM/main/L0 MergeRequest PR pipeline 28032]( completed with status: 'SUCCESS' [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#issuecomment-3928786399)
- `2026-02-24T09:16:22Z` `issue` by `chenfeiz0326`; signals: b200, perf; excerpt: "/bot run --disable-fail-fast --stage-list "DGX B200-8 GPUs-PyTorch-PerfSanity-Post-Merge-1"" (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#issuecomment-3950256035)
- `2026-02-24T12:41:02Z` `issue` by `rosenrodt`; signals: b200, perf; excerpt: "/bot run --disable-fail-fast --stage-list "DGX B200-8 GPUs-PyTorch-PerfSanity-Post-Merge-1"" (https://github.com/NVIDIA/TensorRT-LLM/pull/11165#issuecomment-3951502435)
