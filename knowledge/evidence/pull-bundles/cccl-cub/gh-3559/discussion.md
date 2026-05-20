# PR Discussion Digest

- Source PR: [NVIDIA/cccl#3559](https://github.com/NVIDIA/cccl/pull/3559)
- Source page: `sources/prs/cccl-cub/PR-3559.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-3559`
- Generated at: `2026-05-20T15:19:34.400589+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-28T07:56:56Z`
- Merged: `2025-02-07T09:58:10Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=3
- Human participants with discussion text: bernhardmgruber, elstehle, gonidelis, miscco
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-01-28T08:27:30Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/3559#pullrequestreview-2577435218)
- `2025-02-05T17:15:28Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3559#pullrequestreview-2596430167)
- `2025-02-05T18:28:05Z` `COMMENTED` by `bernhardmgruber` - I changed the tuning selection logic to be more akin to what the benchmark does. @gevtushenko I would ... (https://github.com/NVIDIA/cccl/pull/3559#pullrequestreview-2596634578)
- `2025-02-07T09:58:08Z` `APPROVED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/3559#pullrequestreview-2601303800)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/tuning/tuning_scan.cuh`: 3 inline comment(s)

## High-Signal Discussion

- `2025-02-06T19:14:04Z` `issue` by `bernhardmgruber`; signals: benchmark, hang, kernel, sm100; excerpt: "I diffed the SASS for SM100 from the commit on which @gonidelis did his benchmark to the tip of this PR including all my ..." (https://github.com/NVIDIA/cccl/pull/3559#issuecomment-2640772586)
- `2025-02-05T18:28:05Z` `review` `COMMENTED` by `bernhardmgruber`; signals: benchmark, hang; excerpt: "I changed the tuning selection logic to be more akin to what the benchmark does. @gevtushenko I would like your review here. I remember ..." (https://github.com/NVIDIA/cccl/pull/3559#pullrequestreview-2596634578)
- `2025-02-05T18:25:22Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:791; signals: benchmark, sm100; excerpt: "Here, we check whether the AccumT matches what we would use in the benchmark. If it does, we take a sm100 tuning, otherwise we ..." (https://github.com/NVIDIA/cccl/pull/3559#discussion_r1943460467)
- `2025-02-05T18:26:52Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:335; signals: benchmark, sm90; excerpt: "Compared with the sm90 tunings, we switch on the value size here, no the accum size, because that's what we actually also iterate in ..." (https://github.com/NVIDIA/cccl/pull/3559#discussion_r1943462496)
- `2025-02-05T17:00:34Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:173; signals: general review; excerpt: "Q: Why was this readded? It's not used anywhere." (https://github.com/NVIDIA/cccl/pull/3559#discussion_r1943334717)
