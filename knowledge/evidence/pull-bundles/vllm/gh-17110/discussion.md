# PR Discussion Digest

- Source PR: [vllm-project/vllm#17110](https://github.com/vllm-project/vllm/pull/17110)
- Source page: `sources/prs/vllm/PR-17110.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-17110`
- Generated at: `2026-05-20T15:35:06.292939+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-24T13:34:40Z`
- Merged: `2025-05-14T10:03:12Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 11 (approved=2, changes_requested=1, commented=8)
- Inline review comments: 10
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=0, outdated=4
- Human participants with discussion text: SageMoore, hongxiayang, mergify, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-08T16:16:21Z` `CHANGES_REQUESTED` by `SageMoore` - In general I would like us to contain all of the 1 stage vs 2 stage dispatching logic ... (https://github.com/vllm-project/vllm/pull/17110#pullrequestreview-2825638817)
- `2025-05-08T16:34:18Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/17110#pullrequestreview-2825739643)
- `2025-05-08T22:10:04Z` `APPROVED` by `hongxiayang` - Verified with llama4 bf16 128e model. LGTM in general. Agreed the environment variable part can be simplified. (https://github.com/vllm-project/vllm/pull/17110#pullrequestreview-2826469714)
- `2025-05-08T22:10:35Z` `COMMENTED` by `hongxiayang` (https://github.com/vllm-project/vllm/pull/17110#pullrequestreview-2826470293)
- `2025-05-08T22:15:04Z` `COMMENTED` by `hongxiayang` (https://github.com/vllm-project/vllm/pull/17110#pullrequestreview-2826475460)
- `2025-05-09T07:15:48Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/17110#pullrequestreview-2827254188)
- `2025-05-10T06:34:39Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/17110#pullrequestreview-2830427809)
- `2025-05-10T06:35:57Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/17110#pullrequestreview-2830430168)
- `2025-05-10T11:53:35Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/17110#pullrequestreview-2830759013)
- `2025-05-12T20:27:37Z` `COMMENTED` by `SageMoore` - I'd like to propose an alternative implementation. Instead of passing this new environment variable around, let's just keep ... (https://github.com/vllm-project/vllm/pull/17110#pullrequestreview-2834392867)
- `2025-05-13T13:32:22Z` `APPROVED` by `SageMoore` - Looks reasonable. Thanks for cleaning up the dispatching logic! (https://github.com/vllm-project/vllm/pull/17110#pullrequestreview-2836807473)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/fp8.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-05-12T22:37:12Z` `issue` by `hongxiayang`; signals: fp8, hang, kernel, layout, moe, perf, performance; excerpt: "I'd like to propose an alternative implementation. Instead of passing this new environment variable around, let's just keep the existing VLLM ROCM USE AITER ..." (https://github.com/vllm-project/vllm/pull/17110#issuecomment-2874355154)
- `2025-05-12T20:27:37Z` `review` `COMMENTED` by `SageMoore`; signals: fp8, hang, kernel, layout, moe; excerpt: "I'd like to propose an alternative implementation. Instead of passing this new environment variable around, let's just keep the existing VLLM ROCM USE AITER ..." (https://github.com/vllm-project/vllm/pull/17110#pullrequestreview-2834392867)
- `2025-05-13T13:00:05Z` `issue` by `tjtanaa`; signals: fp8, hang, kernel, layout, moe; excerpt: "I'd like to propose an alternative implementation. Instead of passing this new environment variable around, let's just keep the existing VLLM ROCM USE AITER ..." (https://github.com/vllm-project/vllm/pull/17110#issuecomment-2876421572)
- `2025-05-10T11:53:34Z` `inline` by `tjtanaa` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1133; signals: attention, moe, triton; excerpt: "To pass the pre-commit tests of file vllm/model executor/layers/quantization/compressed tensors/compressed tensors moe.py , we have adjusted the logic of assignment of fused experts function ..." (https://github.com/vllm-project/vllm/pull/17110#discussion_r2083122991)
- `2025-05-10T06:34:39Z` `inline` by `tjtanaa` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1133; signals: gemm, moe; excerpt: "I have removed the argument allow deep gemm. use ck moe 2stages is kept as there is an RFC that highlights Accessing envs.ENV is ..." (https://github.com/vllm-project/vllm/pull/17110#discussion_r2082939886)
- `2025-05-08T15:59:22Z` `inline` by `SageMoore` `vllm/model_executor/layers/quantization/fp8.py`:588; signals: fp8; excerpt: "It looks like this variable is only used to warn that we are falling back to a different implementation. Let's remove it to simplify ..." (https://github.com/vllm-project/vllm/pull/17110#discussion_r2080014382)
- `2025-05-08T16:34:18Z` `inline` by `tjtanaa` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:345; signals: moe; excerpt: "@SageMoore There is an RFC that highlights Accessing envs.ENV is very costly. RFC Issue . Thus, all the env are only invoked and stored ..." (https://github.com/vllm-project/vllm/pull/17110#discussion_r2080076439)
- `2025-05-08T22:15:04Z` `inline` by `hongxiayang` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:23; signals: moe; excerpt: "This seems too much to check 3 environment variables. envs.VLLM ROCM USE AITER 2STAGE MOE is enough as it is only used when the ..." (https://github.com/vllm-project/vllm/pull/17110#discussion_r2080535440)
- `2025-05-09T07:15:48Z` `inline` by `tjtanaa` `vllm/model_executor/layers/quantization/fp8.py`:588; signals: fp8; excerpt: "Same comment as below There is an RFC that highlights Accessing envs.ENV is very costly. RFC Issue . Thus, all the env are only ..." (https://github.com/vllm-project/vllm/pull/17110#discussion_r2081077532)
- `2025-05-10T06:35:57Z` `inline` by `tjtanaa` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:23; signals: moe; excerpt: "The is rocm aiter 2stage moe enabled() has been removed since envs.VLLM ROCM USE AITER 2STAGE MOE is being called in the layer class ..." (https://github.com/vllm-project/vllm/pull/17110#discussion_r2082940809)
- `2025-05-08T16:01:27Z` `inline` by `SageMoore` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:345; signals: moe; excerpt: "Instead of passing this boolean around, can you check the environment variable here?" (https://github.com/vllm-project/vllm/pull/17110#discussion_r2080018482)
- `2025-05-08T16:15:04Z` `inline` by `SageMoore` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1133; signals: moe; excerpt: "Nit: I doesn't look like you need this?" (https://github.com/vllm-project/vllm/pull/17110#discussion_r2080045967)
