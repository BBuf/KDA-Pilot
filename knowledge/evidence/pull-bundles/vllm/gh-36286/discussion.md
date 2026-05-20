# PR Discussion Digest

- Source PR: [vllm-project/vllm#36286](https://github.com/vllm-project/vllm/pull/36286)
- Source page: `sources/prs/vllm/PR-36286.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36286`
- Generated at: `2026-05-20T15:40:10.773006+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-06T22:16:35Z`
- Merged: `2026-03-31T19:43:33Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 33 (approved=2, commented=31)
- Inline review comments: 35
- Review threads observed: 20
- Resolved/outdated thread markers: resolved=15, outdated=15
- Human participants with discussion text: bnellnm, mergify, robertgshaw2-redhat, yzong-rh
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-06T22:18:58Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request is a significant and well-executed refactoring of the Mixture of Experts (MoE) infrastructure, ... (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3906331030)
- `2026-03-06T22:39:27Z` `COMMENTED` by `yzong-rh` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3906401440)
- `2026-03-07T01:52:01Z` `COMMENTED` by `yzong-rh` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3906951744)
- `2026-03-10T15:35:04Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3923388288)
- `2026-03-10T15:47:59Z` `COMMENTED` by `bnellnm` - Looks good to me. Just had one minor question. (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3923490547)
- `2026-03-10T17:38:49Z` `COMMENTED` by `yzong-rh` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3924242788)
- `2026-03-10T18:22:08Z` `APPROVED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3924500454)
- `2026-03-10T22:33:21Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925836185)
- `2026-03-10T22:34:57Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925842684)
- `2026-03-10T22:35:06Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925843162)
- `2026-03-10T22:36:06Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925846215)
- `2026-03-10T22:37:25Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925850927)
- `2026-03-10T22:42:14Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925869491)
- `2026-03-10T22:48:46Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925892635)
- `2026-03-10T22:49:15Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925894310)
- `2026-03-10T22:49:31Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925895138)
- `2026-03-10T22:50:50Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925898816)
- `2026-03-10T22:53:32Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925906395)
- `2026-03-10T22:53:48Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925907273)
- `2026-03-10T22:57:18Z` `COMMENTED` by `yzong-rh` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925874285)
- `2026-03-10T22:59:21Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925929820)
- `2026-03-10T23:01:44Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925937949)
- `2026-03-10T23:03:25Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925943311)
- `2026-03-10T23:07:28Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36286#pullrequestreview-3925956238)
- ... 9 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`: 13 inline comment(s)
- `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`: 6 inline comment(s)
- `vllm/utils/flashinfer.py`: 4 inline comment(s)
- `vllm/model_executor/layers/fused_moe/oracle/fp8.py`: 4 inline comment(s)
- `vllm/lora/layers/fused_moe.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/flashinfer_cutedsl_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-10T17:38:49Z` `inline` by `yzong-rh` `vllm/model_executor/layers/fused_moe/oracle/fp8.py`:568; signals: fp8, kernel, moe; excerpt: "Yeah, monolithic path does not support shared experts. We do an assert within [FusedMoEKernel]( when we use the monolithic implementation. Technically, we assert that ..." (https://github.com/vllm-project/vllm/pull/36286#discussion_r2913400958)
- `2026-03-10T22:43:39Z` `inline` by `yzong-rh` `vllm/lora/layers/fused_moe.py`:52; signals: gemm, kernel, moe; excerpt: "In in the false branch above in inject lora into fused moe It's one of the two places where select gemm impl is called. ..." (https://github.com/vllm-project/vllm/pull/36286#discussion_r2914892573)
- `2026-03-10T22:35:06Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py`:437; signals: fp4, moe, nvfp4; excerpt: "ditto, nice catch on this" (https://github.com/vllm-project/vllm/pull/36286#discussion_r2914864390)
- `2026-03-10T22:48:46Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/flashinfer_cutedsl_moe.py`:64; signals: cute, flashinfer, moe; excerpt: "this is a good fix, but irrelevant to this PR. Please remove it and we can add it in a separate PR" (https://github.com/vllm-project/vllm/pull/36286#discussion_r2914911118)
- `2026-03-10T22:49:16Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:88; signals: fp4, moe, nvfp4; excerpt: "good fix, but irrelevant to this PR. Please remove it and we can add it in another Pr" (https://github.com/vllm-project/vllm/pull/36286#discussion_r2914912878)
- `2026-03-10T22:53:48Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py`:437; signals: fp4, moe, nvfp4; excerpt: "but we can remove it since its irrelevant to this PR" (https://github.com/vllm-project/vllm/pull/36286#discussion_r2914926753)
- `2026-03-31T18:14:46Z` `inline` by `yzong-rh` `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`:315; signals: cutlass, flashinfer, moe; excerpt: "Yeah it fixed flashinfer cutlass." (https://github.com/vllm-project/vllm/pull/36286#discussion_r3017535050)
- `2026-03-10T15:35:04Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/oracle/fp8.py`:568; signals: fp8, moe; excerpt: "Is this check because the monolithic path doesn't implement shared experts? If so, do we have an assert for that?" (https://github.com/vllm-project/vllm/pull/36286#discussion_r2912633626)
- `2026-03-10T22:48:23Z` `inline` by `yzong-rh` `vllm/model_executor/layers/fused_moe/unquantized_fused_moe_method.py`:112; signals: fp8, moe; excerpt: "Yeah, will do. Will also update [fp8.py]( as well. Actually maybe not, will leave it to some other PR" (https://github.com/vllm-project/vllm/pull/36286#discussion_r2914909803)
- `2026-03-10T23:01:44Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`:248; signals: moe, triton; excerpt: "I would prefer if this function did not exist. we now have 2 spots where we set AVAILABLE BACKENDS. I would suggest just having ..." (https://github.com/vllm-project/vllm/pull/36286#discussion_r2914957446)
- `2026-03-10T23:18:11Z` `inline` by `yzong-rh` `vllm/model_executor/layers/fused_moe/oracle/unquantized.py`:260; signals: fp8, moe; excerpt: "Yeah, I followed orcale/fp8.py which also has a NONE backend for TPU and OOT. I think it was because of 32908 But since UnquantizedFusedMoE ..." (https://github.com/vllm-project/vllm/pull/36286#discussion_r2915010565)
- `2026-03-10T23:27:51Z` `inline` by `bnellnm` `vllm/lora/layers/fused_moe.py`:52; signals: kernel, moe; excerpt: "I think this is correct. We didn't have monolithic kernels when the LoRA stuff was done initially. We'd have to do some work to ..." (https://github.com/vllm-project/vllm/pull/36286#discussion_r2915037443)
