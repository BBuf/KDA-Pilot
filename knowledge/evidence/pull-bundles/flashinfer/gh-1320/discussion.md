# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1320](https://github.com/flashinfer-ai/flashinfer/pull/1320)
- Source page: `sources/prs/flashinfer/PR-1320.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1320`
- Generated at: `2026-05-20T15:22:18.608511+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-24T18:34:38Z`
- Merged: `2025-07-28T06:54:01Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 14 (approved=1, commented=13)
- Inline review comments: 16
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=6
- Human participants with discussion text: aleozlx, sergachev, yzh119
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-24T18:35:18Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @sergachev, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3052776727)
- `2025-07-24T18:37:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds a fast implementation of DeepSeek-style block-scaled FP8 GEMM using TRTLLM-Gen. This includes ... (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3052784137)
- `2025-07-24T19:53:05Z` `COMMENTED` by `sergachev` (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3053080355)
- `2025-07-24T20:47:02Z` `COMMENTED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3053236010)
- `2025-07-24T20:53:03Z` `COMMENTED` by `sergachev` (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3053261199)
- `2025-07-25T11:30:30Z` `COMMENTED` by `yzh119` - Thanks for the contribution, left some comments on code structure. (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3055067567)
- `2025-07-25T11:31:14Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3055071181)
- `2025-07-25T12:34:44Z` `COMMENTED` by `sergachev` (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3055231624)
- `2025-07-25T13:31:23Z` `COMMENTED` by `sergachev` (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3055420170)
- `2025-07-25T17:34:20Z` `COMMENTED` by `sergachev` (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3056293929)
- `2025-07-26T00:17:23Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3057175725)
- `2025-07-26T00:22:11Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3057177994)
- `2025-07-28T00:05:14Z` `COMMENTED` by `sergachev` (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3059733210)
- `2025-07-28T06:53:51Z` `APPROVED` by `yzh119` - LGTM, thanks for your great work! (https://github.com/flashinfer-ai/flashinfer/pull/1320#pullrequestreview-3060714641)

## Inline Comment Hotspots

- `include/flashinfer/trtllm/gemm/trtllmGen_gemm_export/trtllm/gen/CommonUtils.h`: 5 inline comment(s)
- `csrc/trtllm_gemm_runner.cu`: 4 inline comment(s)
- `flashinfer/gemm.py`: 3 inline comment(s)
- `include/flashinfer/trtllm/gemm/trtllmGen_gemm_export/GemmInterface.h`: 2 inline comment(s)
- `include/flashinfer/trtllm/gemm/trtllmGen_gemm_export/Enums.h`: 1 inline comment(s)
- `tests/test_fp8_blockwise_gemm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-26T00:22:06Z` `inline` by `yzh119` `flashinfer/gemm.py`:1460; signals: cutlass, flashinfer, fp8, gemm; excerpt: "Can we also unify this to gemm fp8 nt groupwise? Seems functionality is similar. We can add another parameter backend which could be chosen ..." (https://github.com/flashinfer-ai/flashinfer/pull/1320#discussion_r2232273119)
- `2025-07-26T00:19:35Z` `inline` by `yzh119` `tests/test_fp8_blockwise_gemm.py`:1; signals: block, fp8, gemm; excerpt: "Can you also check this unittest? Seems lots of functionalities are duplicate." (https://github.com/flashinfer-ai/flashinfer/pull/1320#discussion_r2232271956)
- `2025-07-25T11:30:05Z` `inline` by `yzh119` `include/flashinfer/trtllm/gemm/trtllmGen_gemm_export/trtllm/gen/CommonUtils.h`:1; signals: flashinfer, gemm; excerpt: "A lot pf these codes are duplicate of Would you mind doing a refactor and make them under include/flashinfer/trtllm/ as common utility functions?" (https://github.com/flashinfer-ai/flashinfer/pull/1320#discussion_r2230857585)
- `2025-07-25T12:34:44Z` `inline` by `sergachev` `include/flashinfer/trtllm/gemm/trtllmGen_gemm_export/trtllm/gen/CommonUtils.h`:1; signals: flashinfer, gemm; excerpt: "I don't follow the logic of duplicating the generation scripts then manually merging artifacts produced by them but OK." (https://github.com/flashinfer-ai/flashinfer/pull/1320#discussion_r2230974066)
- `2025-07-25T13:31:23Z` `inline` by `sergachev` `include/flashinfer/trtllm/gemm/trtllmGen_gemm_export/trtllm/gen/CommonUtils.h`:1; signals: flashinfer, gemm; excerpt: "In fact all these generated files despite having the same content use different namespaces, [gemm]( vs [batchedGemm]( As a consequence, all files using them ..." (https://github.com/flashinfer-ai/flashinfer/pull/1320#discussion_r2231094786)
- `2025-07-26T00:17:23Z` `inline` by `yzh119` `include/flashinfer/trtllm/gemm/trtllmGen_gemm_export/trtllm/gen/CommonUtils.h`:1; signals: flashinfer, gemm; excerpt: "In fact all these generated files despite having the same content use different namespaces, [gemm]( vs [batchedGemm]( As a consequence, all files using them ..." (https://github.com/flashinfer-ai/flashinfer/pull/1320#discussion_r2232270002)
- `2025-07-24T19:53:05Z` `inline` by `sergachev` `include/flashinfer/trtllm/gemm/trtllmGen_gemm_export/GemmInterface.h`:483; signals: flashinfer, gemm; excerpt: "I'll refer to the existing" (https://github.com/flashinfer-ai/flashinfer/pull/1320#discussion_r2229446873)
- `2025-07-25T11:31:10Z` `inline` by `yzh119` `include/flashinfer/trtllm/gemm/trtllmGen_gemm_export/Enums.h`:1; signals: flashinfer, gemm; excerpt: "And these headers (duplicate of" (https://github.com/flashinfer-ai/flashinfer/pull/1320#discussion_r2230859814)
- `2025-07-25T17:34:20Z` `inline` by `sergachev` `include/flashinfer/trtllm/gemm/trtllmGen_gemm_export/trtllm/gen/CommonUtils.h`:1; signals: flashinfer, gemm; excerpt: "This is what it would take to merge the headers: Do you agree that this should be a separate PR?" (https://github.com/flashinfer-ai/flashinfer/pull/1320#discussion_r2231680255)
- `2025-07-28T00:05:14Z` `inline` by `sergachev` `flashinfer/gemm.py`:1460; signals: flashinfer, gemm; excerpt: "Done." (https://github.com/flashinfer-ai/flashinfer/pull/1320#discussion_r2234185716)
- `2025-07-24T20:53:03Z` `inline` by `sergachev` `csrc/trtllm_gemm_runner.cu`:24; signals: gemm; excerpt: "Compilation used to require a particular order of headers, some relying on the other ones. Looks like it isn't necessary anymore, removed." (https://github.com/flashinfer-ai/flashinfer/pull/1320#discussion_r2229553252)
- `2025-07-24T20:47:01Z` `inline` by `aleozlx` `csrc/trtllm_gemm_runner.cu`:24; signals: gemm; excerpt: "? curious what happened here" (https://github.com/flashinfer-ai/flashinfer/pull/1320#discussion_r2229541845)
