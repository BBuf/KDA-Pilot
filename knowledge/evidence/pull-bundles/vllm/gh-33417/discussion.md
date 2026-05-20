# PR Discussion Digest

- Source PR: [vllm-project/vllm#33417](https://github.com/vllm-project/vllm/pull/33417)
- Source page: `sources/prs/vllm/PR-33417.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-33417`
- Generated at: `2026-05-20T15:39:37.038089+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-30T12:55:32Z`
- Merged: `2026-01-31T22:06:42Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 6
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=4, outdated=6
- Human participants with discussion text: copilot-pull-request-reviewer, geraldstanje, kaigouthro, mergify, mgoin, renehonig, rnik12, shahizat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2026-01-30T13:02:58Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview This PR aims to fix a bug where NVFP4 MoE kernels fail on RTX Blackwell ... (https://github.com/vllm-project/vllm/pull/33417#pullrequestreview-3728165087)
- `2026-01-30T13:09:00Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a wide range of changes. The primary change, as indicated by the ... (https://github.com/vllm-project/vllm/pull/33417#pullrequestreview-3728187112)
- `2026-01-30T13:38:11Z` `COMMENTED` by `copilot-pull-request-reviewer` - Copilot encountered an error and was unable to review this pull request. You can try again by re-requesting ... (https://github.com/vllm-project/vllm/pull/33417#pullrequestreview-3728377908)
- `2026-01-30T17:41:14Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/33417#pullrequestreview-3729573280)
- `2026-01-31T01:26:00Z` `APPROVED` by `mgoin` - Thanks! (https://github.com/vllm-project/vllm/pull/33417#pullrequestreview-3731244855)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`: 1 inline comment(s)
- `vllm/transformers_utils/configs/__init__.py`: 1 inline comment(s)
- `vllm/model_executor/models/kimi_k25.py`: 1 inline comment(s)
- `vllm/entrypoints/chat_utils.py`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/flashinfer_cutedsl_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-30T13:02:58Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: attention, blackwell, cuda, cute, cutlass, flashinfer, fp4, hang; excerpt: "Pull request overview This PR aims to fix a bug where NVFP4 MoE kernels fail on RTX Blackwell GPUs (SM12.0) by adding device capability ..." (https://github.com/vllm-project/vllm/pull/33417#pullrequestreview-3728165087)
- `2026-01-30T13:02:56Z` `inline` by `copilot-pull-request-reviewer` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`:99; signals: blackwell, cutlass, flashinfer, fp4, hang, kernel, moe, nvfp4; excerpt: "This PR has a significant discrepancy between its title/description and the actual changes. The title states "fix: Add SM120 (RTX Blackwell) support for NVFP4 ..." (https://github.com/vllm-project/vllm/pull/33417#discussion_r2746166698)
- `2026-01-30T15:01:44Z` `issue` by `mgoin`; signals: cutlass, flashinfer, fp4, moe, nvfp4, sm120; excerpt: "Why can't you use the vLLM CUTLASS moe for nvfp4? That was added for SM120 support. I'm not sure if all of these flashinfer ..." (https://github.com/vllm-project/vllm/pull/33417#issuecomment-3824203565)
- `2026-01-30T18:53:57Z` `issue` by `renehonig`; signals: cutlass, flashinfer, hang, kernel, moe, sm120; excerpt: "From my local testing it seems like the only kernel that should be expanded in support is flashinfer cutlass moe, however I found this ..." (https://github.com/vllm-project/vllm/pull/33417#issuecomment-3825174254)
- `2026-01-30T17:41:52Z` `issue` by `mgoin`; signals: cutlass, flashinfer, kernel, moe, sm120; excerpt: "From my local testing it seems like the only kernel that should be expanded in support is flashinfer cutlass moe, however I found this ..." (https://github.com/vllm-project/vllm/pull/33417#issuecomment-3824893413)
- `2026-01-30T19:00:11Z` `issue` by `mgoin`; signals: autotune, block, cutlass, hang, kernel; excerpt: "@renehonig Yes it turns out the autotuner errors are not actually blocking startup, still it will be confusing for users. We can allow it ..." (https://github.com/vllm-project/vllm/pull/33417#issuecomment-3825198854)
- `2026-01-30T17:38:35Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/flashinfer_cutedsl_moe.py`:59; signals: cute, flashinfer, moe, sm100; excerpt: "Looking at flashinfer source for this function, I only see a SM100 implementation" (https://github.com/vllm-project/vllm/pull/33417#discussion_r2747309076)
- `2026-01-30T17:34:32Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`:36; signals: flashinfer, moe; excerpt: "When I tested this I get" (https://github.com/vllm-project/vllm/pull/33417#discussion_r2747294720)
- `2026-01-30T13:13:27Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @renehonig, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/33417#issuecomment-3823686316)
- `2026-01-30T13:38:11Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: general review; excerpt: "Copilot encountered an error and was unable to review this pull request. You can try again by re-requesting a review." (https://github.com/vllm-project/vllm/pull/33417#pullrequestreview-3728377908)
- `2026-01-30T19:24:09Z` `issue` by `renehonig`; signals: hang; excerpt: "@mgoin many thanks again, I have incorporated your changes." (https://github.com/vllm-project/vllm/pull/33417#issuecomment-3825336472)
- `2026-01-30T13:02:57Z` `inline` by `copilot-pull-request-reviewer` `vllm/transformers_utils/configs/__init__.py`:86; signals: general review; excerpt: "The name 'KimiK25Config' is exported by all but is not defined." (https://github.com/vllm-project/vllm/pull/33417#discussion_r2746166737)
