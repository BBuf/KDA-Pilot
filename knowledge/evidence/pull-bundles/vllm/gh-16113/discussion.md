# PR Discussion Digest

- Source PR: [vllm-project/vllm#16113](https://github.com/vllm-project/vllm/pull/16113)
- Source page: `sources/prs/vllm/PR-16113.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16113`
- Generated at: `2026-05-20T15:34:51.402562+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-06T04:33:08Z`
- Merged: `2025-04-07T15:06:27Z`

## Discussion Counts

- Issue comments: 28
- Review submissions: 12 (approved=1, changes_requested=1, commented=10)
- Inline review comments: 10
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=5
- Human participants with discussion text: DarkLight1337, LagPixelLOL, luccafong, ywang96
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-06T06:41:49Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2745053003)
- `2025-04-06T07:24:51Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2745061082)
- `2025-04-06T07:26:04Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2745061332)
- `2025-04-06T07:29:40Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2745062064)
- `2025-04-06T07:30:27Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2745062227)
- `2025-04-06T07:31:26Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2745062400)
- `2025-04-06T07:38:42Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2745063849)
- `2025-04-06T07:43:33Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2745065025)
- `2025-04-06T09:30:34Z` `CHANGES_REQUESTED` by `ywang96` - Can confirm there's something wrong with this branch per report from @LagPixelLOL and I can repro it too, ... (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2745088830)
- `2025-04-07T02:43:14Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2745416877)
- `2025-04-07T02:43:43Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2745417217)
- `2025-04-07T15:06:03Z` `APPROVED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2747183941)

## Inline Comment Hotspots

- `tests/models/registry.py`: 5 inline comment(s)
- `tests/models/decoder_only/vision_language/test_models.py`: 3 inline comment(s)
- `vllm/model_executor/models/mllama4.py`: 1 inline comment(s)
- `tests/models/multimodal/processing/test_common.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-04-06T18:15:02Z` `issue` by `luccafong`; signals: cutlass, fp8, hang, moe; excerpt: "Did some testing and confirmed the issue only happens to Llama-4-Maverick-17B-128E-Instruct-FP8 since Llama-4-Scout-17B-16E-Instruct is working fine on this branch. is there conflict change in ..." (https://github.com/vllm-project/vllm/pull/16113#issuecomment-2781541618)
- `2025-04-06T18:58:58Z` `issue` by `ywang96`; signals: cutlass, fp8, hang, moe; excerpt: "Did some testing and confirmed the issue only happens to Llama-4-Maverick-17B-128E-Instruct-FP8 since Llama-4-Scout-17B-16E-Instruct is working fine on this branch. is there conflict change in ..." (https://github.com/vllm-project/vllm/pull/16113#issuecomment-2781566801)
- `2025-04-07T04:47:46Z` `issue` by `LagPixelLOL`; signals: compile, fp8, h200, race; excerpt: "Using the same command I sent, but I tried to send a single request with 999,500 tokens of context on 4x H200 running FP8, ..." (https://github.com/vllm-project/vllm/pull/16113#issuecomment-2782007441)
- `2025-04-07T04:58:37Z` `issue` by `ywang96`; signals: compile, fp8, h200, race; excerpt: "Using the same command I sent, but I tried to send a single request with 999,990 tokens of context on 4x H200 running FP8, ..." (https://github.com/vllm-project/vllm/pull/16113#issuecomment-2782019126)
- `2025-04-07T05:03:19Z` `issue` by `LagPixelLOL`; signals: cache, fp8, h200, kv cache; excerpt: "@ywang96 It can, when using FP8 KV cache, it supports exactly 1 million context. It's not that it doesn't support it, the index error ..." (https://github.com/vllm-project/vllm/pull/16113#issuecomment-2782024291)
- `2025-04-07T05:09:07Z` `issue` by `ywang96`; signals: cache, fp8, h200, kv cache; excerpt: "@ywang96 It can, when using FP8 KV cache, it supports exactly 1 million context. It's not that it doesn't support it, the index error ..." (https://github.com/vllm-project/vllm/pull/16113#issuecomment-2782031045)
- `2025-04-06T09:30:34Z` `review` `CHANGES_REQUESTED` by `ywang96`; signals: block; excerpt: "Can confirm there's something wrong with this branch per report from @LagPixelLOL and I can repro it too, but the model is working fine ..." (https://github.com/vllm-project/vllm/pull/16113#pullrequestreview-2745088830)
- `2025-04-07T05:27:36Z` `issue` by `ywang96`; signals: cache, kv cache; excerpt: "Upon further testing, it seems that it not only happens at 999500, it starts to happen right about the set max context length - ..." (https://github.com/vllm-project/vllm/pull/16113#issuecomment-2782057224)
- `2025-04-07T05:34:43Z` `issue` by `LagPixelLOL`; signals: compile, race; excerpt: "I managed to get a not messed up stack trace. It seems that the last call still inside vLLM was (VllmWorker rank=1 pid=18180) ERROR ..." (https://github.com/vllm-project/vllm/pull/16113#issuecomment-2782066325)
- `2025-04-06T06:41:49Z` `inline` by `ywang96` `vllm/model_executor/models/mllama4.py`:813; signals: aligned; excerpt: "Could we update the forward here so it's more aligned with the similar pattern that other MM models adopt?" (https://github.com/vllm-project/vllm/pull/16113#discussion_r2030055957)
- `2025-04-06T06:03:18Z` `issue` by `ywang96`; signals: hang; excerpt: "Since we're not in a huge rush to merge this PR into main, a few action items (and notes to myself): [x] Fix model ..." (https://github.com/vllm-project/vllm/pull/16113#issuecomment-2781239239)
- `2025-04-06T06:15:13Z` `issue` by `luccafong`; signals: hang; excerpt: "Since we're not in a huge rush to merge this PR into main, a few action items (and notes to myself): [x] Fix model ..." (https://github.com/vllm-project/vllm/pull/16113#issuecomment-2781245944)
