# PR Discussion Digest

- Source PR: [NVIDIA/cccl#7844](https://github.com/NVIDIA/cccl/pull/7844)
- Source page: `sources/prs/cccl-cub/PR-7844.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-7844`
- Generated at: `2026-05-20T15:20:20.225645+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-02T10:08:39Z`
- Merged: `2026-03-02T17:23:12Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 11
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: bernhardmgruber, davebayer, miscco
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-02T10:51:36Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/7844#pullrequestreview-3875384625)
- `2026-03-02T11:35:07Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7844#pullrequestreview-3875638944)
- `2026-03-02T11:37:35Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7844#pullrequestreview-3875650649)
- `2026-03-02T11:41:09Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7844#pullrequestreview-3875665624)
- `2026-03-02T11:42:10Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7844#pullrequestreview-3875670790)
- `2026-03-02T11:43:33Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7844#pullrequestreview-3875678617)
- `2026-03-02T14:02:49Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7844#pullrequestreview-3876430171)
- `2026-03-02T14:42:39Z` `APPROVED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/7844#pullrequestreview-3876652396)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/kernels/kernel_segmented_radix_sort.cuh`: 5 inline comment(s)
- `cub/benchmarks/bench/segmented_radix_sort/keys.cu`: 2 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_radix_sort.cuh`: 2 inline comment(s)
- `cub/cub/device/dispatch/dispatch_segmented_radix_sort.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-02T10:51:12Z` `inline` by `miscco` `cub/cub/device/dispatch/kernels/kernel_segmented_radix_sort.cuh`:176; signals: kernel, tile; excerpt: "Question: This is the only place we use volatile for temporary storage, is this actually needed?" (https://github.com/NVIDIA/cccl/pull/7844#discussion_r2871749435)
- `2026-03-02T10:46:23Z` `inline` by `miscco` `cub/cub/device/dispatch/kernels/kernel_segmented_radix_sort.cuh`:105; signals: kernel; excerpt: "Nitpick: I believe it would be easier to read / more consistent throughout CUB if we would turn that into a function per algorithm. ..." (https://github.com/NVIDIA/cccl/pull/7844#discussion_r2871728192)
- `2026-03-02T11:43:32Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/segmented_radix_sort/keys.cu`:23; signals: benchmark; excerpt: "But we are no longer using the DispatchSegmentedRadixSort struct, but the new dispatch function. I can create a function pointer here, but then we ..." (https://github.com/NVIDIA/cccl/pull/7844#discussion_r2871978280)
- `2026-03-02T10:43:31Z` `inline` by `miscco` `cub/benchmarks/bench/segmented_radix_sort/keys.cu`:23; signals: benchmark; excerpt: "Nitpick: I would not say that removing the alias is an improvement" (https://github.com/NVIDIA/cccl/pull/7844#discussion_r2871713473)
- `2026-03-02T11:37:35Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_segmented_radix_sort.cuh`:176; signals: kernel; excerpt: "OMG this is definitely a code smell. We should open an issue for that." (https://github.com/NVIDIA/cccl/pull/7844#discussion_r2871954162)
- `2026-03-02T11:41:09Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_segmented_radix_sort.cuh`:176; signals: kernel; excerpt: "7846" (https://github.com/NVIDIA/cccl/pull/7844#discussion_r2871968025)
- `2026-03-02T11:42:10Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_segmented_radix_sort.cuh`:105; signals: kernel; excerpt: "Done." (https://github.com/NVIDIA/cccl/pull/7844#discussion_r2871972356)
- `2026-03-02T10:47:28Z` `inline` by `miscco` `cub/cub/device/dispatch/tuning/tuning_radix_sort.cuh`:933; signals: general review; excerpt: "Question: When do we actually deprecate those? We should set a definite version where we mark those as deprecated so that users have a ..." (https://github.com/NVIDIA/cccl/pull/7844#discussion_r2871732853)
- `2026-03-02T11:35:07Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_radix_sort.cuh`:933; signals: general review; excerpt: "We can deprecate them when 7465 is done, because then users no longer need to rely on passing custom policy hubs to dispatchers. They ..." (https://github.com/NVIDIA/cccl/pull/7844#discussion_r2871943189)
- `2026-03-02T10:48:38Z` `inline` by `miscco` `cub/cub/device/dispatch/dispatch_segmented_radix_sort.cuh`:700; signals: general review; excerpt: "Nitpick: We should just unconditionally set this" (https://github.com/NVIDIA/cccl/pull/7844#discussion_r2871737935)
- `2026-03-02T14:02:49Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/dispatch_segmented_radix_sort.cuh`:700; signals: general review; excerpt: "Turns out this is a bug :) Reverting" (https://github.com/NVIDIA/cccl/pull/7844#discussion_r2872631680)
