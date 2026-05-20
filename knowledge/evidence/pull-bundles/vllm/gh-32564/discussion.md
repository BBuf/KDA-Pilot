# PR Discussion Digest

- Source PR: [vllm-project/vllm#32564](https://github.com/vllm-project/vllm/pull/32564)
- Source page: `sources/prs/vllm/PR-32564.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-32564`
- Generated at: `2026-05-20T15:39:30.715627+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-19T02:12:32Z`
- Merged: `2026-03-03T18:39:50Z`

## Discussion Counts

- Issue comments: 25
- Review submissions: 48 (approved=2, commented=46)
- Inline review comments: 51
- Review threads observed: 36
- Resolved/outdated thread markers: resolved=8, outdated=25
- Human participants with discussion text: bnellnm, djmmoss, jdebache, mergify, mgoin, robertgshaw2-redhat, zyongye
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-19T02:14:22Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for FlashInfer's TRT-LLM FP4 MoE kernels by adding a new FlashInferTrtLlmNvFp4Experts ... (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3676029468)
- `2026-01-19T18:00:20Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3679159090)
- `2026-01-19T23:36:49Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3679869827)
- `2026-01-20T18:12:23Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3683626084)
- `2026-01-20T19:29:12Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3683937951)
- `2026-01-22T17:48:37Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3693771809)
- `2026-01-26T18:47:01Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3707471390)
- `2026-01-29T18:58:39Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3724470442)
- `2026-01-29T18:59:10Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3724472253)
- `2026-01-29T19:00:16Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3724477095)
- `2026-01-29T19:03:50Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3724491324)
- `2026-01-29T19:09:22Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3724510269)
- `2026-01-29T19:10:01Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3724512369)
- `2026-01-29T19:10:36Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3724514418)
- `2026-01-29T19:11:14Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3724516768)
- `2026-01-29T19:11:51Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3724518999)
- `2026-01-29T19:16:09Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3724533952)
- `2026-01-29T19:17:17Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3724538458)
- `2026-01-29T19:23:17Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3724562511)
- `2026-01-30T00:56:06Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3725749493)
- `2026-01-30T00:56:20Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3725750117)
- `2026-01-30T00:56:41Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3725751191)
- `2026-01-30T01:12:55Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3725802516)
- `2026-02-02T22:09:39Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/32564#pullrequestreview-3741857744)
- ... 24 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/modular_kernel.py`: 20 inline comment(s)
- `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/fused_moe/prepare_finalize.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fallback.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/config.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe_modular_method.py`: 2 inline comment(s)
- `vllm/model_executor/models/llama4.py`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-19T18:57:08Z` `inline` by `zyongye` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`; signals: fp4, kernel, moe, mxfp4, nvfp4; excerpt: "We can rename this file to trtllm fp4 moe.py since mxfp4 are using the same kernel interface" (https://github.com/vllm-project/vllm/pull/32564#discussion_r2829618303)
- `2026-02-02T22:09:38Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py`:72; signals: fp4, kernel, moe, nvfp4; excerpt: "Is there ever a case where only one of these is supported? If they are both always supported, should we just pick the monolothic ..." (https://github.com/vllm-project/vllm/pull/32564#discussion_r2756268907)
- `2026-02-02T22:51:39Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/flashinfer_trtllm_nvfp4_moe.py`:25; signals: flashinfer, fp4, moe, nvfp4; excerpt: "Can this be a standalone class? Similar comment from the NaiveEP classes." (https://github.com/vllm-project/vllm/pull/32564#discussion_r2756362454)
- `2026-02-16T18:02:04Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/oracle/nvfp4.py`:72; signals: fp4, kernel, moe, nvfp4; excerpt: "we want to use the Modular kernel if its deployed with Dp/Ep and the Monolithic kernel otherwise" (https://github.com/vllm-project/vllm/pull/32564#discussion_r2813542633)
- `2026-02-17T16:47:14Z` `inline` by `bnellnm` `tests/kernels/moe/modular_kernel_tools/common.py`:669; signals: dtype, kernel, moe; excerpt: "nit: i think we should make a method on the mk that hides the impl, e.g. mk.topk indices dtype(). similarly for any other properties ..." (https://github.com/vllm-project/vllm/pull/32564#discussion_r2818004858)
- `2026-02-17T17:13:48Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:271; signals: fp4, moe, nvfp4; excerpt: "I forget if this is just copied from before, but since we ignore this passed in routed scaling factor to hardcode routed scaling factor=None ..." (https://github.com/vllm-project/vllm/pull/32564#discussion_r2818120235)
- `2026-02-17T17:16:04Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:205; signals: fp4, moe, nvfp4; excerpt: "this seems copied but can you leave a comment of what type this is?" (https://github.com/vllm-project/vllm/pull/32564#discussion_r2818128931)
- `2026-02-17T18:24:46Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:205; signals: fp4, moe, nvfp4; excerpt: "Its a dummy arg" (https://github.com/vllm-project/vllm/pull/32564#discussion_r2818460775)
- `2026-03-03T18:38:42Z` `inline` by `robertgshaw2-redhat` `tests/evals/gsm8k/configs/moe-refactor/config-h100.txt`:11; signals: failing, h100, moe; excerpt: "note: these are failing on main --- unclear why. issue does not reproduce locally" (https://github.com/vllm-project/vllm/pull/32564#discussion_r2879914416)
- `2026-01-20T18:12:23Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/modular_kernel.py`:1273; signals: kernel, moe; excerpt: "I think we should have a monolithic subclass of FusedMoEModularKernel that bypasses the prepare/finalize and experts classes. A lot of the logic just doesn't ..." (https://github.com/vllm-project/vllm/pull/32564#discussion_r2709532174)
- `2026-01-22T17:48:37Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/modular_kernel.py`:1273; signals: kernel, moe; excerpt: "Which kernels support both? Even if they do, we can factor out the common functionality for use by monolithic and modular cases?" (https://github.com/vllm-project/vllm/pull/32564#discussion_r2717975037)
- `2026-01-26T18:47:00Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/modular_kernel.py`:1273; signals: kernel, moe; excerpt: "I was thinking more about this. In the case of "Monolithic kernel", we will still need dispatch/combine for the Ag/Rs in the DP/EP case ..." (https://github.com/vllm-project/vllm/pull/32564#discussion_r2728815119)
