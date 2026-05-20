# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8395](https://github.com/NVIDIA/cccl/pull/8395)
- Source page: `sources/prs/cccl-cub/PR-8395.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8395`
- Generated at: `2026-05-20T15:20:43.533912+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-13T18:18:05Z`
- Merged: `2026-04-29T01:06:50Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: bernhardmgruber, fbusato, miscco
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-14T06:33:08Z` `COMMENTED` by `miscco` - The code changes look good to me. However, it looks like there were no benchmark results (https://github.com/NVIDIA/cccl/pull/8395#pullrequestreview-4103759863)
- `2026-04-27T07:21:44Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8395#pullrequestreview-4178878035)
- `2026-04-27T07:21:53Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8395#pullrequestreview-4178878927)

## Inline Comment Hotspots

- `ci/bench.yaml`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-14T20:44:01Z` `issue` by `fbusato`; signals: benchmark, perf, performance, sm100, sm120, sm90; excerpt: "Perf results look ok on sm120, but not on the other architectures. It is fun that I just checked the SASS for Radix Sort ..." (https://github.com/NVIDIA/cccl/pull/8395#issuecomment-4247021098)
- `2026-04-14T06:33:08Z` `review` `COMMENTED` by `miscco`; signals: benchmark, hang; excerpt: "The code changes look good to me. However, it looks like there were no benchmark results" (https://github.com/NVIDIA/cccl/pull/8395#pullrequestreview-4103759863)
- `2026-04-14T20:10:09Z` `issue` by `bernhardmgruber`; signals: perf, sm120; excerpt: "Perf results look ok on sm120, but not on the other architectures." (https://github.com/NVIDIA/cccl/pull/8395#issuecomment-4246807241)
- `2026-04-27T07:21:44Z` `inline` by `bernhardmgruber` `ci/bench.yaml`; signals: hang; excerpt: "Please revert changes to this file." (https://github.com/NVIDIA/cccl/pull/8395#discussion_r3145508683)
