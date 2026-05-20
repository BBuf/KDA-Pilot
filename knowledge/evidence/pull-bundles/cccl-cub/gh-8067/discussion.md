# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8067](https://github.com/NVIDIA/cccl/pull/8067)
- Source page: `sources/prs/cccl-cub/PR-8067.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8067`
- Generated at: `2026-05-20T15:20:28.017155+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-17T13:08:42Z`
- Merged: `2026-05-11T10:43:02Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 7 (approved=4, changes_requested=1, commented=2)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: bernhardmgruber, davebayer, miscco, pciolkosz
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-17T13:57:46Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8067#pullrequestreview-3960992382)
- `2026-03-17T14:37:21Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8067#pullrequestreview-3961292070)
- `2026-03-17T16:02:03Z` `APPROVED` by `pciolkosz` (https://github.com/NVIDIA/cccl/pull/8067#pullrequestreview-3961949689)
- `2026-05-11T09:43:19Z` `CHANGES_REQUESTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8067#pullrequestreview-4262363651)
- `2026-05-11T09:45:38Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/8067#pullrequestreview-4262378228)
- `2026-05-11T09:49:27Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8067#pullrequestreview-4262401193)
- `2026-05-11T09:49:37Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8067#pullrequestreview-4262402334)

## Inline Comment Hotspots

- `cudax/include/cuda/experimental/__group/this_group.cuh`: 3 inline comment(s)

## High-Signal Discussion

- `2026-05-11T09:43:15Z` `inline` by `miscco` `cudax/include/cuda/experimental/__group/this_group.cuh`:476; signals: cuda, sm90; excerpt: "Critical: This is not valid pre SM90, see" (https://github.com/NVIDIA/cccl/pull/8067#discussion_r3217802879)
- `2026-05-11T09:45:38Z` `inline` by `davebayer` `cudax/include/cuda/experimental/__group/this_group.cuh`:476; signals: cuda, hopper; excerpt: "I don't think you are right, only NV THREAD SCOPE CLUSTER is unsupported before Hopper:" (https://github.com/NVIDIA/cccl/pull/8067#discussion_r3217815596)
- `2026-05-11T09:49:26Z` `inline` by `miscco` `cudax/include/cuda/experimental/__group/this_group.cuh`:476; signals: cuda; excerpt: "Oh sorry you are right" (https://github.com/NVIDIA/cccl/pull/8067#discussion_r3217836271)
