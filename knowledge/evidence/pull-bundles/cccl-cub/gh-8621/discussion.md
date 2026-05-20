# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8621](https://github.com/NVIDIA/cccl/pull/8621)
- Source page: `sources/prs/cccl-cub/PR-8621.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8621`
- Generated at: `2026-05-20T15:20:49.012012+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-22T13:46:19Z`
- Merged: `2026-05-12T11:17:58Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 11
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=2
- Human participants with discussion text: bernhardmgruber, miscco
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-24T12:37:25Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8621#pullrequestreview-4170265558)
- `2026-04-24T13:38:52Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8621#pullrequestreview-4170869036)
- `2026-04-24T17:06:05Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8621#pullrequestreview-4172200496)
- `2026-04-29T19:12:49Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8621#pullrequestreview-4199982697)
- `2026-05-11T09:54:30Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8621#pullrequestreview-4262437718)
- `2026-05-12T08:28:59Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8621#pullrequestreview-4270523888)
- `2026-05-12T09:04:29Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8621#pullrequestreview-4270793989)
- `2026-05-12T09:08:46Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8621#pullrequestreview-4270824445)
- `2026-05-12T09:09:06Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8621#pullrequestreview-4270826569)

## Inline Comment Hotspots

- `libcudacxx/include/cuda/std/__memory/pointer_traits.h`: 3 inline comment(s)
- `cub/cub/device/device_radix_sort.cuh`: 3 inline comment(s)
- `thrust/thrust/system/cuda/detail/sort.h`: 2 inline comment(s)
- `thrust/testing/cuda/sort.cu`: 2 inline comment(s)
- `libcudacxx/include/cuda/std/__pstl/cuda/sort.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-24T12:05:28Z` `inline` by `bernhardmgruber` `libcudacxx/include/cuda/std/__memory/pointer_traits.h`:237; signals: cuda, memory; excerpt: "Remark: can to address is not a great name. Can we call this can call to address or can convert to address? Or something ..." (https://github.com/NVIDIA/cccl/pull/8621#discussion_r3137548290)
- `2026-04-29T19:10:59Z` `inline` by `bernhardmgruber` `thrust/thrust/system/cuda/detail/sort.h`:280; signals: cuda, regression; excerpt: "Critical: This is a regression, because Thrust used the radix sort path also for non-contiguous iterators (I am assuming ::cuda::std:: can to address is ..." (https://github.com/NVIDIA/cccl/pull/8621#discussion_r3163536532)
- `2026-04-24T13:38:50Z` `inline` by `miscco` `libcudacxx/include/cuda/std/__memory/pointer_traits.h`:237; signals: cuda, memory; excerpt: "We use that a lot, can meow" (https://github.com/NVIDIA/cccl/pull/8621#discussion_r3138056911)
- `2026-04-24T17:06:05Z` `inline` by `bernhardmgruber` `libcudacxx/include/cuda/std/__memory/pointer_traits.h`:237; signals: cuda, memory; excerpt: "Fine" (https://github.com/NVIDIA/cccl/pull/8621#discussion_r3139219457)
- `2026-04-24T12:32:42Z` `inline` by `bernhardmgruber` `libcudacxx/include/cuda/std/__pstl/cuda/sort.h`:178; signals: cuda; excerpt: "Suggestion: Please factor out this condition into a variable template. Ideally use it in Thrust as well. There we have: with a slightly different ..." (https://github.com/NVIDIA/cccl/pull/8621#discussion_r3137692037)
- `2026-04-29T19:12:40Z` `inline` by `bernhardmgruber` `cub/cub/device/device_radix_sort.cuh`:57; signals: cuda; excerpt: "Suggestion: Drop the check for ::cuda::std:: can to address and add it in PSTL if necessary. We don't need this check for Thrust." (https://github.com/NVIDIA/cccl/pull/8621#discussion_r3163545108)
- `2026-05-11T09:54:29Z` `inline` by `miscco` `thrust/thrust/system/cuda/detail/sort.h`:280; signals: cuda; excerpt: "Yeah you are right, I updated to constraint to only include the type requirements and not the ones for iterators" (https://github.com/NVIDIA/cccl/pull/8621#discussion_r3217867493)
- `2026-05-12T08:27:59Z` `inline` by `bernhardmgruber` `cub/cub/device/device_radix_sort.cuh`:42; signals: hang; excerpt: "Important: Since the choice over radix vs merge sort does not depend on the iterator type, we should change back to the original definition ..." (https://github.com/NVIDIA/cccl/pull/8621#discussion_r3224864460)
- `2026-05-12T08:28:54Z` `inline` by `bernhardmgruber` `thrust/testing/cuda/sort.cu`:142; signals: cuda; excerpt: "Important: These new tests do not cover iterators other than pointers. That would become obsolete if can use radix sort would take the value ..." (https://github.com/NVIDIA/cccl/pull/8621#discussion_r3224869945)
- `2026-05-12T09:09:08Z` `issue` by `bernhardmgruber`; signals: perf, performance; excerpt: "Please create a tracking issue to investigate the small performance difference to Thrust." (https://github.com/NVIDIA/cccl/pull/8621#issuecomment-4428988450)
- `2026-05-12T09:09:06Z` `inline` by `miscco` `thrust/testing/cuda/sort.cu`:142; signals: cuda; excerpt: "Added tests with cuda::std::reverse iterator" (https://github.com/NVIDIA/cccl/pull/8621#discussion_r3225131916)
- `2026-04-24T12:38:41Z` `issue` by `bernhardmgruber`; signals: benchmark; excerpt: "The benchmark looks a bit negative, but the slowdowns are tiny. I am still wondering a bit whether we missed something. Maybe we should ..." (https://github.com/NVIDIA/cccl/pull/8621#issuecomment-4313204317)
