# PR Discussion Digest

- Source PR: [vllm-project/vllm#39917](https://github.com/vllm-project/vllm/pull/39917)
- Source page: `sources/prs/vllm/PR-39917.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-39917`
- Generated at: `2026-05-20T15:40:46.660520+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-15T15:11:21Z`
- Merged: `2026-05-07T18:24:57Z`

## Discussion Counts

- Issue comments: 23
- Review submissions: 16 (approved=1, commented=15)
- Inline review comments: 18
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=10, outdated=6
- Human participants with discussion text: Nekofish-L, TomerBN-Nvidia, aoshen02, hao-aaron, lequytra, mergify, ywang96
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2026-04-15T15:13:10Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the expert routing capture mechanism to use a GPU device cache and ... (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4114723574)
- `2026-04-16T11:33:40Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4120527433)
- `2026-04-16T11:33:57Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4120528933)
- `2026-04-16T11:34:21Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4120531014)
- `2026-04-16T11:34:39Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4120532570)
- `2026-04-28T12:05:11Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4188553969)
- `2026-04-28T12:08:10Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4188572749)
- `2026-04-28T12:09:32Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4188580569)
- `2026-04-28T12:14:21Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4188609515)
- `2026-04-28T12:35:14Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4188776187)
- `2026-04-28T12:42:36Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4188828803)
- `2026-05-01T23:17:47Z` `COMMENTED` by `lequytra` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4213776004)
- `2026-05-03T06:41:10Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4215979351)
- `2026-05-06T15:04:59Z` `COMMENTED` by `aoshen02` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4229328505)
- `2026-05-06T15:10:03Z` `COMMENTED` by `TomerBN-Nvidia` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4237304200)
- `2026-05-06T16:02:58Z` `APPROVED` by `ywang96` (https://github.com/vllm-project/vllm/pull/39917#pullrequestreview-4237710499)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`: 5 inline comment(s)
- `vllm/v1/worker/gpu_model_runner.py`: 5 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 2 inline comment(s)
- `vllm/v1/core/sched/scheduler.py`: 2 inline comment(s)
- `vllm/entrypoints/openai/completion/serving.py`: 2 inline comment(s)
- `docs/training/routed_experts_replay.md`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/runner/moe_runner.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-28T12:06:23Z` `issue` by `TomerBN-Nvidia`; signals: alignment, attention, block, cache, hang, kv cache, layout, memory; excerpt: "Could you also briefly clarify how would you support the prefix cache, like what's the design? @aoshen524 Prefix-cache support for routed-experts replay ============================================== Goal: ..." (https://github.com/vllm-project/vllm/pull/39917#issuecomment-4335045607)
- `2026-04-28T12:09:32Z` `inline` by `TomerBN-Nvidia` `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`:74; signals: block, correctness, dtype, memory, moe, perf; excerpt: "int16 is the storage dtype of the per-rank GPU device buffer; it does not participate in any NCCL collective. Routing data leaves the worker ..." (https://github.com/vllm-project/vllm/pull/39917#discussion_r3153966684)
- `2026-04-20T09:16:03Z` `issue` by `TomerBN-Nvidia`; signals: accuracy, correctness, perf, performance; excerpt: "Could you add an experiment that is about the accuracy(after trained for multi turn) compared with the baseline or the baseline + old R3 ..." (https://github.com/vllm-project/vllm/pull/39917#issuecomment-4279328473)
- `2026-04-20T13:13:50Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @TomerBN-Nvidia, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/39917#issuecomment-4281050508)
- `2026-04-27T07:20:16Z` `issue` by `TomerBN-Nvidia`; signals: bf16, memory; excerpt: "Could you share with me the experiment configuration of vllm? I want to run it. @aoshen524 It has been validated across many configurations and ..." (https://github.com/vllm-project/vllm/pull/39917#issuecomment-4324994775)
- `2026-05-06T13:25:47Z` `issue` by `TomerBN-Nvidia`; signals: cache, pipeline; excerpt: "@aoshen02 The "preempted requests will be re-prefilled from scratch" line undersells what's happening — any routing already accumulated in host cache for that req ..." (https://github.com/vllm-project/vllm/pull/39917#issuecomment-4388494388)
- `2026-05-07T06:56:53Z` `issue` by `TomerBN-Nvidia`; signals: block, moe; excerpt: "@hao-aaron thanks for catching this and posting the fallback. Pushed in 1d7860d0a — adopted your count moe layers helper covering Nemotron layers block type, ..." (https://github.com/vllm-project/vllm/pull/39917#issuecomment-4394811866)
- `2026-04-16T11:33:40Z` `inline` by `TomerBN-Nvidia` `vllm/model_executor/layers/fused_moe/layer.py`:219; signals: moe; excerpt: "Good catch on the global counter concern. In practice vLLM V1 runs one model per process, so the counter resets naturally. This matches the ..." (https://github.com/vllm-project/vllm/pull/39917#discussion_r3092862436)
- `2026-04-16T11:33:57Z` `inline` by `TomerBN-Nvidia` `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`:818; signals: moe; excerpt: "Same as the layer.py comment -- assigning IDs during bind is a sound alternative. The current approach (IDs in constructor) is simpler and matches ..." (https://github.com/vllm-project/vllm/pull/39917#discussion_r3092864068)
- `2026-04-16T11:34:21Z` `inline` by `TomerBN-Nvidia` `vllm/v1/core/sched/scheduler.py`:1393; signals: memory; excerpt: "This is a false positive. Routing data does not flow through the scheduler request object. The new data flow is: model runner - ModelRunnerOutput.routed ..." (https://github.com/vllm-project/vllm/pull/39917#discussion_r3092866162)
- `2026-04-16T11:34:38Z` `inline` by `TomerBN-Nvidia` `vllm/v1/worker/gpu_model_runner.py`:3082; signals: cache; excerpt: "Valid catch! Fixed in 3a0665d -- added host cache.free request(req id) cleanup in update states() for both finished and preempted requests. This matches the ..." (https://github.com/vllm-project/vllm/pull/39917#discussion_r3092867857)
- `2026-04-28T12:35:14Z` `inline` by `TomerBN-Nvidia` `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`:559; signals: moe; excerpt: "@aoshen524 Please let me know what do you think about this solution: If it is fine, I'll merge it to this branch." (https://github.com/vllm-project/vllm/pull/39917#discussion_r3154130294)
