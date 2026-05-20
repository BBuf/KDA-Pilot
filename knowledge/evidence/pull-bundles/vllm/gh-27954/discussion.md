# PR Discussion Digest

- Source PR: [vllm-project/vllm#27954](https://github.com/vllm-project/vllm/pull/27954)
- Source page: `sources/prs/vllm/PR-27954.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-27954`
- Generated at: `2026-05-20T15:38:23.820946+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-03T01:37:28Z`
- Merged: `2025-11-12T01:43:06Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 30 (approved=2, commented=28)
- Inline review comments: 29
- Review threads observed: 15
- Resolved/outdated thread markers: resolved=7, outdated=8
- Human participants with discussion text: bigPYJ1151, chatgpt-codex-connector, fadara01, jikunshang, louie-tsai, mergify
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-11-03T01:39:38Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a significant refactoring of the CPU attention backend, replacing the previous implementation ... (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3409206707)
- `2025-11-03T01:42:03Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3409208157)
- `2025-11-03T09:58:22Z` `COMMENTED` by `bigPYJ1151` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3410245767)
- `2025-11-04T06:41:34Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3414274576)
- `2025-11-04T06:54:52Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3414312184)
- `2025-11-04T07:04:17Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3414342771)
- `2025-11-04T07:19:23Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3414379351)
- `2025-11-04T07:30:23Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3414416775)
- `2025-11-04T07:32:20Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3414424483)
- `2025-11-04T07:44:18Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3414469067)
- `2025-11-04T07:52:40Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3414491609)
- `2025-11-04T08:42:22Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3414787013)
- `2025-11-04T08:49:37Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3414825838)
- `2025-11-04T13:50:00Z` `COMMENTED` by `bigPYJ1151` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3416573789)
- `2025-11-04T13:52:22Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3416585645)
- `2025-11-04T13:53:24Z` `COMMENTED` by `bigPYJ1151` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3416591566)
- `2025-11-04T13:54:17Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3416596638)
- `2025-11-04T13:55:05Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3416601496)
- `2025-11-04T14:01:48Z` `COMMENTED` by `bigPYJ1151` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3416640281)
- `2025-11-04T14:03:13Z` `COMMENTED` by `bigPYJ1151` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3416648248)
- `2025-11-04T14:03:51Z` `COMMENTED` by `bigPYJ1151` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3416651873)
- `2025-11-04T14:07:32Z` `COMMENTED` by `bigPYJ1151` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3416672138)
- `2025-11-04T14:08:49Z` `COMMENTED` by `bigPYJ1151` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3416678869)
- `2025-11-04T14:09:50Z` `COMMENTED` by `fadara01` (https://github.com/vllm-project/vllm/pull/27954#pullrequestreview-3416684021)
- ... 6 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tests/kernels/attention/test_cpu_attn.py`: 6 inline comment(s)
- `vllm/v1/attention/backends/cpu_attn.py`: 5 inline comment(s)
- `csrc/cpu/cpu_attn_impl.hpp`: 5 inline comment(s)
- `csrc/cpu/scratchpad_manager.h`: 3 inline comment(s)
- `tests/models/language/generation/test_common.py`: 3 inline comment(s)
- `vllm/platforms/cpu.py`: 3 inline comment(s)
- `csrc/cpu/cpu_attn.cpp`: 2 inline comment(s)
- `csrc/cpu/cpu_attn_macros.h`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-05T14:19:50Z` `issue` by `bigPYJ1151`; signals: attention, cache, cute, dtype, hang, memory; excerpt: "@fadara01 Tried with 2M L2 and 96 threads to generate the same task schedule, executed tests several times but got no failure. Are these ..." (https://github.com/vllm-project/vllm/pull/27954#issuecomment-3491478239)
- `2025-11-03T01:42:03Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/cpu_attn.py`:324; signals: attention, cache, kernel, kv cache; excerpt: ". However the forward path still unconditionally invokes ops.cpu attn reshape and cache(…, attn metadata.scheduler metadata) and ops.cpu attention with kv cache(…, scheduler metadata=attn ..." (https://github.com/vllm-project/vllm/pull/27954#discussion_r2485156669)
- `2025-11-04T07:44:18Z` `inline` by `fadara01` `tests/models/language/generation/test_common.py`:100; signals: attention, cache, gemm, kv cache; excerpt: "Can we enable a test for google/gemma-2-2b-it and mark it as cpu model? This would be a great end-to-end smoke test for SWA and ..." (https://github.com/vllm-project/vllm/pull/27954#discussion_r2489028818)
- `2025-11-04T14:03:13Z` `inline` by `bigPYJ1151` `tests/kernels/attention/test_cpu_attn.py`:79; signals: attention, bf16, dtype, kernel; excerpt: "This means we just test sink, alibi, softcap with bf16 as the logits processing is using fp32. For other cases all dtypes should be ..." (https://github.com/vllm-project/vllm/pull/27954#discussion_r2490649422)
- `2025-11-05T02:10:46Z` `issue` by `bigPYJ1151`; signals: attention, cache, kernel, nan; excerpt: "I got one test failure with one element miss-match while running tests/kernels/attention/test cpu attn.py on Arm This is the configuration that fails: And this ..." (https://github.com/vllm-project/vllm/pull/27954#issuecomment-3488831884)
- `2025-11-04T06:54:52Z` `inline` by `fadara01` `vllm/v1/attention/backends/cpu_attn.py`:251; signals: attention, cache, kv cache; excerpt: "When use sdpa prefill is true we use vanilla SDPA which does not support sinks. Can we dispatch to cpu attention with kv cache ..." (https://github.com/vllm-project/vllm/pull/27954#discussion_r2488921097)
- `2025-11-04T14:01:48Z` `inline` by `bigPYJ1151` `tests/kernels/attention/test_cpu_attn.py`:324; signals: attention, kernel, perf; excerpt: "This test file is based on I think the abs tolerance looks more strict in is because the input is initialized with , will ..." (https://github.com/vllm-project/vllm/pull/27954#discussion_r2490644272)
- `2025-11-04T14:45:48Z` `inline` by `fadara01` `tests/kernels/attention/test_cpu_attn.py`:324; signals: attention, flash attention, kernel; excerpt: "Acknowledged, I wasn't aware that's the tolerance used for testing flash attention." (https://github.com/vllm-project/vllm/pull/27954#discussion_r2490803105)
- `2025-11-04T06:41:33Z` `inline` by `fadara01` `csrc/cpu/cpu_attn_impl.hpp`:1341; signals: compile, hang; excerpt: "This doesn't compile on Arm because all our vec op::FP32Vec16 constructors are explicit Changing it to: vec op::FP32Vec16 curr kv pos vec(initial arange vals ..." (https://github.com/vllm-project/vllm/pull/27954#discussion_r2488893813)
- `2025-11-04T07:19:23Z` `inline` by `fadara01` `csrc/cpu/scratchpad_manager.h`:1; signals: attention, hang; excerpt: "Can we leave oneDNN changes out? This PR is already too big and I don't think these changes are relevant the new attention backend?" (https://github.com/vllm-project/vllm/pull/27954#discussion_r2488966907)
- `2025-11-04T08:34:51Z` `issue` by `fadara01`; signals: benchmark, perf, regression; excerpt: "I can also confirm that there's no perf regressions on Arm after running this benchmark:" (https://github.com/vllm-project/vllm/pull/27954#issuecomment-3484578640)
- `2025-11-04T07:30:23Z` `inline` by `fadara01` `tests/kernels/attention/test_cpu_attn.py`:324; signals: attention, kernel; excerpt: "the absolute tolerance looks too high. can we use: similar to what we do in" (https://github.com/vllm-project/vllm/pull/27954#discussion_r2488994028)
