# PR Discussion Digest

- Source PR: [NVIDIA/cccl#7924](https://github.com/NVIDIA/cccl/pull/7924)
- Source page: `sources/prs/cccl-cub/PR-7924.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-7924`
- Generated at: `2026-05-20T15:20:21.973586+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-07T15:46:06Z`
- Merged: `2026-03-10T09:47:51Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 7 (approved=2, changes_requested=1, commented=4)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=2
- Human participants with discussion text: bernhardmgruber, miscco, oleksandr-pavlyk
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-07T16:04:18Z` `APPROVED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/7924#pullrequestreview-3909000504)
- `2026-03-09T09:31:17Z` `CHANGES_REQUESTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7924#pullrequestreview-3914039016)
- `2026-03-09T09:35:53Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/7924#pullrequestreview-3914108853)
- `2026-03-09T10:22:34Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/7924#pullrequestreview-3914381887)
- `2026-03-09T16:56:30Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7924#pullrequestreview-3916843146)
- `2026-03-10T09:43:21Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/7924#pullrequestreview-3921078851)
- `2026-03-10T09:45:42Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/7924#pullrequestreview-3921092477)

## Inline Comment Hotspots

- `libcudacxx/include/cuda/std/__pstl/reverse.h`: 7 inline comment(s)
- `libcudacxx/include/cuda/std/__pstl/reverse_copy.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-09T09:28:13Z` `inline` by `bernhardmgruber` `libcudacxx/include/cuda/std/__pstl/reverse.h`:78; signals: benchmark, blackwell, cuda, tma; excerpt: "Important: Please benchmark this algorithm on a Blackwell GPU. IIRC, Thrust dispatches to transform, so the implementation will use TMA to load the data ..." (https://github.com/NVIDIA/cccl/pull/7924#discussion_r2904232642)
- `2026-03-09T09:31:13Z` `inline` by `bernhardmgruber` `libcudacxx/include/cuda/std/__pstl/reverse_copy.h`:67; signals: cuda, tma; excerpt: "Important: Please use the reverse iterator for the result, because then the iterator for reading can remain contiguous and we can use TMA in ..." (https://github.com/NVIDIA/cccl/pull/7924#discussion_r2904247776)
- `2026-03-09T10:22:33Z` `inline` by `miscco` `libcudacxx/include/cuda/std/__pstl/reverse.h`:63; signals: compile, cuda; excerpt: "I am torn here, because we often have issues with older compilers giving warnings" (https://github.com/NVIDIA/cccl/pull/7924#discussion_r2904515624)
- `2026-03-09T16:56:30Z` `inline` by `bernhardmgruber` `libcudacxx/include/cuda/std/__pstl/reverse.h`:67; signals: cuda, hang; excerpt: "Alright. No change needed." (https://github.com/NVIDIA/cccl/pull/7924#discussion_r2906712112)
- `2026-03-10T09:43:21Z` `inline` by `miscco` `libcudacxx/include/cuda/std/__pstl/reverse.h`:63; signals: compile, cuda; excerpt: "Yeah I tested it and got a ton of compile issues" (https://github.com/NVIDIA/cccl/pull/7924#discussion_r2910530584)
- `2026-03-09T09:25:56Z` `inline` by `bernhardmgruber` `libcudacxx/include/cuda/std/__pstl/reverse.h`:63; signals: cuda; excerpt: "Suggestion: could drop ctor and use aggregate init." (https://github.com/NVIDIA/cccl/pull/7924#discussion_r2904221479)
- `2026-03-09T09:29:45Z` `inline` by `bernhardmgruber` `libcudacxx/include/cuda/std/__pstl/reverse.h`:67; signals: cuda; excerpt: "Question: Wouldn't it be simpler if we just did: and not use a reverse iterator?" (https://github.com/NVIDIA/cccl/pull/7924#discussion_r2904240295)
- `2026-03-09T09:35:53Z` `inline` by `miscco` `libcudacxx/include/cuda/std/__pstl/reverse.h`:67; signals: cuda; excerpt: "kind of the same, but then you have to account for -1 all the time" (https://github.com/NVIDIA/cccl/pull/7924#discussion_r2904271718)
- `2026-03-09T16:56:11Z` `issue` by `bernhardmgruber`; signals: benchmark; excerpt: "Note for the future: I64 2^24 51.813 us 1.22% 55.419 us 151.49% 3.606 us 6.96% SLOW If you get a benchmark result that has ..." (https://github.com/NVIDIA/cccl/pull/7924#issuecomment-4025251444)
- `2026-03-09T14:28:14Z` `issue` by `miscco`; signals: blackwell; excerpt: "On blackwell i now get:" (https://github.com/NVIDIA/cccl/pull/7924#issuecomment-4024188381)
