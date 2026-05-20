# PR Discussion Digest

- Source PR: [NVIDIA/cccl#5822](https://github.com/NVIDIA/cccl/pull/5822)
- Source page: `sources/prs/cccl-cub/PR-5822.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-5822`
- Generated at: `2026-05-20T15:19:53.084773+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-09T14:34:40Z`
- Merged: `2025-09-29T12:21:48Z`

## Discussion Counts

- Issue comments: 22
- Review submissions: 8 (approved=2, changes_requested=1, commented=5)
- Inline review comments: 6
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: bernhardmgruber, davebayer, miscco
- Automation comments/reviews omitted from high-signal summary: 17
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-09-09T16:03:54Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/5822#pullrequestreview-3202310956)
- `2025-09-09T16:19:23Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/5822#pullrequestreview-3202366101)
- `2025-09-10T06:41:37Z` `CHANGES_REQUESTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/5822#pullrequestreview-3204634116)
- `2025-09-10T06:48:18Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/5822#pullrequestreview-3204652150)
- `2025-09-10T06:51:48Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/5822#pullrequestreview-3204663608)
- `2025-09-10T08:35:55Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/5822#pullrequestreview-3205080134)
- `2025-09-29T06:28:47Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/5822#pullrequestreview-3278102025)
- `2025-09-29T12:21:17Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/5822#pullrequestreview-3279484792)

## Inline Comment Hotspots

- `libcudacxx/include/cuda/__functional/for_each_canceled.h`: 6 inline comment(s)

## High-Signal Discussion

- `2025-09-10T06:48:18Z` `inline` by `davebayer` `libcudacxx/include/cuda/__functional/for_each_canceled.h`:59; signals: compile, cuda, ptx; excerpt: "msvc doesn't support int128 and it is the only supported compiler on Windows. So, currently it's not supported on windows at all. I agree ..." (https://github.com/NVIDIA/cccl/pull/5822#discussion_r2335728175)
- `2025-09-10T06:51:48Z` `inline` by `miscco` `libcudacxx/include/cuda/__functional/for_each_canceled.h`:59; signals: cuda, perf, performance; excerpt: "I would then then suggest to split the functionality into two I really do not want to take a potential performance hit on linux ..." (https://github.com/NVIDIA/cccl/pull/5822#discussion_r2335736494)
- `2025-09-09T16:19:23Z` `inline` by `davebayer` `libcudacxx/include/cuda/__functional/for_each_canceled.h`:46; signals: cuda, register; excerpt: "Oh, it will be a bit more complicated now, because I had to use register concatenation to make it work" (https://github.com/NVIDIA/cccl/pull/5822#discussion_r2334153541)
- `2025-09-10T08:35:55Z` `inline` by `davebayer` `libcudacxx/include/cuda/__functional/for_each_canceled.h`:59; signals: cuda, ptx; excerpt: "It produces the exact same PTX, see" (https://github.com/NVIDIA/cccl/pull/5822#discussion_r2336004538)
- `2025-09-10T06:41:32Z` `inline` by `miscco` `libcudacxx/include/cuda/__functional/for_each_canceled.h`:59; signals: cuda; excerpt: "I am really not sure whether this is any improvement at all. The list of supported systems without int128 is rather short" (https://github.com/NVIDIA/cccl/pull/5822#discussion_r2335714665)
- `2025-09-09T16:03:53Z` `inline` by `miscco` `libcudacxx/include/cuda/__functional/for_each_canceled.h`:46; signals: cuda; excerpt: "I would like to turn this into int128 when available" (https://github.com/NVIDIA/cccl/pull/5822#discussion_r2334117003)
- `2025-09-09T21:05:13Z` `issue` by `davebayer`; signals: sm100; excerpt: "Can someone actually test if it works on an SM100+ machine?" (https://github.com/NVIDIA/cccl/pull/5822#issuecomment-3272263861)
