# PR Discussion Digest

- Source PR: [sgl-project/sglang#20708](https://github.com/sgl-project/sglang/pull/20708)
- Source page: `sources/prs/sglang/PR-20708.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-20708`
- Generated at: `2026-05-20T15:29:06.554925+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-16T17:17:19Z`
- Merged: `2026-03-18T21:15:33Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 2 (commented=2)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: JustinTong0323, alexnails, dbari
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-16T17:27:55Z` `COMMENTED` by `alexnails` (https://github.com/sgl-project/sglang/pull/20708#pullrequestreview-3955487336)
- `2026-03-16T17:28:40Z` `COMMENTED` by `JustinTong0323` (https://github.com/sgl-project/sglang/pull/20708#pullrequestreview-3955513523)

## Inline Comment Hotspots

- `benchmark/mmmu/eval_utils.py`: 2 inline comment(s)
- `python/sglang/srt/utils/hf_transformers_utils.py`: 1 inline comment(s)
- `python/sglang/srt/parser/reasoning_parser.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-16T17:27:17Z` `inline` by `alexnails` `benchmark/mmmu/eval_utils.py`:128; signals: benchmark; excerpt: "need to add rest of choices" (https://github.com/sgl-project/sglang/pull/20708#discussion_r2941855764)
- `2026-03-16T17:28:40Z` `inline` by `JustinTong0323` `benchmark/mmmu/eval_utils.py`:128; signals: benchmark; excerpt: "it's ok to keep it now as oai model is text only" (https://github.com/sgl-project/sglang/pull/20708#discussion_r2941864857)
- `2026-03-16T17:25:01Z` `inline` by `alexnails` `python/sglang/srt/utils/hf_transformers_utils.py`:1237; signals: general review; excerpt: "do we keep this? (I actually think this is a useful fallback but it should be improved at a later point)" (https://github.com/sgl-project/sglang/pull/20708#discussion_r2941841029)
- `2026-03-16T17:25:32Z` `inline` by `alexnails` `python/sglang/srt/parser/reasoning_parser.py`:447; signals: general review; excerpt: "clean up (02 to 03)" (https://github.com/sgl-project/sglang/pull/20708#discussion_r2941843909)
- `2026-03-17T08:52:48Z` `issue` by `dbari`; signals: general review; excerpt: "Here is a diff to improve the gsm8k score: Tasks Version Filter n-shot Metric Value Stderr ----- ------: ---------------- -----: ----------- --- -----: --- ..." (https://github.com/sgl-project/sglang/pull/20708#issuecomment-4073319807)
- `2026-03-17T17:21:32Z` `issue` by `JustinTong0323`; signals: general review; excerpt: "@dbari I've just pushed the fix you made on the rope. Thanks a lot for that! I also apologize for the earlier wrong decision ..." (https://github.com/sgl-project/sglang/pull/20708#issuecomment-4076676545)
