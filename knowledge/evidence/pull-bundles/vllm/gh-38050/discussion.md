# PR Discussion Digest

- Source PR: [vllm-project/vllm#38050](https://github.com/vllm-project/vllm/pull/38050)
- Source page: `sources/prs/vllm/PR-38050.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38050`
- Generated at: `2026-05-20T15:40:26.413267+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-25T01:23:50Z`
- Merged: `2026-03-25T17:16:41Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: WoosukKwon, mergify, mgoin, zyongye
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-03-25T01:30:09Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new batched Mixture-of-Experts (MoE) implementation using FlashInfer's CuteDSL kernels, named FlashInferCuteDSLBatchedExperts. ... (https://github.com/vllm-project/vllm/pull/38050#pullrequestreview-4003382572)
- `2026-03-25T17:16:25Z` `APPROVED` by `WoosukKwon` - Thanks! (https://github.com/vllm-project/vllm/pull/38050#pullrequestreview-4008413659)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_batched_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-25T17:00:50Z` `issue` by `zyongye`; signals: cute, deepgemm, flashinfer, gemm, moe; excerpt: "Why did the original cutedsl moe get removed? It's not removed. It is moved to flashinfer cutedsl batched moe and we auto select between ..." (https://github.com/vllm-project/vllm/pull/38050#issuecomment-4128227625)
- `2026-03-25T01:46:23Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @zyongye, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/38050#issuecomment-4122576404)
- `2026-03-25T08:25:40Z` `issue` by `mgoin`; signals: cute, moe; excerpt: "Why did the original cutedsl moe get removed?" (https://github.com/vllm-project/vllm/pull/38050#issuecomment-4124656494)
- `2026-03-25T01:24:34Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @zyongye." (https://github.com/vllm-project/vllm/pull/38050#issuecomment-4122509419)
