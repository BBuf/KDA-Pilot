# PR Discussion Digest

- Source PR: [vllm-project/vllm#21166](https://github.com/vllm-project/vllm/pull/21166)
- Source page: `sources/prs/vllm/PR-21166.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21166`
- Generated at: `2026-05-20T15:36:30.079771+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-18T08:52:25Z`
- Merged: `2025-10-07T13:35:26Z`

## Discussion Counts

- Issue comments: 21
- Review submissions: 20 (approved=4, commented=16)
- Inline review comments: 25
- Review threads observed: 18
- Resolved/outdated thread markers: resolved=15, outdated=14
- Human participants with discussion text: BowenBao, SageMoore, bnellnm, elvischenv, fxmarty-amd, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-07-18T08:53:43Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for mxfp6 and mixed mxfp6-mxfp4 formats, which is a valuable enhancement. ... (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3032677966)
- `2025-07-23T09:34:58Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3046520228)
- `2025-07-23T09:35:26Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3046521598)
- `2025-07-23T09:36:07Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3046523609)
- `2025-07-23T09:36:22Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3046524322)
- `2025-07-29T17:51:19Z` `COMMENTED` by `SageMoore` - Thanks for the contribution @fxmarty-amd. This generally looks reasonable to me, though we should get someone with more ... (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3068566304)
- `2025-09-05T01:35:07Z` `APPROVED` by `BowenBao` - LGTM w/ comments from Quark side. (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3186249828)
- `2025-09-10T16:20:50Z` `COMMENTED` by `mgoin` - Sorry for losing track of this PR. I would prefer to wait for to reduce the need to ... (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3206898039)
- `2025-09-24T17:10:03Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3263863994)
- `2025-09-24T17:12:17Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3263875057)
- `2025-09-24T17:12:31Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for mxfp6 and mixed mxfp6-mxfp4 quantization, extending the existing OCP MX ... (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3263875721)
- `2025-09-24T17:40:49Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3263983267)
- `2025-09-24T17:43:19Z` `APPROVED` by `BowenBao` - Changes post MoE refactor looks good. (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3263990110)
- `2025-09-24T19:31:41Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3264394341)
- `2025-09-25T08:48:49Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3266544915)
- `2025-09-30T17:46:59Z` `APPROVED` by `bnellnm` - The MoE layer changes LGTM. (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3286095916)
- `2025-10-02T19:30:35Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3295899015)
- `2025-10-02T19:31:29Z` `APPROVED` by `mgoin` - Looks good to me overall, thanks! Just a nit with the naming, but it could change over time (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3296119755)
- `2025-10-06T17:44:46Z` `COMMENTED` by `mgoin` - @fxmarty-amd It looks like the moe kernels failures are related (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3306266046)
- `2025-10-06T17:48:47Z` `COMMENTED` by `fxmarty-amd` (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3306287581)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 5 inline comment(s)
- `vllm/model_executor/layers/fused_moe/config.py`: 5 inline comment(s)
- `vllm/model_executor/layers/fused_moe/utils.py`: 5 inline comment(s)
- `vllm/model_executor/layers/quantization/quark/quark.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/ocp_mx_utils.py`: 3 inline comment(s)
- `vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/quark/quark_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-24T17:40:49Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/utils.py`:112; signals: dtype, flashinfer, fp4, moe, mxfp4, nvfp4; excerpt: "Agree with the renaming from fp4 quantize to nvfp4 quantize but not sure about fp4 quantize to nvfp4 quantize. I'd suggest renaming fp4 quantize ..." (https://github.com/vllm-project/vllm/pull/21166#discussion_r2376559550)
- `2025-09-04T13:52:13Z` `issue` by `fxmarty-amd`; signals: fp4, fp8, kernel, mxfp4; excerpt: "Hi @SageMoore @mgoin - just wondering if you'd have some time to review this? It'd be helpful for later integration of true mixed precision ..." (https://github.com/vllm-project/vllm/pull/21166#issuecomment-3253841336)
- `2025-09-04T17:04:44Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/fused_moe.py`:1549; signals: fp4, fp8, moe; excerpt: "nit: raise ValueError or NotImplementedError in last else branch? to catch potentially other schemes not impl yet like w fp4 a fp8 for example." (https://github.com/vllm-project/vllm/pull/21166#discussion_r2322826708)
- `2025-10-02T18:32:08Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/utils.py`:230; signals: fp4, moe, mxfp4; excerpt: "Why move away from "mxfp4"? Since we have the scale here, it is mxfp4 right?" (https://github.com/vllm-project/vllm/pull/21166#discussion_r2399719891)
- `2025-08-06T10:25:15Z` `issue` by `fxmarty-amd`; signals: fp4, hang, mxfp4; excerpt: "@SageMoore I moved a slight change from this PR ( to a standalone one: I think it is a very minimal change, just fixing ..." (https://github.com/vllm-project/vllm/pull/21166#issuecomment-3159261524)
- `2025-09-10T17:09:44Z` `issue` by `fxmarty-amd`; signals: fp4, moe, mxfp4; excerpt: "@mgoin good to know there are plans to streamline the handling of quantization for MOEs! I think it is fine to get in first ..." (https://github.com/vllm-project/vllm/pull/21166#issuecomment-3275793877)
- `2025-10-06T17:02:05Z` `issue` by `fxmarty-amd`; signals: fp4, hang, mxfp4; excerpt: "Why move away from "mxfp4"? Since we have the scale here, it is mxfp4 right? I reverted the change and prefixed with mx everywhere ..." (https://github.com/vllm-project/vllm/pull/21166#issuecomment-3372856351)
- `2025-10-06T17:44:46Z` `review` `COMMENTED` by `mgoin`; signals: kernel, moe; excerpt: "@fxmarty-amd It looks like the moe kernels failures are related" (https://github.com/vllm-project/vllm/pull/21166#pullrequestreview-3306266046)
- `2025-09-24T17:12:16Z` `inline` by `fxmarty-amd` `vllm/model_executor/layers/fused_moe/config.py`:396; signals: dtype, moe; excerpt: "FusedMoEParallelConfig currently assume a common dtype for weights/activations, being quant dtype. I added this weight dtype to hopefully not break anything, but it is ..." (https://github.com/vllm-project/vllm/pull/21166#discussion_r2376476816)
- `2025-09-24T19:31:41Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/config.py`:396; signals: dtype, moe; excerpt: "I think this is fine. Each FusedMoEQuantDesc has it's own dtype. quant dtype is meant for activations. The weights can have their own types ..." (https://github.com/vllm-project/vllm/pull/21166#discussion_r2376851281)
- `2025-10-06T17:44:24Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/utils.py`:257; signals: fp8, moe; excerpt: "It looks like mxfp8 should be kept here too?" (https://github.com/vllm-project/vllm/pull/21166#discussion_r2407661629)
- `2025-07-29T17:44:42Z` `inline` by `SageMoore` `vllm/model_executor/layers/fused_moe/config.py`:62; signals: moe; excerpt: "Nit: Instead of doing the string comparisons can you compare with the OCP MX Scheme enum that you added?" (https://github.com/vllm-project/vllm/pull/21166#discussion_r2240539659)
