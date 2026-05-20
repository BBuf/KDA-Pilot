# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8355](https://github.com/NVIDIA/cccl/pull/8355)
- Source page: `sources/prs/cccl-cub/PR-8355.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8355`
- Generated at: `2026-05-20T15:20:41.556958+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-10T08:15:22Z`
- Merged: `2026-04-22T19:13:27Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: bernhardmgruber, davebayer, miscco
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-10T10:57:43Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8355#pullrequestreview-4089117897)
- `2026-04-10T12:18:37Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/8355#pullrequestreview-4089532624)
- `2026-04-13T21:32:14Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8355#pullrequestreview-4102046006)
- `2026-04-14T21:32:13Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8355#pullrequestreview-4109337330)

## Inline Comment Hotspots

- `cub/cub/device/dispatch/kernels/kernel_for_each.cuh`: 3 inline comment(s)
- `cub/cub/util_arch.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-13T21:26:19Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/kernels/kernel_for_each.cuh`:96; signals: cuda, kernel, ptx; excerpt: "I actually like this new approach! It hides the abomination that ::cuda::arch id{CUB PTX ARCH / 10} is. I think it's a bit too ..." (https://github.com/NVIDIA/cccl/pull/8355#discussion_r3075913943)
- `2026-04-22T07:33:42Z` `issue` by `bernhardmgruber`; signals: compile, cuda; excerpt: "CCCL.C seems to fail to build with: The problem is that nvcc 12.9 is used for compilation and SM52 (--generate-code=arch=compute 52,code=[compute 52,sm 52]) is ..." (https://github.com/NVIDIA/cccl/pull/8355#issuecomment-4294392038)
- `2026-04-10T12:18:37Z` `inline` by `davebayer` `cub/cub/device/dispatch/kernels/kernel_for_each.cuh`:96; signals: kernel; excerpt: "As I said in the description, now the policy selector gets info whether the target architecture is a or f, too" (https://github.com/NVIDIA/cccl/pull/8355#discussion_r3064179955)
- `2026-04-10T10:57:43Z` `inline` by `miscco` `cub/cub/device/dispatch/kernels/kernel_for_each.cuh`:96; signals: kernel; excerpt: "This is not really an improvement in my opinion" (https://github.com/NVIDIA/cccl/pull/8355#discussion_r3063783783)
- `2026-04-13T21:27:50Z` `inline` by `bernhardmgruber` `cub/cub/util_arch.cuh`:212; signals: general review; excerpt: "Suggestion: I would love if this function was device-only, since it will give wrong results when called from host code (where the current compilation-pass' ..." (https://github.com/NVIDIA/cccl/pull/8355#discussion_r3075920500)
- `2026-04-13T21:32:02Z` `inline` by `bernhardmgruber` `cub/cub/util_arch.cuh`:211; signals: general review; excerpt: "Suggestion: I would not need this overload, since the policy selector is essentially a callable that turns an arch id into a tuning policy. ..." (https://github.com/NVIDIA/cccl/pull/8355#discussion_r3075940839)
