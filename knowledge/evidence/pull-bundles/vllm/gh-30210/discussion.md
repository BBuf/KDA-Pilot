# PR Discussion Digest

- Source PR: [vllm-project/vllm#30210](https://github.com/vllm-project/vllm/pull/30210)
- Source page: `sources/prs/vllm/PR-30210.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-30210`
- Generated at: `2026-05-20T15:38:55.556086+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-07T14:24:25Z`
- Merged: `2025-12-09T12:20:21Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: Isotr0py, baonudesifeizhai
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-07T14:27:10Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces two fixes to enable GLM-4.6-AWQ model loading. The first fix correctly handles ... (https://github.com/vllm-project/vllm/pull/30210#pullrequestreview-3549324252)
- `2025-12-08T16:32:34Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/30210#pullrequestreview-3552964024)
- `2025-12-09T03:10:38Z` `APPROVED` by `Isotr0py` - Anyway, the wna16 fix for tp=8 fallback looks reasonable to me. (https://github.com/vllm-project/vllm/pull/30210#pullrequestreview-3555137117)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/awq_marlin.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-08T16:32:34Z` `inline` by `Isotr0py` `vllm/model_executor/layers/quantization/awq_marlin.py`:218; signals: moe; excerpt: "Can you update MoeWNA16Config.from config instead of overriding quant method?" (https://github.com/vllm-project/vllm/pull/30210#discussion_r2599301776)
- `2025-12-08T06:37:26Z` `issue` by `Isotr0py`; signals: moe; excerpt: "1. AWQ Marlin fallback compatibility: When AWQ Marlin doesn't support a MoE layer and falls back to MoeWNA16, it fails because MoeWNA16Config.from config() only ..." (https://github.com/vllm-project/vllm/pull/30210#issuecomment-3625253846)
- `2025-12-08T13:35:50Z` `issue` by `baonudesifeizhai`; signals: moe; excerpt: "on only accepts quant method as "awq" or "gptq", not "awq marlin". BTW, I wonder what's the case that AWQ Marlin can't support MoE ..." (https://github.com/vllm-project/vllm/pull/30210#issuecomment-3626983040)
- `2025-12-08T16:28:31Z` `issue` by `Isotr0py`; signals: general review; excerpt: "I see, this is because tp size=8 will cause False for intermediate size per partition % max(64, group size) == 0 (for QuantTrio/GLM-4.6-AWQ with ..." (https://github.com/vllm-project/vllm/pull/30210#issuecomment-3627858977)
