# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8639](https://github.com/NVIDIA/cccl/pull/8639)
- Source page: `sources/prs/cccl-cub/PR-8639.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8639`
- Generated at: `2026-05-20T15:20:51.574765+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-22T21:32:44Z`
- Merged: `2026-04-28T16:25:12Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 30 (approved=1, commented=29)
- Inline review comments: 79
- Review threads observed: 56
- Resolved/outdated thread markers: resolved=43, outdated=27
- Human participants with discussion text: NaderAlAwar, bernhardmgruber, oleksandr-pavlyk
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-23T12:59:30Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4162536434)
- `2026-04-23T13:03:21Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4162561238)
- `2026-04-23T13:06:35Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4162585719)
- `2026-04-23T13:59:50Z` `COMMENTED` by `bernhardmgruber` - Here is some high level review (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4162868436)
- `2026-04-23T14:08:48Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4163153981)
- `2026-04-23T14:11:50Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4163180318)
- `2026-04-23T14:47:44Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4163438176)
- `2026-04-23T20:24:51Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4165693499)
- `2026-04-24T12:48:39Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4170531959)
- `2026-04-24T13:15:23Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4170692013)
- `2026-04-24T13:15:55Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4170695847)
- `2026-04-24T13:56:04Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4171008338)
- `2026-04-24T14:21:44Z` `COMMENTED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4170786303)
- `2026-04-24T16:16:09Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4171934892)
- `2026-04-24T16:36:31Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4172049527)
- `2026-04-24T17:22:54Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4172286038)
- `2026-04-24T21:44:12Z` `APPROVED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4173493289)
- `2026-04-25T16:12:35Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4175828317)
- `2026-04-25T20:20:29Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4176084610)
- `2026-04-26T02:09:48Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4176427416)
- `2026-04-27T09:26:45Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4179629513)
- `2026-04-27T18:47:32Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4183402496)
- `2026-04-27T18:49:56Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4183417014)
- `2026-04-27T18:51:37Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/8639#pullrequestreview-4183426199)
- ... 6 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `cub/cub/device/dispatch/kernels/kernel_segmented_scan.cuh`: 27 inline comment(s)
- `cub/cub/detail/segmented_scan_helpers.cuh`: 17 inline comment(s)
- `cub/cub/device/dispatch/dispatch_segmented_scan.cuh`: 12 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_segmented_scan.cuh`: 9 inline comment(s)
- `cub/test/catch2_test_device_segmented_scan_multi_segment.cu`: 8 inline comment(s)
- `cub/benchmarks/bench/segmented_scan/base.cuh`: 2 inline comment(s)
- `cub/cub/device/dispatch/kernels/kernel_warp_segmented_scan.cuh`: 2 inline comment(s)
- `cub/cub/device/device_segmented_scan.cuh`: 1 inline comment(s)
- `cub/test/catch2_test_device_segmented_scan.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-24T17:22:54Z` `inline` by `oleksandr-pavlyk` `cub/cub/device/dispatch/dispatch_segmented_scan.cuh`:126; signals: benchmark, block, warp; excerpt: "Great question. In 6712, the choice of worker::block is most appropriate when segments are sufficiently large; as segment sizes become smaller, it becomes beneficial ..." (https://github.com/NVIDIA/cccl/pull/8639#discussion_r3139296744)
- `2026-04-23T13:58:46Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_segmented_scan.cuh`:639; signals: block, kernel; excerpt: "Suggestion: the workaround I sometimes use here is to just wrap the tuning policy in a nullary callable and pass its type to the ..." (https://github.com/NVIDIA/cccl/pull/8639#discussion_r3131346507)
- `2026-04-23T14:08:47Z` `inline` by `oleksandr-pavlyk` `cub/cub/device/dispatch/tuning/tuning_segmented_scan.cuh`:111; signals: benchmark, hang; excerpt: "My local benchmarking kept pointing me to 9 as being an optimal value. This should only matter for very short types due to scaling. ..." (https://github.com/NVIDIA/cccl/pull/8639#discussion_r3131417341)
- `2026-04-24T16:16:09Z` `inline` by `oleksandr-pavlyk` `cub/cub/device/dispatch/kernels/kernel_segmented_scan.cuh`:634; signals: compile, kernel; excerpt: "We could, but I think we have shaving a bit of compile time here. With cub::detail::policy getter or cub::detail::device policy getter we would need ..." (https://github.com/NVIDIA/cccl/pull/8639#discussion_r3138973630)
- `2026-04-28T14:01:12Z` `inline` by `bernhardmgruber` `cub/cub/detail/segmented_scan_helpers.cuh`:384; signals: perf, performance; excerpt: "Remark: multi segmented input iterator is technically an input iterator, because it does not return value type& for operator . But that may degrade ..." (https://github.com/NVIDIA/cccl/pull/8639#discussion_r3154697244)
- `2026-04-28T14:18:53Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_segmented_scan.cuh`:45; signals: block, kernel; excerpt: "Remark: I dislike such section comments since the grouping they introduce eventually gets out of sync with the code. Also: what is a thread ..." (https://github.com/NVIDIA/cccl/pull/8639#discussion_r3154820365)
- `2026-04-28T14:29:21Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_segmented_scan.cuh`:279; signals: compile, kernel; excerpt: "Important: Please formulate constraints in a way that forces the constraint's evaluation before the compiler can build the function signature. This avoids ambiguity errors ..." (https://github.com/NVIDIA/cccl/pull/8639#discussion_r3154900217)
- `2026-04-24T21:25:31Z` `inline` by `NaderAlAwar` `cub/cub/device/dispatch/kernels/kernel_warp_segmented_scan.cuh`:566; signals: kernel, warp; excerpt: "Question: This is not called anywhere in this PR currently. Do you intend to keep it?" (https://github.com/NVIDIA/cccl/pull/8639#discussion_r3140370629)
- `2026-04-25T16:12:35Z` `inline` by `oleksandr-pavlyk` `cub/cub/device/dispatch/kernels/kernel_warp_segmented_scan.cuh`:566; signals: kernel, warp; excerpt: "This file was meant to be removed in the commit. I will amend and force push." (https://github.com/NVIDIA/cccl/pull/8639#discussion_r3142219917)
- `2026-04-28T14:09:04Z` `inline` by `oleksandr-pavlyk` `cub/cub/device/dispatch/kernels/kernel_segmented_scan.cuh`:106; signals: block, kernel; excerpt: "Done. Used static constexpr auto agent policy = SegmentedScanPolicyGetterT{}().block;." (https://github.com/NVIDIA/cccl/pull/8639#discussion_r3154753831)
- `2026-04-28T14:24:07Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_segmented_scan.cuh`:191; signals: block, kernel; excerpt: "Suggestion: the added value of this documentation block is very little, can we delete it?" (https://github.com/NVIDIA/cccl/pull/8639#discussion_r3154860797)
- `2026-04-28T14:27:45Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_segmented_scan.cuh`:220; signals: hang, kernel; excerpt: "Remark: non-canonical for loops are always a bit surprising. No change requested." (https://github.com/NVIDIA/cccl/pull/8639#discussion_r3154888047)
