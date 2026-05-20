# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2402](https://github.com/Dao-AILab/flash-attention/pull/2402)
- Source page: `sources/prs/flash-attention/PR-2402.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2402`
- Generated at: `2026-05-20T15:16:57.921820+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-28T02:23:42Z`
- Merged: `2026-04-11T13:14:52Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: CaesarG, drisspg, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-28T21:06:29Z` `APPROVED` by `drisspg` - Yeah this is forsure a bug and the new equation is correct (https://github.com/Dao-AILab/flash-attention/pull/2402#pullrequestreview-4026026091)
- `2026-04-03T16:45:07Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2402#pullrequestreview-4056410829)
- `2026-04-04T03:45:14Z` `COMMENTED` by `CaesarG` (https://github.com/Dao-AILab/flash-attention/pull/2402#pullrequestreview-4058038430)

## Inline Comment Hotspots

- `flash_attn/cute/flash_bwd.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-01T13:12:35Z` `issue` by `CaesarG`; signals: block, cache, compile, cute, hang, kernel, memory, oom; excerpt: "Hi @drisspg, The full CUTE test suitetests/cute/test flash attn.py is now 100% green ! 🟢 Here is a quick summary of the latest fixes ..." (https://github.com/Dao-AILab/flash-attention/pull/2402#issuecomment-4170009448)
- `2026-03-29T12:00:07Z` `issue` by `CaesarG`; signals: block, compile, cute, hang, kernel, sm100, sm90; excerpt: "Hi @drisspg, thanks for pointing that out! I just took a close look at the unit tests and you are absolutely right. Here is ..." (https://github.com/Dao-AILab/flash-attention/pull/2402#issuecomment-4150010690)
- `2026-04-04T03:45:14Z` `inline` by `CaesarG` `flash_attn/cute/flash_bwd.py`:911; signals: cute, kernel, sm90; excerpt: "Thanks for pointing this out! I just pushed a commit that adds an explicit NotImplementedError guard in interface.py to cleanly error out at the ..." (https://github.com/Dao-AILab/flash-attention/pull/2402#discussion_r3035065714)
- `2026-03-29T14:58:42Z` `issue` by `CaesarG`; signals: cache, perf; excerpt: "Hi @drisspg, a quick update on the progress: I've pushed the new commits containing the full backward pass implementation for softcap, the updated test ..." (https://github.com/Dao-AILab/flash-attention/pull/2402#issuecomment-4150323030)
- `2026-04-03T16:45:07Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd.py`:911; signals: cute; excerpt: "Do we properly error for user provided score mod/bwd funcs on sm80's friends ?" (https://github.com/Dao-AILab/flash-attention/pull/2402#discussion_r3033544289)
- `2026-03-28T21:07:01Z` `issue` by `drisspg`; signals: general review; excerpt: "@CaesarG did you look at the unit tests - do we have tests for softcapping and can we fix them if so that they ..." (https://github.com/Dao-AILab/flash-attention/pull/2402#issuecomment-4148814703)
- `2026-04-11T07:06:37Z` `issue` by `CaesarG`; signals: general review; excerpt: "Hi @tridao @drisspg, Great, let's merge when it's ready Yes, it's fully ready to go from my end! Feel free to merge whenever you're ..." (https://github.com/Dao-AILab/flash-attention/pull/2402#issuecomment-4228398410)
