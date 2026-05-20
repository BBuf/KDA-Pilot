# PR Discussion Digest

- Source PR: [sgl-project/sglang#6885](https://github.com/sgl-project/sglang/pull/6885)
- Source page: `sources/prs/sglang/PR-6885.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6885`
- Generated at: `2026-05-20T15:30:51.947418+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-05T05:08:33Z`
- Merged: `2025-06-07T22:17:35Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 4 (approved=1, changes_requested=1, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: Xu-Wenqing, ch-wan, jonlai211
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-06-05T05:08:54Z` `COMMENTED` by `gemini-code-assist` - Hello @Xu-Wenqing, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/sgl-project/sglang/pull/6885#pullrequestreview-2898886746)
- `2025-06-05T05:10:50Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This pull request introduces a new JSON configuration file for H20 fused MoE kernel tuning, specifically ... (https://github.com/sgl-project/sglang/pull/6885#pullrequestreview-2898892501)
- `2025-06-05T05:15:53Z` `COMMENTED` by `ch-wan` - Thank you for your contribution. We have many users use TP16 for H20. Could you please also tune ... (https://github.com/sgl-project/sglang/pull/6885#pullrequestreview-2898899729)
- `2025-06-05T07:58:23Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/6885#pullrequestreview-2899255567)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/fused_moe_triton/configs/E=257,N=256,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-05T05:15:53Z` `review` `COMMENTED` by `ch-wan`; signals: general review; excerpt: "Thank you for your contribution. We have many users use TP16 for H20. Could you please also tune the config for TP16? Thanks!" (https://github.com/sgl-project/sglang/pull/6885#pullrequestreview-2898899729)
- `2025-06-05T05:53:30Z` `issue` by `Xu-Wenqing`; signals: general review; excerpt: "Thank you for your contribution. We have many users use TP16 for H20. Could you please also tune the config for TP16? Thanks! Sure." (https://github.com/sgl-project/sglang/pull/6885#issuecomment-2942859247)
