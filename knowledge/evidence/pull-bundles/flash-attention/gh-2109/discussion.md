# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2109](https://github.com/Dao-AILab/flash-attention/pull/2109)
- Source page: `sources/prs/flash-attention/PR-2109.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2109`
- Generated at: `2026-05-20T15:16:42.470124+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-29T23:38:03Z`
- Merged: `2026-04-17T17:51:50Z`

## Discussion Counts

- Issue comments: 20
- Review submissions: 18 (approved=1, commented=17)
- Inline review comments: 17
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=2, outdated=5
- Human participants with discussion text: Edenzzzz, cyk2018, dcw02, drisspg, haocizhang, howardzhang-cv, johnnynunez, tridao, zhc-hpc
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-13T02:11:42Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-3794698489)
- `2026-02-13T02:15:47Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-3794705372)
- `2026-02-13T02:15:51Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-3794705456)
- `2026-02-13T02:31:26Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-3794734138)
- `2026-02-14T02:11:19Z` `COMMENTED` by `dcw02` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-3800462708)
- `2026-02-14T02:11:56Z` `COMMENTED` by `dcw02` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-3800463799)
- `2026-03-18T11:51:49Z` `COMMENTED` by `haocizhang` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-3967209767)
- `2026-03-18T15:47:31Z` `COMMENTED` by `dcw02` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-3968898902)
- `2026-03-18T23:05:16Z` `COMMENTED` by `haocizhang` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-3971388396)
- `2026-04-09T17:39:41Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-4084293118)
- `2026-04-09T17:42:17Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-4084308274)
- `2026-04-09T17:43:49Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-4084317155)
- `2026-04-09T23:23:56Z` `COMMENTED` by `dcw02` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-4086092147)
- `2026-04-09T23:50:37Z` `COMMENTED` by `dcw02` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-4086188874)
- `2026-04-09T23:59:09Z` `COMMENTED` by `dcw02` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-4086217651)
- `2026-04-10T07:27:57Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-4088065682)
- `2026-04-10T07:30:08Z` `APPROVED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-4088075798)
- `2026-04-10T20:32:18Z` `COMMENTED` by `dcw02` (https://github.com/Dao-AILab/flash-attention/pull/2109#pullrequestreview-4092337475)

## Inline Comment Hotspots

- `flash_attn/cute/flash_fwd_sm100.py`: 13 inline comment(s)
- `flash_attn/cute/interface.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-03-18T11:51:50Z` `inline` by `haocizhang` `flash_attn/cute/flash_fwd_sm100.py`:2038; signals: correctness, cute, dtype, perf, performance, sm100, tma; excerpt: "Hi @dcw02 , dumb question: why do we set e2e = false when self.q dtype.width == 8? My understanding is that this disables the ..." (https://github.com/Dao-AILab/flash-attention/pull/2109#discussion_r2952885248)
- `2026-01-30T03:55:20Z` `issue` by `dcw02`; signals: bf16, fp8, perf, performance, speedup, tma; excerpt: "It seems curious to me that FP8 can only get 0.95x - 1.15x speedup given it reduces data movement by half. Is it possible ..." (https://github.com/Dao-AILab/flash-attention/pull/2109#issuecomment-3821669084)
- `2026-02-13T02:15:48Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:2499; signals: cute, hang, perf, performance, sm100; excerpt: "I doubt it has much of an impact but did we measure that the non qkv scaled doesnt take any performance hit from these ..." (https://github.com/Dao-AILab/flash-attention/pull/2109#discussion_r2801948432)
- `2026-02-14T02:11:55Z` `inline` by `dcw02` `flash_attn/cute/flash_fwd_sm100.py`:2499; signals: compile, cute, perf, performance, sm100; excerpt: "there was no measurable performance impact but I added compile time gating" (https://github.com/Dao-AILab/flash-attention/pull/2109#discussion_r2806798803)
- `2026-03-18T23:05:16Z` `inline` by `haocizhang` `flash_attn/cute/flash_fwd_sm100.py`:2038; signals: cute, fp8, sm100, tma; excerpt: "I see, thanks for the insights. Just curious—do we have a theory on why this is tied to FP8? My original understanding was that ..." (https://github.com/Dao-AILab/flash-attention/pull/2109#discussion_r2956726528)
- `2026-04-09T23:23:56Z` `inline` by `dcw02` `flash_attn/cute/flash_fwd_sm100.py`:1957; signals: cute, dtype, epilogue, sm100; excerpt: "partial descales are supported, missing q descale / k descale default to 1.0, and v descale is handled independently later in the correction/epilogue path. ..." (https://github.com/Dao-AILab/flash-attention/pull/2109#discussion_r3061198123)
- `2026-03-18T15:47:31Z` `inline` by `dcw02` `flash_attn/cute/flash_fwd_sm100.py`:2038; signals: cute, perf, performance, sm100; excerpt: "this was for performance reasons, I found that the emulation path made performance a lot worse" (https://github.com/Dao-AILab/flash-attention/pull/2109#discussion_r2954436089)
- `2026-03-15T22:41:55Z` `issue` by `dcw02`; signals: bf16, fp8, perf, performance; excerpt: "I did an initial rebase locally but the performance was a lot worse, for both bf16 and fp8 paths. Will look more into it ..." (https://github.com/Dao-AILab/flash-attention/pull/2109#issuecomment-4064072124)
- `2026-04-05T08:48:10Z` `issue` by `dcw02`; signals: benchmark, bf16, perf, performance; excerpt: "finished some tuning, new benchmark numbers: Performance is better than before rebase, we're topping out at 1950 TFLOPs/s. The bf16 numbers are worse but ..." (https://github.com/Dao-AILab/flash-attention/pull/2109#issuecomment-4188551579)
- `2026-04-09T23:50:36Z` `inline` by `dcw02` `flash_attn/cute/flash_fwd_sm100.py`:2378; signals: cute, sm100, tma; excerpt: "yea agreed, I refactored the descale loading into a helper but kept the surrounding softmax scale logic to prevent muddling the different softmax/correction semantics ..." (https://github.com/Dao-AILab/flash-attention/pull/2109#discussion_r3061276136)
- `2026-04-09T17:39:41Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:1957; signals: cute, fp8, sm100; excerpt: "do we support not having all 3 specified? / mixed fp8 qk and high precision v? or vice versa" (https://github.com/Dao-AILab/flash-attention/pull/2109#discussion_r3059635847)
- `2026-04-09T17:42:17Z` `inline` by `drisspg` `flash_attn/cute/flash_fwd_sm100.py`:2378; signals: cute, sm100, tma; excerpt: "should this be a helper since seems to have alot with softmax loop" (https://github.com/Dao-AILab/flash-attention/pull/2109#discussion_r3059648963)
