# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8880](https://github.com/NVIDIA/cccl/pull/8880)
- Source page: `sources/prs/cccl-cub/PR-8880.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8880`
- Generated at: `2026-05-20T15:20:59.695376+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-08T14:55:43Z`
- Merged: `2026-05-18T10:42:02Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 7
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: NaderAlAwar, bernhardmgruber, coderabbitai, davebayer, miscco, oleksandr-pavlyk
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-08T14:56:53Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8880#pullrequestreview-4253146591)
- `2026-05-11T08:36:38Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8880#pullrequestreview-4261908407)
- `2026-05-11T11:04:04Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8880#pullrequestreview-4263038334)
- `2026-05-11T11:04:20Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8880#pullrequestreview-4263040443)
- `2026-05-13T19:09:00Z` `COMMENTED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8880#pullrequestreview-4284620122)
- `2026-05-13T19:36:59Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8880#pullrequestreview-4284784430)
- `2026-05-18T10:21:00Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8880#pullrequestreview-4261404946)
- `2026-05-18T10:26:38Z` `APPROVED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/8880#pullrequestreview-4309314265)

## Inline Comment Hotspots

- `cub/benchmarks/bench/select/flagged.cu`: 3 inline comment(s)
- `cub/benchmarks/bench/select/unique.cu`: 2 inline comment(s)
- `thrust/thrust/system/cuda/detail/unique.h`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-13T15:33:23Z` `issue` by `coderabbitai`; signals: benchmark, block, correctness, cuda, cute, hang, memory, nan; excerpt: "[ cub/benchmarks/bench/select/flagged.cu cub/benchmarks/bench/select/if.cu cub/benchmarks/bench/select/unique.cu cub/cub/device/device select.cuh cub/test/catch2 test device select env.cu thrust/thrust/system/cuda/detail/copy if.h thrust/thrust/system/cuda/detail/remove.h thrust/thrust/system/cuda/detail/unique.h --- 📝 Walkthrough Summary by CodeRabbit Release Notes New ..." (https://github.com/NVIDIA/cccl/pull/8880#issuecomment-4442649568)
- `2026-05-13T19:08:55Z` `inline` by `NaderAlAwar` `cub/benchmarks/bench/select/flagged.cu`:88; signals: benchmark, hang, perf, performance; excerpt: "Critical: for all new in place variant benchmarks, the input values will change between runs. This will affect the performance reported. We should maintain ..." (https://github.com/NVIDIA/cccl/pull/8880#discussion_r3236808984)
- `2026-05-11T08:36:38Z` `inline` by `bernhardmgruber` `thrust/thrust/system/cuda/detail/unique.h`:222; signals: benchmark, cuda; excerpt: "TODO: Thrust needs an in-place unique, for which there is not CUB public API. We should add it and revert the removal of this ..." (https://github.com/NVIDIA/cccl/pull/8880#discussion_r3217399612)
- `2026-05-11T07:40:58Z` `issue` by `bernhardmgruber`; signals: benchmark, hang; excerpt: "There are SASS diffs for cub.bench.select.unique.base on all SM versions They were caused by removing the InPlace benchmarks. I split out the commit dropping ..." (https://github.com/NVIDIA/cccl/pull/8880#issuecomment-4418509960)
- `2026-05-08T14:56:53Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/select/unique.cu`:99; signals: benchmark; excerpt: "I am dropping the InPlace option here, since there is no public API for it and we also have no tunings for it." (https://github.com/NVIDIA/cccl/pull/8880#discussion_r3209488590)
- `2026-05-13T19:36:59Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/select/flagged.cu`:88; signals: benchmark; excerpt: "That's a valid observation! Now I wonder what the original benchmark's use case was? For the in-place versions it measured the in-place implementation but ..." (https://github.com/NVIDIA/cccl/pull/8880#discussion_r3236957376)
- `2026-05-11T07:16:28Z` `inline` by `miscco` `cub/benchmarks/bench/select/flagged.cu`:34; signals: benchmark; excerpt: "I love this" (https://github.com/NVIDIA/cccl/pull/8880#discussion_r3216951004)
- `2026-05-11T11:04:03Z` `inline` by `bernhardmgruber` `cub/benchmarks/bench/select/unique.cu`:99; signals: benchmark; excerpt: "Added back." (https://github.com/NVIDIA/cccl/pull/8880#discussion_r3218355503)
- `2026-05-11T11:04:20Z` `inline` by `bernhardmgruber` `thrust/thrust/system/cuda/detail/unique.h`:222; signals: cuda; excerpt: "Added in 8896" (https://github.com/NVIDIA/cccl/pull/8880#discussion_r3218357001)
- `2026-05-08T17:32:16Z` `issue` by `oleksandr-pavlyk`; signals: compile; excerpt: "Compilation error for some compiler/standard combination:" (https://github.com/NVIDIA/cccl/pull/8880#issuecomment-4408520663)
