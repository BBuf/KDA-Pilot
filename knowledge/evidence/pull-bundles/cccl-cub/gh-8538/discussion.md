# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8538](https://github.com/NVIDIA/cccl/pull/8538)
- Source page: `sources/prs/cccl-cub/PR-8538.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8538`
- Generated at: `2026-05-20T15:20:49.001581+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-20T22:44:09Z`
- Merged: `2026-04-22T09:58:40Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 10
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: bernhardmgruber, elstehle
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-21T07:29:35Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8538#pullrequestreview-4145872735)
- `2026-04-21T09:21:46Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8538#pullrequestreview-4146539933)
- `2026-04-21T20:34:11Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8538#pullrequestreview-4150619937)
- `2026-04-21T20:38:31Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8538#pullrequestreview-4150640068)
- `2026-04-21T20:41:23Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8538#pullrequestreview-4150655024)
- `2026-04-22T06:42:07Z` `COMMENTED` by `elstehle` (https://github.com/NVIDIA/cccl/pull/8538#pullrequestreview-4152555277)
- `2026-04-22T08:10:11Z` `APPROVED` by `elstehle` - Thanks a lot for taking this on! Changes look good to me. (https://github.com/NVIDIA/cccl/pull/8538#pullrequestreview-4152904360)
- `2026-04-22T08:17:39Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8538#pullrequestreview-4153064279)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/kernels/kernel_batched_topk.cuh`: 4 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_batched_topk.cuh`: 3 inline comment(s)
- `cub/benchmarks/bench/segmented_topk/keys.cu`: 2 inline comment(s)
- `cub/cub/device/dispatch/dispatch_batched_topk.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-22T08:05:15Z` `inline` by `elstehle` `cub/cub/device/dispatch/kernels/kernel_batched_topk.cuh`:65; signals: kernel, memory, shared memory, tile; excerpt: "Thanks for pointing this out. In my mind, I assumed that as tile sizes are decreasing, I assumed strictly non-increasing shared memory requirements. That ..." (https://github.com/NVIDIA/cccl/pull/8538#discussion_r3122436979)
- `2026-04-22T08:17:38Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_batched_topk.cuh`:58; signals: cuda, vector; excerpt: "We can't in the current design. We would need a container of dynamic size that works in constexpr land. If you can give me ..." (https://github.com/NVIDIA/cccl/pull/8538#discussion_r3122501528)
- `2026-04-21T20:38:31Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_batched_topk.cuh`:65; signals: kernel; excerpt: "Important remark: I reviewed the initial implementation claude generated and noticed it did not include the SMEM check (fits smem), so I instructed it ..." (https://github.com/NVIDIA/cccl/pull/8538#discussion_r3120179152)
- `2026-04-22T06:42:07Z` `inline` by `elstehle` `cub/benchmarks/bench/segmented_topk/keys.cu`:39; signals: benchmark; excerpt: "Yeah, I think so. I think before we tune, we want to make sure to make bits per pass a tuning parameter, but that's ..." (https://github.com/NVIDIA/cccl/pull/8538#discussion_r3122030572)
- `2026-04-22T08:09:17Z` `inline` by `elstehle` `cub/cub/device/dispatch/kernels/kernel_batched_topk.cuh`:83; signals: kernel; excerpt: "Yeah, the motivation for find first smem fitting policy is that it will be needed once we support larger-than-what-fits-into-one-worker-per-segment segments, as we want to ..." (https://github.com/NVIDIA/cccl/pull/8538#discussion_r3122456965)
- `2026-04-21T07:29:31Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/segmented_topk/keys.cu`:39; signals: benchmark; excerpt: "Remark: I think this was just wrong before?" (https://github.com/NVIDIA/cccl/pull/8538#discussion_r3115759985)
- `2026-04-21T20:34:11Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_batched_topk.cuh`:83; signals: kernel; excerpt: "Remark: This code was entirely unused." (https://github.com/NVIDIA/cccl/pull/8538#discussion_r3120159385)
- `2026-04-22T07:49:26Z` `inline` by `elstehle` `cub/cub/device/dispatch/tuning/tuning_batched_topk.cuh`:58; signals: general review; excerpt: "question: How would we envision this to work with varying number of worker per segment policies. E.g., if sm 120 had 6, but sm ..." (https://github.com/NVIDIA/cccl/pull/8538#discussion_r3122357636)
- `2026-04-22T08:10:11Z` `review` `APPROVED` by `elstehle`; signals: hang; excerpt: "Thanks a lot for taking this on! Changes look good to me." (https://github.com/NVIDIA/cccl/pull/8538#pullrequestreview-4152904360)
- `2026-04-21T09:21:46Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_batched_topk.cuh`:26; signals: general review; excerpt: "TODO: rename" (https://github.com/NVIDIA/cccl/pull/8538#discussion_r3116379238)
- `2026-04-21T20:41:23Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_batched_topk.cuh`:154; signals: general review; excerpt: "Remark: this was also unused" (https://github.com/NVIDIA/cccl/pull/8538#discussion_r3120192581)
