# PR Discussion Digest

- Source PR: [sgl-project/sglang#25299](https://github.com/sgl-project/sglang/pull/25299)
- Source page: `sources/prs/sglang/PR-25299.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-25299`
- Generated at: `2026-05-20T15:29:48.817872+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-14T16:43:14Z`
- Merged: `2026-05-19T23:04:14Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Fridge003, YAMY1234, ch-wan, samuellees
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2026-05-17T07:12:30Z` `APPROVED` by `samuellees` - Nice clean fix. Also left some comments about constant rename^ ^ (https://github.com/sgl-project/sglang/pull/25299#pullrequestreview-4304957757)
- `2026-05-18T22:00:55Z` `COMMENTED` by `YAMY1234` (https://github.com/sgl-project/sglang/pull/25299#pullrequestreview-4314287893)
- `2026-05-18T22:01:02Z` `COMMENTED` by `YAMY1234` (https://github.com/sgl-project/sglang/pull/25299#pullrequestreview-4314288730)
- `2026-05-19T10:00:01Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/25299#pullrequestreview-4317895657)
- `2026-05-19T17:09:40Z` `COMMENTED` by `YAMY1234` (https://github.com/sgl-project/sglang/pull/25299#pullrequestreview-4321283915)
- `2026-05-19T21:45:14Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/25299#pullrequestreview-4323450425)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`: 6 inline comment(s)

## High-Signal Discussion

- `2026-05-19T17:09:40Z` `inline` by `YAMY1234` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:563; signals: attention, cache, cuda, memory, oom; excerpt: "Good point. I updated this in 6f6201f. The cache is populated only after the static 8M-element skip and only on a non-capture path. Small ..." (https://github.com/sgl-project/sglang/pull/25299#discussion_r3268170161)
- `2026-05-19T09:59:58Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:563; signals: attention, cache; excerpt: "I have one question: when we compute the cached budget, what workload is it? I guess it might be at the first prefill batch ..." (https://github.com/sgl-project/sglang/pull/25299#discussion_r3265402260)
- `2026-05-19T17:09:39Z` `issue` by `YAMY1234`; signals: fp4, hang; excerpt: "Ran full GPQA Diamond with sgl-eval on DeepSeek V3.2 FP4, GB300 TP4. Command used: sgl-eval run gpqa --n-repeats 8 --num-threads 128 --temperature 1.0 --top-p ..." (https://github.com/sgl-project/sglang/pull/25299#issuecomment-4490179983)
- `2026-05-17T07:10:22Z` `inline` by `samuellees` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:547; signals: attention; excerpt: "Could you please name 0.3 as constants like MQA LOGITS FREE MEM FRACTION = 0.5?" (https://github.com/sgl-project/sglang/pull/25299#discussion_r3254188033)
- `2026-05-17T07:10:47Z` `inline` by `samuellees` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:554; signals: attention; excerpt: "Same with 0.3" (https://github.com/sgl-project/sglang/pull/25299#discussion_r3254188507)
- `2026-05-18T22:00:54Z` `inline` by `YAMY1234` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:547; signals: attention; excerpt: "Thanks, Adjusted!" (https://github.com/sgl-project/sglang/pull/25299#discussion_r3262452539)
- `2026-05-18T22:01:02Z` `inline` by `YAMY1234` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:554; signals: attention; excerpt: "Thanks, Adjusted!" (https://github.com/sgl-project/sglang/pull/25299#discussion_r3262453035)
- `2026-05-19T09:57:27Z` `issue` by `Fridge003`; signals: benchmark; excerpt: "@YAMY1234 Please try benchmarking on GPQA or AIME25 benchmark with sgl-eval:" (https://github.com/sgl-project/sglang/pull/25299#issuecomment-4486600254)
