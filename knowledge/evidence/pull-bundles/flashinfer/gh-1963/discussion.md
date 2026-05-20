# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1963](https://github.com/flashinfer-ai/flashinfer/pull/1963)
- Source page: `sources/prs/flashinfer/PR-1963.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1963`
- Generated at: `2026-05-20T15:23:40.674483+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-21T17:07:44Z`
- Merged: `2025-10-31T06:28:23Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 9 (approved=1, changes_requested=1, commented=7)
- Inline review comments: 6
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: coderabbitai, yongwww, yzh119
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-21T17:09:04Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1963#pullrequestreview-3361834870)
- `2025-10-21T17:09:52Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly removes redundant contiguity checks on scale factor tensors in the SM120 GEMM ... (https://github.com/flashinfer-ai/flashinfer/pull/1963#pullrequestreview-3361837827)
- `2025-10-21T22:02:48Z` `COMMENTED` by `yongwww` (https://github.com/flashinfer-ai/flashinfer/pull/1963#pullrequestreview-3362869980)
- `2025-10-24T11:03:03Z` `COMMENTED` by `yzh119` - Can you add unittests for non-contiguous SFA/SFB (if it's really supported)? (https://github.com/flashinfer-ai/flashinfer/pull/1963#pullrequestreview-3375777055)
- `2025-10-27T01:05:37Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1963#pullrequestreview-3381549872)
- `2025-10-29T01:20:49Z` `COMMENTED` by `yongwww` (https://github.com/flashinfer-ai/flashinfer/pull/1963#pullrequestreview-3391392184)
- `2025-10-29T01:52:50Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🧹 Nitpick comments (1) tests/gemm/test groupwise scaled gemm fp8.py (1) 394-394: Consider testing both ... (https://github.com/flashinfer-ai/flashinfer/pull/1963#pullrequestreview-3391429848)
- `2025-10-29T08:42:58Z` `CHANGES_REQUESTED` by `yzh119` - Added a commit with more problem shapes: and lots of UT failed. It only works for small problem ... (https://github.com/flashinfer-ai/flashinfer/pull/1963#pullrequestreview-3392219448)
- `2025-10-31T05:26:49Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1963#pullrequestreview-3402641818)

## Inline Comment Hotspots

- `csrc/gemm_groupwise_sm120.cu`: 5 inline comment(s)
- `tests/gemm/test_groupwise_scaled_gemm_fp8.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-29T01:52:50Z` `review` `COMMENTED` by `coderabbitai`; signals: block, flashinfer, fp8, gemm, hang, kernel, regression, sm120; excerpt: "Actionable comments posted: 1 🧹 Nitpick comments (1) tests/gemm/test groupwise scaled gemm fp8.py (1) 394-394: Consider testing both scale major modes in manual execution. ..." (https://github.com/flashinfer-ai/flashinfer/pull/1963#pullrequestreview-3391429848)
- `2025-10-21T17:08:06Z` `issue` by `coderabbitai`; signals: aligned, flashinfer, fp8, gemm, hang, kernel, layout, memory; excerpt: "Walkthrough Added .contiguous() calls to expanded scale tensors in two SM120 code paths within GEMM operations. This ensures expanded tensors transition from shape (1,1) ..." (https://github.com/flashinfer-ai/flashinfer/pull/1963#issuecomment-3427883339)
- `2025-10-24T11:02:25Z` `inline` by `yzh119` `csrc/gemm_groupwise_sm120.cu`:94; signals: gemm, kernel, sm120; excerpt: "looks like the contiguity is not required I don't understand, if we allow non-contiguous SFA/SFB, at least we should pass the strides from tensors ..." (https://github.com/flashinfer-ai/flashinfer/pull/1963#discussion_r2459822554)
- `2025-10-29T01:52:49Z` `inline` by `coderabbitai` `tests/gemm/test_groupwise_scaled_gemm_fp8.py`:340; signals: benchmark, fp8, gemm; excerpt: "⚠️ Potential issue 🟡 Minor Fix terminology: "non-continuous" → "non-contiguous". Line 339 uses "non-continuous" but the standard PyTorch terminology is "non-contiguous" (matching the function ..." (https://github.com/flashinfer-ai/flashinfer/pull/1963#discussion_r2471524469)
- `2025-10-21T17:09:00Z` `inline` by `yzh119` `csrc/gemm_groupwise_sm120.cu`:94; signals: gemm, layout, sm120; excerpt: "Do we have any assumptions on the layout of SFA or SFB?" (https://github.com/flashinfer-ai/flashinfer/pull/1963#discussion_r2449090346)
- `2025-10-21T22:02:48Z` `inline` by `yongwww` `csrc/gemm_groupwise_sm120.cu`:94; signals: gemm, layout, sm120; excerpt: "The layout of SFA and SFB: looks like the contiguity is not required (" (https://github.com/flashinfer-ai/flashinfer/pull/1963#discussion_r2449814983)
- `2025-10-27T01:05:34Z` `inline` by `yzh119` `csrc/gemm_groupwise_sm120.cu`:94; signals: gemm, sm120; excerpt: "Any updates on this @yongwww ?" (https://github.com/flashinfer-ai/flashinfer/pull/1963#discussion_r2464217648)
- `2025-10-29T01:20:49Z` `inline` by `yongwww` `csrc/gemm_groupwise_sm120.cu`:94; signals: gemm, sm120; excerpt: "ut was added" (https://github.com/flashinfer-ai/flashinfer/pull/1963#discussion_r2471491572)
- `2025-10-29T08:42:58Z` `review` `CHANGES_REQUESTED` by `yzh119`; signals: layout; excerpt: "Added a commit with more problem shapes: and lots of UT failed. It only works for small problem shapes such as 256x256x256 I don't ..." (https://github.com/flashinfer-ai/flashinfer/pull/1963#pullrequestreview-3392219448)
- `2025-10-31T04:15:46Z` `issue` by `yongwww`; signals: correctness, fp8; excerpt: "I realized that the previous fix for the issues we encountered in e2e (vLLM, Llama-3.1-8B-Instruct-FP8) is not correct, removing the contiguity check in this ..." (https://github.com/flashinfer-ai/flashinfer/pull/1963#issuecomment-3471271772)
- `2025-10-24T11:03:03Z` `review` `COMMENTED` by `yzh119`; signals: general review; excerpt: "Can you add unittests for non-contiguous SFA/SFB (if it's really supported)?" (https://github.com/flashinfer-ai/flashinfer/pull/1963#pullrequestreview-3375777055)
