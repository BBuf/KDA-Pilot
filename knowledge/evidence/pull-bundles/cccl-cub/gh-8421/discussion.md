# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8421](https://github.com/NVIDIA/cccl/pull/8421)
- Source page: `sources/prs/cccl-cub/PR-8421.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8421`
- Generated at: `2026-05-20T15:20:43.536269+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-14T21:26:52Z`
- Merged: `2026-04-21T09:32:08Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 7
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=5
- Human participants with discussion text: bernhardmgruber, griwes
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-16T21:48:58Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8421#pullrequestreview-4124487565)
- `2026-04-20T21:53:09Z` `COMMENTED` by `griwes` (https://github.com/NVIDIA/cccl/pull/8421#pullrequestreview-4143767634)
- `2026-04-20T23:05:00Z` `COMMENTED` by `griwes` (https://github.com/NVIDIA/cccl/pull/8421#pullrequestreview-4144030526)
- `2026-04-21T09:31:30Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8421#pullrequestreview-4146602960)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/tuning/tuning_unique_by_key.cuh`: 6 inline comment(s)
- `cub/cub/device/device_select.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-16T21:25:08Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_unique_by_key.cuh`:992; signals: sm100, sm90; excerpt: "In this case, the sm100 tuning was not sufficiently better than the older sm90 tuning, so @gonidelis added the TODO comment and we fell ..." (https://github.com/NVIDIA/cccl/pull/8421#discussion_r3096456684)
- `2026-04-20T21:53:09Z` `inline` by `griwes` `cub/cub/device/dispatch/tuning/tuning_unique_by_key.cuh`:1530; signals: hang; excerpt: "I believe I fixed the dispatch path with the c.parallel changes, but yeah, I'll mark this function correctly; good catch." (https://github.com/NVIDIA/cccl/pull/8421#discussion_r3113891563)
- `2026-04-20T23:05:00Z` `inline` by `griwes` `cub/cub/device/dispatch/tuning/tuning_unique_by_key.cuh`:894; signals: race; excerpt: "I think :D :D :D :D :D :D is more appropriate, given the number of opening braces in that hunk :P" (https://github.com/NVIDIA/cccl/pull/8421#discussion_r3114134099)
- `2026-04-16T21:19:15Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_unique_by_key.cuh`:902; signals: general review; excerpt: "Suggestion: I would prefer to construct the delay constructor policy directly here instead of creating the type and converting it. I had this generated ..." (https://github.com/NVIDIA/cccl/pull/8421#discussion_r3096431414)
- `2026-04-16T21:28:13Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_unique_by_key.cuh`:1530; signals: general review; excerpt: "Important: Reaching out to MaxPolicy is only correct in device code, so let's make sure we are not calling this on the host: Edit: ..." (https://github.com/NVIDIA/cccl/pull/8421#discussion_r3096469396)
- `2026-04-16T21:44:05Z` `inline` by `bernhardmgruber` `cub/cub/device/device_select.cuh`:41; signals: general review; excerpt: "Remark: I don't mind if the comment is deleted, but the TODO is not addressed yet. This will be done with 7464, which will ..." (https://github.com/NVIDIA/cccl/pull/8421#discussion_r3096534232)
- `2026-04-16T21:15:47Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_unique_by_key.cuh`:894; signals: general review; excerpt: ":D :D :D :D" (https://github.com/NVIDIA/cccl/pull/8421#discussion_r3096417084)
