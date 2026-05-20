# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2360](https://github.com/Dao-AILab/flash-attention/pull/2360)
- Source page: `sources/prs/flash-attention/PR-2360.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2360`
- Generated at: `2026-05-20T15:16:54.120621+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-17T01:45:42Z`
- Merged: `2026-03-18T19:46:03Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 7
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: henrylhtsang, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-03-18T09:16:48Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2360#pullrequestreview-3966241813)
- `2026-03-18T09:19:10Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2360#pullrequestreview-3966260296)
- `2026-03-18T09:20:14Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2360#pullrequestreview-3966269360)
- `2026-03-18T09:21:21Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2360#pullrequestreview-3966279440)
- `2026-03-18T09:22:23Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2360#pullrequestreview-3966288605)
- `2026-03-18T09:26:55Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2360#pullrequestreview-3966326634)
- `2026-03-18T19:06:03Z` `COMMENTED` by `henrylhtsang` (https://github.com/Dao-AILab/flash-attention/pull/2360#pullrequestreview-3970209190)
- `2026-03-18T19:45:15Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2360#pullrequestreview-3970390770)

## Inline Comment Hotspots

- `flash_attn/cute/flash_fwd_sm90.py`: 7 inline comment(s)

## High-Signal Discussion

- `2026-03-18T09:21:20Z` `inline` by `tridao` `flash_attn/cute/flash_fwd_sm90.py`:635; signals: cute, sm90, tma, warp; excerpt: "TMA: only warp 0 loads. cp async: all warps load is load warp = warp idx in wg == 0 or not self.use tma ..." (https://github.com/Dao-AILab/flash-attention/pull/2360#discussion_r2952014348)
- `2026-03-18T09:19:10Z` `inline` by `tridao` `flash_attn/cute/flash_fwd_sm90.py`:476; signals: cute, pipeline, sm90; excerpt: "We should eventually implement a variant of PipelineAsync that does thread gating (i.e. only 1 thread out of 32 will signal). But that's for ..." (https://github.com/Dao-AILab/flash-attention/pull/2360#discussion_r2951999552)
- `2026-03-18T19:06:03Z` `inline` by `henrylhtsang` `flash_attn/cute/flash_fwd_sm90.py`:476; signals: cute, sm90, warp; excerpt: "noob question: how will that work for cp.async? something like a syncwarp then one thread to signal arrival?" (https://github.com/Dao-AILab/flash-attention/pull/2360#discussion_r2955638872)
- `2026-03-18T19:45:15Z` `inline` by `tridao` `flash_attn/cute/flash_fwd_sm90.py`:476; signals: cute, sm90, warp; excerpt: "nvm producer commit would need all threads to commit (not just 1), but consumer release we can do sync warp then elect one thread ..." (https://github.com/Dao-AILab/flash-attention/pull/2360#discussion_r2955823902)
- `2026-03-18T09:16:48Z` `inline` by `tridao` `flash_attn/cute/flash_fwd_sm90.py`:445; signals: cute, sm90, tma; excerpt: "can use 1 if const expr(self.use tma Q) else self.num Q load threads" (https://github.com/Dao-AILab/flash-attention/pull/2360#discussion_r2951984249)
- `2026-03-18T09:20:14Z` `inline` by `tridao` `flash_attn/cute/flash_fwd_sm90.py`:635; signals: cute, sm90, warp; excerpt: "this should be called is load warp then" (https://github.com/Dao-AILab/flash-attention/pull/2360#discussion_r2952006758)
- `2026-03-18T09:22:23Z` `inline` by `tridao` `flash_attn/cute/flash_fwd_sm90.py`:681; signals: cute, sm90; excerpt: "can remove this TODO now" (https://github.com/Dao-AILab/flash-attention/pull/2360#discussion_r2952021846)
- `2026-03-17T17:55:09Z` `issue` by `henrylhtsang`; signals: pipeline; excerpt: "Should we switch so that pipeline k no longer counts transaction for Q? Would that simplify things? yeah that would likely make things more ..." (https://github.com/Dao-AILab/flash-attention/pull/2360#issuecomment-4076888570)
- `2026-03-17T21:34:05Z` `issue` by `henrylhtsang`; signals: perf; excerpt: "Ready for another look. It simplifies the logic quite a bit. I checked perf roughly, separating Q from pipelike k is roughly perf neutral." (https://github.com/Dao-AILab/flash-attention/pull/2360#issuecomment-4078134652)
- `2026-03-17T07:26:47Z` `issue` by `tridao`; signals: pipeline; excerpt: "Should we switch so that pipeline k no longer counts transaction for Q? Would that simplify things?" (https://github.com/Dao-AILab/flash-attention/pull/2360#issuecomment-4072921937)
