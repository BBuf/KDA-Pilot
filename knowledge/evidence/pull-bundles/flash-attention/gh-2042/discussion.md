# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2042](https://github.com/Dao-AILab/flash-attention/pull/2042)
- Source page: `sources/prs/flash-attention/PR-2042.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2042`
- Generated at: `2026-05-20T15:16:39.278897+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-03T01:51:14Z`
- Merged: `2025-12-15T23:40:43Z`

## Discussion Counts

- Issue comments: 21
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 10
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=5
- Human participants with discussion text: drisspg, fengxie, jayhshah, ngimel, tqchen, tridao, yjk21
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-03T04:14:36Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2042#pullrequestreview-3533109587)
- `2025-12-03T05:15:03Z` `COMMENTED` by `ngimel` (https://github.com/Dao-AILab/flash-attention/pull/2042#pullrequestreview-3533200866)
- `2025-12-03T12:52:29Z` `COMMENTED` by `tqchen` (https://github.com/Dao-AILab/flash-attention/pull/2042#pullrequestreview-3534900097)
- `2025-12-03T19:14:06Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2042#pullrequestreview-3536547735)
- `2025-12-03T19:18:21Z` `COMMENTED` by `tqchen` (https://github.com/Dao-AILab/flash-attention/pull/2042#pullrequestreview-3536565410)
- `2025-12-03T19:29:11Z` `COMMENTED` by `tqchen` (https://github.com/Dao-AILab/flash-attention/pull/2042#pullrequestreview-3536599970)
- `2025-12-07T21:57:52Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2042#pullrequestreview-3549638338)
- `2025-12-08T23:28:26Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2042#pullrequestreview-3554538114)
- `2025-12-12T20:15:47Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2042#pullrequestreview-3573452402)
- `2025-12-12T20:22:06Z` `COMMENTED` by `tqchen` (https://github.com/Dao-AILab/flash-attention/pull/2042#pullrequestreview-3573470222)
- `2025-12-13T01:10:26Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2042#pullrequestreview-3574030571)

## Inline Comment Hotspots

- `flash_attn/cute/interface.py`: 8 inline comment(s)
- `flash_attn/cute/pyproject.toml`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-12T13:10:11Z` `issue` by `yjk21`; signals: alignment, cache, compile, cute, cutlass; excerpt: "it expects mdK semaphore.strides[2] to be 1 which might provides some evidence Ohh, actually the strides I get when converting the tensor with utils.convert ..." (https://github.com/Dao-AILab/flash-attention/pull/2042#issuecomment-3646420623)
- `2025-12-03T22:09:43Z` `issue` by `tqchen`; signals: compile, cute, kernel, perf; excerpt: "Thanks @drisspg, these comments are very valuable! I want to chime in and provide some updates here. None mixing issue This is indeed a ..." (https://github.com/Dao-AILab/flash-attention/pull/2042#issuecomment-3609051885)
- `2025-12-12T20:22:05Z` `inline` by `tqchen` `flash_attn/cute/pyproject.toml`:30; signals: cute, flashinfer; excerpt: "Flashinfer uses apache-tvm-ffi =0.1.5<0.2, due to considerations in although very unlikely we will break abi" (https://github.com/Dao-AILab/flash-attention/pull/2042#discussion_r2615469711)
- `2025-12-12T12:30:20Z` `issue` by `tqchen`; signals: kernel, tma; excerpt: "E ValueError: Mismatched mdK semaphore.strides[2] on argument 19 when calling: call (mQ: Tensor([n0, n1, n2, n3], bfloat16), mK: Tensor([n4, n5, n6, n7], bfloat16), mV: ..." (https://github.com/Dao-AILab/flash-attention/pull/2042#issuecomment-3646299456)
- `2025-12-12T17:11:55Z` `issue` by `jayhshah`; signals: cute, cutlass; excerpt: "@yjk21 I just tried your short script, also printing the cute tensor c as well, and it prints out for me: so it looks ..." (https://github.com/Dao-AILab/flash-attention/pull/2042#issuecomment-3647420061)
- `2025-12-03T12:51:53Z` `inline` by `tqchen` `flash_attn/cute/interface.py`:1429; signals: cute; excerpt: "None is supported, the main convention as of now is we need to explicitly pass in None as part of positional arguments" (https://github.com/Dao-AILab/flash-attention/pull/2042#discussion_r2584995317)
- `2025-12-03T19:14:06Z` `inline` by `drisspg` `flash_attn/cute/interface.py`:1429; signals: cute; excerpt: "hmm experimentally I am having alot of trouble getting this to work without ICE. It seems like interleaving Optional + non optional is not ..." (https://github.com/Dao-AILab/flash-attention/pull/2042#discussion_r2586314349)
- `2025-12-03T19:29:11Z` `inline` by `tqchen` `flash_attn/cute/interface.py`:1429; signals: cute; excerpt: "Confirmed the issue, is related to arguments have default value None, not None as argument that is interleaved (if all arguments do not have ..." (https://github.com/Dao-AILab/flash-attention/pull/2042#discussion_r2586352448)
- `2025-12-03T04:14:36Z` `inline` by `drisspg` `flash_attn/cute/interface.py`:963; signals: cute; excerpt: "this is annoying" (https://github.com/Dao-AILab/flash-attention/pull/2042#discussion_r2583562065)
- `2025-12-03T05:14:57Z` `inline` by `ngimel` `flash_attn/cute/interface.py`:1029; signals: cute; excerpt: "given the number of times this conversion is called would make sense to factor it out as" (https://github.com/Dao-AILab/flash-attention/pull/2042#discussion_r2583647749)
- `2025-12-03T19:18:21Z` `inline` by `tqchen` `flash_attn/cute/interface.py`:1429; signals: cute; excerpt: "Thanks a lot for the note, let me cross check a bit and get back" (https://github.com/Dao-AILab/flash-attention/pull/2042#discussion_r2586324950)
- `2025-12-07T21:57:52Z` `inline` by `drisspg` `flash_attn/cute/interface.py`:971; signals: cute; excerpt: "hmm" (https://github.com/Dao-AILab/flash-attention/pull/2042#discussion_r2596637011)
