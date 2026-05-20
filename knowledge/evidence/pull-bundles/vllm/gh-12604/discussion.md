# PR Discussion Digest

- Source PR: [vllm-project/vllm#12604](https://github.com/vllm-project/vllm/pull/12604)
- Source page: `sources/prs/vllm/PR-12604.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-12604`
- Generated at: `2026-05-20T15:33:49.409793+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-31T06:40:54Z`
- Merged: `2025-02-05T21:31:38Z`

## Discussion Counts

- Issue comments: 49
- Review submissions: 29 (approved=1, commented=28)
- Inline review comments: 34
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=10, outdated=7
- Human participants with discussion text: DarkLight1337, Holmes2002, Isotr0py, PkuDavidGuan, ZhonghaoLu, dprokhorov17, fearnworks, hxujal, jeejeelee, jjovalle99, jmtatsch, kevin-ssy, linchen111, mergify, pbarker, ransheng11, rstone3017, thiner, wulipc, xiayq1
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 29

## Review Decisions

- `2025-02-03T02:33:13Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2588762821)
- `2025-02-03T03:23:00Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2588821352)
- `2025-02-03T03:23:54Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2588821905)
- `2025-02-03T07:27:05Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2589103149)
- `2025-02-03T07:31:24Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2589109806)
- `2025-02-03T07:35:41Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2589116233)
- `2025-02-03T07:53:05Z` `COMMENTED` by `wulipc` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2589144909)
- `2025-02-03T09:36:46Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2589373147)
- `2025-02-03T10:11:18Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2589460000)
- `2025-02-03T10:12:25Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2589462477)
- `2025-02-03T10:17:30Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2589474116)
- `2025-02-03T11:45:08Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2589659733)
- `2025-02-03T16:25:27Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2590432764)
- `2025-02-03T18:59:30Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2590760393)
- `2025-02-04T02:08:39Z` `COMMENTED` by `wulipc` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2591534341)
- `2025-02-04T03:26:19Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2591629862)
- `2025-02-04T03:32:05Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2591634203)
- `2025-02-04T03:39:10Z` `APPROVED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2591640432)
- `2025-02-04T05:17:17Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2591760377)
- `2025-02-04T05:40:23Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2591786340)
- `2025-02-04T06:03:40Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2591812985)
- `2025-02-04T07:19:53Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2591928732)
- `2025-02-04T07:23:02Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2591933734)
- `2025-02-04T07:23:31Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/12604#pullrequestreview-2591934536)
- ... 5 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/models/qwen2_5_vl.py`: 32 inline comment(s)
- `tests/models/decoder_only/vision_language/test_models.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-02-05T07:31:15Z` `issue` by `rstone3017`; signals: cache, cuda, memory, perf, race, tile; excerpt: "You need to install the latest code of transformers from their main branch. I am on I was able to make it work in ..." (https://github.com/vllm-project/vllm/pull/12604#issuecomment-2635922221)
- `2025-02-03T11:44:35Z` `inline` by `Isotr0py` `vllm/model_executor/models/qwen2_5_vl.py`:207; signals: alignment, attention; excerpt: "This vision attention implementation is out of date after 11719 merged, I think we should use the current Qwen2-VL vision attention implementation in main ..." (https://github.com/vllm-project/vllm/pull/12604#discussion_r1939242840)
- `2025-02-03T07:35:41Z` `inline` by `ywang96` `vllm/model_executor/models/qwen2_5_vl.py`:326; signals: attention, hang; excerpt: "I'm going to keep them separate since Qwen Team's PR made some changes to the attention module." (https://github.com/vllm-project/vllm/pull/12604#discussion_r1938909062)
- `2025-02-02T23:36:34Z` `issue` by `ywang96`; signals: aligned, hang; excerpt: "This PR is ready for review. A few notes: 1. In order to run this model, we need a new release from transformers for ..." (https://github.com/vllm-project/vllm/pull/12604#issuecomment-2629615284)
- `2025-02-04T05:14:12Z` `issue` by `jeejeelee`; signals: aligned, hang; excerpt: "This PR is ready for review. A few notes: 1. In order to run this model, we need a new release from transformers for ..." (https://github.com/vllm-project/vllm/pull/12604#issuecomment-2632898558)
- `2025-02-04T17:19:14Z` `issue` by `ywang96`; signals: perf, performance; excerpt: "You need to install the latest code of transformers from their main branch. I am on I was able to make it work in ..." (https://github.com/vllm-project/vllm/pull/12604#issuecomment-2634601398)
- `2025-02-05T07:18:13Z` `issue` by `PkuDavidGuan`; signals: perf, performance; excerpt: "You need to install the latest code of transformers from their main branch. I am on I was able to make it work in ..." (https://github.com/vllm-project/vllm/pull/12604#issuecomment-2635874892)
- `2025-02-03T10:11:18Z` `inline` by `ywang96` `vllm/model_executor/models/qwen2_5_vl.py`:749; signals: hang; excerpt: "@wulipc I reverted the change to add fps as an input here. This is because unlike min pixels and max pixels, fps is not ..." (https://github.com/vllm-project/vllm/pull/12604#discussion_r1939119191)
- `2025-02-03T10:17:30Z` `inline` by `ywang96` `vllm/model_executor/models/qwen2_5_vl.py`:466; signals: attention; excerpt: "The two ViTs are quite different in terms of: 1. Different MLP 2. Different layernorms 3. Additional logic around window size in Qwen2.5-VL We ..." (https://github.com/vllm-project/vllm/pull/12604#discussion_r1939127838)
- `2025-02-04T07:19:53Z` `inline` by `ywang96` `vllm/model_executor/models/qwen2_5_vl.py`:207; signals: hang; excerpt: "I noticed this change significantly broke the model so I reverted it." (https://github.com/vllm-project/vllm/pull/12604#discussion_r1940623900)
- `2025-02-04T11:19:48Z` `issue` by `dprokhorov17`; signals: pipeline; excerpt: "I have build vllm and this branch from source and I do get the following error: TypeError: Unknown image model type: qwen2 5 vl ..." (https://github.com/vllm-project/vllm/pull/12604#issuecomment-2633608774)
- `2025-02-03T02:30:30Z` `inline` by `DarkLight1337` `vllm/model_executor/models/qwen2_5_vl.py`:693; signals: general review; excerpt: "I think we can inherit from Qwen2VLProcessingInfo and just override get hf config, get hf processor and get image processor" (https://github.com/vllm-project/vllm/pull/12604#discussion_r1938685129)
