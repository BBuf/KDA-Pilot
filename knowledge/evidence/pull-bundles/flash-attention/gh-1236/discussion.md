# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1236](https://github.com/Dao-AILab/flash-attention/pull/1236)
- Source page: `sources/prs/flash-attention/PR-1236.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1236`
- Generated at: `2026-05-20T15:16:29.273089+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-09-18T02:48:11Z`
- Merged: `2024-10-15T07:21:22Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 19 (commented=19)
- Inline review comments: 27
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=0, outdated=8
- Human participants with discussion text: ipiszy, jayhshah, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2024-09-19T07:22:51Z` `COMMENTED` by `ipiszy` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2314629670)
- `2024-09-19T07:24:18Z` `COMMENTED` by `ipiszy` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2314633238)
- `2024-09-19T07:46:51Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2314689869)
- `2024-09-30T07:18:19Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2336590340)
- `2024-09-30T07:29:35Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2336619772)
- `2024-09-30T15:10:00Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2337868785)
- `2024-10-01T01:17:29Z` `COMMENTED` by `ipiszy` - Thanks @jayhshah @ganeshcolfax . It seems that gqa can be used without split-k, is it correct? I wonder ... (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2338904599)
- `2024-10-01T15:19:02Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2340693617)
- `2024-10-01T15:23:39Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2340712033)
- `2024-10-01T15:30:35Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2340736596)
- `2024-10-01T15:32:35Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2340741472)
- `2024-10-01T15:33:12Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2340743008)
- `2024-10-01T16:14:26Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2340843897)
- `2024-10-01T17:03:15Z` `COMMENTED` by `ipiszy` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2340938279)
- `2024-10-01T18:13:39Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2341083040)
- `2024-10-01T18:29:44Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2341111437)
- `2024-10-01T20:02:31Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2341334231)
- `2024-10-02T17:55:35Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2343674046)
- `2024-10-15T00:48:47Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2367899921)

## Inline Comment Hotspots

- `hopper/seq_len.h`: 8 inline comment(s)
- `hopper/flash_api.cpp`: 6 inline comment(s)
- `hopper/flash_attn_interface.py`: 3 inline comment(s)
- `csrc/composable_kernel`: 3 inline comment(s)
- `hopper/flash_fwd_launch_template.h`: 3 inline comment(s)
- `hopper/test_flash_attn.py`: 2 inline comment(s)
- `hopper/mainloop_fwd_sm90_tma_gmma_ws.hpp`: 2 inline comment(s)

## High-Signal Discussion

- `2024-10-01T15:19:02Z` `inline` by `jayhshah` `hopper/mainloop_fwd_sm90_tma_gmma_ws.hpp`:569; signals: fp8, hopper, kernel, perf, sm90, tma; excerpt: "Removed it -- I thought it was convenient to leave in when testing fp8 kernel perf, but it does clutter the code more." (https://github.com/Dao-AILab/flash-attention/pull/1236#discussion_r1783056542)
- `2024-10-01T18:13:39Z` `inline` by `jayhshah` `hopper/seq_len.h`:21; signals: cache, hang, hopper, kv cache, layout; excerpt: "I'm using FixedSeqLenTraitsDynamic in the kv cache setup where actual seqlen is <= cache seqlen. I only need actual seqlen to be updated every ..." (https://github.com/Dao-AILab/flash-attention/pull/1236#discussion_r1783300591)
- `2024-10-15T00:48:47Z` `inline` by `jayhshah` `hopper/seq_len.h`:21; signals: fp8, hopper, kernel, perf, regression; excerpt: "In the latest update I removed Is dynamic entirely. I found another way to handle perf regression with the fp8 kernel, through introducing another ..." (https://github.com/Dao-AILab/flash-attention/pull/1236#discussion_r1800275662)
- `2024-10-01T15:23:39Z` `inline` by `jayhshah` `hopper/seq_len.h`:21; signals: fp8, hopper, kernel, perf; excerpt: "I meant to include a template parameter to guard against reading actual seq len when not needed as that degrades fp8 kernel perf. Actual ..." (https://github.com/Dao-AILab/flash-attention/pull/1236#discussion_r1783069269)
- `2024-10-01T18:29:44Z` `inline` by `jayhshah` `hopper/seq_len.h`:21; signals: cache, hopper, kv cache, layout; excerpt: "In the kv cache setup I don't have access to total k, so won't be able to use VarSeqLenTraits layouts." (https://github.com/Dao-AILab/flash-attention/pull/1236#discussion_r1783318266)
- `2024-09-19T07:24:18Z` `inline` by `ipiszy` `hopper/flash_attn_interface.py`:179; signals: hopper, perf, regression; excerpt: "Furthermore, does it make sense to just enable GQA optimization by default when input is GQA? I feel it won't cause perf regressions even ..." (https://github.com/Dao-AILab/flash-attention/pull/1236#discussion_r1766301046)
- `2024-10-01T01:11:21Z` `inline` by `ipiszy` `hopper/mainloop_fwd_sm90_tma_gmma_ws.hpp`:569; signals: hopper, sm90, tma; excerpt: "Why not just removing deprecated code?" (https://github.com/Dao-AILab/flash-attention/pull/1236#discussion_r1781998237)
- `2024-10-01T01:17:29Z` `review` `COMMENTED` by `ipiszy`; signals: benchmark, perf; excerpt: "Thanks @jayhshah @ganeshcolfax . It seems that gqa can be used without split-k, is it correct? I wonder what's the perf if it's just ..." (https://github.com/Dao-AILab/flash-attention/pull/1236#pullrequestreview-2338904599)
- `2024-09-19T07:22:51Z` `inline` by `ipiszy` `hopper/flash_attn_interface.py`:179; signals: block, hopper; excerpt: "I wonder does it make sense to give user an option to enable GQA optimization for general use cases outside of decoding? e.g. It's ..." (https://github.com/Dao-AILab/flash-attention/pull/1236#discussion_r1766298928)
- `2024-10-01T01:00:47Z` `inline` by `ipiszy` `hopper/flash_fwd_launch_template.h`:204; signals: hopper, tile; excerpt: "Adjusting Q tile size would make it more efficient for small seq len, thanks for the fix" (https://github.com/Dao-AILab/flash-attention/pull/1236#discussion_r1781993264)
- `2024-10-01T15:30:34Z` `inline` by `jayhshah` `hopper/flash_api.cpp`:370; signals: hang, hopper; excerpt: "Fixed and changed int to const int." (https://github.com/Dao-AILab/flash-attention/pull/1236#discussion_r1783085401)
- `2024-10-01T20:02:31Z` `inline` by `jayhshah` `hopper/seq_len.h`:19; signals: hang, hopper; excerpt: "Can be both, I changed the SeqLenTraits class to make it easier to enable this in a future PR." (https://github.com/Dao-AILab/flash-attention/pull/1236#discussion_r1783456117)
