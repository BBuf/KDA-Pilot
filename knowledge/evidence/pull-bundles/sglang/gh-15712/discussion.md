# PR Discussion Digest

- Source PR: [sgl-project/sglang#15712](https://github.com/sgl-project/sglang/pull/15712)
- Source page: `sources/prs/sglang/PR-15712.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15712`
- Generated at: `2026-05-20T15:28:14.854777+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-24T02:40:49Z`
- Merged: `2026-01-07T15:45:35Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 5 (approved=1, changes_requested=1, commented=3)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: ClawSeven, Fridge003, Insideyyy, sunxxuns
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-12-24T07:22:41Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/15712#pullrequestreview-3610142682)
- `2025-12-24T08:05:11Z` `COMMENTED` by `Insideyyy` (https://github.com/sgl-project/sglang/pull/15712#pullrequestreview-3610233548)
- `2025-12-29T04:12:27Z` `CHANGES_REQUESTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/15712#pullrequestreview-3614999477)
- `2026-01-04T06:36:14Z` `COMMENTED` by `Insideyyy` (https://github.com/sgl-project/sglang/pull/15712#pullrequestreview-3624847255)
- `2026-01-07T15:45:23Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/15712#pullrequestreview-3635522032)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-12-29T04:12:23Z` `inline` by `Fridge003` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`:633; signals: h100, h200, kernel, moe, perf, performance, triton; excerpt: "Can you add a condition checking whether the device is H20? Since the performance on H100/H200 hasn't been verified" (https://github.com/sgl-project/sglang/pull/15712#discussion_r2650149853)
- `2025-12-24T08:05:10Z` `inline` by `Insideyyy` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`:632; signals: block, kernel, memory, moe, triton; excerpt: "I don't think it's necessary to constrain batch size. For large Ms, config["BLOCK SIZE M"] is expected to be = 64 after tuning, otherwise ..." (https://github.com/sgl-project/sglang/pull/15712#discussion_r2645079946)
- `2025-12-24T07:22:39Z` `inline` by `Fridge003` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`:632; signals: benchmark, kernel, moe, triton; excerpt: "From the kernel benchmark, swap ab seems bringing benefit only on small Ms (batch sizes)? Do we need to add batch size to the ..." (https://github.com/sgl-project/sglang/pull/15712#discussion_r2645001965)
- `2026-01-04T06:36:14Z` `inline` by `Insideyyy` `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe_triton_kernels.py`:633; signals: kernel, moe, triton; excerpt: "Added. Now it will only be enabled on H20." (https://github.com/sgl-project/sglang/pull/15712#discussion_r2659447290)
