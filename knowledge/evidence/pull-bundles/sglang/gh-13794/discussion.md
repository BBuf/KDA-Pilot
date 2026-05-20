# PR Discussion Digest

- Source PR: [sgl-project/sglang#13794](https://github.com/sgl-project/sglang/pull/13794)
- Source page: `sources/prs/sglang/PR-13794.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13794`
- Generated at: `2026-05-20T15:27:51.017743+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-23T12:49:58Z`
- Merged: `2025-12-01T23:26:28Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 11
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=5
- Human participants with discussion text: Fridge003, TomerBN-Nvidia, ch-wan, ispobock
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-23T12:52:10Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for non-gated Mixture of Experts (MoE) layers with fp4 and fp8 ... (https://github.com/sgl-project/sglang/pull/13794#pullrequestreview-3497736622)
- `2025-11-26T12:51:23Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/sgl-project/sglang/pull/13794#pullrequestreview-3510818019)
- `2025-11-26T12:54:20Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/sgl-project/sglang/pull/13794#pullrequestreview-3510828837)
- `2025-11-26T12:54:54Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/sgl-project/sglang/pull/13794#pullrequestreview-3510830915)
- `2025-11-30T22:01:04Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13794#pullrequestreview-3522456866)
- `2025-12-01T00:01:41Z` `APPROVED` by `ch-wan` - LGTM. I only have one minor comment. (https://github.com/sgl-project/sglang/pull/13794#pullrequestreview-3522747387)
- `2025-12-01T08:55:43Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/sgl-project/sglang/pull/13794#pullrequestreview-3523875740)
- `2025-12-01T08:57:15Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/sgl-project/sglang/pull/13794#pullrequestreview-3523885391)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 10 inline comment(s)
- `python/sglang/srt/server_args.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-30T21:51:06Z` `inline` by `Fridge003` `python/sglang/srt/server_args.py`:1510; signals: fp4, fp8, hang; excerpt: "Qualified quantization methods should be modelopt fp4, modelopt fp8 and bfloat16 here. This assertion message should be changed" (https://github.com/sgl-project/sglang/pull/13794#discussion_r2574949514)
- `2025-11-26T12:51:23Z` `inline` by `TomerBN-Nvidia` `python/sglang/srt/layers/quantization/modelopt_quant.py`:838; signals: aligned; excerpt: "is is aligned with other parts of the code" (https://github.com/sgl-project/sglang/pull/13794#discussion_r2564890690)
- `2025-11-26T12:54:20Z` `inline` by `TomerBN-Nvidia` `python/sglang/srt/layers/quantization/modelopt_quant.py`:1614; signals: general review; excerpt: "refactored this part" (https://github.com/sgl-project/sglang/pull/13794#discussion_r2564899672)
- `2025-11-26T12:54:53Z` `inline` by `TomerBN-Nvidia` `python/sglang/srt/layers/quantization/modelopt_quant.py`:1687; signals: general review; excerpt: "done" (https://github.com/sgl-project/sglang/pull/13794#discussion_r2564901426)
- `2025-11-30T21:53:54Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/modelopt_quant.py`:8; signals: general review; excerpt: "Should be moved to around line 90. Needs try-catch for detecting ImportError" (https://github.com/sgl-project/sglang/pull/13794#discussion_r2574956534)
- `2025-11-30T23:56:11Z` `inline` by `ch-wan` `python/sglang/srt/layers/quantization/modelopt_quant.py`:1623; signals: general review; excerpt: "Move it below to the comment in the next line" (https://github.com/sgl-project/sglang/pull/13794#discussion_r2575244266)
- `2025-12-01T08:55:42Z` `inline` by `TomerBN-Nvidia` `python/sglang/srt/layers/quantization/modelopt_quant.py`:1623; signals: general review; excerpt: "Done" (https://github.com/sgl-project/sglang/pull/13794#discussion_r2576185955)
- `2025-12-01T08:57:15Z` `inline` by `TomerBN-Nvidia` `python/sglang/srt/layers/quantization/modelopt_quant.py`:8; signals: general review; excerpt: "Fixed" (https://github.com/sgl-project/sglang/pull/13794#discussion_r2576192868)
