# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8898](https://github.com/NVIDIA/cccl/pull/8898)
- Source page: `sources/prs/cccl-cub/PR-8898.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8898`
- Generated at: `2026-05-20T15:20:59.697659+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-11T14:59:47Z`
- Merged: `2026-05-12T16:39:32Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: bernhardmgruber, davebayer, miscco
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-11T15:01:17Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8898#pullrequestreview-4264817082)
- `2026-05-12T11:16:24Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8898#pullrequestreview-4271711682)
- `2026-05-12T13:43:05Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/8898#pullrequestreview-4272808697)
- `2026-05-12T13:45:52Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8898#pullrequestreview-4272834578)
- `2026-05-12T14:20:59Z` `APPROVED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/8898#pullrequestreview-4273190001)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/tuning/tuning_segmented_radix_sort.cuh`: 3 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_radix_sort.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-12T11:16:04Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_radix_sort.cuh`:912; signals: general review; excerpt: "Important: The function call should be qualified, a user could reasonably have a function named like that" (https://github.com/NVIDIA/cccl/pull/8898#discussion_r3225911374)
- `2026-05-11T15:01:14Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_segmented_radix_sort.cuh`:2; signals: general review; excerpt: "Since the main content are the tuning values, I decided to retain the original copyright." (https://github.com/NVIDIA/cccl/pull/8898#discussion_r3219925746)
- `2026-05-12T13:43:05Z` `inline` by `davebayer` `cub/cub/device/dispatch/tuning/tuning_segmented_radix_sort.cuh`:61; signals: general review; excerpt: "Aren't policy selectors required to be empty?" (https://github.com/NVIDIA/cccl/pull/8898#discussion_r3226866681)
- `2026-05-12T13:45:51Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_segmented_radix_sort.cuh`:61; signals: general review; excerpt: "The public ones yes. The ones we need for CCCL.C are all stateful to handle type erasure." (https://github.com/NVIDIA/cccl/pull/8898#discussion_r3226888294)
