# PR Discussion Digest

- Source PR: [vllm-project/vllm#23045](https://github.com/vllm-project/vllm/pull/23045)
- Source page: `sources/prs/vllm/PR-23045.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23045`
- Generated at: `2026-05-20T15:37:16.404384+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-17T04:52:38Z`
- Merged: `2025-08-20T14:35:26Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 7
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: ElizaWszola, mgoin, shixianc, yewentao256
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-17T04:54:03Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request integrates CUDA permute/unpermute kernels for MoE FP8 operations, aiming to improve performance. The ... (https://github.com/vllm-project/vllm/pull/23045#pullrequestreview-3126192188)
- `2025-08-17T13:17:00Z` `COMMENTED` by `yewentao256` - Thanks for the work! Please also fix as Gemini suggests, DCO and pre-commit issue. (https://github.com/vllm-project/vllm/pull/23045#pullrequestreview-3126335764)
- `2025-08-17T17:09:17Z` `COMMENTED` by `shixianc` (https://github.com/vllm-project/vllm/pull/23045#pullrequestreview-3126408881)
- `2025-08-19T06:45:05Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/23045#pullrequestreview-3130945047)
- `2025-08-19T15:06:35Z` `COMMENTED` by `shixianc` (https://github.com/vllm-project/vllm/pull/23045#pullrequestreview-3132762856)
- `2025-08-20T14:34:38Z` `APPROVED` by `mgoin` - Great work, thank you! (https://github.com/vllm-project/vllm/pull/23045#pullrequestreview-3136928737)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/cutlass_moe.py`: 2 inline comment(s)
- `csrc/quantization/cutlass_w8a8/moe/get_group_starts.cuh`: 2 inline comment(s)
- `csrc/torch_bindings.cpp`: 2 inline comment(s)
- `csrc/moe/moe_permute_unpermute_op.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-19T15:08:19Z` `issue` by `shixianc`; signals: block, cuda, cutlass, fp8, kernel, moe, speedup, triton; excerpt: "Nice work, I really like the speedups! Regarding the failed fused moe tests, did you manually inspect the ground truth vs. CUTLASS MoE outputs ..." (https://github.com/vllm-project/vllm/pull/23045#issuecomment-3201149478)
- `2025-08-19T02:17:13Z` `issue` by `shixianc`; signals: block, cuda, fp8, kernel, moe; excerpt: "@mgoin @yewentao256 Thanks for the quick review! Addressed all comments and attached quality test in the description. The only issue in unittest is 33 ..." (https://github.com/vllm-project/vllm/pull/23045#issuecomment-3198988655)
- `2025-08-17T17:09:16Z` `inline` by `shixianc` `csrc/quantization/cutlass_w8a8/moe/get_group_starts.cuh`:37; signals: cutlass, kernel, moe, overflow; excerpt: "Added to this file and also caller. This is mainly to avoid large M K overflows, and the new kernel generates int64 expert offsets ..." (https://github.com/vllm-project/vllm/pull/23045#discussion_r2280953796)
- `2025-08-17T13:12:15Z` `inline` by `yewentao256` `csrc/quantization/cutlass_w8a8/moe/get_group_starts.cuh`:37; signals: cutlass, hang, moe; excerpt: "If change to int64, please add a comment to clarify" (https://github.com/vllm-project/vllm/pull/23045#discussion_r2280875635)
- `2025-08-17T17:41:38Z` `issue` by `shixianc`; signals: block, fp8, moe; excerpt: "@mgoin @yewentao256 Thanks for the quick review! Addressed all comments and attached quality test in the description. The only issue in unittest is 33 ..." (https://github.com/vllm-project/vllm/pull/23045#issuecomment-3194545492)
- `2025-08-19T06:48:41Z` `issue` by `ElizaWszola`; signals: cutlass, moe, speedup; excerpt: "Nice work, I really like the speedups! Regarding the failed fused moe tests, did you manually inspect the ground truth vs. CUTLASS MoE outputs ..." (https://github.com/vllm-project/vllm/pull/23045#issuecomment-3199453290)
- `2025-08-17T13:17:00Z` `review` `COMMENTED` by `yewentao256`; signals: general review; excerpt: "Thanks for the work! Please also fix as Gemini suggests, DCO and pre-commit issue." (https://github.com/vllm-project/vllm/pull/23045#pullrequestreview-3126335764)
- `2025-08-17T14:37:30Z` `issue` by `mgoin`; signals: accuracy; excerpt: "Excellent analysis and work! We were just talking about unreverting Eliza's work this week, so this is timely. I didn't see the accuracy evals ..." (https://github.com/vllm-project/vllm/pull/23045#issuecomment-3194428736)
- `2025-08-19T06:45:05Z` `inline` by `ElizaWszola` `csrc/torch_bindings.cpp`:453; signals: general review; excerpt: "nit: can you format this part similar to other ops in torch bindings.cpp?" (https://github.com/vllm-project/vllm/pull/23045#discussion_r2284288604)
- `2025-08-19T15:06:35Z` `inline` by `shixianc` `csrc/torch_bindings.cpp`:453; signals: general review; excerpt: "updated." (https://github.com/vllm-project/vllm/pull/23045#discussion_r2285566916)
