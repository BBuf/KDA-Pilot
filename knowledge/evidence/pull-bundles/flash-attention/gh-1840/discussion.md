# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1840](https://github.com/Dao-AILab/flash-attention/pull/1840)
- Source page: `sources/prs/flash-attention/PR-1840.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1840`
- Generated at: `2026-05-20T15:16:34.296649+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-26T17:29:57Z`
- Merged: `2025-10-08T04:01:04Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 31 (approved=2, commented=29)
- Inline review comments: 34
- Review threads observed: 18
- Resolved/outdated thread markers: resolved=16, outdated=12
- Human participants with discussion text: drisspg, tridao, v0i0
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-04T04:55:35Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3183416394)
- `2025-09-15T23:04:51Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226563474)
- `2025-09-15T23:05:29Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226564236)
- `2025-09-15T23:05:55Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226564719)
- `2025-09-15T23:06:16Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226565087)
- `2025-09-15T23:06:35Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226565484)
- `2025-09-15T23:07:15Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226566285)
- `2025-09-15T23:08:00Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226567229)
- `2025-09-15T23:08:11Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226567475)
- `2025-09-15T23:08:22Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226567857)
- `2025-09-15T23:09:03Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226568829)
- `2025-09-15T23:09:35Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226569756)
- `2025-09-16T00:43:16Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226708204)
- `2025-09-16T00:45:05Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3226711631)
- `2025-09-16T14:43:24Z` `APPROVED` by `v0i0` - this is awesome! (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3230311886)
- `2025-09-16T17:08:13Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3230945992)
- `2025-09-16T17:26:41Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3231001312)
- `2025-09-17T19:23:57Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3235930621)
- `2025-09-17T19:47:06Z` `COMMENTED` by `v0i0` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3236032357)
- `2025-09-17T21:51:35Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3236382115)
- `2025-09-17T21:52:24Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3236383415)
- `2025-09-17T23:22:19Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3236542600)
- `2025-09-18T00:24:06Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3236738629)
- `2025-09-18T04:47:35Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/1840#pullrequestreview-3237265888)
- ... 7 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `flash_attn/cute/flash_fwd_sm100.py`: 18 inline comment(s)
- `flash_attn/cute/utils.py`: 9 inline comment(s)
- `flash_attn/cute/flash_fwd.py`: 5 inline comment(s)
- `flash_attn/cute/interface.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-15T23:05:29Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:476; signals: cute, hang, sm100; excerpt: "I think that this is alittle counter intuitive, but was least intrusive in terms of changes, I can refactor if we dont like it" (https://github.com/Dao-AILab/flash-attention/pull/1840#discussion_r2350294792)
- `2025-09-15T23:08:00Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:1975; signals: cute, perf, sm100; excerpt: "VEC SIZE must = 1 for for current global load patterns, at least in inductor). I tried a number of different vec sizes w/ ..." (https://github.com/Dao-AILab/flash-attention/pull/1840#discussion_r2350297070)
- `2025-09-17T19:23:56Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:1975; signals: autotune, cute, sm100; excerpt: "just tested again after upgrading to cutedsl and for simple causal vecsize 2 does have an impact of around 100 tflops but for something ..." (https://github.com/Dao-AILab/flash-attention/pull/1840#discussion_r2356533354)
- `2025-09-17T21:52:23Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:1975; signals: cute, perf, sm100; excerpt: "tried 2, 4, 8, perf caps at 2 for the 5 different examples I looked at. updates so that if we have buffers we ..." (https://github.com/Dao-AILab/flash-attention/pull/1840#discussion_r2356868169)
- `2025-10-02T02:12:06Z` `inline` by `tridao` `flash_attn/cute/flash_fwd_sm100.py`:1272; signals: block, cute, sm100; excerpt: "it should be self.q stage, but so far we've kept that at 2. There are other places where we hardcode m block 2 so ..." (https://github.com/Dao-AILab/flash-attention/pull/1840#discussion_r2396443824)
- `2025-09-16T14:33:20Z` `inline` by `v0i0` `flash_attn/cute/flash_fwd_sm100.py`:1968; signals: cute, sm100, tma; excerpt: "how is this different from the apply score mod in flash fwd.py? maybe move to softmax.py and share?" (https://github.com/Dao-AILab/flash-attention/pull/1840#discussion_r2352723011)
- `2025-09-16T14:34:17Z` `inline` by `v0i0` `flash_attn/cute/flash_fwd_sm100.py`:1975; signals: cute, sm100, vector; excerpt: "huh i would have expected vectorized fp32 sass for vec size == 2, do you happen to have the sass?" (https://github.com/Dao-AILab/flash-attention/pull/1840#discussion_r2352725669)
- `2025-09-15T23:07:15Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:1272; signals: cute, sm100; excerpt: "want to figure out statically if this should always be 2 not sure if its possible to have another work mapping that breaks this" (https://github.com/Dao-AILab/flash-attention/pull/1840#discussion_r2350296339)
- `2025-09-17T23:22:19Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:1968; signals: cute, sm100; excerpt: "So I thought about this and IMO they are just different enough to not warrant being merged I have been playing w different ways ..." (https://github.com/Dao-AILab/flash-attention/pull/1840#discussion_r2356987010)
- `2025-10-02T02:15:40Z` `inline` by `tridao` `flash_attn/cute/flash_fwd.py`:605; signals: cute, kernel; excerpt: "Maybe for the varlen case we set the divmod to be None, and inside the kernel do if const expr. But if we don't ..." (https://github.com/Dao-AILab/flash-attention/pull/1840#discussion_r2396446947)
- `2025-09-04T04:55:35Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:1993; signals: cute, sm100; excerpt: "I need to do modulus wrapping so as to not load from out of bound vals" (https://github.com/Dao-AILab/flash-attention/pull/1840#discussion_r2320826687)
- `2025-09-15T23:04:51Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:23; signals: cute, sm100; excerpt: "editor mistake" (https://github.com/Dao-AILab/flash-attention/pull/1840#discussion_r2350294218)
