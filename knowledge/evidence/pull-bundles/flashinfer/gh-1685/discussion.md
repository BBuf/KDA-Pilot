# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1685](https://github.com/flashinfer-ai/flashinfer/pull/1685)
- Source page: `sources/prs/flashinfer/PR-1685.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1685`
- Generated at: `2026-05-20T15:23:14.977733+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-16T10:05:12Z`
- Merged: `2025-09-19T09:13:55Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 14 (approved=1, commented=13)
- Inline review comments: 14
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=6, outdated=2
- Human participants with discussion text: elvischenv, fzyzcjy, joker-eph, nvpohanh, weireweire, yzh119
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 6

## Review Decisions

- `2025-09-16T10:05:32Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @weireweire, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1685#pullrequestreview-3228897226)
- `2025-09-16T10:08:04Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request ports a separate reduction kernel from TensorRT-LLM for use in fused multi-head attention, ... (https://github.com/flashinfer-ai/flashinfer/pull/1685#pullrequestreview-3228916469)
- `2025-09-16T16:57:26Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1685#pullrequestreview-3230889170)
- `2025-09-17T01:47:04Z` `COMMENTED` by `weireweire` (https://github.com/flashinfer-ai/flashinfer/pull/1685#pullrequestreview-3232196900)
- `2025-09-17T02:30:43Z` `COMMENTED` by `weireweire` (https://github.com/flashinfer-ai/flashinfer/pull/1685#pullrequestreview-3232337207)
- `2025-09-17T02:32:49Z` `COMMENTED` by `weireweire` (https://github.com/flashinfer-ai/flashinfer/pull/1685#pullrequestreview-3232343169)
- `2025-09-17T05:37:27Z` `COMMENTED` by `yzh119` - Overall LGTM, left some minor suggestions (https://github.com/flashinfer-ai/flashinfer/pull/1685#pullrequestreview-3232725992)
- `2025-09-17T11:21:55Z` `COMMENTED` by `elvischenv` (https://github.com/flashinfer-ai/flashinfer/pull/1685#pullrequestreview-3233950710)
- `2025-09-17T16:37:44Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1685#pullrequestreview-3235320800)
- `2025-09-18T06:29:46Z` `COMMENTED` by `elvischenv` (https://github.com/flashinfer-ai/flashinfer/pull/1685#pullrequestreview-3237470812)
- `2025-09-19T06:23:56Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1685#pullrequestreview-3243333649)

## Inline Comment Hotspots

- `csrc/fmhaReduction.cu`: 3 inline comment(s)
- `csrc/kernelUtils.h`: 3 inline comment(s)
- `flashinfer/artifacts.py`: 3 inline comment(s)
- `include/flashinfer/trtllm/fmha/fmhaKernels.cuh`: 3 inline comment(s)
- `include/flashinfer/trtllm/common/cudaUtils.h`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-19T06:47:18Z` `issue` by `weireweire`; signals: accuracy, attention, bf16, blackwell, fp8, regression; excerpt: "@yzh119 we found there are some accuracy regression on fp16/bf16 sink test test blackwell trtllm gen decode attention sink, I just added a 1% ..." (https://github.com/flashinfer-ai/flashinfer/pull/1685#issuecomment-3310835217)
- `2025-09-17T11:21:47Z` `inline` by `elvischenv` `flashinfer/artifacts.py`:112; signals: attention, blackwell, flashinfer, fp8, kernel; excerpt: "Since this update introduced TRTLLM-gen FP8 sinks attn kernel support, do you think we need to update tests/test attention sink blackwell.py or tests/test trtllm ..." (https://github.com/flashinfer-ai/flashinfer/pull/1685#discussion_r2355183064)
- `2025-09-17T05:34:59Z` `inline` by `yzh119` `include/flashinfer/trtllm/common/cudaUtils.h`:100; signals: cuda, flashinfer, hang, tensorrt; excerpt: "I don't think it's being called anywhere in flashinfer (and even in tensorrt-llm: but I think your change is correct." (https://github.com/flashinfer-ai/flashinfer/pull/1685#discussion_r2354351040)
- `2025-09-18T06:29:46Z` `inline` by `elvischenv` `flashinfer/artifacts.py`:112; signals: accuracy, flashinfer, fp8, regression; excerpt: "GPT-OSS E2E accuracy results with this PR: kv=auto: kv=FP8: Also verified the fix for ctx/gen attn regression: before regression: current main: PR: Maybe we ..." (https://github.com/flashinfer-ai/flashinfer/pull/1685#discussion_r2357653259)
- `2025-09-17T02:32:49Z` `inline` by `weireweire` `include/flashinfer/trtllm/common/cudaUtils.h`:100; signals: cuda, flashinfer, hang, kernel; excerpt: "@yzh119 please review if this change is right. It's not related to the reduce kernel though." (https://github.com/flashinfer-ai/flashinfer/pull/1685#discussion_r2354108866)
- `2025-09-17T16:37:44Z` `inline` by `yzh119` `flashinfer/artifacts.py`:112; signals: flashinfer, fp8; excerpt: "Good idea, yes I think it's good to add fp8 tests" (https://github.com/flashinfer-ai/flashinfer/pull/1685#discussion_r2356102220)
- `2025-09-16T16:50:49Z` `inline` by `yzh119` `csrc/kernelUtils.h`:1; signals: kernel; excerpt: "Could we move this header to include instead?" (https://github.com/flashinfer-ai/flashinfer/pull/1685#discussion_r2353104982)
- `2025-09-17T01:47:04Z` `inline` by `weireweire` `csrc/kernelUtils.h`:1; signals: kernel; excerpt: "we can, but I see other util headers in this folder." (https://github.com/flashinfer-ai/flashinfer/pull/1685#discussion_r2354012085)
- `2025-09-17T02:30:43Z` `inline` by `weireweire` `csrc/kernelUtils.h`:1; signals: kernel; excerpt: "moved, and I don't know when do we use .h or .cuh" (https://github.com/flashinfer-ai/flashinfer/pull/1685#discussion_r2354105189)
- `2025-09-17T05:37:27Z` `review` `COMMENTED` by `yzh119`; signals: general review; excerpt: "Overall LGTM, left some minor suggestions" (https://github.com/flashinfer-ai/flashinfer/pull/1685#pullrequestreview-3232725992)
- `2025-09-17T05:37:02Z` `inline` by `yzh119` `csrc/fmhaReduction.cu`:276; signals: general review; excerpt: "a minor request is to reorder stream and enable pdl to be consistent of the remaining codebase" (https://github.com/flashinfer-ai/flashinfer/pull/1685#discussion_r2354353613)
