# PR Discussion Digest

- Source PR: [vllm-project/vllm#30116](https://github.com/vllm-project/vllm/pull/30116)
- Source page: `sources/prs/vllm/PR-30116.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-30116`
- Generated at: `2026-05-20T15:38:53.431833+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-05T06:58:48Z`
- Merged: `2025-12-09T05:30:06Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Isotr0py, a4lg
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-05T07:00:45Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request introduces a mechanism to handle 'sideloaded' parameters, particularly for MoE expert weights in ... (https://github.com/vllm-project/vllm/pull/30116#pullrequestreview-3543368755)
- `2025-12-09T02:37:43Z` `APPROVED` by `Isotr0py` - Anyway, let's get this PR merged first (https://github.com/vllm-project/vllm/pull/30116#pullrequestreview-3555036204)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-12-06T00:34:15Z` `issue` by `a4lg`; signals: hang, memory, moe; excerpt: "@Isotr0py I see, so 27772 broke the existing Qwen3-MoE GGUF support, right? Including Qwen3-MoE, yes ("Failed to map GGUF parameters" error). But considering 30118, ..." (https://github.com/vllm-project/vllm/pull/30116#issuecomment-3619057933)
- `2025-12-07T03:51:30Z` `issue` by `a4lg`; signals: hang, moe; excerpt: "I restored remote access to my dev machine (although I don't want to run vllm serve remotely) and that's the full diff on my ..." (https://github.com/vllm-project/vllm/pull/30116#issuecomment-3621563193)
- `2025-12-09T00:43:12Z` `issue` by `a4lg`; signals: hang, moe; excerpt: "Okay I'm back. For now, this change would be effective only on Qwen-MoE architectures since HF Transformers doesn't support DeepSeek + GGUF integration (so ..." (https://github.com/vllm-project/vllm/pull/30116#issuecomment-3629680394)
- `2025-12-06T12:32:45Z` `issue` by `a4lg`; signals: moe; excerpt: "Ah, I just remembered! For Qwen2-MoE models, I needed two additional modifications. - Correct Qwen2MoeModel.embed tokens initialization. - Conversion from (n) 1D tensor to ..." (https://github.com/vllm-project/vllm/pull/30116#issuecomment-3620135997)
- `2025-12-09T02:15:17Z` `issue` by `a4lg`; signals: moe; excerpt: "And I checked that the latter part of my git stash diff was indeed necessary. In Qwen2-MoE GGUF models, shared expert weight (GGUF: blk.{id}.ffn ..." (https://github.com/vllm-project/vllm/pull/30116#issuecomment-3629897673)
- `2025-12-05T16:41:23Z` `issue` by `Isotr0py`; signals: moe; excerpt: "I see, so broke the existing Qwen3-MoE GGUF support, right?" (https://github.com/vllm-project/vllm/pull/30116#issuecomment-3617662146)
- `2025-12-06T13:59:13Z` `issue` by `Isotr0py`; signals: general review; excerpt: "Conversion from (n) 1D tensor to (1,n) 2D tensor on certain weights. Hmmm, which weights need this reshape? I just checked" (https://github.com/vllm-project/vllm/pull/30116#issuecomment-3620429245)
