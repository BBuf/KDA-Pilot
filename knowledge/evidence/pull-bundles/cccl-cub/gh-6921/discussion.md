# PR Discussion Digest

- Source PR: [NVIDIA/cccl#6921](https://github.com/NVIDIA/cccl/pull/6921)
- Source page: `sources/prs/cccl-cub/PR-6921.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-6921`
- Generated at: `2026-05-20T15:20:06.830740+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-09T08:43:33Z`
- Merged: `2025-12-10T17:46:23Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: bernhardmgruber, elstehle, miscco
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-09T15:15:02Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/6921#pullrequestreview-3557998365)
- `2025-12-09T15:28:35Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6921#pullrequestreview-3558073902)
- `2025-12-10T12:12:06Z` `APPROVED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/6921#pullrequestreview-3562258213)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/tuning/tuning_transform.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-09T15:14:59Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_transform.cuh`:438; signals: cuda; excerpt: "What about nv bfloat16 ? Should this be ::cuda::std:: is extended floating point v Also why is this and not &&" (https://github.com/NVIDIA/cccl/pull/6921#discussion_r2603095606)
- `2025-12-10T08:41:08Z` `issue` by `bernhardmgruber`; signals: kernel, vector; excerpt: "Using the vectorized kernel for all workloads results in:" (https://github.com/NVIDIA/cccl/pull/6921#issuecomment-3635980462)
- `2025-12-09T15:28:35Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_transform.cuh`:438; signals: general review; excerpt: "Yes, it should be &&. And this is based on data by @NaderAlAwar. I actually do wonder whether it would be better to just ..." (https://github.com/NVIDIA/cccl/pull/6921#discussion_r2603150002)
