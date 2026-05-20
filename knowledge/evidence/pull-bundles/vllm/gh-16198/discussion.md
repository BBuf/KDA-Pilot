# PR Discussion Digest

- Source PR: [vllm-project/vllm#16198](https://github.com/vllm-project/vllm/pull/16198)
- Source page: `sources/prs/vllm/PR-16198.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16198`
- Generated at: `2026-05-20T15:34:51.405928+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-07T16:32:49Z`
- Merged: `2025-04-09T02:12:35Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 15 (approved=4, commented=11)
- Inline review comments: 12
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: DarkLight1337, ProExpertProg, SageMoore, hongxiayang, houseroad, tjtanaa, xw285cornell
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-07T17:03:07Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2747515094)
- `2025-04-07T17:19:26Z` `COMMENTED` by `SageMoore` - This looks reasonable. Let's try @ProExpertProg's suggestion for fixing the topk weights issue. (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2747552750)
- `2025-04-07T17:29:06Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2747574257)
- `2025-04-07T19:18:19Z` `APPROVED` by `houseroad` - Looks fine for unblocking now. We need to create 2 follow ups. (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2747855620)
- `2025-04-07T20:40:02Z` `COMMENTED` by `xw285cornell` (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2748059213)
- `2025-04-07T20:57:18Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2748098883)
- `2025-04-07T21:13:50Z` `COMMENTED` by `hongxiayang` (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2748129686)
- `2025-04-07T21:15:45Z` `COMMENTED` by `hongxiayang` (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2748132920)
- `2025-04-08T02:06:10Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2748484234)
- `2025-04-08T03:47:18Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2748577366)
- `2025-04-08T10:15:53Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2749445259)
- `2025-04-08T14:59:45Z` `APPROVED` by `ProExpertProg` - Thanks for adding support for tags! LGTM assuming this tag fixed the original issue! (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2750327140)
- `2025-04-08T15:01:28Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2750333664)
- `2025-04-08T15:30:22Z` `APPROVED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2750434466)
- `2025-04-08T15:51:41Z` `APPROVED` by `DarkLight1337` - Stamp (https://github.com/vllm-project/vllm/pull/16198#pullrequestreview-2750520673)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 8 inline comment(s)
- `vllm/attention/backends/rocm_flash_attn.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-04-08T10:15:53Z` `inline` by `tjtanaa` `vllm/model_executor/layers/fused_moe/fused_moe.py`:477; signals: compile, moe, race, register; excerpt: "@ProExpertProg Thank you for the leads. It seems there is a way to add the tag through the PyTorch Python API as well. We ..." (https://github.com/vllm-project/vllm/pull/16198#discussion_r2032869536)
- `2025-04-07T16:56:27Z` `issue` by `hongxiayang`; signals: block, perf, performance; excerpt: "@simon-mo @houseroad @SageMoore Can you help to merge this? This will unblock us from aiter integration for performance improvement. Thanks!" (https://github.com/vllm-project/vllm/pull/16198#issuecomment-2784004794)
- `2025-04-07T17:29:06Z` `inline` by `tjtanaa` `vllm/model_executor/layers/fused_moe/fused_moe.py`:477; signals: cuda, moe; excerpt: "I think the issue might not be related to inductor as it does not happen on CUDA. the topk weights.stride() on CUDA returns (1,1) ..." (https://github.com/vllm-project/vllm/pull/16198#discussion_r2031693908)
- `2025-04-07T19:16:49Z` `inline` by `houseroad` `vllm/attention/backends/rocm_flash_attn.py`:470; signals: attention, race; excerpt: "Create an issue to trace this progress?" (https://github.com/vllm-project/vllm/pull/16198#discussion_r2031864974)
- `2025-04-07T17:03:07Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/fused_moe/fused_moe.py`:477; signals: moe; excerpt: "Is it possible that this is related to Inductor always putting matrices in row-major order? And we should add a modifier to the custom ..." (https://github.com/vllm-project/vllm/pull/16198#discussion_r2031657018)
- `2025-04-07T21:15:45Z` `inline` by `hongxiayang` `vllm/attention/backends/rocm_flash_attn.py`:470; signals: attention; excerpt: "Agreed about tracking this issue if we want to fully support V0. We will create one internally. Does that sound good to you?" (https://github.com/vllm-project/vllm/pull/16198#discussion_r2032019622)
- `2025-04-08T02:06:10Z` `inline` by `tjtanaa` `vllm/model_executor/layers/fused_moe/fused_moe.py`:477; signals: moe; excerpt: "@ProExpertProg @houseroad The topk weights is generated using Llama4MoE.custom routing function which is just a series of native PyTorch operator. So, there is no ..." (https://github.com/vllm-project/vllm/pull/16198#discussion_r2032263011)
- `2025-04-08T03:47:18Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/fused_moe/fused_moe.py`:477; signals: moe; excerpt: "It's not about the custom op generating but about consuming a tensor, so the wna16 op consumes this tensor and it might get transposed, ..." (https://github.com/vllm-project/vllm/pull/16198#discussion_r2032330451)
- `2025-04-07T19:14:41Z` `inline` by `houseroad` `vllm/model_executor/layers/fused_moe/fused_moe.py`:477; signals: moe; excerpt: "Can we create an issue to track this hack if @ProExpertProg's suggestion doesn't work" (https://github.com/vllm-project/vllm/pull/16198#discussion_r2031859148)
- `2025-04-07T20:40:02Z` `inline` by `xw285cornell` `vllm/attention/backends/rocm_flash_attn.py`:470; signals: attention; excerpt: "i think the output will be incorrect with global attention" (https://github.com/vllm-project/vllm/pull/16198#discussion_r2031976420)
- `2025-04-07T20:57:18Z` `inline` by `houseroad` `vllm/attention/backends/rocm_flash_attn.py`:470; signals: attention; excerpt: "I remember it seems reasonable, but we should definitely have the right approach here." (https://github.com/vllm-project/vllm/pull/16198#discussion_r2031998930)
- `2025-04-07T21:13:49Z` `inline` by `hongxiayang` `vllm/model_executor/layers/fused_moe/fused_moe.py`:477; signals: moe; excerpt: "there is an issue created:" (https://github.com/vllm-project/vllm/pull/16198#discussion_r2032017542)
