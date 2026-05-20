# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8212](https://github.com/NVIDIA/cccl/pull/8212)
- Source page: `sources/prs/cccl-cub/PR-8212.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8212`
- Generated at: `2026-05-20T15:20:32.192854+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-30T09:27:45Z`
- Merged: `2026-03-31T06:22:25Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 11 (approved=3, commented=8)
- Inline review comments: 13
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: NaderAlAwar, bernhardmgruber, miscco
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-30T13:11:03Z` `APPROVED` by `miscco` - Mostly nits (https://github.com/NVIDIA/cccl/pull/8212#pullrequestreview-4030405071)
- `2026-03-30T13:48:03Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8212#pullrequestreview-4030706336)
- `2026-03-30T13:51:40Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8212#pullrequestreview-4030730163)
- `2026-03-30T13:52:53Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8212#pullrequestreview-4030738471)
- `2026-03-30T14:04:27Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8212#pullrequestreview-4030850864)
- `2026-03-30T14:06:24Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8212#pullrequestreview-4030868468)
- `2026-03-30T14:07:38Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8212#pullrequestreview-4030879094)
- `2026-03-30T14:27:26Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8212#pullrequestreview-4031017031)
- `2026-03-30T15:11:12Z` `COMMENTED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8212#pullrequestreview-4031325570)
- `2026-03-30T16:15:58Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8212#pullrequestreview-4031734719)
- `2026-03-30T16:18:20Z` `APPROVED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8212#pullrequestreview-4031747196)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/dispatch_histogram.cuh`: 6 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_histogram.cuh`: 5 inline comment(s)
- `cub/cub/device/dispatch/kernels/kernel_histogram.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-30T13:48:03Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_histogram.cuh`:352; signals: kernel, perf; excerpt: "Why? I just want to reduce a bunch of ints, so there is no need for that reduction to be performed left-to-right to preserve ..." (https://github.com/NVIDIA/cccl/pull/8212#discussion_r3009923231)
- `2026-03-30T15:10:53Z` `inline` by `NaderAlAwar` `cub/cub/device/dispatch/dispatch_histogram.cuh`:769; signals: ptx; excerpt: "Critical: this should be static cast (arch id) 10, like scan. MaxPolicy::Invoke is keyed on PTX versions (500/900/1000), not raw arch ids (50/90/100)." (https://github.com/NVIDIA/cccl/pull/8212#discussion_r3010454994)
- `2026-03-30T13:02:26Z` `inline` by `miscco` `cub/cub/device/dispatch/kernels/kernel_histogram.cuh`:352; signals: kernel; excerpt: "Technically this should be Because it is meant to be run serially" (https://github.com/NVIDIA/cccl/pull/8212#discussion_r3009658064)
- `2026-03-30T14:06:23Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_histogram.cuh`:319; signals: kernel; excerpt: "Not at all, it's just a hardcoded parameter of the init kernel." (https://github.com/NVIDIA/cccl/pull/8212#discussion_r3010054678)
- `2026-03-30T13:07:06Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_histogram.cuh`:307; signals: general review; excerpt: "Nitpick: This goes contrary to the other policy selectors where we start with the newest policy and then move down. Its also a bit ..." (https://github.com/NVIDIA/cccl/pull/8212#discussion_r3009682563)
- `2026-03-30T13:51:40Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_histogram.cuh`:292; signals: general review; excerpt: "The function was called t scale in the old policy hub and I frankly don't know what its meaning is. @gevtushenko moved it around ..." (https://github.com/NVIDIA/cccl/pull/8212#discussion_r3009945326)
- `2026-03-30T13:52:53Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_histogram.cuh`:307; signals: general review; excerpt: "ok, the state in this PR makes absolutely no sense. I wonder why it does not cause any SASS diffs then." (https://github.com/NVIDIA/cccl/pull/8212#discussion_r3009953006)
- `2026-03-30T14:07:38Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_histogram.cuh`:834; signals: general review; excerpt: "I guess it's PRIVATIZED SMEM BINS (256) + 1, since the number of levels is usually one higher than the number of bins. I ..." (https://github.com/NVIDIA/cccl/pull/8212#discussion_r3010063347)
- `2026-03-30T13:04:36Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_histogram.cuh`:292; signals: general review; excerpt: "Can we have a better name?" (https://github.com/NVIDIA/cccl/pull/8212#discussion_r3009669790)
- `2026-03-30T13:08:43Z` `inline` by `miscco` `cub/cub/device/dispatch/dispatch_histogram.cuh`:319; signals: general review; excerpt: "Question: Should this be something from the policy?" (https://github.com/NVIDIA/cccl/pull/8212#discussion_r3009691011)
- `2026-03-30T13:10:12Z` `inline` by `miscco` `cub/cub/device/dispatch/dispatch_histogram.cuh`:834; signals: general review; excerpt: "Is there a correlation to PRIVATIZED SMEM BINS ?" (https://github.com/NVIDIA/cccl/pull/8212#discussion_r3009699236)
- `2026-03-30T14:04:27Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_histogram.cuh`:307; signals: general review; excerpt: "ok, it should have worked, but it's very confusing. Fixed." (https://github.com/NVIDIA/cccl/pull/8212#discussion_r3010040202)
