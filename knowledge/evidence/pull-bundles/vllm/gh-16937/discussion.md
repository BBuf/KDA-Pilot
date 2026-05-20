# PR Discussion Digest

- Source PR: [vllm-project/vllm#16937](https://github.com/vllm-project/vllm/pull/16937)
- Source page: `sources/prs/vllm/PR-16937.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16937`
- Generated at: `2026-05-20T15:35:04.446698+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-21T17:54:15Z`
- Merged: `2025-04-25T22:43:07Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 19 (approved=1, commented=18)
- Inline review comments: 24
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=13, outdated=9
- Human participants with discussion text: DarkLight1337, WoosukKwon, benchislett, ekagra-ranjan, fan-niu, lfopensource, markmc, mergify, wwl2755
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-04-21T20:07:46Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2782150040)
- `2025-04-21T20:08:11Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2782150687)
- `2025-04-21T20:08:26Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2782151078)
- `2025-04-21T20:09:22Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2782152540)
- `2025-04-21T20:20:59Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2782170661)
- `2025-04-21T20:26:15Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2782179804)
- `2025-04-22T02:43:08Z` `COMMENTED` by `wwl2755` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2782610402)
- `2025-04-23T20:05:30Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2788571181)
- `2025-04-23T20:07:50Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2788575665)
- `2025-04-23T20:29:51Z` `COMMENTED` by `WoosukKwon` - @benchislett Thanks for submitting the PR! This is amazing! 🚀 Left some minor comments on the style. Please ... (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2788591348)
- `2025-04-24T12:32:05Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2790953586)
- `2025-04-24T12:35:08Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2790975633)
- `2025-04-24T12:37:17Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2790991543)
- `2025-04-24T12:39:16Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2791005561)
- `2025-04-24T12:41:28Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2791012467)
- `2025-04-24T13:12:53Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2791152757)
- `2025-04-24T16:19:27Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2791804751)
- `2025-04-24T16:21:32Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2791809754)
- `2025-04-24T16:23:18Z` `APPROVED` by `WoosukKwon` - @benchislett LGTM. Thanks for the PR! Really excited to have this 🚀 Please merge from main to fix ... (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2791817180)

## Inline Comment Hotspots

- `vllm/model_executor/models/llama.py`: 9 inline comment(s)
- `vllm/model_executor/models/llama_eagle3.py`: 5 inline comment(s)
- `vllm/config.py`: 3 inline comment(s)
- `vllm/v1/worker/gpu_model_runner.py`: 3 inline comment(s)
- `vllm/engine/arg_utils.py`: 1 inline comment(s)
- `vllm/v1/spec_decode/eagle.py`: 1 inline comment(s)
- `tests/models/registry.py`: 1 inline comment(s)
- `vllm/model_executor/models/llama_eagle.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-04-25T14:27:04Z` `issue` by `benchislett`; signals: failing, hang, memory, oom; excerpt: "@DarkLight1337 (cc @WoosukKwon) I'm not sure how to address these failing tests. There are two failures: - The base EAGLE test is failing with ..." (https://github.com/vllm-project/vllm/pull/16937#issuecomment-2830588407)
- `2025-04-25T18:50:40Z` `issue` by `ekagra-ranjan`; signals: benchmark, h100, memory, throughput; excerpt: "Are you measuring output token throughput, or TPOT? @benchislett Thanks for pointing it out. The output tokens/s by running /offline inference/eagle.py is indeed not ..." (https://github.com/vllm-project/vllm/pull/16937#issuecomment-2831180173)
- `2025-04-24T16:46:49Z` `issue` by `benchislett`; signals: benchmark, perf, performance; excerpt: "@ekagra-ranjan the branch is functional in its current state. you are welcome to benchmark it yourself, but I think the cost should be the ..." (https://github.com/vllm-project/vllm/pull/16937#issuecomment-2828254603)
- `2025-04-24T22:24:13Z` `issue` by `ekagra-ranjan`; signals: benchmark, h100, speedup; excerpt: "I just did the [bench]( for K=2,4,7 and compared EAGLE1 and EAGLE3. The AL matches with your run. In your RTX 4090 run, EAGLE-3 ..." (https://github.com/vllm-project/vllm/pull/16937#issuecomment-2828992581)
- `2025-04-24T17:08:26Z` `issue` by `benchislett`; signals: perf, performance; excerpt: "@ekagra-ranjan I mean to say that the cost of evaluating an EAGLE layer should be the same for EAGLE1 vs EAGLE3. So the performance ..." (https://github.com/vllm-project/vllm/pull/16937#issuecomment-2828305438)
- `2025-04-25T14:24:27Z` `issue` by `benchislett`; signals: perf, throughput; excerpt: "@ekagra-ranjan this seems reasonable. Are you measuring output token throughput, or TPOT? These are not quite the same, I believe output token throughput is ..." (https://github.com/vllm-project/vllm/pull/16937#issuecomment-2830581294)
- `2025-04-24T12:37:17Z` `inline` by `benchislett` `vllm/v1/worker/gpu_model_runner.py`:168; signals: hang; excerpt: "I think it makes sense to have this functionality distinct from EAGLE3. For now it is the only method that needs hidden state outputs, ..." (https://github.com/vllm-project/vllm/pull/16937#discussion_r2058319330)
- `2025-04-23T20:29:51Z` `review` `COMMENTED` by `WoosukKwon`; signals: general review; excerpt: "@benchislett Thanks for submitting the PR! This is amazing! 🚀 Left some minor comments on the style. Please check out my comments." (https://github.com/vllm-project/vllm/pull/16937#pullrequestreview-2788591348)
- `2025-04-24T13:12:53Z` `inline` by `benchislett` `vllm/model_executor/models/llama.py`:338; signals: hang; excerpt: "Ah, I thought this was referring to the other variable. Will change to a tuple." (https://github.com/vllm-project/vllm/pull/16937#discussion_r2058421682)
- `2025-04-24T21:22:26Z` `issue` by `ekagra-ranjan`; signals: h100; excerpt: "Output tokens/s on H100 BS1 cmd: VLLM USE V1=1 python examples/offline inference/eagle.py --dataset="./data/mt bench/question.jsonl" --num spec tokens 7 --max num seqs 1 --num prompts ..." (https://github.com/vllm-project/vllm/pull/16937#issuecomment-2828889840)
- `2025-04-21T20:26:14Z` `inline` by `benchislett` `vllm/model_executor/models/llama.py`:116; signals: general review; excerpt: "nit: I can probably refactor this into llama eagle3.py so there's a smaller diff to the main llama.py model file." (https://github.com/vllm-project/vllm/pull/16937#discussion_r2052955918)
- `2025-04-22T02:42:40Z` `inline` by `wwl2755` `vllm/config.py`:2355; signals: general review; excerpt: "nit: It seems the current EAGLE3 is only for llama architecture, so maybe we should document this & add an assertion to avoid users ..." (https://github.com/vllm-project/vllm/pull/16937#discussion_r2053241057)
