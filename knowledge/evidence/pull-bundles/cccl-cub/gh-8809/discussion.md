# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8809](https://github.com/NVIDIA/cccl/pull/8809)
- Source page: `sources/prs/cccl-cub/PR-8809.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8809`
- Generated at: `2026-05-20T15:20:57.331274+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-05T13:09:17Z`
- Merged: `2026-05-07T12:18:59Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: NaderAlAwar, bernhardmgruber, miscco
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-06T18:22:29Z` `COMMENTED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8809#pullrequestreview-4237791471)
- `2026-05-07T07:05:49Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8809#pullrequestreview-4241812911)
- `2026-05-07T12:18:48Z` `APPROVED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8809#pullrequestreview-4243898615)

## Inline Comment Hotspots

- `cub/test/catch2_test_device_reduce_env.cu`: 2 inline comment(s)
- `cub/cub/device/device_reduce.cuh`: 1 inline comment(s)
- `c/parallel/src/reduce.cu`: 1 inline comment(s)
- `cub/benchmarks/bench/reduce/nondeterministic.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-06T18:22:12Z` `inline` by `NaderAlAwar` `cub/benchmarks/bench/reduce/nondeterministic.cu`:30; signals: benchmark; excerpt: "Important: we should only be returning the nondeterministic policy now" (https://github.com/NVIDIA/cccl/pull/8809#discussion_r3196614527)
- `2026-05-06T18:19:55Z` `inline` by `NaderAlAwar` `c/parallel/src/reduce.cu`:376; signals: general review; excerpt: "Critical: the if and else bodies need to be swapped. The if branch should use reduce nondeterministic" (https://github.com/NVIDIA/cccl/pull/8809#discussion_r3196608462)
- `2026-05-06T18:18:21Z` `inline` by `NaderAlAwar` `cub/cub/device/device_reduce.cuh`:194; signals: general review; excerpt: "Important: this should use reduce nondeterministic not reduce" (https://github.com/NVIDIA/cccl/pull/8809#discussion_r3196604528)
- `2026-05-06T18:20:49Z` `inline` by `NaderAlAwar` `cub/test/catch2_test_device_reduce_env.cu`:210; signals: general review; excerpt: "Important: should use reduce nondeterministic instead of reduce" (https://github.com/NVIDIA/cccl/pull/8809#discussion_r3196610720)
- `2026-05-06T18:21:15Z` `inline` by `NaderAlAwar` `cub/test/catch2_test_device_reduce_env.cu`:336; signals: general review; excerpt: "Important: same as above, should use nondeterministic" (https://github.com/NVIDIA/cccl/pull/8809#discussion_r3196611795)
- `2026-05-07T05:59:26Z` `issue` by `miscco`; signals: general review; excerpt: "haven't seen this one in a while @Jacobfaib that is why I am really worries about using [[no unique address]]" (https://github.com/NVIDIA/cccl/pull/8809#issuecomment-4394466968)
