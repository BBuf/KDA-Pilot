# PR Discussion Digest

- Source PR: [pytorch/pytorch#150705](https://github.com/pytorch/pytorch/pull/150705)
- Source page: `sources/prs/pytorch/PR-150705.md`
- Evidence bundle: `evidence/pull-bundles/pytorch/gh-150705`
- Generated at: `2026-05-20T15:26:58.408716+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-04T20:49:11Z`
- Merged: `unknown`

## Discussion Counts

- Issue comments: 16
- Review submissions: 7 (approved=2, commented=4, dismissed=1)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: ZainRizvi, atalman, eqy, malfet, nWEIdia
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-04T21:22:45Z` `COMMENTED` by `eqy` (https://github.com/pytorch/pytorch/pull/150705#pullrequestreview-2744127408)
- `2025-04-04T21:29:49Z` `APPROVED` by `atalman` - lgtm (https://github.com/pytorch/pytorch/pull/150705#pullrequestreview-2744139432)
- `2025-04-04T21:34:33Z` `COMMENTED` by `malfet` (https://github.com/pytorch/pytorch/pull/150705#pullrequestreview-2744146789)
- `2025-04-04T21:45:35Z` `DISMISSED` by `ZainRizvi` (https://github.com/pytorch/pytorch/pull/150705#pullrequestreview-2744159279)
- `2025-04-04T21:49:14Z` `COMMENTED` by `atalman` (https://github.com/pytorch/pytorch/pull/150705#pullrequestreview-2744163758)
- `2025-04-04T21:51:24Z` `COMMENTED` by `atalman` (https://github.com/pytorch/pytorch/pull/150705#pullrequestreview-2744165895)
- `2025-04-23T15:46:50Z` `APPROVED` by `eqy` (https://github.com/pytorch/pytorch/pull/150705#pullrequestreview-2787824952)

## Inline Comment Hotspots

- `aten/src/ATen/native/cuda/MemoryAccess.cuh`: 5 inline comment(s)

## High-Signal Discussion

- `2025-04-04T21:34:33Z` `inline` by `malfet` `aten/src/ATen/native/cuda/MemoryAccess.cuh`:489; signals: alignment, cuda, memory; excerpt: "No, I don't think so. Before vec8 alignment were only available to USE ROCM, after it was enabled unconditionally and I want it to ..." (https://github.com/pytorch/pytorch/pull/150705#discussion_r2029462805)
- `2025-04-04T21:21:23Z` `inline` by `eqy` `aten/src/ATen/native/cuda/MemoryAccess.cuh`:489; signals: cuda, memory; excerpt: "should USE ROCM here also be inverted if the CUDA VERSION condition is = 12080" (https://github.com/pytorch/pytorch/pull/150705#discussion_r2029450813)
- `2025-04-04T21:45:09Z` `inline` by `ZainRizvi` `aten/src/ATen/native/cuda/MemoryAccess.cuh`:500; signals: cuda, memory; excerpt: "Shouldn't there be some logic to handle the case when CUDA VERSION < 12080?" (https://github.com/pytorch/pytorch/pull/150705#discussion_r2029470740)
- `2025-04-04T21:49:14Z` `inline` by `atalman` `aten/src/ATen/native/cuda/MemoryAccess.cuh`:500; signals: cuda, memory; excerpt: "Hi @ZainRizvi this is basically redoing only if CUDA = 12.8" (https://github.com/pytorch/pytorch/pull/150705#discussion_r2029473583)
- `2025-04-04T21:51:24Z` `inline` by `atalman` `aten/src/ATen/native/cuda/MemoryAccess.cuh`:500; signals: cuda, memory; excerpt: "Hence this code should not be applied by default but only for CUDA 12.8+" (https://github.com/pytorch/pytorch/pull/150705#discussion_r2029475015)
- `2025-04-07T19:03:37Z` `issue` by `atalman`; signals: cuda, vector; excerpt: "Hi @malfet looks like we are getting `/var/lib/jenkins/workspace/aten/src/ATen/test/cuda vectorized test.cu:50: Failure`. I think test also need to be updated for this PR." (https://github.com/pytorch/pytorch/pull/150705#issuecomment-2784289772)
- `2025-04-05T00:26:01Z` `issue` by `malfet`; signals: general review; excerpt: "Do we need to tag ciflow binary to check the size reduction? No, not really, one generated in ciflow/trunk should be sufficient. I.e. from ..." (https://github.com/pytorch/pytorch/pull/150705#issuecomment-2779947113)
- `2025-04-05T13:48:48Z` `issue` by `atalman`; signals: general review; excerpt: "attached ciflow/binaries just in case, to validate that binaries are built correctly and we see difference between cu 126 and cu 128" (https://github.com/pytorch/pytorch/pull/150705#issuecomment-2780733006)
