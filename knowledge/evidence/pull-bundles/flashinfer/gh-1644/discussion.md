# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1644](https://github.com/flashinfer-ai/flashinfer/pull/1644)
- Source page: `sources/prs/flashinfer/PR-1644.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1644`
- Generated at: `2026-05-20T15:23:08.195858+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-05T20:25:45Z`
- Merged: `2025-09-09T22:23:55Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 15 (approved=1, commented=14)
- Inline review comments: 15
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=6
- Human participants with discussion text: nvmbreughe, ttyio, yzh119
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-09-05T20:26:00Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @nvmbreughe, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3190700132)
- `2025-09-05T20:27:26Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for the mx fp4 quantization format within the cudnn backend, which ... (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3190704745)
- `2025-09-05T20:51:10Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3190758736)
- `2025-09-05T22:04:44Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3190903376)
- `2025-09-05T22:09:29Z` `COMMENTED` by `nvmbreughe` (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3190917399)
- `2025-09-06T21:03:27Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3193899441)
- `2025-09-08T17:14:35Z` `COMMENTED` by `nvmbreughe` (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3197411721)
- `2025-09-08T17:16:09Z` `COMMENTED` by `nvmbreughe` (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3197416585)
- `2025-09-08T17:30:16Z` `COMMENTED` by `nvmbreughe` (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3197455371)
- `2025-09-08T20:51:39Z` `COMMENTED` by `nvmbreughe` (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3198143063)
- `2025-09-08T20:51:51Z` `COMMENTED` by `nvmbreughe` (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3198143525)
- `2025-09-09T04:31:24Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3199162636)
- `2025-09-09T18:40:08Z` `COMMENTED` by `nvmbreughe` (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3202816960)
- `2025-09-09T19:30:08Z` `APPROVED` by `yzh119` - LGTM! (https://github.com/flashinfer-ai/flashinfer/pull/1644#pullrequestreview-3202988088)

## Inline Comment Hotspots

- `flashinfer/gemm.py`: 13 inline comment(s)
- `tests/test_mm_fp4.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-08T17:14:26Z` `inline` by `nvmbreughe` `flashinfer/gemm.py`:1853; signals: block, flashinfer, fp4, gemm, mxfp4, nvfp4; excerpt: "The problem is that torch.uint8 may also be used for nvfp4. If we want to avoid an extra boolean, we can distinguish either by ..." (https://github.com/flashinfer-ai/flashinfer/pull/1644#discussion_r2330861213)
- `2025-09-05T20:51:09Z` `inline` by `ttyio` `flashinfer/gemm.py`:1919; signals: block, flashinfer, fp4, gemm, hang, nvfp4; excerpt: "change the check here, block size 16 is for nvfp4 only?" (https://github.com/flashinfer-ai/flashinfer/pull/1644#discussion_r2326026808)
- `2025-09-05T22:09:28Z` `inline` by `nvmbreughe` `flashinfer/gemm.py`:1919; signals: block, flashinfer, fp4, gemm, mxfp4; excerpt: "mxfp4 can use both 16 or 32 (in theory it can be arbitrary). I updated the check to make this more clear, and also ..." (https://github.com/flashinfer-ai/flashinfer/pull/1644#discussion_r2326137472)
- `2025-09-09T04:31:24Z` `inline` by `yzh119` `flashinfer/gemm.py`:1970; signals: flashinfer, fp4, gemm, kernel, mxfp4; excerpt: "Since mxfp4 needs e8m0, is it ok to skip the test for python < 2.8? Before torch2.7, we use uint8 as container of e8m0 ..." (https://github.com/flashinfer-ai/flashinfer/pull/1644#discussion_r2331980265)
- `2025-09-05T22:04:44Z` `inline` by `ttyio` `flashinfer/gemm.py`:1922; signals: block, flashinfer, fp4, gemm, mxfp4; excerpt: "should we only allow block size 32 for mxfp4? I checked some reference:" (https://github.com/flashinfer-ai/flashinfer/pull/1644#discussion_r2326129288)
- `2025-09-06T21:01:52Z` `inline` by `yzh119` `flashinfer/gemm.py`:1853; signals: flashinfer, fp4, gemm, mxfp4; excerpt: "How about inferring from scale data types instead? When descale tensor has data type float8 e4m3fn, uses mxfp4, when descale tensor has data type ..." (https://github.com/flashinfer-ai/flashinfer/pull/1644#discussion_r2328364463)
- `2025-09-09T18:40:08Z` `inline` by `nvmbreughe` `flashinfer/gemm.py`:1970; signals: flashinfer, fp4, fp8, gemm; excerpt: "Hi @yzh119 , I removed the dependency on the torch type completely so no version check is needed. The code looks cleaner this way. ..." (https://github.com/flashinfer-ai/flashinfer/pull/1644#discussion_r2334455877)
- `2025-09-08T17:30:11Z` `inline` by `nvmbreughe` `flashinfer/gemm.py`:1970; signals: flashinfer, fp4, gemm, mxfp4; excerpt: "Thank you for pointing this out. Since mxfp4 needs e8m0, is it ok to skip the test for python < 2.8?" (https://github.com/flashinfer-ai/flashinfer/pull/1644#discussion_r2330892429)
- `2025-09-06T21:02:55Z` `inline` by `yzh119` `flashinfer/gemm.py`:1970; signals: flashinfer, gemm; excerpt: "Also note that torch.float8 e8m0fnu is introduced in torch 2.8 and we should care about the case of torch 2.7 before it's end-of-life." (https://github.com/flashinfer-ai/flashinfer/pull/1644#discussion_r2328364718)
- `2025-09-08T20:51:39Z` `inline` by `nvmbreughe` `flashinfer/gemm.py`:1853; signals: flashinfer, gemm; excerpt: "Addressed with option 1)." (https://github.com/flashinfer-ai/flashinfer/pull/1644#discussion_r2331355099)
- `2025-09-08T20:51:51Z` `inline` by `nvmbreughe` `flashinfer/gemm.py`:1970; signals: flashinfer, gemm; excerpt: "Addressed. Thanks again." (https://github.com/flashinfer-ai/flashinfer/pull/1644#discussion_r2331355448)
- `2025-09-08T17:16:09Z` `inline` by `nvmbreughe` `tests/test_mm_fp4.py`:75; signals: fp4; excerpt: "Check was updated to 32 only." (https://github.com/flashinfer-ai/flashinfer/pull/1644#discussion_r2330864669)
