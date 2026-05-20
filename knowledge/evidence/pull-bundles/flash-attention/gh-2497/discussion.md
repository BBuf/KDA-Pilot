# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2497](https://github.com/Dao-AILab/flash-attention/pull/2497)
- Source page: `sources/prs/flash-attention/PR-2497.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2497`
- Generated at: `2026-05-20T15:17:11.153847+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-27T01:36:47Z`
- Merged: `2026-05-01T17:25:40Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 11
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=0
- Human participants with discussion text: Johnsonms, copilot-pull-request-reviewer, tridao, wangsiyu
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-27T06:01:41Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview This PR optimizes the SM100 (Blackwell) dedicated hd=256 FMHA backward kernels by improving global-memory access ... (https://github.com/Dao-AILab/flash-attention/pull/2497#pullrequestreview-4178435454)
- `2026-04-28T01:35:31Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview Copilot reviewed 2 out of 2 changed files in this pull request and generated 4 ... (https://github.com/Dao-AILab/flash-attention/pull/2497#pullrequestreview-4185235086)
- `2026-04-28T03:08:53Z` `COMMENTED` by `Johnsonms` (https://github.com/Dao-AILab/flash-attention/pull/2497#pullrequestreview-4185582822)
- `2026-05-01T16:38:35Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2497#pullrequestreview-4212178507)

## Inline Comment Hotspots

- `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dkdvkernel.py`: 8 inline comment(s)
- `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dqkernel.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-04-27T06:01:41Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: blackwell, coalesc, cute, epilogue, hang, kernel, layout, memory; excerpt: "Pull request overview This PR optimizes the SM100 (Blackwell) dedicated hd=256 FMHA backward kernels by improving global-memory access patterns and replacing scattered epilogue stores ..." (https://github.com/Dao-AILab/flash-attention/pull/2497#pullrequestreview-4178435454)
- `2026-04-27T06:01:40Z` `inline` by `copilot-pull-request-reviewer` `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dqkernel.py`:819; signals: cute, epilogue, kernel, pipeline, race, sm100, tile, tma; excerpt: "s epi dQ is aliased onto sdO, but sdO is also the TMA staging buffer used by the load/mma pipeline. Since the load warp ..." (https://github.com/Dao-AILab/flash-attention/pull/2497#discussion_r3145142691)
- `2026-04-27T06:01:40Z` `inline` by `copilot-pull-request-reviewer` `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dkdvkernel.py`:2881; signals: cute, epilogue, kernel, memory, pipeline, race, sm100, tile; excerpt: "s epi dK is staged by recasting sP memory. sP participates in the compute pipeline (P buffer) and can be reused/overwritten by other warps ..." (https://github.com/Dao-AILab/flash-attention/pull/2497#discussion_r3145142739)
- `2026-04-27T06:01:41Z` `inline` by `copilot-pull-request-reviewer` `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dkdvkernel.py`:2885; signals: cute, epilogue, kernel, pipeline, sm100, tile, tma, warp; excerpt: "s epi dV is aliased onto sdOT, but sdOT is also a TMA staging buffer for dOT loads and can be refilled for the ..." (https://github.com/Dao-AILab/flash-attention/pull/2497#discussion_r3145142755)
- `2026-04-27T06:01:40Z` `inline` by `copilot-pull-request-reviewer` `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dqkernel.py`:2223; signals: block, cute, epilogue, kernel, sm100, tile, tma; excerpt: "The non-varlen TMA epilogue path stores full (epi tile[0], epi cols dQ) boxes via TMA but does not guard against tail tiles where seqlen ..." (https://github.com/Dao-AILab/flash-attention/pull/2497#discussion_r3145142717)
- `2026-04-27T06:01:41Z` `inline` by `copilot-pull-request-reviewer` `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dkdvkernel.py`:3007; signals: block, cute, epilogue, kernel, sm100, tile, tma; excerpt: "The non-varlen TMA epilogue path writes full (tile shape K=64, epi cols dKV) boxes to GMEM, but it’s enabled for any block with blk ..." (https://github.com/Dao-AILab/flash-attention/pull/2497#discussion_r3145142776)
- `2026-04-28T01:35:31Z` `inline` by `copilot-pull-request-reviewer` `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dkdvkernel.py`:555; signals: cute, epilogue, kernel, layout, sm100, tma; excerpt: "This comment says the new dK/dV TMA epilogue atoms/layouts are “threaded through but unused”, but they are now used by epilogue() for the non-varlen ..." (https://github.com/Dao-AILab/flash-attention/pull/2497#discussion_r3151075517)
- `2026-04-28T01:35:31Z` `inline` by `copilot-pull-request-reviewer` `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dqkernel.py`:2235; signals: cute, epilogue, kernel, sm100, tile, tma; excerpt: "The new non-varlen TMA epilogue path stores full fixed-size (M, epi cols dQ) tiles via bulk tensor stores, but it no longer applies the ..." (https://github.com/Dao-AILab/flash-attention/pull/2497#discussion_r3151075530)
- `2026-04-28T01:35:31Z` `inline` by `copilot-pull-request-reviewer` `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dkdvkernel.py`:3008; signals: cute, epilogue, kernel, sm100, tile, tma; excerpt: "The new non-varlen TMA bulk-store epilogue writes a full (tile shape K, hd=256) tile to GMEM without any K-dimension tail predication. Previously self.store(...) guarded ..." (https://github.com/Dao-AILab/flash-attention/pull/2497#discussion_r3151075542)
- `2026-04-27T06:01:39Z` `inline` by `copilot-pull-request-reviewer` `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dkdvkernel.py`:3050; signals: cute, kernel, sm100, tile, tma; excerpt: "Same issue as dV: the non-varlen TMA store for dK does not handle the last partial K tile (when seqlen k cur batch isn’t ..." (https://github.com/Dao-AILab/flash-attention/pull/2497#discussion_r3145142655)
- `2026-04-28T01:35:30Z` `inline` by `copilot-pull-request-reviewer` `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dkdvkernel.py`:3052; signals: cute, kernel, sm100, tile, tma; excerpt: "Same tail issue for the dK TMA store path: the bulk-store writes a full tile without the coordinate bounds checks that self.store(...) previously applied. ..." (https://github.com/Dao-AILab/flash-attention/pull/2497#discussion_r3151075495)
- `2026-04-28T03:08:53Z` `inline` by `Johnsonms` `flash_attn/cute/sm100_hd256_2cta_fmha_backward_dkdvkernel.py`:3052; signals: cute, kernel, sm100, tile, tma; excerpt: "Comments 1, 4, 5 (dKdV TMA writes unpredicated / no K-dim bounds check): TMA bulk tensor stores respect the global dimensions baked into the ..." (https://github.com/Dao-AILab/flash-attention/pull/2497#discussion_r3151330367)
