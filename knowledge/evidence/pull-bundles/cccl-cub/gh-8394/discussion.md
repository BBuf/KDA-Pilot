# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8394](https://github.com/NVIDIA/cccl/pull/8394)
- Source page: `sources/prs/cccl-cub/PR-8394.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8394`
- Generated at: `2026-05-20T15:20:43.532089+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-13T15:59:35Z`
- Merged: `2026-04-14T17:37:41Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 7
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: davebayer, miscco, pciolkosz
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-14T01:55:09Z` `COMMENTED` by `pciolkosz` (https://github.com/NVIDIA/cccl/pull/8394#pullrequestreview-4102691923)
- `2026-04-14T05:59:52Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/8394#pullrequestreview-4103637385)
- `2026-04-14T06:03:42Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/8394#pullrequestreview-4103650481)
- `2026-04-14T06:24:17Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/8394#pullrequestreview-4103725337)
- `2026-04-14T09:36:27Z` `APPROVED` by `miscco` - Looks great from my part (https://github.com/NVIDIA/cccl/pull/8394#pullrequestreview-4104895639)
- `2026-04-14T17:37:06Z` `APPROVED` by `pciolkosz` (https://github.com/NVIDIA/cccl/pull/8394#pullrequestreview-4107973143)

## Inline Comment Hotspots

- `libcudacxx/include/cuda/__hierarchy/queries/extents.h`: 3 inline comment(s)
- `libcudacxx/test/libcudacxx/cuda/hierarchy/cluster_level/hierarchy_query_signatures.compile.pass.cpp`: 2 inline comment(s)
- `libcudacxx/test/libcudacxx/cuda/hierarchy/warp_level/hierarchy_query_signatures.compile.pass.cpp`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-14T06:03:42Z` `inline` by `davebayer` `libcudacxx/test/libcudacxx/cuda/hierarchy/warp_level/hierarchy_query_signatures.compile.pass.cpp`:48; signals: compile, cuda, warp; excerpt: "It's implemented in 3., index and rank queries are not yet supported with warp and cluster is problematic when it's not part of the ..." (https://github.com/NVIDIA/cccl/pull/8394#discussion_r3077414859)
- `2026-04-14T01:23:12Z` `inline` by `pciolkosz` `libcudacxx/test/libcudacxx/cuda/hierarchy/warp_level/hierarchy_query_signatures.compile.pass.cpp`:48; signals: compile, cuda, warp; excerpt: "Should there be extents test here?" (https://github.com/NVIDIA/cccl/pull/8394#discussion_r3076641305)
- `2026-04-14T05:59:52Z` `inline` by `davebayer` `libcudacxx/test/libcudacxx/cuda/hierarchy/cluster_level/hierarchy_query_signatures.compile.pass.cpp`:76; signals: compile, cuda; excerpt: "I extend the support to allow cluster queries even when cluster level is not part of the hierarchy, so this is correct" (https://github.com/NVIDIA/cccl/pull/8394#discussion_r3077401946)
- `2026-04-14T00:36:01Z` `inline` by `pciolkosz` `libcudacxx/test/libcudacxx/cuda/hierarchy/cluster_level/hierarchy_query_signatures.compile.pass.cpp`:76; signals: compile, cuda; excerpt: "Shouldn't this be over cluster queries?" (https://github.com/NVIDIA/cccl/pull/8394#discussion_r3076526082)
- `2026-04-14T01:00:41Z` `inline` by `pciolkosz` `libcudacxx/include/cuda/__hierarchy/queries/extents.h`:274; signals: cuda; excerpt: "I would add a note here that it only works if x dim is larger than 32, maybe even assert?" (https://github.com/NVIDIA/cccl/pull/8394#discussion_r3076585507)
- `2026-04-14T01:02:37Z` `inline` by `pciolkosz` `libcudacxx/include/cuda/__hierarchy/queries/extents.h`:297; signals: cuda; excerpt: "I think we can merge if and else if curr exts come from a lambda or a helper" (https://github.com/NVIDIA/cccl/pull/8394#discussion_r3076589701)
- `2026-04-14T06:24:17Z` `inline` by `davebayer` `libcudacxx/include/cuda/__hierarchy/queries/extents.h`:297; signals: cuda; excerpt: "It's not that simple, I'd rather keep it as is if you don't mind" (https://github.com/NVIDIA/cccl/pull/8394#discussion_r3077487701)
