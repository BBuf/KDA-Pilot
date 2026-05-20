# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8331](https://github.com/NVIDIA/cccl/pull/8331)
- Source page: `sources/prs/cccl-cub/PR-8331.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8331`
- Generated at: `2026-05-20T15:20:39.744221+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-08T18:03:25Z`
- Merged: `2026-04-09T11:26:29Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=3
- Human participants with discussion text: bernhardmgruber, miscco
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-08T18:07:17Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8331#pullrequestreview-4077208125)
- `2026-04-08T18:14:45Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8331#pullrequestreview-4077231658)
- `2026-04-09T07:30:33Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8331#pullrequestreview-4080476923)
- `2026-04-09T07:34:20Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8331#pullrequestreview-4080499232)

## Inline Comment Hotspots

- `cub/cub/block/radix_rank_sort_operations.cuh`: 5 inline comment(s)

## High-Signal Discussion

- `2026-04-08T18:11:29Z` `inline` by `miscco` `cub/cub/block/radix_rank_sort_operations.cuh`:169; signals: block; excerpt: "Nitpick: I would prefer if that would be something like is decomposable is fundamental is already taken an means a different thing" (https://github.com/NVIDIA/cccl/pull/8331#discussion_r3053277053)
- `2026-04-09T07:30:33Z` `inline` by `bernhardmgruber` `cub/cub/block/radix_rank_sort_operations.cuh`:169; signals: block; excerpt: "This trait does not describe decomposable types. It is true for types for which cub::Traits is specialized in a way where that allows us ..." (https://github.com/NVIDIA/cccl/pull/8331#discussion_r3056176113)
- `2026-04-08T18:07:18Z` `inline` by `bernhardmgruber` `cub/cub/block/radix_rank_sort_operations.cuh`:269; signals: block; excerpt: "@gevtushenko was this intended to be recursive?" (https://github.com/NVIDIA/cccl/pull/8331#discussion_r3053256000)
- `2026-04-08T18:12:47Z` `inline` by `miscco` `cub/cub/block/radix_rank_sort_operations.cuh`:263; signals: block; excerpt: "Nitpick: can we move the remove cv into the traits t alias?" (https://github.com/NVIDIA/cccl/pull/8331#discussion_r3053284608)
- `2026-04-09T07:34:19Z` `inline` by `bernhardmgruber` `cub/cub/block/radix_rank_sort_operations.cuh`:263; signals: block; excerpt: "yes" (https://github.com/NVIDIA/cccl/pull/8331#discussion_r3056193386)
