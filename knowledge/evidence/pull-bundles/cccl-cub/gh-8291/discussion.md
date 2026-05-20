# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8291](https://github.com/NVIDIA/cccl/pull/8291)
- Source page: `sources/prs/cccl-cub/PR-8291.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8291`
- Generated at: `2026-05-20T15:20:36.774433+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-04T22:11:17Z`
- Merged: `2026-04-30T10:24:40Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: Jacobfaib, bernhardmgruber, davebayer, miscco
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-29T22:15:09Z` `COMMENTED` by `Jacobfaib` (https://github.com/NVIDIA/cccl/pull/8291#pullrequestreview-4201067753)
- `2026-04-30T07:55:43Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8291#pullrequestreview-4203408687)
- `2026-04-30T07:57:19Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8291#pullrequestreview-4203417964)
- `2026-04-30T08:30:23Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8291#pullrequestreview-4203621993)
- `2026-04-30T09:52:19Z` `APPROVED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/8291#pullrequestreview-4204147809)

## Inline Comment Hotspots

- `thrust/thrust/system/cuda/detail/extrema.h`: 6 inline comment(s)

## High-Signal Discussion

- `2026-04-30T07:55:43Z` `inline` by `bernhardmgruber` `thrust/thrust/system/cuda/detail/extrema.h`:366; signals: cuda; excerpt: "I'll spell just auto to follow the rule and mess with everybody ;) clang-tidy will hopefully handle this in the future." (https://github.com/NVIDIA/cccl/pull/8291#discussion_r3166433994)
- `2026-04-30T07:57:19Z` `inline` by `bernhardmgruber` `thrust/thrust/system/cuda/detail/extrema.h`:343; signals: cuda; excerpt: "CUB would be fine, but we use the raw cudaStream t everywhere in Thrust currently. cuda cub::stream is also part of the public API. ..." (https://github.com/NVIDIA/cccl/pull/8291#discussion_r3166441868)
- `2026-04-29T22:05:49Z` `inline` by `Jacobfaib` `thrust/thrust/system/cuda/detail/extrema.h`:343; signals: cuda; excerpt: "stream ref? Or does CUB not understand this?" (https://github.com/NVIDIA/cccl/pull/8291#discussion_r3164459706)
- `2026-04-29T22:07:47Z` `inline` by `Jacobfaib` `thrust/thrust/system/cuda/detail/extrema.h`:357; signals: cuda; excerpt: "Needs include or summat like that." (https://github.com/NVIDIA/cccl/pull/8291#discussion_r3164469481)
- `2026-04-29T22:10:35Z` `inline` by `Jacobfaib` `thrust/thrust/system/cuda/detail/extrema.h`:366; signals: cuda; excerpt: "Nit: you could say auto (even better, auto const!) here since you spell out void in the cast." (https://github.com/NVIDIA/cccl/pull/8291#discussion_r3164481610)
- `2026-04-08T13:29:16Z` `issue` by `bernhardmgruber`; signals: overflow; excerpt: "Looks like we are not returning the right values: This may have been an issue in 8285, where abs() was causing integer overflow when ..." (https://github.com/NVIDIA/cccl/pull/8291#issuecomment-4206588022)
