# PR Discussion Digest

- Source PR: [vllm-project/vllm#16752](https://github.com/vllm-project/vllm/pull/16752)
- Source page: `sources/prs/vllm/PR-16752.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16752`
- Generated at: `2026-05-20T15:34:59.646347+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-17T03:26:34Z`
- Merged: `2025-04-25T03:06:50Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 9 (approved=3, commented=6)
- Inline review comments: 10
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: SageMoore, hongxiayang, houseroad, sijiac, tjtanaa, vllmellm
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-24T06:27:16Z` `COMMENTED` by `sijiac` (https://github.com/vllm-project/vllm/pull/16752#pullrequestreview-2789839756)
- `2025-04-24T14:45:38Z` `COMMENTED` by `hongxiayang` (https://github.com/vllm-project/vllm/pull/16752#pullrequestreview-2791494358)
- `2025-04-24T15:20:29Z` `COMMENTED` by `hongxiayang` (https://github.com/vllm-project/vllm/pull/16752#pullrequestreview-2791604983)
- `2025-04-24T15:25:26Z` `COMMENTED` by `vllmellm` (https://github.com/vllm-project/vllm/pull/16752#pullrequestreview-2791643162)
- `2025-04-24T15:26:42Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/16752#pullrequestreview-2791647971)
- `2025-04-24T16:00:31Z` `COMMENTED` by `vllmellm` (https://github.com/vllm-project/vllm/pull/16752#pullrequestreview-2791751214)
- `2025-04-24T16:35:17Z` `APPROVED` by `hongxiayang` - I have verified the code end to end with llama4 fp8 E128 model. Looks good. Approving this with ... (https://github.com/vllm-project/vllm/pull/16752#pullrequestreview-2791848747)
- `2025-04-24T22:55:27Z` `APPROVED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/16752#pullrequestreview-2792689762)
- `2025-04-24T23:04:36Z` `APPROVED` by `houseroad` (https://github.com/vllm-project/vllm/pull/16752#pullrequestreview-2792698300)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`: 10 inline comment(s)

## High-Signal Discussion

- `2025-04-24T15:17:52Z` `inline` by `hongxiayang` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:219; signals: moe, perf, performance, register; excerpt: "Should we only register these custom ops when VLLM USE V1=1 for V0 compatibility and performance reasons?" (https://github.com/vllm-project/vllm/pull/16752#discussion_r2058691625)
- `2025-04-23T14:59:06Z` `issue` by `hongxiayang`; signals: cuda, cudagraph, perf, performance; excerpt: "cc @houseroad This enables AITER kennel Cudagraph mode for llama4 models in V1 for performance." (https://github.com/vllm-project/vllm/pull/16752#issuecomment-2824605100)
- `2025-04-24T06:21:03Z` `inline` by `sijiac` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:149; signals: bf16, dtype, moe; excerpt: "sry, is it possible to just return torch.empty like(a1, dtype=torch.bf16)? any reason we need to call the moe sorting ck in the fake impl?" (https://github.com/vllm-project/vllm/pull/16752#discussion_r2057628499)
- `2025-04-24T06:24:40Z` `inline` by `sijiac` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:232; signals: kernel, moe, register; excerpt: "shuffle weight is not a pybind kernel just a normal pytorch func, do we still need to register it as a custom op? : ..." (https://github.com/vllm-project/vllm/pull/16752#discussion_r2057632850)
- `2025-04-24T14:45:38Z` `inline` by `hongxiayang` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:232; signals: kernel, moe, register; excerpt: "shuffle weight is not a pybind kernel just a normal pytorch func, do we still need to register it as a custom op? : ..." (https://github.com/vllm-project/vllm/pull/16752#discussion_r2058624071)
- `2025-04-24T06:15:03Z` `inline` by `sijiac` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:72; signals: kernel, moe; excerpt: "ideally, we should have some comments to tell the use case for each kernel, like - asm moe tkw1: for w8a8 - ck moe: ..." (https://github.com/vllm-project/vllm/pull/16752#discussion_r2057621679)
- `2025-04-24T06:26:40Z` `inline` by `sijiac` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:284; signals: gemm, moe; excerpt: "is allow deep gemm actually used?" (https://github.com/vllm-project/vllm/pull/16752#discussion_r2057635424)
- `2025-04-24T15:26:41Z` `inline` by `tjtanaa` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:219; signals: moe, register; excerpt: "The ops register under direct register custom op are also compatible with V0." (https://github.com/vllm-project/vllm/pull/16752#discussion_r2058722327)
- `2025-04-24T06:13:23Z` `inline` by `sijiac` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:86; signals: moe; excerpt: "torch.empty like(hidden states)?" (https://github.com/vllm-project/vllm/pull/16752#discussion_r2057619850)
- `2025-04-24T15:25:26Z` `inline` by `vllmellm` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:86; signals: moe; excerpt: "Thanks for pointing this out. We have updated the code accordingly." (https://github.com/vllm-project/vllm/pull/16752#discussion_r2058719093)
- `2025-04-24T16:00:30Z` `inline` by `vllmellm` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:284; signals: moe; excerpt: "This is just added for mypy." (https://github.com/vllm-project/vllm/pull/16752#discussion_r2058784272)
- `2025-04-24T16:35:17Z` `review` `APPROVED` by `hongxiayang`; signals: fp8; excerpt: "I have verified the code end to end with llama4 fp8 E128 model. Looks good. Approving this with comments." (https://github.com/vllm-project/vllm/pull/16752#pullrequestreview-2791848747)
