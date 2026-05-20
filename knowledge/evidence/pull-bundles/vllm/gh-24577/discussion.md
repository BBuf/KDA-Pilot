# PR Discussion Digest

- Source PR: [vllm-project/vllm#24577](https://github.com/vllm-project/vllm/pull/24577)
- Source page: `sources/prs/vllm/PR-24577.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-24577`
- Generated at: `2026-05-20T15:37:47.157081+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-10T10:55:50Z`
- Merged: `2025-09-10T19:33:41Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: elvischenv, mgoin
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-10T10:57:09Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables FP8 KV cache for the FlashInfer backend on non-sm100 GPUs. The changes ... (https://github.com/vllm-project/vllm/pull/24577#pullrequestreview-3205609292)
- `2025-09-10T15:58:09Z` `APPROVED` by `mgoin` - LGTM, thanks! Validated locally on sm89 (L40s) for eval and perf on gsm8k. Perhaps we should default to ... (https://github.com/vllm-project/vllm/pull/24577#pullrequestreview-3206826000)

## Inline Comment Hotspots

- `vllm/platforms/cuda.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-10T15:58:09Z` `review` `APPROVED` by `mgoin`; signals: cache, flashinfer, fp8, kv cache, perf, sm90; excerpt: "LGTM, thanks! Validated locally on sm89 (L40s) for eval and perf on gsm8k. Perhaps we should default to flashinfer for non-sm90 if it is ..." (https://github.com/vllm-project/vllm/pull/24577#pullrequestreview-3206826000)
- `2025-09-10T18:08:59Z` `issue` by `mgoin`; signals: attention, cache, flashinfer, fp8, kv cache; excerpt: "It has been the case for a while that attention backends that only do FP8 kv cache storage, like xformers, are compatible for hardware ..." (https://github.com/vllm-project/vllm/pull/24577#issuecomment-3276006875)
- `2025-09-10T17:32:48Z` `issue` by `mgoin`; signals: cache, fp8, kv cache; excerpt: "@elvischenv Here are my results on A100 with FP8 KV Cache, it seems to work fine for kv cache compression. See the available concurrency ..." (https://github.com/vllm-project/vllm/pull/24577#issuecomment-3275887615)
- `2025-09-10T18:07:32Z` `issue` by `elvischenv`; signals: attention, dtype, fp8; excerpt: "@gau-nernst Thanks for reporting the issue. For the support of query quantization, I have created a more general fix 24600. It will first try ..." (https://github.com/vllm-project/vllm/pull/24577#issuecomment-3276002716)
- `2025-09-10T16:20:11Z` `issue` by `elvischenv`; signals: cache, fp8, kv cache; excerpt: "Ampere does not support FP8 kv cache. only sm =89 supported." (https://github.com/vllm-project/vllm/pull/24577#issuecomment-3275652731)
- `2025-09-10T17:47:38Z` `issue` by `elvischenv`; signals: fp8; excerpt: "@mgoin First to know that. I just think Ampere is not supported FP8 compute natively. Also there is a thread discussing that:" (https://github.com/vllm-project/vllm/pull/24577#issuecomment-3275944839)
