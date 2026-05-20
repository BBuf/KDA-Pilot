# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8107](https://github.com/NVIDIA/cccl/pull/8107)
- Source page: `sources/prs/cccl-cub/PR-8107.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8107`
- Generated at: `2026-05-20T15:20:28.019934+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-19T09:49:11Z`
- Merged: `2026-04-20T13:31:44Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 11
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=6, outdated=4
- Human participants with discussion text: Jacobfaib, bernhardmgruber, miscco
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2026-03-19T13:40:43Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8107#pullrequestreview-3974446480)
- `2026-04-20T11:31:53Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8107#pullrequestreview-4139476757)
- `2026-04-20T13:21:00Z` `COMMENTED` by `Jacobfaib` (https://github.com/NVIDIA/cccl/pull/8107#pullrequestreview-4140255146)
- `2026-04-20T13:28:44Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8107#pullrequestreview-4140396260)

## Inline Comment Hotspots

- `libcudacxx/benchmarks/bench/shift_left/basic.cu`: 3 inline comment(s)
- `libcudacxx/benchmarks/bench/shift_right/basic.cu`: 3 inline comment(s)
- `libcudacxx/include/cuda/std/__pstl/cuda/shift_left.h`: 2 inline comment(s)
- `libcudacxx/include/cuda/std/__pstl/cuda/shift_right.h`: 1 inline comment(s)
- `libcudacxx/include/cuda/std/__pstl/shift_right.h`: 1 inline comment(s)
- `libcudacxx/test/libcudacxx/std/algorithms/alg.modifying/alg.shift/pstl_shift_left.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-20T11:21:34Z` `inline` by `bernhardmgruber` `libcudacxx/benchmarks/bench/shift_left/basic.cu`:26; signals: benchmark, cuda; excerpt: "Suggestion: Since we don't care about the shifted values, why do we need to bound the random numbers? I think we should just: to ..." (https://github.com/NVIDIA/cccl/pull/8107#discussion_r3110238442)
- `2026-04-20T11:27:40Z` `inline` by `bernhardmgruber` `libcudacxx/benchmarks/bench/shift_right/basic.cu`:38; signals: benchmark, cuda; excerpt: "For the bandwidth metrics we always specify the minimum amount of reads and writes for a hypothetical ideal processor, independent of the actual implementation ..." (https://github.com/NVIDIA/cccl/pull/8107#discussion_r3110269125)
- `2026-04-20T13:19:38Z` `inline` by `Jacobfaib` `libcudacxx/test/libcudacxx/std/algorithms/alg.modifying/alg.shift/pstl_shift_left.cu`:35; signals: compile, cuda; excerpt: "We compare with nullptr below but we should also ensure the return is some kind of pointer, auto will make the compiler do that." (https://github.com/NVIDIA/cccl/pull/8107#discussion_r3110920463)
- `2026-04-20T13:17:13Z` `inline` by `Jacobfaib` `libcudacxx/benchmarks/bench/shift_left/basic.cu`:3; signals: benchmark, cuda; excerpt: "Wrong license header?" (https://github.com/NVIDIA/cccl/pull/8107#discussion_r3110903242)
- `2026-04-20T13:17:42Z` `inline` by `Jacobfaib` `libcudacxx/benchmarks/bench/shift_right/basic.cu`:3; signals: benchmark, cuda; excerpt: "Wrong license header?" (https://github.com/NVIDIA/cccl/pull/8107#discussion_r3110906851)
- `2026-03-19T09:53:04Z` `issue` by `miscco`; signals: perf, performance; excerpt: "Performance is as expected, we might want to consider providing a switch to device select to compact to the right, but that would be ..." (https://github.com/NVIDIA/cccl/pull/8107#issuecomment-4088983081)
- `2026-04-20T13:16:38Z` `inline` by `Jacobfaib` `libcudacxx/include/cuda/std/__pstl/shift_right.h`; signals: cuda; excerpt: "Could you add tests that exercise the various static assert()s? I.e. a selected backend and non random-access iterators?" (https://github.com/NVIDIA/cccl/pull/8107#discussion_r3110899227)
- `2026-03-19T11:23:50Z` `inline` by `miscco` `libcudacxx/include/cuda/std/__pstl/cuda/shift_right.h`:93; signals: cuda; excerpt: "This one might be micro optimization" (https://github.com/NVIDIA/cccl/pull/8107#discussion_r2959413458)
- `2026-04-20T13:12:08Z` `inline` by `Jacobfaib` `libcudacxx/include/cuda/std/__pstl/cuda/shift_left.h`:29; signals: cuda; excerpt: "Where are these warnings being emitted? We should do a follow-up to fix them" (https://github.com/NVIDIA/cccl/pull/8107#discussion_r3110869452)
