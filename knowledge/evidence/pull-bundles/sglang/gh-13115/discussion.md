# PR Discussion Digest

- Source PR: [sgl-project/sglang#13115](https://github.com/sgl-project/sglang/pull/13115)
- Source page: `sources/prs/sglang/PR-13115.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13115`
- Generated at: `2026-05-20T15:27:44.385254+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-12T03:39:54Z`
- Merged: `2025-12-06T08:45:54Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 6
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: Fridge003, rainj-me, weireweire
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-12-05T07:28:02Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13115#pullrequestreview-3543427032)
- `2025-12-05T18:14:35Z` `COMMENTED` by `rainj-me` (https://github.com/sgl-project/sglang/pull/13115#pullrequestreview-3545853423)
- `2025-12-05T18:17:15Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13115#pullrequestreview-3545861242)
- `2025-12-05T18:30:59Z` `COMMENTED` by `rainj-me` (https://github.com/sgl-project/sglang/pull/13115#pullrequestreview-3545914329)
- `2025-12-05T18:31:22Z` `COMMENTED` by `rainj-me` (https://github.com/sgl-project/sglang/pull/13115#pullrequestreview-3545915369)
- `2025-12-05T18:34:28Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13115#pullrequestreview-3545926275)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 4 inline comment(s)
- `python/sglang/srt/server_args.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-05T07:27:59Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_v2.py`:234; signals: fp4, fp8, gemm, nvfp4; excerpt: "Why appending the condition of SGLANG NVFP4 CKPT FP8 GEMM IN ATTN" (https://github.com/sgl-project/sglang/pull/13115#discussion_r2591681519)
- `2025-12-05T18:14:35Z` `inline` by `rainj-me` `python/sglang/srt/models/deepseek_v2.py`:234; signals: moe; excerpt: "Try to avoid the MTP layer automatically quantize to ue8m0. Set moe a2a backend to none will help, but this is too hacky. I'm ..." (https://github.com/sgl-project/sglang/pull/13115#discussion_r2593535589)
- `2025-12-05T07:25:18Z` `inline` by `Fridge003` `python/sglang/srt/server_args.py`:3013; signals: general review; excerpt: "Please update the server argument document with this argument" (https://github.com/sgl-project/sglang/pull/13115#discussion_r2591675583)
- `2025-12-05T18:17:12Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_v2.py`:234; signals: general review; excerpt: "I can try to fix this later" (https://github.com/sgl-project/sglang/pull/13115#discussion_r2593541230)
- `2025-12-05T18:30:59Z` `inline` by `rainj-me` `python/sglang/srt/server_args.py`:3013; signals: general review; excerpt: "fixed" (https://github.com/sgl-project/sglang/pull/13115#discussion_r2593579215)
- `2025-12-05T18:31:22Z` `inline` by `rainj-me` `python/sglang/srt/models/deepseek_v2.py`:234; signals: general review; excerpt: "OK, let me revert it." (https://github.com/sgl-project/sglang/pull/13115#discussion_r2593580185)
