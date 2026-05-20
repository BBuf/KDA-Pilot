# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8611](https://github.com/NVIDIA/cccl/pull/8611)
- Source page: `sources/prs/cccl-cub/PR-8611.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8611`
- Generated at: `2026-05-20T15:20:49.008588+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-22T06:20:49Z`
- Merged: `2026-04-24T01:20:55Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 8 (approved=2, changes_requested=1, commented=5)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: bernhardmgruber, gonidelis
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-22T06:24:38Z` `COMMENTED` by `gonidelis` (https://github.com/NVIDIA/cccl/pull/8611#pullrequestreview-4152472142)
- `2026-04-23T20:21:52Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8611#pullrequestreview-4165672397)
- `2026-04-23T20:23:03Z` `COMMENTED` by `gonidelis` (https://github.com/NVIDIA/cccl/pull/8611#pullrequestreview-4165681709)
- `2026-04-23T21:17:02Z` `APPROVED` by `bernhardmgruber` - LGTM, let's just wait for the final verification benchmark including I128 (https://github.com/NVIDIA/cccl/pull/8611#pullrequestreview-4166058920)
- `2026-04-23T22:51:34Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8611#pullrequestreview-4166619393)
- `2026-04-23T22:51:41Z` `CHANGES_REQUESTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8611#pullrequestreview-4166619967)
- `2026-04-23T23:37:12Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8611#pullrequestreview-4166830487)
- `2026-04-23T23:42:56Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8611#pullrequestreview-4166855551)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/tuning/tuning_scan.cuh`: 5 inline comment(s)

## High-Signal Discussion

- `2026-04-23T20:21:52Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:937; signals: b200, sm100, sm120; excerpt: "I am confused. This is adding a tuning for sm120, but the comment is saying "on B200". The values are also the same as ..." (https://github.com/NVIDIA/cccl/pull/8611#discussion_r3133581766)
- `2026-04-22T06:55:31Z` `issue` by `bernhardmgruber`; signals: benchmark, regression; excerpt: "given that i32 doesn't gain much but f32 does should i constrain case 2 with an embeded if (input type == type t::float32 && ..." (https://github.com/NVIDIA/cccl/pull/8611#issuecomment-4294190812)
- `2026-04-22T07:41:07Z` `issue` by `bernhardmgruber`; signals: sm120; excerpt: "Great work so far! Please also tune for I128. I will make some experiments for SM120 using your new values." (https://github.com/NVIDIA/cccl/pull/8611#issuecomment-4294431719)
- `2026-04-22T08:52:26Z` `issue` by `bernhardmgruber`; signals: sm120; excerpt: "I applied the following diff to remove any SM120 specific tuning and then compared the new tunings in this PR against what we had ..." (https://github.com/NVIDIA/cccl/pull/8611#issuecomment-4294852015)
- `2026-04-22T14:21:50Z` `issue` by `gonidelis`; signals: b200; excerpt: "i120 is workstation and b200 is datacenter the bad results are no surprise to me" (https://github.com/NVIDIA/cccl/pull/8611#issuecomment-4297029488)
- `2026-04-22T14:58:54Z` `issue` by `gonidelis`; signals: b200; excerpt: "B200 results for current state - f64 is positively affected from i64 coincidentally" (https://github.com/NVIDIA/cccl/pull/8611#issuecomment-4297336306)
- `2026-04-23T21:17:02Z` `review` `APPROVED` by `bernhardmgruber`; signals: benchmark; excerpt: "LGTM, let's just wait for the final verification benchmark including I128" (https://github.com/NVIDIA/cccl/pull/8611#pullrequestreview-4166058920)
- `2026-04-23T23:36:04Z` `issue` by `gonidelis`; signals: speedup; excerpt: "FINAL SPEEDUP RESULTS FOR CURRENT ToT OF THIS BRANCH" (https://github.com/NVIDIA/cccl/pull/8611#issuecomment-4309077406)
- `2026-04-22T06:24:38Z` `inline` by `gonidelis` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:961; signals: general review; excerpt: "reported scores are for f32, not for i32 which only had noise" (https://github.com/NVIDIA/cccl/pull/8611#discussion_r3121959592)
- `2026-04-23T20:23:03Z` `inline` by `gonidelis` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:937; signals: general review; excerpt: "fried brain commits fried commits" (https://github.com/NVIDIA/cccl/pull/8611#discussion_r3133588183)
- `2026-04-23T22:51:34Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:944; signals: general review; excerpt: "Critical: this removes the old I16 tuning, please leave it in place." (https://github.com/NVIDIA/cccl/pull/8611#discussion_r3134377497)
- `2026-04-23T23:37:12Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_scan.cuh`:953; signals: general review; excerpt: "Please retain:" (https://github.com/NVIDIA/cccl/pull/8611#discussion_r3134564109)
