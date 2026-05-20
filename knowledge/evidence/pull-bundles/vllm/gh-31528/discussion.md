# PR Discussion Digest

- Source PR: [vllm-project/vllm#31528](https://github.com/vllm-project/vllm/pull/31528)
- Source page: `sources/prs/vllm/PR-31528.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-31528`
- Generated at: `2026-05-20T15:39:21.712229+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-30T10:38:02Z`
- Merged: `2026-01-12T16:55:49Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 19 (approved=2, commented=17)
- Inline review comments: 22
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=10, outdated=6
- Human participants with discussion text: bnellnm, chatgpt-codex-connector, cursor, danielafrimi, mergify, mgoin, rabi
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-12-30T10:39:57Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for "no mul" activation functions (specifically silu no mul, gelu no ... (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3617860616)
- `2025-12-30T10:42:52Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review , it will still crash at runtime. Consider adding explicit cases for those activations (e.g., ... (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3617865814)
- `2025-12-30T19:33:07Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3619087792)
- `2025-12-31T08:39:41Z` `COMMENTED` by `danielafrimi` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3620470896)
- `2026-01-04T19:08:56Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3625134556)
- `2026-01-05T09:39:51Z` `COMMENTED` by `danielafrimi` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3626130907)
- `2026-01-05T17:04:03Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3627684873)
- `2026-01-05T19:10:25Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3628101007)
- `2026-01-07T09:18:57Z` `COMMENTED` by `danielafrimi` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3633987106)
- `2026-01-07T09:19:38Z` `COMMENTED` by `danielafrimi` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3633989459)
- `2026-01-07T20:25:48Z` `APPROVED` by `mgoin` - Looks good to me! Sorry for all the back and forth, appreciate the careful work @danielafrimi (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3636672968)
- `2026-01-09T01:46:08Z` `COMMENTED` by `rabi` - I was not aware of this PR. I've a few questions with respect to the changes here. - ... (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3641941733)
- `2026-01-11T09:39:39Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3647555011)
- `2026-01-11T11:08:59Z` `COMMENTED` by `danielafrimi` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3647605000)
- `2026-01-11T11:44:06Z` `COMMENTED` by `danielafrimi` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3647626961)
- `2026-01-11T12:44:16Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3647660835)
- `2026-01-11T14:39:50Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3647780288)
- `2026-01-12T16:08:12Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3651573310)
- `2026-01-12T16:54:57Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3651757202)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/modular_kernel.py`: 7 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 5 inline comment(s)
- `vllm/model_executor/layers/fused_moe/utils.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_batched_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/deep_gemm_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/cutlass_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-05T09:39:51Z` `inline` by `danielafrimi` `vllm/model_executor/layers/fused_moe/fused_moe.py`:2102; signals: correctness, deepgemm, gemm, hang, moe; excerpt: "@mgoin Did some changes to support this. Ive changed many files All FusedMoEPermuteExpertsUnpermute implementations now support getting the activation params and allocating the buffer ..." (https://github.com/vllm-project/vllm/pull/31528#discussion_r2660871740)
- `2026-01-11T09:39:40Z` `inline` by `cursor` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:424; signals: cache, kernel, moe, triton; excerpt: "TritonOSSExperts apply uses hardcoded N//2 despite workspace fix High Severity The workspace shapes method was updated to size workspace1 using activation out dim, but ..." (https://github.com/vllm-project/vllm/pull/31528#discussion_r2679386040)
- `2026-01-11T12:44:16Z` `inline` by `cursor` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:654; signals: cutlass, fp4, memory, moe; excerpt: "Non-batched format missing activation-aware workspace sizing Low Severity In CutlassExpertsFp4.workspace shapes, the activation out dim is calculated on line 648 but only used in ..." (https://github.com/vllm-project/vllm/pull/31528#discussion_r2679510954)
- `2026-01-05T17:04:03Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/fused_moe.py`:2102; signals: hang, kernel, moe; excerpt: "Hmm it is a lot of changes, I would have thought this would be an internal property for the modular kernel. If we are ..." (https://github.com/vllm-project/vllm/pull/31528#discussion_r2662198192)
- `2026-01-11T09:39:40Z` `inline` by `cursor` `vllm/model_executor/layers/fused_moe/deep_gemm_moe.py`:156; signals: deepgemm, gemm, moe; excerpt: "DeepGemmExperts act mul quant still uses hardcoded N//2 High Severity The workspace shapes method was updated to use activation out dim, but the act ..." (https://github.com/vllm-project/vllm/pull/31528#discussion_r2679386039)
- `2026-01-09T01:46:08Z` `review` `COMMENTED` by `rabi`; signals: flashinfer, hang; excerpt: "I was not aware of this PR. I've a few questions with respect to the changes here. - This is adding activation parameter to ..." (https://github.com/vllm-project/vllm/pull/31528#pullrequestreview-3641941733)
- `2025-12-30T19:33:03Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/modular_kernel.py`:605; signals: kernel, moe; excerpt: "@danielafrimi what if we pull out the section in fused moe.py to make the activation a helper util function that we can use in ..." (https://github.com/vllm-project/vllm/pull/31528#discussion_r2653726434)
- `2026-01-04T19:08:53Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/fused_moe.py`:2102; signals: memory, moe; excerpt: "Is there any way that we are aware of the activation function here? We have it on FusedMoE.activation so we should actually know this ..." (https://github.com/vllm-project/vllm/pull/31528#discussion_r2659865784)
- `2026-01-05T19:10:25Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/batched_deep_gemm_moe.py`:318; signals: gemm, moe; excerpt: "I think it would be good to encapsulate this in a method on the base experts class, e.g. adjust N for activation N(N, activation)." (https://github.com/vllm-project/vllm/pull/31528#discussion_r2662530708)
- `2026-01-09T01:20:03Z` `inline` by `rabi` `vllm/model_executor/layers/fused_moe/modular_kernel.py`:595; signals: kernel, moe; excerpt: "Rather than string suffix parsing (which could be fragile) I thought it would be better to have explicit configuration state like the is act ..." (https://github.com/vllm-project/vllm/pull/31528#discussion_r2674459990)
- `2026-01-11T09:39:39Z` `inline` by `cursor` `vllm/model_executor/layers/fused_moe/fused_moe.py`:2317; signals: cache, moe; excerpt: "Workspace dimensions swapped causing undersized buffer for cache1 High Severity The workspace1 and workspace2 dimensions are swapped. In apply(), intermediate cache1 resizes workspace2 to ..." (https://github.com/vllm-project/vllm/pull/31528#discussion_r2679386035)
- `2026-01-11T09:39:40Z` `inline` by `cursor` `vllm/model_executor/layers/fused_moe/fused_batched_moe.py`:878; signals: cache, moe; excerpt: "BatchedExperts apply method uses hardcoded N//2 despite workspace fix High Severity The workspace shapes method was updated to use activation out dim for workspace2 ..." (https://github.com/vllm-project/vllm/pull/31528#discussion_r2679386038)
