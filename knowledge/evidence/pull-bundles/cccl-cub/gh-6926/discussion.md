# PR Discussion Digest

- Source PR: [NVIDIA/cccl#6926](https://github.com/NVIDIA/cccl/pull/6926)
- Source page: `sources/prs/cccl-cub/PR-6926.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-6926`
- Generated at: `2026-05-20T15:20:06.834282+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-09T20:20:25Z`
- Merged: `2025-12-11T16:47:45Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 7 (approved=2, changes_requested=1, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: NaderAlAwar, bernhardmgruber, shwina
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-09T20:54:18Z` `COMMENTED` by `shwina` (https://github.com/NVIDIA/cccl/pull/6926#pullrequestreview-3559683637)
- `2025-12-09T23:36:50Z` `COMMENTED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/6926#pullrequestreview-3560147358)
- `2025-12-10T07:36:03Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6926#pullrequestreview-3561149745)
- `2025-12-10T07:37:26Z` `CHANGES_REQUESTED` by `bernhardmgruber` - This PR mixes two concerns, which should be proposed separately: 1. the rewrite of the dispatching from the ... (https://github.com/NVIDIA/cccl/pull/6926#pullrequestreview-3561155332)
- `2025-12-11T03:41:19Z` `COMMENTED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/6926#pullrequestreview-3565464029)
- `2025-12-11T12:23:27Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6926#pullrequestreview-3567189799)
- `2025-12-11T15:41:37Z` `APPROVED` by `shwina` - This looks good to me. Ideally, we would like to not replicate the handling of user-provided "guarantees" like ... (https://github.com/NVIDIA/cccl/pull/6926#pullrequestreview-3568078427)

## Inline Comment Hotspots

- `python/cuda_cccl/cuda/compute/_cccl_interop.py`: 2 inline comment(s)
- `cub/cub/device/dispatch/dispatch_reduce_nondeterministic.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-10T07:36:03Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_reduce_nondeterministic.cuh`:165; signals: benchmark, hang; excerpt: "Important: this seems like a full duplication of the logic in dispatch nondeterministic t for a reason I don't understand yet. Why is this ..." (https://github.com/NVIDIA/cccl/pull/6926#discussion_r2605532825)
- `2025-12-09T23:36:50Z` `inline` by `NaderAlAwar` `python/cuda_cccl/cuda/compute/_cccl_interop.py`:515; signals: cuda, hang; excerpt: "No I commented these out mistakenly. Undid the change." (https://github.com/NVIDIA/cccl/pull/6926#discussion_r2604701415)
- `2025-12-09T20:54:18Z` `inline` by `shwina` `python/cuda_cccl/cuda/compute/_cccl_interop.py`:515; signals: cuda; excerpt: "Should we be skipping sass check for a specific test?" (https://github.com/NVIDIA/cccl/pull/6926#discussion_r2604334910)
- `2025-12-10T07:37:26Z` `review` `CHANGES_REQUESTED` by `bernhardmgruber`; signals: general review; excerpt: "This PR mixes two concerns, which should be proposed separately: 1. the rewrite of the dispatching from the old to the new tuning API ..." (https://github.com/NVIDIA/cccl/pull/6926#pullrequestreview-3561155332)
- `2025-12-11T03:41:19Z` `inline` by `NaderAlAwar` `cub/cub/device/dispatch/dispatch_reduce_nondeterministic.cuh`:165; signals: general review; excerpt: "Moved rewrite of nondeterministic reduce dispatch to 6932" (https://github.com/NVIDIA/cccl/pull/6926#discussion_r2608997687)
- `2025-12-11T15:41:37Z` `review` `APPROVED` by `shwina`; signals: general review; excerpt: "This looks good to me. Ideally, we would like to not replicate the handling of user-provided "guarantees" like determinism at the CCCL.c level. The ..." (https://github.com/NVIDIA/cccl/pull/6926#pullrequestreview-3568078427)
