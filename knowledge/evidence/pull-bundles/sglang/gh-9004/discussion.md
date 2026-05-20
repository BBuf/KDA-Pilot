# PR Discussion Digest

- Source PR: [sgl-project/sglang#9004](https://github.com/sgl-project/sglang/pull/9004)
- Source page: `sources/prs/sglang/PR-9004.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-9004`
- Generated at: `2026-05-20T15:31:30.303844+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-09T12:48:08Z`
- Merged: `2025-08-23T07:38:40Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 5 (commented=5)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: ch-wan, fzyzcjy, yiakwy-xpu-ml-framework-team, zhyncs
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-09T12:48:25Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @fzyzcjy, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/9004#pullrequestreview-3102947522)
- `2025-08-09T12:52:46Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new, higher-precision backend for FlashInfer MXFP4 MoE, enable flashinfer mxfp4 bf16 ... (https://github.com/sgl-project/sglang/pull/9004#pullrequestreview-3102948582)
- `2025-08-09T20:52:29Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/9004#pullrequestreview-3103256006)
- `2025-08-10T01:48:22Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/9004#pullrequestreview-3103438652)
- `2025-08-13T03:27:56Z` `COMMENTED` by `yiakwy-xpu-ml-framework-team` (https://github.com/sgl-project/sglang/pull/9004#pullrequestreview-3113823506)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/mxfp4.py`: 2 inline comment(s)
- `python/sglang/srt/server_args.py`: 2 inline comment(s)
- `python/sglang/srt/managers/schedule_batch.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-13T07:58:04Z` `issue` by `yiakwy-xpu-ml-framework-team`; signals: attention, bf16, fp4, h100, mxfp4, throughput; excerpt: "@fzyzcjy Note since gpt-oss bf16 120b sft model quantized to mxfp4 with only 61 GB size, you can simply run it in a single ..." (https://github.com/sgl-project/sglang/pull/9004#issuecomment-3182635772)
- `2025-08-13T03:27:49Z` `inline` by `yiakwy-xpu-ml-framework-team` `python/sglang/srt/layers/quantization/mxfp4.py`:573; signals: block, fp4, fp8, hopper, mxfp4; excerpt: "I am working on block-wise fp8 quantization from mxfp4, and the intuition is that since PTQ mxfp4 (32-groups with E8M0 scalar) passed the acceptance, ..." (https://github.com/sgl-project/sglang/pull/9004#discussion_r2271979871)
- `2025-08-10T01:48:22Z` `inline` by `ch-wan` `python/sglang/srt/managers/schedule_batch.py`:112; signals: flashinfer, fp4, moe, mxfp4; excerpt: "Can we use a different arg name like flashinfer mxfp4 moe config? It's more clear and extensible." (https://github.com/sgl-project/sglang/pull/9004#discussion_r2265079070)
- `2025-08-13T07:16:38Z` `issue` by `yiakwy-xpu-ml-framework-team`; signals: bf16, fp4, mxfp4; excerpt: "@fzyzcjy I am using gpt-oss 120b MXFP4 (sft from bf16 gpt-oss-120b TP8), my bench data is 402.55 toks/s (are you talking about total token/sec ..." (https://github.com/sgl-project/sglang/pull/9004#issuecomment-3182471482)
- `2025-08-16T01:52:55Z` `issue` by `fzyzcjy`; signals: bf16; excerpt: "done rewritten to use latest main, and tests: gpqa low gpqa mid speed bs64 ------- -------- -------- ---------- default 57.0 66.0 10509 bf16 57.2 ..." (https://github.com/sgl-project/sglang/pull/9004#issuecomment-3193138372)
