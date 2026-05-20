# PR Discussion Digest

- Source PR: [vllm-project/vllm#16727](https://github.com/vllm-project/vllm/pull/16727)
- Source page: `sources/prs/vllm/PR-16727.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16727`
- Generated at: `2026-05-20T15:34:59.641400+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-16T14:02:16Z`
- Merged: `2025-04-22T03:42:34Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 15 (approved=3, commented=12)
- Inline review comments: 15
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=0, outdated=8
- Human participants with discussion text: DarkLight1337, SageMoore, hongxiayang, houseroad, kliuae, mergify, sijiac, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-16T20:03:15Z` `COMMENTED` by `hongxiayang` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2773708085)
- `2025-04-16T20:06:32Z` `COMMENTED` by `hongxiayang` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2773715240)
- `2025-04-16T20:11:40Z` `COMMENTED` by `hongxiayang` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2773727916)
- `2025-04-16T20:13:48Z` `COMMENTED` by `hongxiayang` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2773733508)
- `2025-04-16T21:28:52Z` `COMMENTED` by `sijiac` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2773877446)
- `2025-04-17T10:04:01Z` `COMMENTED` by `kliuae` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2775236670)
- `2025-04-17T10:11:36Z` `COMMENTED` by `kliuae` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2775254573)
- `2025-04-18T07:05:08Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2777839094)
- `2025-04-18T10:37:36Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2778299323)
- `2025-04-21T14:35:58Z` `COMMENTED` by `SageMoore` - Looks reasonable. Just a few nits. (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2781382481)
- `2025-04-21T15:14:44Z` `COMMENTED` by `kliuae` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2781525959)
- `2025-04-21T15:14:49Z` `COMMENTED` by `kliuae` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2781526748)
- `2025-04-21T15:50:46Z` `APPROVED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2781652058)
- `2025-04-21T23:05:34Z` `APPROVED` by `hongxiayang` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2782388468)
- `2025-04-22T03:22:15Z` `APPROVED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/16727#pullrequestreview-2782666574)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`: 9 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 5 inline comment(s)
- `vllm/envs.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-04-17T10:11:35Z` `inline` by `kliuae` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:48; signals: compile, kernel, moe, register; excerpt: "We are wrapping the kernel call because in our future PR addressing the enablement of torch compile for aiter MoE kernels, we will be ..." (https://github.com/vllm-project/vllm/pull/16727#discussion_r2048653829)
- `2025-04-16T21:16:40Z` `inline` by `sijiac` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:151; signals: gemm, kernel, moe; excerpt: "Let's assert apply router weight on input=True or do the if branch check when calling the tkw1 kernel? btw, we should have some comments ..." (https://github.com/vllm-project/vllm/pull/16727#discussion_r2047774238)
- `2025-04-17T10:04:00Z` `inline` by `kliuae` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:22; signals: block, kernel, moe; excerpt: "In this enablement we are following the block scaled moe case in using VLLM ROCM USE AITER MOE as a master switch for enabling ..." (https://github.com/vllm-project/vllm/pull/16727#discussion_r2048643175)
- `2025-04-16T21:21:36Z` `inline` by `sijiac` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:48; signals: kernel, moe; excerpt: "Do we need an additional wrapper for the tkw1 kernel, given that it’s just a kernel call plus an activation type conversion? the activation ..." (https://github.com/vllm-project/vllm/pull/16727#discussion_r2047779470)
- `2025-04-16T21:27:43Z` `inline` by `sijiac` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:77; signals: fp8, moe; excerpt: "tkw1 is not a general support of FP8 FMOE channel / rowwise scaling, it only supports the case when apply router weight on input ..." (https://github.com/vllm-project/vllm/pull/16727#discussion_r2047786300)
- `2025-04-18T10:37:36Z` `inline` by `tjtanaa` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:83; signals: memory, moe; excerpt: "Verified: Will remove the comment. 2025-04-18:10:35:16 INFO [loggers.evaluation tracker:272] Output path not provided, skipping saving results aggregated vllm (pretrained=deepseek-ai/DeepSeek-V3,tensor parallel size=8,max model len=30000,gpu memory ..." (https://github.com/vllm-project/vllm/pull/16727#discussion_r2050471343)
- `2025-04-16T20:03:15Z` `inline` by `hongxiayang` `vllm/envs.py`:81; signals: kernel; excerpt: "Can we make the env name more align with the kernel name , in this case, to include tkw1 in the name?" (https://github.com/vllm-project/vllm/pull/16727#discussion_r2047662597)
- `2025-04-21T14:34:23Z` `inline` by `SageMoore` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:257; signals: moe; excerpt: "Nit: Do you need to store this in the class? It doesn't look like you are using it outside of this function." (https://github.com/vllm-project/vllm/pull/16727#discussion_r2052489016)
- `2025-04-16T20:06:32Z` `inline` by `hongxiayang` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:22; signals: moe; excerpt: "Does this tkw1 enablement need to depend on is rocm aiter moe enabled() ?" (https://github.com/vllm-project/vllm/pull/16727#discussion_r2047667077)
- `2025-04-16T20:11:40Z` `inline` by `hongxiayang` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:48; signals: moe; excerpt: "Can be simplified to one-liner ?" (https://github.com/vllm-project/vllm/pull/16727#discussion_r2047673692)
- `2025-04-18T07:05:08Z` `inline` by `houseroad` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:83; signals: moe; excerpt: "can we verify before landing?" (https://github.com/vllm-project/vllm/pull/16727#discussion_r2050193076)
- `2025-04-21T14:30:50Z` `inline` by `SageMoore` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:271; signals: moe; excerpt: "Nit: Can you merge these into one if statement?" (https://github.com/vllm-project/vllm/pull/16727#discussion_r2052474843)
