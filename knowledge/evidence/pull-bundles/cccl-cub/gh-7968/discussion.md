# PR Discussion Digest

- Source PR: [NVIDIA/cccl#7968](https://github.com/NVIDIA/cccl/pull/7968)
- Source page: `sources/prs/cccl-cub/PR-7968.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-7968`
- Generated at: `2026-05-20T15:20:25.746006+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-10T03:57:18Z`
- Merged: `2026-03-13T18:07:15Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 9
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: bernhardmgruber, gonidelis
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-10T10:44:56Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7968#pullrequestreview-3921453024)
- `2026-03-12T15:39:33Z` `COMMENTED` by `bernhardmgruber` - Looks mostly good, here a few things before we can merge: (https://github.com/NVIDIA/cccl/pull/7968#pullrequestreview-3937669995)
- `2026-03-12T22:33:51Z` `COMMENTED` by `gonidelis` (https://github.com/NVIDIA/cccl/pull/7968#pullrequestreview-3940196264)
- `2026-03-13T18:01:05Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7968#pullrequestreview-3946020666)
- `2026-03-13T18:05:46Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7968#pullrequestreview-3946051287)
- `2026-03-13T18:06:51Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7968#pullrequestreview-3946057145)
- `2026-03-13T18:07:11Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7968#pullrequestreview-3946059110)

## Inline Comment Hotspots

- `cub/test/catch2_test_device_merge_sort_env_api.cu`: 4 inline comment(s)
- `cub/test/catch2_test_device_merge_sort_env.cu`: 3 inline comment(s)
- `cub/cub/device/device_merge_sort.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-12T15:39:33Z` `review` `COMMENTED` by `bernhardmgruber`; signals: general review; excerpt: "Looks mostly good, here a few things before we can merge:" (https://github.com/NVIDIA/cccl/pull/7968#pullrequestreview-3937669995)
- `2026-03-10T10:44:39Z` `inline` by `bernhardmgruber` `cub/cub/device/device_merge_sort.cuh`:308; signals: general review; excerpt: "Note: I need to figure out what kind of determinism we provide. The merge sort implementation is stable according to the docs, so it ..." (https://github.com/NVIDIA/cccl/pull/7968#discussion_r2910870050)
- `2026-03-13T18:01:05Z` `inline` by `bernhardmgruber` `cub/cub/device/device_merge_sort.cuh`:308; signals: general review; excerpt: "I concluded we just ignore determinism for now and revisit the discussion if we ever want to add an algorithm with different determinism than ..." (https://github.com/NVIDIA/cccl/pull/7968#discussion_r2932930740)
- `2026-03-12T15:37:34Z` `inline` by `bernhardmgruber` `cub/test/catch2_test_device_merge_sort_env.cu`:39; signals: general review; excerpt: "Important: Please also verify that the values were correctly reordered" (https://github.com/NVIDIA/cccl/pull/7968#discussion_r2925553503)
- `2026-03-12T15:38:01Z` `inline` by `bernhardmgruber` `cub/test/catch2_test_device_merge_sort_env.cu`:105; signals: general review; excerpt: "Same here." (https://github.com/NVIDIA/cccl/pull/7968#discussion_r2925556754)
- `2026-03-12T15:38:50Z` `inline` by `bernhardmgruber` `cub/test/catch2_test_device_merge_sort_env_api.cu`:22; signals: general review; excerpt: "Suggestion: remove the empty line Applies to the other examples as well." (https://github.com/NVIDIA/cccl/pull/7968#discussion_r2925562717)
- `2026-03-12T15:39:11Z` `inline` by `bernhardmgruber` `cub/test/catch2_test_device_merge_sort_env_api.cu`:28; signals: general review; excerpt: "Important: check expected keys" (https://github.com/NVIDIA/cccl/pull/7968#discussion_r2925565068)
- `2026-03-12T22:33:51Z` `inline` by `gonidelis` `cub/test/catch2_test_device_merge_sort_env_api.cu`:28; signals: general review; excerpt: "unstable sort, this should be flavory" (https://github.com/NVIDIA/cccl/pull/7968#discussion_r2927774746)
- `2026-03-13T18:05:45Z` `inline` by `bernhardmgruber` `cub/test/catch2_test_device_merge_sort_env_api.cu`:28; signals: general review; excerpt: "Right. They keys will be stable but not the values. Good thinking!" (https://github.com/NVIDIA/cccl/pull/7968#discussion_r2932957973)
- `2026-03-13T18:06:51Z` `inline` by `bernhardmgruber` `cub/test/catch2_test_device_merge_sort_env.cu`:105; signals: general review; excerpt: "Values could be unstable, so let's omit the check." (https://github.com/NVIDIA/cccl/pull/7968#discussion_r2932963267)
- `2026-03-12T00:52:38Z` `issue` by `gonidelis`; signals: general review; excerpt: "After long discussion with @bernhardmgruber we decided not to specify any deterministic guarantees for DeviceMergeSort" (https://github.com/NVIDIA/cccl/pull/7968#issuecomment-4043165592)
