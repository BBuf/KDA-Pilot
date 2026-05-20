# PR Discussion Digest

- Source PR: [sgl-project/sglang#18073](https://github.com/sgl-project/sglang/pull/18073)
- Source page: `sources/prs/sglang/PR-18073.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18073`
- Generated at: `2026-05-20T15:28:33.135270+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-01T15:33:31Z`
- Merged: `2026-02-03T02:03:17Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: BBuf, HydraQYH
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-01T15:36:08Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new fused CUDA kernel for QK-Norm across heads, which is a ... (https://github.com/sgl-project/sglang/pull/18073#pullrequestreview-3735958014)
- `2026-02-02T01:37:26Z` `COMMENTED` by `HydraQYH` - Just one question here. (https://github.com/sgl-project/sglang/pull/18073#pullrequestreview-3736974611)
- `2026-02-02T09:09:23Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/18073#pullrequestreview-3738158937)
- `2026-02-02T09:12:34Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/18073#pullrequestreview-3738172215)
- `2026-02-02T09:13:14Z` `APPROVED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/18073#pullrequestreview-3738175466)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/csrc/elementwise/qknorm_across_heads.cuh`: 4 inline comment(s)

## High-Signal Discussion

- `2026-02-02T01:36:56Z` `inline` by `HydraQYH` `python/sglang/jit_kernel/csrc/elementwise/qknorm_across_heads.cuh`:113; signals: blackwell, kernel, warp; excerpt: "For diffusion models, what is the typical range of its hidden dim? If hidden dim is small enough that a single warp can handle ..." (https://github.com/sgl-project/sglang/pull/18073#discussion_r2752239983)
- `2026-02-02T09:09:23Z` `inline` by `BBuf` `python/sglang/jit_kernel/csrc/elementwise/qknorm_across_heads.cuh`:113; signals: kernel; excerpt: "1536, 3072, 5120 is the most common shape. refer to" (https://github.com/sgl-project/sglang/pull/18073#discussion_r2753310118)
- `2026-02-02T09:12:34Z` `inline` by `HydraQYH` `python/sglang/jit_kernel/csrc/elementwise/qknorm_across_heads.cuh`:113; signals: kernel; excerpt: "Got it." (https://github.com/sgl-project/sglang/pull/18073#discussion_r2753321396)
- `2026-02-02T01:37:26Z` `review` `COMMENTED` by `HydraQYH`; signals: general review; excerpt: "Just one question here." (https://github.com/sgl-project/sglang/pull/18073#pullrequestreview-3736974611)
