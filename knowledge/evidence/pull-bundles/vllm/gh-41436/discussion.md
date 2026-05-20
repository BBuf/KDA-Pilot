# PR Discussion Digest

- Source PR: [vllm-project/vllm#41436](https://github.com/vllm-project/vllm/pull/41436)
- Source page: `sources/prs/vllm/PR-41436.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-41436`
- Generated at: `2026-05-20T15:40:53.630293+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-01T01:04:46Z`
- Merged: `2026-05-18T17:46:13Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: BowenBao, claude, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-01T01:08:22Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors and extends ROCm MXFP4 MoE support by introducing specialized AITER backends for ... (https://github.com/vllm-project/vllm/pull/41436#pullrequestreview-4209430235)
- `2026-05-05T22:34:18Z` `COMMENTED` by `claude` - Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer ... (https://github.com/vllm-project/vllm/pull/41436#pullrequestreview-4232018458)
- `2026-05-13T18:42:40Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/41436#pullrequestreview-4284296372)
- `2026-05-13T21:16:32Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/41436#pullrequestreview-4285415794)
- `2026-05-13T21:21:21Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/41436#pullrequestreview-4285446674)
- `2026-05-18T17:46:06Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/41436#pullrequestreview-4312405041)

## Inline Comment Hotspots

- `tests/kernels/moe/test_ocp_mx_moe.py`: 2 inline comment(s)
- `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-13T21:16:31Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:267; signals: cuda, fp4, moe, mxfp4, perf, regression; excerpt: "yes this is by design. I feel making it an opt-in option helps avoid confusion and silent perf regression. I updated the error message ..." (https://github.com/vllm-project/vllm/pull/41436#discussion_r3237495909)
- `2026-05-13T21:21:21Z` `inline` by `BowenBao` `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml`:12; signals: fp4, moe, mxfp4; excerpt: "I'll add --moe-backend aiter now that your PR landed. Probably still need VLLM ROCM USE AITER: "1" as a master envar, there are likely ..." (https://github.com/vllm-project/vllm/pull/41436#discussion_r3237523050)
- `2026-05-13T18:18:54Z` `inline` by `mgoin` `tests/evals/gsm8k/configs/Qwen3.5-35B-A3B-MXFP4-AITER-TP2.yaml`:12; signals: fp4, moe, mxfp4; excerpt: "Can you set the --moe-backend aiter instead? Why not add that functionality?" (https://github.com/vllm-project/vllm/pull/41436#discussion_r3236524550)
- `2026-05-13T18:36:53Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:267; signals: fp4, moe, mxfp4; excerpt: "Did you mean to remove emulation?" (https://github.com/vllm-project/vllm/pull/41436#discussion_r3236626437)
- `2026-05-05T22:34:18Z` `review` `COMMENTED` by `claude`; signals: general review; excerpt: "Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer can comment @claude review to run ..." (https://github.com/vllm-project/vllm/pull/41436#pullrequestreview-4232018458)
- `2026-05-13T22:11:11Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @BowenBao." (https://github.com/vllm-project/vllm/pull/41436#issuecomment-4445595492)
