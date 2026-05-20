# PR Discussion Digest

- Source PR: [sgl-project/sglang#10678](https://github.com/sgl-project/sglang/pull/10678)
- Source page: `sources/prs/sglang/PR-10678.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-10678`
- Generated at: `2026-05-20T15:27:20.212639+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-20T00:36:42Z`
- Merged: `2025-09-22T02:36:08Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 9 (approved=2, changes_requested=1, commented=6)
- Inline review comments: 9
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=6, outdated=5
- Human participants with discussion text: Edenzzzz, Fridge003, JustinTong0323, Qiaolin-Yu, gameofdimension, hebiao064, jzft-nuosu, merrymercy, skyzh
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-09-20T00:38:55Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for deterministic inference, which is a significant feature. The changes are ... (https://github.com/sgl-project/sglang/pull/10678#pullrequestreview-3247791220)
- `2025-09-20T06:43:09Z` `COMMENTED` by `JustinTong0323` (https://github.com/sgl-project/sglang/pull/10678#pullrequestreview-3248595310)
- `2025-09-20T22:45:11Z` `APPROVED` by `Fridge003` - LGTM (https://github.com/sgl-project/sglang/pull/10678#pullrequestreview-3249304552)
- `2025-09-20T23:07:38Z` `APPROVED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/10678#pullrequestreview-3249308650)
- `2025-09-21T01:50:55Z` `COMMENTED` by `Edenzzzz` (https://github.com/sgl-project/sglang/pull/10678#pullrequestreview-3249335645)
- `2025-09-21T17:50:39Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/10678#pullrequestreview-3250104490)
- `2025-09-21T22:16:38Z` `COMMENTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/10678#pullrequestreview-3250180910)
- `2025-09-21T22:19:26Z` `CHANGES_REQUESTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/10678#pullrequestreview-3250182386)
- `2025-09-22T00:41:20Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/10678#pullrequestreview-3250241598)

## Inline Comment Hotspots

- `python/sglang/srt/layers/sampler.py`: 6 inline comment(s)
- `python/sglang/srt/managers/schedule_batch.py`: 2 inline comment(s)
- `python/sglang/srt/layers/layernorm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-21T01:50:55Z` `inline` by `Edenzzzz` `python/sglang/srt/layers/sampler.py`:299; signals: compile; excerpt: "can wrap this part inside torch.compile" (https://github.com/sgl-project/sglang/pull/10678#discussion_r2365895922)
- `2025-09-22T01:20:52Z` `issue` by `Fridge003`; signals: hang; excerpt: "hey - I noticed that when I set the split size to 128 on this commit There's another place affected by the split size, ..." (https://github.com/sgl-project/sglang/pull/10678#issuecomment-3316453325)
- `2025-09-21T22:19:22Z` `inline` by `merrymercy` `python/sglang/srt/layers/sampler.py`:130; signals: general review; excerpt: "We should use hash(sampling seed, position) as the real seed. Otherwise, each position will use the same seed to sample" (https://github.com/sgl-project/sglang/pull/10678#discussion_r2366417298)
- `2025-09-20T06:42:11Z` `inline` by `JustinTong0323` `python/sglang/srt/managers/schedule_batch.py`:497; signals: general review; excerpt: "In token-in-token-out scenarios, self.origin input text could be None." (https://github.com/sgl-project/sglang/pull/10678#discussion_r2365357134)
- `2025-09-21T17:50:38Z` `inline` by `Fridge003` `python/sglang/srt/layers/sampler.py`:299; signals: general review; excerpt: "Can be left for future" (https://github.com/sgl-project/sglang/pull/10678#discussion_r2366326199)
- `2025-09-21T22:14:39Z` `inline` by `merrymercy` `python/sglang/srt/layers/sampler.py`:281; signals: general review; excerpt: "this should not be needed" (https://github.com/sgl-project/sglang/pull/10678#discussion_r2366415748)
- `2025-09-21T22:15:42Z` `inline` by `merrymercy` `python/sglang/srt/managers/schedule_batch.py`:496; signals: general review; excerpt: "do not add it here, add it in sampling params.py" (https://github.com/sgl-project/sglang/pull/10678#discussion_r2366416089)
- `2025-09-22T00:41:19Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/layers/sampler.py`:130; signals: general review; excerpt: "done" (https://github.com/sgl-project/sglang/pull/10678#discussion_r2366473227)
- `2025-09-22T00:49:20Z` `issue` by `skyzh`; signals: general review; excerpt: "hey - I noticed that when I set the split size to 128 on this commit fb1e8acd2954b6267c73a199427976d89887ff0e: The patch would yield multiple unique samples ..." (https://github.com/sgl-project/sglang/pull/10678#issuecomment-3316417773)
