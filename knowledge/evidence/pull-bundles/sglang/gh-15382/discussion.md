# PR Discussion Digest

- Source PR: [sgl-project/sglang#15382](https://github.com/sgl-project/sglang/pull/15382)
- Source page: `sources/prs/sglang/PR-15382.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15382`
- Generated at: `2026-05-20T15:28:11.128249+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-18T07:18:51Z`
- Merged: `2025-12-19T13:27:02Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 4 (commented=4)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: IPostYellow, mickqian, ryang-max
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-12-18T12:32:06Z` `COMMENTED` by `mickqian` (https://github.com/sgl-project/sglang/pull/15382#pullrequestreview-3592706513)
- `2025-12-19T08:04:55Z` `COMMENTED` by `ryang-max` (https://github.com/sgl-project/sglang/pull/15382#pullrequestreview-3597440050)
- `2025-12-19T08:05:06Z` `COMMENTED` by `ryang-max` (https://github.com/sgl-project/sglang/pull/15382#pullrequestreview-3597440505)
- `2025-12-19T08:05:14Z` `COMMENTED` by `ryang-max` (https://github.com/sgl-project/sglang/pull/15382#pullrequestreview-3597441081)

## Inline Comment Hotspots

- `python/sglang/multimodal_gen/runtime/server_args.py`: 2 inline comment(s)
- `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`: 2 inline comment(s)
- `python/sglang/multimodal_gen/runtime/platforms/cuda.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-19T08:04:55Z` `inline` by `ryang-max` `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`:749; signals: pipeline; excerpt: "dit cpu offload was used to switch transformer in denoising process, which is useful for all serving modes; but for this, it's to offload ..." (https://github.com/sgl-project/sglang/pull/15382#discussion_r2634103520)
- `2025-12-18T12:31:49Z` `inline` by `mickqian` `python/sglang/multimodal_gen/runtime/pipelines_core/stages/denoising.py`:749; signals: pipeline; excerpt: "should we set dit cpu offload" (https://github.com/sgl-project/sglang/pull/15382#discussion_r2630880473)
- `2025-12-18T12:32:01Z` `inline` by `mickqian` `python/sglang/multimodal_gen/runtime/platforms/cuda.py`:248; signals: cuda; excerpt: "should we use sage by default?" (https://github.com/sgl-project/sglang/pull/15382#discussion_r2630881050)
- `2025-12-19T08:05:14Z` `inline` by `ryang-max` `python/sglang/multimodal_gen/runtime/platforms/cuda.py`:248; signals: cuda; excerpt: "Yes, resolved" (https://github.com/sgl-project/sglang/pull/15382#discussion_r2634104514)
- `2025-12-18T12:31:14Z` `inline` by `mickqian` `python/sglang/multimodal_gen/runtime/server_args.py`:222; signals: general review; excerpt: "duplicate with is local mode?" (https://github.com/sgl-project/sglang/pull/15382#discussion_r2630878507)
- `2025-12-19T08:05:06Z` `inline` by `ryang-max` `python/sglang/multimodal_gen/runtime/server_args.py`:222; signals: general review; excerpt: "Resolved" (https://github.com/sgl-project/sglang/pull/15382#discussion_r2634103929)
