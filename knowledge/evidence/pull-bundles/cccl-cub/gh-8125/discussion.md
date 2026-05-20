# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8125](https://github.com/NVIDIA/cccl/pull/8125)
- Source page: `sources/prs/cccl-cub/PR-8125.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8125`
- Generated at: `2026-05-20T15:20:30.180830+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-20T22:17:52Z`
- Merged: `2026-04-24T08:25:02Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 18
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=12, outdated=7
- Human participants with discussion text: Jacobfaib, NaderAlAwar, fbusato, miscco
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-15T15:11:29Z` `COMMENTED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8125#pullrequestreview-4114060383)
- `2026-04-20T23:12:05Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/8125#pullrequestreview-4144054293)
- `2026-04-20T23:23:08Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/8125#pullrequestreview-4144089718)
- `2026-04-20T23:26:27Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/8125#pullrequestreview-4144099102)
- `2026-04-20T23:49:27Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/8125#pullrequestreview-4144171193)
- `2026-04-20T23:56:23Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/8125#pullrequestreview-4144194742)
- `2026-04-21T13:09:40Z` `APPROVED` by `NaderAlAwar` (https://github.com/NVIDIA/cccl/pull/8125#pullrequestreview-4147868048)
- `2026-04-21T16:04:04Z` `COMMENTED` by `Jacobfaib` (https://github.com/NVIDIA/cccl/pull/8125#pullrequestreview-4149079001)
- `2026-04-21T16:06:43Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8125#pullrequestreview-4148233156)
- `2026-04-21T20:02:24Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/8125#pullrequestreview-4150461427)
- `2026-04-24T08:24:59Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8125#pullrequestreview-4169036980)

## Inline Comment Hotspots

- `cudax/include/cuda/experimental/__copy/copy_shared_memory_utils.cuh`: 12 inline comment(s)
- `cudax/include/cuda/experimental/__copy/copy_shared_memory.cuh`: 6 inline comment(s)

## High-Signal Discussion

- `2026-04-15T15:11:26Z` `inline` by `NaderAlAwar` `cudax/include/cuda/experimental/__copy/copy_shared_memory_utils.cuh`:209; signals: block, cuda, kernel, memory, tile, tiling, warp; excerpt: "Question: have you considered rounding this to a multiple of 32? This kernel’s tiling is explicitly warp-oriented ( max tile size == 32), but ..." (https://github.com/NVIDIA/cccl/pull/8125#discussion_r3087481228)
- `2026-04-15T14:26:54Z` `inline` by `NaderAlAwar` `cudax/include/cuda/experimental/__copy/copy_shared_memory_utils.cuh`:132; signals: cuda, kernel, memory, shared memory, tile; excerpt: "Important: this shared-memory sizing seems inconsistent with the kernel’s actual staging type used in shared memory. This check uses sizeof( TpOut) while the kernel ..." (https://github.com/NVIDIA/cccl/pull/8125#discussion_r3087201099)
- `2026-04-15T14:40:04Z` `inline` by `NaderAlAwar` `cudax/include/cuda/experimental/__copy/copy_shared_memory_utils.cuh`:153; signals: cuda, memory, occupancy, tile; excerpt: "Important: this occupancy check seems more conservative than the actual launch. Here num tiles is only multiplied over tile rank, i.e. the tiled prefix, ..." (https://github.com/NVIDIA/cccl/pull/8125#discussion_r3087289119)
- `2026-04-15T14:56:17Z` `inline` by `NaderAlAwar` `cudax/include/cuda/experimental/__copy/copy_shared_memory_utils.cuh`:207; signals: block, cuda, memory, shared memory; excerpt: "Important: this should probably use MaxSharedMemoryPerMultiprocessor to match the behavior described in the docstring. The comment says this is dividing the SM thread budget ..." (https://github.com/NVIDIA/cccl/pull/8125#discussion_r3087390580)
- `2026-04-15T15:00:57Z` `inline` by `NaderAlAwar` `cudax/include/cuda/experimental/__copy/copy_shared_memory_utils.cuh`:210; signals: block, cuda, memory, occupancy; excerpt: "Question: should this just use normal integer division? It feels lik ceil div can overestimate the number of allowed threads per block and lead ..." (https://github.com/NVIDIA/cccl/pull/8125#discussion_r3087419493)
- `2026-04-20T23:23:06Z` `inline` by `fbusato` `cudax/include/cuda/experimental/__copy/copy_shared_memory_utils.cuh`:209; signals: cuda, kernel, memory, warp; excerpt: "technically the kernel can run with any number of threads. The main issue is that partial warps can waste resources, so it makes sense ..." (https://github.com/NVIDIA/cccl/pull/8125#discussion_r3114185337)
- `2026-04-20T23:49:25Z` `inline` by `fbusato` `cudax/include/cuda/experimental/__copy/copy_shared_memory_utils.cuh`:153; signals: block, cuda, memory, tile; excerpt: "right, this check is too conservative. External dimensions, e.g. 4, 128, 128 with 128x128 tile, misses x4 blocks." (https://github.com/NVIDIA/cccl/pull/8125#discussion_r3114258740)
- `2026-04-21T13:08:40Z` `inline` by `NaderAlAwar` `cudax/include/cuda/experimental/__copy/copy_shared_memory_utils.cuh`:209; signals: block, cuda, memory, shared memory; excerpt: "Suggestion: I believe this should also use normal integer division not ceil div if it is supposed to represent resident blocks per SM by ..." (https://github.com/NVIDIA/cccl/pull/8125#discussion_r3117627047)
- `2026-04-21T20:02:24Z` `inline` by `fbusato` `cudax/include/cuda/experimental/__copy/copy_shared_memory.cuh`:215; signals: cuda, memory, tile; excerpt: "unfortunately no, partial tile sizes can be only be compute at runtime because depends on thread indexing" (https://github.com/NVIDIA/cccl/pull/8125#discussion_r3120011636)
- `2026-04-15T13:42:34Z` `inline` by `NaderAlAwar` `cudax/include/cuda/experimental/__copy/copy_shared_memory.cuh`:81; signals: aligned, cuda, memory; excerpt: "Nit: please add one space to all other param descriptions so that they are aligned" (https://github.com/NVIDIA/cccl/pull/8125#discussion_r3086904574)
- `2026-04-20T23:12:03Z` `inline` by `fbusato` `cudax/include/cuda/experimental/__copy/copy_shared_memory_utils.cuh`:132; signals: cuda, memory, shared memory; excerpt: "use sizeof( TpIn) makes totally sense, as shared memory is used only for the input type" (https://github.com/NVIDIA/cccl/pull/8125#discussion_r3114154047)
- `2026-04-21T15:56:59Z` `inline` by `Jacobfaib` `cudax/include/cuda/experimental/__copy/copy_shared_memory.cuh`:215; signals: compile, cuda, memory; excerpt: "Is it possible to use the the fast div mod here? Compilers will probably struggle on this" (https://github.com/NVIDIA/cccl/pull/8125#discussion_r3118741864)
