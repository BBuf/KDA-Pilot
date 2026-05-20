# PR Discussion Digest

- Source PR: [vllm-project/vllm#36307](https://github.com/vllm-project/vllm/pull/36307)
- Source page: `sources/prs/vllm/PR-36307.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36307`
- Generated at: `2026-05-20T15:40:10.777358+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-07T04:23:53Z`
- Merged: `2026-03-12T14:32:32Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: mergify, mgoin, wzhao18
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2026-03-07T04:25:54Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a modular FP8 MoE kernel for the TRTLLM backend, which is a ... (https://github.com/vllm-project/vllm/pull/36307#pullrequestreview-3907318510)
- `2026-03-07T04:28:32Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/36307#pullrequestreview-3907324218)
- `2026-03-10T22:57:24Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/36307#pullrequestreview-3925921893)
- `2026-03-12T10:04:02Z` `APPROVED` by `mgoin` - LGTM as an interim step then, thanks! (https://github.com/vllm-project/vllm/pull/36307#pullrequestreview-3935325230)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`: 8 inline comment(s)

## High-Signal Discussion

- `2026-03-07T04:28:31Z` `inline` by `wzhao18` `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`:199; signals: fp4, fp8, kernel, moe, nvfp4; excerpt: "routing method type is not actually used by the kernel in the routed case. Setting to 1 will work. This is done in the ..." (https://github.com/vllm-project/vllm/pull/36307#discussion_r2898936804)
- `2026-03-10T18:59:03Z` `issue` by `mgoin`; signals: accuracy, dtype, hang, moe; excerpt: "Note: to get Minimax to run with trtllm moe, it is required to set minimax's [router logits dtype]( to bfloat16, as trtllm backend only ..." (https://github.com/vllm-project/vllm/pull/36307#issuecomment-4033735513)
- `2026-03-12T10:02:39Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`:186; signals: fp8, moe; excerpt: "Could we fuse this from the activation quant before? This could be quite slow. Worth considering when fixing the output issue" (https://github.com/vllm-project/vllm/pull/36307#discussion_r2923524567)
- `2026-03-10T22:57:24Z` `inline` by `wzhao18` `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`:186; signals: fp8, moe; excerpt: "fixed." (https://github.com/vllm-project/vllm/pull/36307#discussion_r2914941767)
- `2026-03-12T10:03:05Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`:199; signals: fp8, moe; excerpt: "Can you note that this is ignored in this case?" (https://github.com/vllm-project/vllm/pull/36307#discussion_r2923526646)
- `2026-03-10T17:58:58Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @wzhao18, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/36307#issuecomment-4033386436)
- `2026-03-10T18:03:58Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @wzhao18, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/36307#issuecomment-4033414009)
- `2026-03-10T19:36:55Z` `issue` by `wzhao18`; signals: dtype, hang; excerpt: "@mgoin I did not actually change the router logits dtype for Minimax in the PR. I only changed it locally for testing as the ..." (https://github.com/vllm-project/vllm/pull/36307#issuecomment-4033954007)
- `2026-03-10T06:20:39Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @wzhao18." (https://github.com/vllm-project/vllm/pull/36307#issuecomment-4028989602)
