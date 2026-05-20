# PR Discussion Digest

- Source PR: [vllm-project/vllm#37128](https://github.com/vllm-project/vllm/pull/37128)
- Source page: `sources/prs/vllm/PR-37128.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-37128`
- Generated at: `2026-05-20T15:40:17.888432+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-15T22:44:20Z`
- Merged: `2026-03-21T03:37:05Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 16 (approved=2, commented=14)
- Inline review comments: 26
- Review threads observed: 17
- Resolved/outdated thread markers: resolved=6, outdated=7
- Human participants with discussion text: AndreasKaratzas, BowenBao, mergify, mgoin, robertgshaw2-redhat, yzong-rh, zyongye
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 6

## Review Decisions

- `2026-03-15T22:52:24Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request is a significant and well-executed refactoring of the MXFP4 MoE implementation. Moving the ... (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3950750452)
- `2026-03-17T16:48:19Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the MXFP4 Mixture-of-Experts (MoE) backend selection and implementation by introducing a dedicated ... (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3962267825)
- `2026-03-19T21:45:48Z` `COMMENTED` by `yzong-rh` - Thanks for the contribution! LGTM if @mgoin or @robertgshaw2-redhat are ok as well. Maybe add gpt-oss to tests/evals/gsm8k/configs/moe-refactor? ... (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3977699458)
- `2026-03-19T22:59:21Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3978468659)
- `2026-03-19T23:18:00Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3978538925)
- `2026-03-19T23:20:41Z` `APPROVED` by `yzong-rh` (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3978548188)
- `2026-03-19T23:20:55Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3978549220)
- `2026-03-20T20:04:18Z` `COMMENTED` by `mgoin` - LGTM overall, just comments on a few things that seem to be missing (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3983630891)
- `2026-03-20T20:50:39Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3984000762)
- `2026-03-20T20:53:32Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3984013482)
- `2026-03-20T20:59:12Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3984039618)
- `2026-03-20T21:00:28Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3984045831)
- `2026-03-20T21:02:33Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3984056458)
- `2026-03-20T21:31:24Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/37128#pullrequestreview-3984186598)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`: 7 inline comment(s)
- `vllm/model_executor/layers/quantization/mxfp4.py`: 4 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/experts/trtllm_mxfp4_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/quark/quark_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`: 2 inline comment(s)
- `tests/kernels/quantization/test_mxfp4_oracle_selection.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`: 1 inline comment(s)
- `docs/design/moe_kernel_features.md`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-19T21:20:48Z` `inline` by `yzong-rh` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:202; signals: fp4, kernel, moe, mxfp4, triton; excerpt: "Ideally, we should rely on [FusedMoEExperts::is supported config]( and not duplicate triton kernel support here." (https://github.com/vllm-project/vllm/pull/37128#discussion_r2962773576)
- `2026-03-20T20:00:39Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/mxfp4.py`:917; signals: fp4, hang, moe, mxfp4, warp; excerpt: "@zyongye see this section where num warps is changed for batched moe, this seems to have been lost as it is defaulted to 8 ..." (https://github.com/vllm-project/vllm/pull/37128#discussion_r2967736313)
- `2026-03-20T20:50:39Z` `inline` by `zyongye` `vllm/model_executor/layers/quantization/mxfp4.py`:917; signals: fp4, kernel, mxfp4, triton; excerpt: "Yes, since there are no batched Triton experts ever. This is literally redundant, back when I first integrated this kernel to test if triton ..." (https://github.com/vllm-project/vllm/pull/37128#discussion_r2967926327)
- `2026-03-19T23:18:00Z` `inline` by `zyongye` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:202; signals: fp4, fp8, moe, mxfp4; excerpt: "I will keep this the same for now just to be consistent with fp8." (https://github.com/vllm-project/vllm/pull/37128#discussion_r2963223686)
- `2026-03-20T20:02:59Z` `inline` by `mgoin` `docs/design/moe_kernel_features.md`:91; signals: fp4, kernel, moe, nvfp4; excerpt: "This still serves to TrtLlmNvFp4ExpertsMonolithic for the nvfp4 precision" (https://github.com/vllm-project/vllm/pull/37128#discussion_r2967745532)
- `2026-03-19T23:20:55Z` `inline` by `zyongye` `vllm/model_executor/layers/fused_moe/layer.py`:220; signals: fp4, moe, mxfp4; excerpt: "I will keep this and just delete is mxfp4 quant to keep the interface. Because maybe roundup layer hidden size is from prepare and ..." (https://github.com/vllm-project/vllm/pull/37128#discussion_r2963233725)
- `2026-03-20T20:02:01Z` `inline` by `mgoin` `tests/kernels/quantization/test_mxfp4_oracle_selection.py`; signals: fp4, kernel, mxfp4; excerpt: "Not sure if it is worth having such fine-grained and mocked up oracle selection. Could be annoying as functions get refactored and new backends ..." (https://github.com/vllm-project/vllm/pull/37128#discussion_r2967741702)
- `2026-03-20T20:53:32Z` `inline` by `zyongye` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:864; signals: kernel, moe, triton; excerpt: "yea there's no "base base oai triton experts" that connect the monolithic and modular variant to share the config." (https://github.com/vllm-project/vllm/pull/37128#discussion_r2967936504)
- `2026-03-20T20:59:12Z` `inline` by `zyongye` `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`:23; signals: fp4, mxfp4, warp; excerpt: "because I deleted it on the caller side. The actual usage has a default value num warps=8 on the library [side](" (https://github.com/vllm-project/vllm/pull/37128#discussion_r2967956115)
- `2026-03-19T21:15:45Z` `inline` by `yzong-rh` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:219; signals: fp4, moe, mxfp4; excerpt: "NIT: Remove commet?" (https://github.com/vllm-project/vllm/pull/37128#discussion_r2962751038)
- `2026-03-19T21:15:55Z` `inline` by `yzong-rh` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:229; signals: fp4, moe, mxfp4; excerpt: "NIT: Remove comment?" (https://github.com/vllm-project/vllm/pull/37128#discussion_r2962751960)
- `2026-03-19T21:22:43Z` `inline` by `yzong-rh` `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`:354; signals: fp4, moe, mxfp4; excerpt: "Note to self: TODO: Create XPU monolithic expert." (https://github.com/vllm-project/vllm/pull/37128#discussion_r2962780631)
