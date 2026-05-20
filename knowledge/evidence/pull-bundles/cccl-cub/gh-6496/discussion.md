# PR Discussion Digest

- Source PR: [NVIDIA/cccl#6496](https://github.com/NVIDIA/cccl/pull/6496)
- Source page: `sources/prs/cccl-cub/PR-6496.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-6496`
- Generated at: `2026-05-20T15:19:57.094043+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-05T13:01:50Z`
- Merged: `2025-11-05T18:17:24Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=3, commented=1)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: ahendriksen, bernhardmgruber, davebayer, miscco
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-05T13:05:41Z` `APPROVED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/6496#pullrequestreview-3421895264)
- `2025-11-05T15:19:25Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/6496#pullrequestreview-3422804261)
- `2025-11-05T15:22:44Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6496#pullrequestreview-3422832236)
- `2025-11-05T15:45:40Z` `APPROVED` by `ahendriksen` - LGTM (https://github.com/NVIDIA/cccl/pull/6496#pullrequestreview-3422951626)

## Inline Comment Hotspots

- `cub/cub/block/block_load_to_shared.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-05T15:22:44Z` `inline` by `bernhardmgruber` `cub/cub/block/block_load_to_shared.cuh`:251; signals: block, sm90; excerpt: "Because here, only the SM90 code path used a barrier for async copy synchronization. The SM80 code path uses a commit group and thus ..." (https://github.com/NVIDIA/cccl/pull/6496#discussion_r2495046447)
- `2025-11-05T15:18:46Z` `inline` by `miscco` `cub/cub/block/block_load_to_shared.cuh`:251; signals: block; excerpt: "Why is this SM 90 when we support it from SM 80 onwards?" (https://github.com/NVIDIA/cccl/pull/6496#discussion_r2495024999)
