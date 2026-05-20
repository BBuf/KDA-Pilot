# PR Discussion Digest

- Source PR: [sgl-project/sglang#12065](https://github.com/sgl-project/sglang/pull/12065)
- Source page: `sources/prs/sglang/PR-12065.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12065`
- Generated at: `2026-05-20T15:27:32.567836+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-24T08:18:33Z`
- Merged: `2025-11-17T04:12:25Z`

## Discussion Counts

- Issue comments: 14
- Review submissions: 13 (changes_requested=2, commented=11)
- Inline review comments: 70
- Review threads observed: 64
- Resolved/outdated thread markers: resolved=62, outdated=51
- Human participants with discussion text: ConcentrativeMan, FENP, Fridge003, ch-wan, lixiaolx, whybeyoung, yiakwy-xpu-ml-framework-team, zhuyijie88
- Automation comments/reviews omitted from high-signal summary: 29
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 7

## Review Decisions

- `2025-10-24T08:25:23Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces context parallelism for deepseek-v3.2-DSA models to reduce the time-to-first-token for long sequences. ... (https://github.com/sgl-project/sglang/pull/12065#pullrequestreview-3375078202)
- `2025-10-31T05:30:04Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12065#pullrequestreview-3391878971)
- `2025-10-31T05:36:54Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12065#pullrequestreview-3402660608)
- `2025-10-31T08:08:23Z` `COMMENTED` by `zhuyijie88` (https://github.com/sgl-project/sglang/pull/12065#pullrequestreview-3392123213)
- `2025-11-07T09:32:36Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12065#pullrequestreview-3407973714)
- `2025-11-10T01:33:34Z` `COMMENTED` by `sglang-bot` (https://github.com/sgl-project/sglang/pull/12065#pullrequestreview-3440542372)
- `2025-11-10T01:51:45Z` `CHANGES_REQUESTED` by `sglang-bot` - Can you also add a test case (to show the launch command). It does not need to be ... (https://github.com/sgl-project/sglang/pull/12065#pullrequestreview-3440543853)
- `2025-11-10T06:10:26Z` `COMMENTED` by `sglang-bot` (https://github.com/sgl-project/sglang/pull/12065#pullrequestreview-3441028271)
- `2025-11-13T09:08:37Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12065#pullrequestreview-3458219821)
- `2025-11-13T13:44:35Z` `COMMENTED` by `lixiaolx` (https://github.com/sgl-project/sglang/pull/12065#pullrequestreview-3459869533)
- `2025-11-13T19:29:37Z` `CHANGES_REQUESTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12065#pullrequestreview-3461348074)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 14 inline comment(s)
- `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`: 9 inline comment(s)
- `python/sglang/srt/server_args.py`: 9 inline comment(s)
- `docs/basic_usage/deepseek_v32.md`: 8 inline comment(s)
- `python/sglang/srt/layers/dp_attention.py`: 5 inline comment(s)
- `python/sglang/srt/utils/common.py`: 4 inline comment(s)
- `python/sglang/srt/model_executor/forward_batch_info.py`: 3 inline comment(s)
- `python/sglang/srt/layers/attention/nsa_backend.py`: 3 inline comment(s)
- `python/sglang/srt/layers/communicator.py`: 3 inline comment(s)
- `python/sglang/srt/managers/schedule_policy.py`: 2 inline comment(s)
- `python/sglang/srt/environ.py`: 2 inline comment(s)
- `python/sglang/srt/distributed/parallel_state.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-29T08:27:18Z` `inline` by `zhuyijie88` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:855; signals: attention, perf, performance; excerpt: "How much performance benifit from ragged treatment, which splits hidden states into prev and next parts?" (https://github.com/sgl-project/sglang/pull/12065#discussion_r2472116652)
- `2025-10-30T23:07:14Z` `inline` by `Fridge003` `python/sglang/srt/server_args.py`:1047; signals: cache, dtype, kv cache; excerpt: "Also print the message of kv cache dtype and tp size" (https://github.com/sgl-project/sglang/pull/12065#discussion_r2479740243)
- `2025-10-31T05:24:31Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:736; signals: attention, hang; excerpt: "Can be changed to if self.enable cp: Then assert cp input dict is not None" (https://github.com/sgl-project/sglang/pull/12065#discussion_r2480197549)
- `2025-10-31T05:17:05Z` `issue` by `Fridge003`; signals: accuracy, benchmark; excerpt: "Can you please test the accuracy of GPQA with this PR: The result should be about 0.80 Or other benchmark on long context, since ..." (https://github.com/sgl-project/sglang/pull/12065#issuecomment-3471375060)
- `2025-10-30T22:54:36Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:144; signals: attention; excerpt: "- Add a self.enable cp for checking whether cp is used - self.cp size/self.cp rank should be None by default. Can be initialized to ..." (https://github.com/sgl-project/sglang/pull/12065#discussion_r2479714193)
- `2025-10-31T01:33:08Z` `inline` by `Fridge003` `python/sglang/srt/utils/common.py`:3590; signals: attention; excerpt: "Can we move them to python/sglang/srt/layers/attention/nsa/utils.py, since they are only used for NSA currently." (https://github.com/sgl-project/sglang/pull/12065#discussion_r2479926189)
- `2025-10-31T05:36:48Z` `inline` by `Fridge003` `python/sglang/srt/distributed/device_communicators/pynccl.py`:213; signals: attention; excerpt: "Can we put all the added communication functions into a single place? Now it's scattered in four files: pynccl.py, parallel state.py, communicator.py, dp attention.py ..." (https://github.com/sgl-project/sglang/pull/12065#discussion_r2480215228)
- `2025-11-07T09:06:09Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:172; signals: attention; excerpt: "I feel only line 162-165 needs to be added for this file. For other variables what are their difference from original codes?" (https://github.com/sgl-project/sglang/pull/12065#discussion_r2502221062)
- `2025-11-13T13:44:25Z` `inline` by `lixiaolx` `python/sglang/srt/layers/attention/nsa_backend.py`:172; signals: attention; excerpt: "I feel only line 162-165 needs to be added for this file. For other variables what are their difference from original codes? When CP ..." (https://github.com/sgl-project/sglang/pull/12065#discussion_r2523528088)
- `2025-10-29T06:41:26Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:43; signals: attention; excerpt: "Remove logger if it's unused" (https://github.com/sgl-project/sglang/pull/12065#discussion_r2471890336)
- `2025-10-29T08:13:20Z` `inline` by `zhuyijie88` `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`:143; signals: attention; excerpt: "Does cp communication group reuse attention tp communication group ?" (https://github.com/sgl-project/sglang/pull/12065#discussion_r2472080764)
- `2025-10-31T01:20:42Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/nsa_backend.py`:39; signals: attention; excerpt: "Remove logger" (https://github.com/sgl-project/sglang/pull/12065#discussion_r2479912139)
