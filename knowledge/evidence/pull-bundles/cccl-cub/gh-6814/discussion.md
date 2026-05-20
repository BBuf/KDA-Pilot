# PR Discussion Digest

- Source PR: [NVIDIA/cccl#6814](https://github.com/NVIDIA/cccl/pull/6814)
- Source page: `sources/prs/cccl-cub/PR-6814.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-6814`
- Generated at: `2026-05-20T15:20:04.056897+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-30T09:34:15Z`
- Merged: `2025-12-01T20:09:36Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 10 (approved=1, commented=9)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: bernhardmgruber, fbusato, miscco, oleksandr-pavlyk
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-30T09:54:43Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/6814#pullrequestreview-3521201334)
- `2025-11-30T09:55:40Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/6814#pullrequestreview-3521201632)
- `2025-11-30T21:16:56Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/6814#pullrequestreview-3522384089)
- `2025-12-01T07:29:00Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6814#pullrequestreview-3523533465)
- `2025-12-01T07:31:23Z` `COMMENTED` by `bernhardmgruber` - This LGTM, but we absolutely must have a SASS diff of a fitting test/benchmark before/after SM80 to verify ... (https://github.com/NVIDIA/cccl/pull/6814#pullrequestreview-3523540934)
- `2025-12-01T09:54:08Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/6814#pullrequestreview-3524142948)
- `2025-12-01T17:52:46Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/6814#pullrequestreview-3526307736)
- `2025-12-01T18:20:03Z` `COMMENTED` by `fbusato` - the reduce op sync aggregation has been made in a similar way in I will need to update ... (https://github.com/NVIDIA/cccl/pull/6814#pullrequestreview-3526389443)
- `2025-12-01T18:22:53Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/6814#pullrequestreview-3526413680)
- `2025-12-01T18:22:55Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/6814#pullrequestreview-3526413749)

## Inline Comment Hotspots

- `cub/cub/warp/specializations/warp_reduce_shfl.cuh`: 8 inline comment(s)

## High-Signal Discussion

- `2025-12-01T08:11:14Z` `issue` by `bernhardmgruber`; signals: block, compile, sm90; excerpt: "Unfortunately, this is creating a lot more instructions on SM90 (and 100) for test cub.test.block.reduce.dimx 32.dimyz 1 (compiled for 75,90,100) For example: We previously ..." (https://github.com/NVIDIA/cccl/pull/6814#issuecomment-3595176461)
- `2025-11-30T09:54:44Z` `inline` by `miscco` `cub/cub/warp/specializations/warp_reduce_shfl.cuh`:77; signals: hang, warp; excerpt: "Note to self: I believe we can relax that constrain to is integral && sizeof(T) , int, unsigned ; Then casting back to the ..." (https://github.com/NVIDIA/cccl/pull/6814#discussion_r2573553172)
- `2025-12-01T18:22:55Z` `inline` by `miscco` `cub/cub/warp/specializations/warp_reduce_shfl.cuh`:52; signals: hang, warp; excerpt: "This PR tries hard to not change SASS, because we want it in relatively fast and I leave the optimization that greatly affects SASS ..." (https://github.com/NVIDIA/cccl/pull/6814#discussion_r2578175183)
- `2025-12-01T07:31:23Z` `review` `COMMENTED` by `bernhardmgruber`; signals: benchmark; excerpt: "This LGTM, but we absolutely must have a SASS diff of a fitting test/benchmark before/after SM80 to verify this. I can take that." (https://github.com/NVIDIA/cccl/pull/6814#pullrequestreview-3523540934)
- `2025-12-01T18:20:03Z` `review` `COMMENTED` by `fbusato`; signals: hang; excerpt: "the reduce op sync aggregation has been made in a similar way in I will need to update this PR to align with this ..." (https://github.com/NVIDIA/cccl/pull/6814#pullrequestreview-3526389443)
- `2025-11-30T21:16:52Z` `inline` by `miscco` `cub/cub/warp/specializations/warp_reduce_shfl.cuh`:357; signals: warp; excerpt: "Note to reviewer, I believe we can also considerably clean those up, but that would make the PR quite unwieldly" (https://github.com/NVIDIA/cccl/pull/6814#discussion_r2574874931)
- `2025-12-01T17:52:46Z` `inline` by `miscco` `cub/cub/warp/specializations/warp_reduce_shfl.cuh`:546; signals: warp; excerpt: "Question: Why do we only do the reduce meow sync optimization when having a full lane, it explicitly takes the valid lanes as arguments?" (https://github.com/NVIDIA/cccl/pull/6814#discussion_r2578087801)
- `2025-11-30T09:55:40Z` `inline` by `miscco` `cub/cub/warp/specializations/warp_reduce_shfl.cuh`:466; signals: warp; excerpt: ""Dispatch to specialized implementations"" (https://github.com/NVIDIA/cccl/pull/6814#discussion_r2573553572)
- `2025-12-01T07:28:59Z` `inline` by `bernhardmgruber` `cub/cub/warp/specializations/warp_reduce_shfl.cuh`:466; signals: warp; excerpt: ":rofl:" (https://github.com/NVIDIA/cccl/pull/6814#discussion_r2575929316)
- `2025-12-01T18:15:32Z` `inline` by `fbusato` `cub/cub/warp/specializations/warp_reduce_shfl.cuh`:52; signals: warp; excerpt: "can we also add integer promotion here?" (https://github.com/NVIDIA/cccl/pull/6814#discussion_r2578153383)
- `2025-12-01T18:22:53Z` `inline` by `fbusato` `cub/cub/warp/specializations/warp_reduce_shfl.cuh`:52; signals: warp; excerpt: "already handled in the other PR" (https://github.com/NVIDIA/cccl/pull/6814#discussion_r2578175114)
- `2025-11-30T23:57:06Z` `issue` by `oleksandr-pavlyk`; signals: cuda; excerpt: "Per reduce xor sync is there. That is true, but we do not have a function object that does logical XOR in the library ..." (https://github.com/NVIDIA/cccl/pull/6814#issuecomment-3593923443)
