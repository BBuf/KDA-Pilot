# PR Discussion Digest

- Source PR: [sgl-project/sglang#6093](https://github.com/sgl-project/sglang/pull/6093)
- Source page: `sources/prs/sglang/PR-6093.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6093`
- Generated at: `2026-05-20T15:30:36.126507+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-07T18:17:06Z`
- Merged: `2025-06-02T20:48:04Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 10 (commented=10)
- Inline review comments: 13
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: Fridge003, elfiegg, pavanimajety, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-30T18:11:58Z` `COMMENTED` by `elfiegg` - Thanks Pavani for the work! I left some comments and realized it might require some structure changes and ... (https://github.com/sgl-project/sglang/pull/6093#pullrequestreview-2882030193)
- `2025-05-30T18:23:41Z` `COMMENTED` by `pavanimajety` (https://github.com/sgl-project/sglang/pull/6093#pullrequestreview-2882108989)
- `2025-06-02T16:21:37Z` `COMMENTED` by `pavanimajety` (https://github.com/sgl-project/sglang/pull/6093#pullrequestreview-2889132958)
- `2025-06-02T16:21:53Z` `COMMENTED` by `pavanimajety` (https://github.com/sgl-project/sglang/pull/6093#pullrequestreview-2889133921)
- `2025-06-02T16:23:09Z` `COMMENTED` by `pavanimajety` (https://github.com/sgl-project/sglang/pull/6093#pullrequestreview-2889138548)
- `2025-06-02T18:15:32Z` `COMMENTED` by `elfiegg` (https://github.com/sgl-project/sglang/pull/6093#pullrequestreview-2889471077)
- `2025-06-02T18:21:25Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/6093#pullrequestreview-2889492075)
- `2025-06-02T18:21:30Z` `COMMENTED` by `pavanimajety` (https://github.com/sgl-project/sglang/pull/6093#pullrequestreview-2889492319)
- `2025-06-02T18:24:58Z` `COMMENTED` by `pavanimajety` (https://github.com/sgl-project/sglang/pull/6093#pullrequestreview-2889501008)
- `2025-06-02T18:32:58Z` `COMMENTED` by `elfiegg` (https://github.com/sgl-project/sglang/pull/6093#pullrequestreview-2889531646)

## Inline Comment Hotspots

- `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`: 7 inline comment(s)
- `python/sglang/srt/layers/moe/cutlass_moe.py`: 4 inline comment(s)
- `sgl-kernel/csrc/moe/prepare_moe_input.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2025-05-30T18:08:51Z` `inline` by `elfiegg` `sgl-kernel/csrc/moe/prepare_moe_input.cu`:189; signals: block, fp4, fp8, kernel, layout, moe; excerpt: "is it better to merge this with prepare moe input and set a flag for passing in blockscale offset (or simply flag it with ..." (https://github.com/sgl-project/sglang/pull/6093#discussion_r2116366129)
- `2025-06-02T18:21:30Z` `inline` by `pavanimajety` `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`:288; signals: block, fp4, kernel, memory, moe, nvfp4; excerpt: "These don't actually have any overhead though. It's just allocates memory during capture and reuses it during replay. It provides for a cleaner interface ..." (https://github.com/sgl-project/sglang/pull/6093#discussion_r2121860110)
- `2025-06-02T18:32:57Z` `inline` by `elfiegg` `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`:288; signals: block, cache, fp4, kernel, moe, nvfp4; excerpt: "if torch fails to cache it - in eager mode these will be called again and again though? also the two comments seem contradictory ..." (https://github.com/sgl-project/sglang/pull/6093#discussion_r2121889880)
- `2025-05-30T17:53:33Z` `inline` by `elfiegg` `python/sglang/srt/layers/moe/cutlass_moe.py`:316; signals: cutlass, fp4, fp8, moe, perf; excerpt: "For fp8 bs these tensors are initiated after weights are loaded, and are passed into this class for perf reasons. I suggest for fp4 ..." (https://github.com/sgl-project/sglang/pull/6093#discussion_r2116344472)
- `2025-05-30T18:04:48Z` `inline` by `elfiegg` `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`:289; signals: block, fp4, kernel, moe, nvfp4; excerpt: "have you tested graph mode, would it work? these static tensor initiations can be moved outside of this kernel" (https://github.com/sgl-project/sglang/pull/6093#discussion_r2116361192)
- `2025-06-02T18:24:58Z` `inline` by `pavanimajety` `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`:288; signals: block, fp4, kernel, moe, nvfp4; excerpt: "They also go out of scope after the kernel finishes running, which also makes it slightly better I think." (https://github.com/sgl-project/sglang/pull/6093#discussion_r2121865773)
- `2025-05-30T18:23:41Z` `inline` by `pavanimajety` `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`:289; signals: block, fp4, kernel, moe, nvfp4; excerpt: "yes, this has been tested with graph mode." (https://github.com/sgl-project/sglang/pull/6093#discussion_r2116394447)
- `2025-06-02T18:14:31Z` `inline` by `elfiegg` `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`:288; signals: block, fp4, kernel, moe, nvfp4; excerpt: "Can we try moving all these static tensors out of the kernel?" (https://github.com/sgl-project/sglang/pull/6093#discussion_r2121844877)
- `2025-06-02T18:21:25Z` `inline` by `zhyncs` `sgl-kernel/csrc/moe/nvfp4_blockwise_moe.cu`:288; signals: block, fp4, kernel, moe, nvfp4; excerpt: "agree" (https://github.com/sgl-project/sglang/pull/6093#discussion_r2121859931)
- `2025-06-02T16:21:37Z` `inline` by `pavanimajety` `python/sglang/srt/layers/moe/cutlass_moe.py`:320; signals: cutlass, hang, moe; excerpt: "Changed the logic, so initializing only empty which should have no overhead" (https://github.com/sgl-project/sglang/pull/6093#discussion_r2121628406)
- `2025-05-30T17:57:01Z` `inline` by `elfiegg` `python/sglang/srt/layers/moe/cutlass_moe.py`:320; signals: cutlass, moe; excerpt: "This tensor is also static and requires buffer filling. consider also moving it outside of the class and initiating it after weights are loaded" (https://github.com/sgl-project/sglang/pull/6093#discussion_r2116348976)
- `2025-06-02T16:23:09Z` `inline` by `pavanimajety` `python/sglang/srt/layers/moe/cutlass_moe.py`:316; signals: cutlass, moe; excerpt: "Modified it- The initialization happens in the test now and for the checkpoint it will happen in the post weight loading phase(part of second ..." (https://github.com/sgl-project/sglang/pull/6093#discussion_r2121631844)
