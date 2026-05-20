# PR Discussion Digest

- Source PR: [vllm-project/vllm#31406](https://github.com/vllm-project/vllm/pull/31406)
- Source page: `sources/prs/vllm/PR-31406.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-31406`
- Generated at: `2026-05-20T15:39:19.975218+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-27T09:09:03Z`
- Merged: `2026-01-05T16:00:24Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 13 (approved=1, commented=12)
- Inline review comments: 12
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: DarkLight1337, Isotr0py, NickLucche, chatgpt-codex-connector, noooop, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-12-27T09:12:29Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for encoder-only and cross-attention to the Triton attention backend. This is ... (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3614265561)
- `2025-12-28T17:35:37Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review . Without the previous gather-and-repartition step, x.view( new shape) will raise a size mismatch (or, ... (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3614768929)
- `2025-12-28T17:52:20Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new Triton kernel for memory-efficient prefill attention, which includes support for ... (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3614773848)
- `2025-12-28T17:55:30Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3614774677)
- `2025-12-29T05:29:03Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3615066210)
- `2025-12-29T05:42:36Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3615079095)
- `2025-12-29T06:26:15Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3615150421)
- `2025-12-29T09:03:44Z` `COMMENTED` by `noooop` (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3615373535)
- `2025-12-29T09:40:26Z` `COMMENTED` by `NickLucche` - can we add this backend to whisper-specific CI tests (test transcription validation whisper.py)? (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3615462442)
- `2025-12-31T03:11:23Z` `COMMENTED` by `noooop` (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3620133950)
- `2026-01-04T06:47:56Z` `COMMENTED` by `noooop` (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3624850680)
- `2026-01-04T10:26:08Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3624931244)
- `2026-01-05T08:28:22Z` `APPROVED` by `NickLucche` - @Isotr0py This is LGTM from whisper-side, both from accuracy and latency at fp16 (don't really have a comparison ... (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3625701343)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/triton_attn.py`: 8 inline comment(s)
- `vllm/attention/ops/triton_prefill_attention.py`: 3 inline comment(s)
- `tests/kernels/attention/test_triton_prefill_attention.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-31T03:11:23Z` `inline` by `noooop` `vllm/v1/attention/backends/triton_attn.py`:430; signals: attention, dtype, gemm, kernel, perf, performance, triton; excerpt: "Sure, seems that the embeddinggemma e2e test can't catch this. Let me add a kernel test for encoder-only attention backend then. The embedding model ..." (https://github.com/vllm-project/vllm/pull/31406#discussion_r2654696821)
- `2026-01-04T10:18:34Z` `issue` by `noooop`; signals: latency, perf, performance, throughput, triton; excerpt: "The performance of TRITON ATTN looks good. X-axis: Throughput (request/s) Y-axis: Latency, Time needed for one step (ms) <- logarithmic scale The curve lower ..." (https://github.com/vllm-project/vllm/pull/31406#issuecomment-3707943392)
- `2026-01-05T03:29:56Z` `issue` by `tjtanaa`; signals: latency, perf, performance, throughput, triton; excerpt: "The performance of TRITON ATTN looks good. X-axis: Throughput (request/s) Y-axis: Latency, Time needed for one step (ms) <- logarithmic scale The curve lower ..." (https://github.com/vllm-project/vllm/pull/31406#issuecomment-3708820032)
- `2025-12-29T05:42:36Z` `inline` by `Isotr0py` `vllm/v1/attention/backends/triton_attn.py`:430; signals: attention, gemm, kernel, triton; excerpt: "Sure, seems that the embeddinggemma e2e test can't catch this. Let me add a kernel test for encoder-only attention backend then." (https://github.com/vllm-project/vllm/pull/31406#discussion_r2650230608)
- `2026-01-05T08:28:22Z` `review` `APPROVED` by `NickLucche`; signals: accuracy, attention, benchmark, latency; excerpt: "@Isotr0py This is LGTM from whisper-side, both from accuracy and latency at fp16 (don't really have a comparison to run at fp32 for enc-dec ..." (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3625701343)
- `2025-12-29T06:26:15Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/triton_attn.py`:430; signals: attention, flash attention, triton; excerpt: "@Isotr0py Just a sharing, maybe it can help you with your tasks, there was once the triton flash attention as well. It was removed ..." (https://github.com/vllm-project/vllm/pull/31406#discussion_r2650281759)
- `2025-12-29T09:03:43Z` `inline` by `noooop` `vllm/v1/attention/backends/triton_attn.py`:430; signals: attention, dtype, triton; excerpt: "try modernbert VLLM CI DTYPE=float32 pytest -s -vvv tests/models/language/pooling mteb test/test gte.py::test rerank models mteb[model info0]" (https://github.com/vllm-project/vllm/pull/31406#discussion_r2650503863)
- `2026-01-04T06:47:56Z` `inline` by `noooop` `vllm/v1/attention/backends/triton_attn.py`:430; signals: attention, dtype, triton; excerpt: "- Feels like the sliding window implementation needs further investigation. pytest -s -vvv tests/models/language/pooling mteb test/test gte.py::test rerank models mteb[model info0] Model: Alibaba-NLP/gte-reranker-modernbert-base VLLM: ..." (https://github.com/vllm-project/vllm/pull/31406#discussion_r2659452407)
- `2026-01-05T07:05:55Z` `inline` by `NickLucche` `tests/kernels/attention/test_triton_prefill_attention.py`:48; signals: attention, kernel, triton; excerpt: "I think we always have a sliding window parameter in this branch" (https://github.com/vllm-project/vllm/pull/31406#discussion_r2660487800)
- `2025-12-29T05:29:03Z` `inline` by `DarkLight1337` `vllm/v1/attention/backends/triton_attn.py`:430; signals: attention, triton; excerpt: "I see that in FA implementation, there is which is not in Triton implementation. Does that need to be added?" (https://github.com/vllm-project/vllm/pull/31406#discussion_r2650218599)
- `2025-12-28T17:35:37Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: attention; excerpt: "💡 Codex Review . Without the previous gather-and-repartition step, x.view( new shape) will raise a size mismatch (or, if forced, misassign heads) on multi-GPU ..." (https://github.com/vllm-project/vllm/pull/31406#pullrequestreview-3614768929)
- `2025-12-28T17:55:30Z` `inline` by `Isotr0py` `vllm/attention/ops/triton_prefill_attention.py`:118; signals: attention, triton; excerpt: "Good bot" (https://github.com/vllm-project/vllm/pull/31406#discussion_r2649840481)
