# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2218](https://github.com/Dao-AILab/flash-attention/pull/2218)
- Source page: `sources/prs/flash-attention/PR-2218.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2218`
- Generated at: `2026-05-20T15:16:45.604626+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-31T01:30:19Z`
- Merged: `2026-03-28T23:37:45Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 20 (approved=1, commented=19)
- Inline review comments: 19
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=13, outdated=10
- Human participants with discussion text: chatgpt-codex-connector, drisspg, jayhshah, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-05T04:46:07Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. Reviewed commit: 143421ddcb ℹ️ About ... (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3754536629)
- `2026-03-07T02:35:39Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3907069157)
- `2026-03-07T05:42:59Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3907599647)
- `2026-03-07T05:43:41Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3907601604)
- `2026-03-07T05:47:26Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3907612048)
- `2026-03-07T05:47:59Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3907614219)
- `2026-03-07T05:49:33Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3907620368)
- `2026-03-07T05:50:43Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3907624061)
- `2026-03-07T05:51:02Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3907624931)
- `2026-03-10T05:08:10Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3919780925)
- `2026-03-10T05:10:12Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3919789861)
- `2026-03-10T17:06:51Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3924023333)
- `2026-03-18T22:06:20Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3971116906)
- `2026-03-18T22:06:59Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3971119463)
- `2026-03-18T22:09:34Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3971129645)
- `2026-03-18T22:11:04Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3971135580)
- `2026-03-18T22:55:57Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3971340311)
- `2026-03-19T13:13:31Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3975033103)
- `2026-03-19T15:25:43Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3975946061)
- `2026-03-20T12:48:11Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2218#pullrequestreview-3981331288)

## Inline Comment Hotspots

- `flash_attn/cute/flash_fwd_sm100.py`: 15 inline comment(s)
- `flash_attn/cute/interface.py`: 3 inline comment(s)
- `tests/cute/conftest.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-10T01:27:05Z` `issue` by `drisspg`; signals: attention, cute, dtype, flash attention, kernel, perf, race; excerpt: "Okay a few follow ups; one thing I found really helpful is these log messages + script to construct the trace from logs. I ..." (https://github.com/Dao-AILab/flash-attention/pull/2218#issuecomment-4027984776)
- `2026-03-19T15:25:43Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:190; signals: autotune, correctness, cute, perf, performance, sm100; excerpt: "Yup exactly, I feel quite good about the correctness but the performance still has a few weird cliffs, that I want to understand better. ..." (https://github.com/Dao-AILab/flash-attention/pull/2218#discussion_r2960822987)
- `2026-02-05T20:00:09Z` `issue` by `jayhshah`; signals: benchmark, kernel, regression, sm90, tile; excerpt: "I threw up a branch way of doing dynamic persistent scheduler with a semaphore, it should be useful for ablations and eventually the sm90 ..." (https://github.com/Dao-AILab/flash-attention/pull/2218#issuecomment-3855908052)
- `2026-02-05T04:46:07Z` `inline` by `chatgpt-codex-connector` `flash_attn/cute/flash_fwd_sm100.py`:1012; signals: block, compile, cute, sm100; excerpt: ", which will fail to compile. This is triggered by use clc scheduler=True with causal/local or varlen inputs; consider gating this block on the ..." (https://github.com/Dao-AILab/flash-attention/pull/2218#discussion_r2767097575)
- `2026-03-07T05:47:59Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:2844; signals: cute, sm100, warp; excerpt: "e.g. empty warp id num warps" (https://github.com/Dao-AILab/flash-attention/pull/2218#discussion_r2899054615)
- `2026-03-07T05:49:34Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:2849; signals: cute, sm100; excerpt: "So I have found these debug prints really helpful, and think we shud maybe leave them in? but im cool if we dont want ..." (https://github.com/Dao-AILab/flash-attention/pull/2218#discussion_r2899056924)
- `2026-03-18T22:06:59Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:190; signals: cute, sm100; excerpt: "you need to opt in (env var for now since I didnt wire up to interface) just yet but even if you request there ..." (https://github.com/Dao-AILab/flash-attention/pull/2218#discussion_r2956502538)
- `2026-03-18T22:55:57Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:190; signals: cute, sm100; excerpt: "you need to opt in (env var for now since I didnt wire up to interface so we we see if we can and ..." (https://github.com/Dao-AILab/flash-attention/pull/2218#discussion_r2956687368)
- `2026-03-07T02:35:39Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:2844; signals: cute, sm100; excerpt: "make this not magic number" (https://github.com/Dao-AILab/flash-attention/pull/2218#discussion_r2898776947)
- `2026-03-07T05:42:59Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:187; signals: cute, sm100; excerpt: "this is the one to remove since it always prints" (https://github.com/Dao-AILab/flash-attention/pull/2218#discussion_r2899050026)
- `2026-03-07T05:43:41Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:229; signals: cute, sm100; excerpt: "this is a little too belt and suspenders" (https://github.com/Dao-AILab/flash-attention/pull/2218#discussion_r2899050659)
- `2026-03-07T05:47:26Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:1768; signals: cute, sm100; excerpt: "still want to come up with a DRY'r way to do this" (https://github.com/Dao-AILab/flash-attention/pull/2218#discussion_r2899054049)
