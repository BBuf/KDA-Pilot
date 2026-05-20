# PR Discussion Digest

- Source PR: [NVIDIA/cccl#6077](https://github.com/NVIDIA/cccl/pull/6077)
- Source page: `sources/prs/cccl-cub/PR-6077.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-6077`
- Generated at: `2026-05-20T15:19:53.096950+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-30T14:40:34Z`
- Merged: `2025-11-06T09:19:09Z`

## Discussion Counts

- Issue comments: 25
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: bernhardmgruber, miscco, pauleonix
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-11-03T16:11:23Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6077#pullrequestreview-3411787834)
- `2025-11-03T17:01:22Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6077#pullrequestreview-3412032062)
- `2025-11-03T21:25:04Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6077#pullrequestreview-3412989174)
- `2025-11-06T09:18:43Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6077#pullrequestreview-3427106699)

## Inline Comment Hotspots

- `cub/cub/agent/agent_merge.cuh`: 2 inline comment(s)
- `cub/cub/device/dispatch/tuning/tuning_merge.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-04T10:27:59Z` `issue` by `bernhardmgruber`; signals: benchmark, blackwell, block, hopper; excerpt: "I reran some benchmarks and looked at the results in this PR as well. It looks like we should always use BlockLoadToShared on Blackwell, ..." (https://github.com/NVIDIA/cccl/pull/6077#issuecomment-3485165639)
- `2025-11-05T01:02:36Z` `issue` by `bernhardmgruber`; signals: block, hang, sm90, tma; excerpt: "So, there is a SASS change when UseBlockLoadToShared is false on sm90. This is relevant, because tuning may try to disable BlockLoadToShared even on ..." (https://github.com/NVIDIA/cccl/pull/6077#issuecomment-3488633490)
- `2025-11-03T21:25:04Z` `inline` by `bernhardmgruber` `cub/cub/device/dispatch/tuning/tuning_merge.cuh`:101; signals: benchmark, block, cache; excerpt: "We still need to update the tuning benchmarks. If BlockLoadToShared is always faster (and I am inclined to believe so), then we should not ..." (https://github.com/NVIDIA/cccl/pull/6077#discussion_r2487896024)
- `2025-10-01T02:08:11Z` `issue` by `pauleonix`; signals: b200, h200; excerpt: "cub.bench.merge.keys.base B200 (UBLKCPY) ['/home/pgrossebley/SM 100 merge keys final old.json', '/home/pgrossebley/SM 100 merge keys final newest.json'] base [0] NVIDIA B200 KeyT{ct} OffsetT{ct} Elements{io} Entropy Ref ..." (https://github.com/NVIDIA/cccl/pull/6077#issuecomment-3354426768)
- `2025-10-01T02:10:14Z` `issue` by `pauleonix`; signals: b200, h200; excerpt: "cub.bench.merge.pairs.base B200 (UBLKCPY) ['/home/pgrossebley/SM 100 merge pairs final old.json', '/home/pgrossebley/SM 100 merge pairs final newest.json'] base [0] NVIDIA B200 KeyT{ct} ValueT{ct} OffsetT{ct} Elements{io} Entropy ..." (https://github.com/NVIDIA/cccl/pull/6077#issuecomment-3354432016)
- `2025-10-05T00:46:17Z` `issue` by `pauleonix`; signals: benchmark, kernel; excerpt: "@bernhardmgruber It seems that benchmarking small problem sizes (2^16) is not super reproducible on the RTX 5090. I replaced the old results with a ..." (https://github.com/NVIDIA/cccl/pull/6077#issuecomment-3368639031)
- `2025-11-03T16:11:12Z` `inline` by `bernhardmgruber` `cub/cub/agent/agent_merge.cuh`:295; signals: block; excerpt: "Important: I think this should be items use block load to shared" (https://github.com/NVIDIA/cccl/pull/6077#discussion_r2487048623)
- `2025-10-01T12:04:14Z` `issue` by `bernhardmgruber`; signals: benchmark; excerpt: "The benchmark looks very promising! There are few runs though that regressed a lot, like some 2^16 workloads with more than 20% slowdown. I ..." (https://github.com/NVIDIA/cccl/pull/6077#issuecomment-3356000138)
- `2025-11-03T17:01:22Z` `inline` by `bernhardmgruber` `cub/cub/agent/agent_merge.cuh`:295; signals: general review; excerpt: "Yes, this is exposed by new tests: 6455. But only after some refactoring that I have not yet pushed to this branch." (https://github.com/NVIDIA/cccl/pull/6077#discussion_r2487222609)
- `2025-10-04T21:28:20Z` `issue` by `pauleonix`; signals: general review; excerpt: "cub.bench.merge.pairs.base (cont'd due to character limit for GH comments) A100 (LDGSTS) ['/home/pgrossebley/SM 80 merge pairs final old.json', '/home/pgrossebley/SM 80 merge pairs final newest.json'] base ..." (https://github.com/NVIDIA/cccl/pull/6077#issuecomment-3368550296)
- `2025-11-05T13:58:39Z` `issue` by `bernhardmgruber`; signals: general review; excerpt: "@pauleonix and @elstehle 6460 offers a refactoring and additional tuning policies on top of this PR. We should merge it into this PR and ..." (https://github.com/NVIDIA/cccl/pull/6077#issuecomment-3491367174)
