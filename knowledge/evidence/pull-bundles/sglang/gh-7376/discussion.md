# PR Discussion Digest

- Source PR: [sgl-project/sglang#7376](https://github.com/sgl-project/sglang/pull/7376)
- Source page: `sources/prs/sglang/PR-7376.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7376`
- Generated at: `2026-05-20T15:31:11.554916+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-20T04:55:48Z`
- Merged: `2025-06-24T04:38:07Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 7
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=1, outdated=3
- Human participants with discussion text: Alcanderian, jonahbernard, pyc96, zhyncs
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-06-20T04:56:09Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @pyc96, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7376#pullrequestreview-2944557741)
- `2025-06-20T04:56:46Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request aims to fix an issue with MTP (Multi-Path Transformer) in Deepseek R1 Fp4 ... (https://github.com/sgl-project/sglang/pull/7376#pullrequestreview-2944558381)
- `2025-06-21T11:51:24Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7376#pullrequestreview-2947745333)
- `2025-06-24T04:37:53Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/7376#pullrequestreview-2952145284)

## Inline Comment Hotspots

- `python/sglang/srt/model_loader/loader.py`: 3 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-21T18:13:28Z` `issue` by `pyc96`; signals: fp4, perf, performance, regression; excerpt: "How can we reproduce the gsm8k acc from to [here]( Ummm, I am not able to reproduce it either. I verified the performance of ..." (https://github.com/sgl-project/sglang/pull/7376#issuecomment-2993705498)
- `2025-06-21T18:15:48Z` `issue` by `Alcanderian`; signals: fp4, perf, performance, regression; excerpt: "How can we reproduce the gsm8k acc from to [here]( Ummm, I am not able to reproduce it either. I verified the performance of ..." (https://github.com/sgl-project/sglang/pull/7376#issuecomment-2993706408)
- `2025-06-22T22:50:47Z` `issue` by `pyc96`; signals: throughput; excerpt: "Bs=1 Output throughput: 146.233 token/s" (https://github.com/sgl-project/sglang/pull/7376#issuecomment-2994502136)
- `2025-06-21T11:51:24Z` `inline` by `Alcanderian` `python/sglang/srt/model_loader/loader.py`:161; signals: general review; excerpt: "It is better to move it into DeepseekV2ForCausalLM:: init after applying this" (https://github.com/sgl-project/sglang/pull/7376#discussion_r2160016616)
