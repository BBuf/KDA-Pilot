# PR Discussion Digest

- Source PR: [vllm-project/vllm#28775](https://github.com/vllm-project/vllm/pull/28775)
- Source page: `sources/prs/vllm/PR-28775.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28775`
- Generated at: `2026-05-20T15:38:33.735220+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-15T06:24:57Z`
- Merged: `2025-12-30T16:11:39Z`

## Discussion Counts

- Issue comments: 27
- Review submissions: 13 (approved=1, commented=12)
- Inline review comments: 20
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=5, outdated=14
- Human participants with discussion text: AndreasKaratzas, DarkLight1337, LucasWilkinson, chatgpt-codex-connector, mergify, yt0428
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-11-15T06:27:11Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for the openPangu Pro Moe v2 model, which introduces a new ... (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3467783074)
- `2025-11-15T06:27:36Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3467783170)
- `2025-12-10T04:31:40Z` `COMMENTED` by `LucasWilkinson` - Thanks for the diagram that helps! First round of comments cc @heheda12345 and @NickLucche I tagged you two ... (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3559664367)
- `2025-12-10T06:17:42Z` `COMMENTED` by `yt0428` (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3560913030)
- `2025-12-10T06:30:09Z` `COMMENTED` by `yt0428` (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3560955790)
- `2025-12-10T06:43:05Z` `COMMENTED` by `yt0428` (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3560992502)
- `2025-12-10T06:45:57Z` `COMMENTED` by `yt0428` (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3560999230)
- `2025-12-16T06:22:29Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3581501485)
- `2025-12-16T06:23:00Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3581502566)
- `2025-12-17T18:28:27Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3589083116)
- `2025-12-18T01:24:04Z` `COMMENTED` by `yt0428` (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3590294371)
- `2025-12-19T16:14:11Z` `COMMENTED` by `LucasWilkinson` - @yt0428 sorry for all the back and forth and thanks for all the clean-up! this is looking much ... (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3599171733)
- `2025-12-24T22:24:38Z` `APPROVED` by `LucasWilkinson` - LGTM; thanks for the back and forth! (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3611639896)

## Inline Comment Hotspots

- `vllm/v1/worker/gpu_model_runner.py`: 6 inline comment(s)
- `vllm/v1/attention/backends/flash_diffkv_attn.py`: 4 inline comment(s)
- `vllm/model_executor/models/openpangu.py`: 2 inline comment(s)
- `vllm/v1/attention/backends/flash_sink_attn.py`: 2 inline comment(s)
- `vllm/v1/core/sched/scheduler.py`: 2 inline comment(s)
- `vllm/attention/layer.py`: 1 inline comment(s)
- `vllm/v1/kv_cache_interface.py`: 1 inline comment(s)
- `vllm/v1/worker/gpu_input_batch.py`: 1 inline comment(s)
- `vllm/v1/worker/kv_connector_model_runner_mixin.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-15T06:27:36Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/flash_sink_attn.py`:694; signals: attention, block, cache, cute, fp8, kv cache; excerpt: "![P0 Badge]( Define cached KV buffers for decode paths without new keys Inside FlashSinkAttentionImpl.forward the variables key cache, value cache, and num sink blocks ..." (https://github.com/vllm-project/vllm/pull/28775#discussion_r2529645826)
- `2025-12-13T10:39:46Z` `issue` by `yt0428`; signals: attention, block, cache, kv cache, layout, perf; excerpt: "@LucasWilkinson Hello, I have refactored the code by: Remove the FLASH DIFFKV ATTN backend, instead, FLASH ATTN backend is extended to support the different ..." (https://github.com/vllm-project/vllm/pull/28775#issuecomment-3649200767)
- `2025-12-16T06:22:29Z` `inline` by `LucasWilkinson` `vllm/v1/worker/gpu_model_runner.py`:5214; signals: attention, block, cache, kernel, kv cache; excerpt: "I wonder if it would be cleaner to just move get kv cache shape to the AttentionMetadataBuilder since that would be naturally aware of ..." (https://github.com/vllm-project/vllm/pull/28775#discussion_r2621950010)
- `2025-12-10T06:43:05Z` `inline` by `yt0428` `vllm/v1/attention/backends/flash_diffkv_attn.py`; signals: attention, cache, kv cache; excerpt: "I think we can upgrade the get kv cache shape function to receive an additional args head size v, which equals head size by ..." (https://github.com/vllm-project/vllm/pull/28775#discussion_r2605403080)
- `2025-12-19T16:14:11Z` `review` `COMMENTED` by `LucasWilkinson`; signals: attention, block; excerpt: "@yt0428 sorry for all the back and forth and thanks for all the clean-up! this is looking much better! lets do for now to ..." (https://github.com/vllm-project/vllm/pull/28775#pullrequestreview-3599171733)
- `2025-12-10T04:19:38Z` `inline` by `LucasWilkinson` `vllm/v1/kv_cache_interface.py`:162; signals: attention, cache; excerpt: "I think we can simplify this by just adding head size v with it defaulting to head size v = head size to FullAttentionSpec ..." (https://github.com/vllm-project/vllm/pull/28775#discussion_r2605134466)
- `2025-12-10T04:29:18Z` `inline` by `LucasWilkinson` `vllm/v1/worker/gpu_model_runner.py`:5312; signals: attention, cache; excerpt: "nit: similar to we should move this into a AttentionWithStaticSink layer; I think then you can just populate it on the first model pass ..." (https://github.com/vllm-project/vllm/pull/28775#discussion_r2605148422)
- `2025-12-17T18:28:26Z` `inline` by `LucasWilkinson` `vllm/v1/worker/gpu_model_runner.py`:5214; signals: attention, mla; excerpt: "If this is too messy to do know I think we can make a FlashAttentionDiffKVBackend subclass of FlashAttentionBackend that just assumes 192/128 (is that ..." (https://github.com/vllm-project/vllm/pull/28775#discussion_r2628164449)
- `2025-12-18T01:24:04Z` `inline` by `yt0428` `vllm/v1/worker/gpu_model_runner.py`:5214; signals: cache, kv cache; excerpt: "Do you mean something like this: This way we don't have to modify get kv cache shape interface anymore." (https://github.com/vllm-project/vllm/pull/28775#discussion_r2629160143)
- `2025-12-13T07:52:26Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @yt0428, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/28775#issuecomment-3649089976)
- `2025-12-13T08:29:56Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @yt0428, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/28775#issuecomment-3649113439)
- `2025-12-17T02:45:18Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @yt0428, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/28775#issuecomment-3663390320)
