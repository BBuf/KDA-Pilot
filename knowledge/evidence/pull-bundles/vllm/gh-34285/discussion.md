# PR Discussion Digest

- Source PR: [vllm-project/vllm#34285](https://github.com/vllm-project/vllm/pull/34285)
- Source page: `sources/prs/vllm/PR-34285.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-34285`
- Generated at: `2026-05-20T15:39:47.261475+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-10T23:32:35Z`
- Merged: `2026-03-27T06:38:27Z`

## Discussion Counts

- Issue comments: 30
- Review submissions: 27 (approved=5, commented=22)
- Inline review comments: 23
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=11, outdated=9
- Human participants with discussion text: AndreasKaratzas, BowenBao, ChuanLi1101, Rohan138, bnellnm, fxmarty-amd, gshtras, hongxiayang, mergify, robertgshaw2-redhat, smitkadvani, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-10T23:34:55Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the logic for rounding up the hidden size in FusedMoE layers, moving ... (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3782161655)
- `2026-02-10T23:36:28Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the logic for rounding up the hidden size in FusedMoE layers by ... (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3782164942)
- `2026-02-11T00:37:01Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the hidden size roundup logic for FusedMoE layers by moving it into ... (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3782352489)
- `2026-02-16T22:56:10Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the hidden size and intermediate size rounding logic in the FusedMoE layer ... (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3810827264)
- `2026-02-18T23:41:44Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3822748416)
- `2026-02-19T01:06:48Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3822968661)
- `2026-02-23T20:41:55Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3843442414)
- `2026-02-24T00:50:00Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3844351709)
- `2026-02-24T00:51:21Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3844355069)
- `2026-02-24T21:11:56Z` `COMMENTED` by `Rohan138` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3850557134)
- `2026-02-24T21:48:36Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3850718364)
- `2026-02-25T21:51:24Z` `COMMENTED` by `Rohan138` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3857202507)
- `2026-02-25T21:54:42Z` `COMMENTED` by `Rohan138` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3857214901)
- `2026-02-27T20:13:24Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3868874082)
- `2026-03-04T02:12:38Z` `APPROVED` by `smitkadvani` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3886325525)
- `2026-03-06T06:42:24Z` `COMMENTED` by `ChuanLi1101` - Left some comments FYI. (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3901717148)
- `2026-03-06T16:54:53Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3904874453)
- `2026-03-06T16:57:24Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3904887951)
- `2026-03-06T18:24:26Z` `APPROVED` by `ChuanLi1101` - LGTM, thanks for addressing the comments. (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3905284448)
- `2026-03-09T09:57:22Z` `APPROVED` by `fxmarty-amd` - LGTM. OCP MX emulation should be refactored as an Mxfp4Backend in a follow up PR (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3914237276)
- `2026-03-09T21:50:16Z` `APPROVED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-3918420781)
- `2026-03-26T03:07:49Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-4011147349)
- `2026-03-26T03:21:33Z` `COMMENTED` by `AndreasKaratzas` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-4011184736)
- `2026-03-26T03:35:41Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/34285#pullrequestreview-4011213908)
- ... 3 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`: 9 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 5 inline comment(s)
- `vllm/model_executor/layers/quantization/quark/quark_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/mxfp4.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-24T21:11:56Z` `inline` by `Rohan138` `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`:156; signals: alignment, fp4, hang, mxfp4, perf; excerpt: "See discussion in 32307; should we round to 128 or 256 on gfx942 for best perf? Currently mxfp4.py calls get padding alignment (gfx942 - ..." (https://github.com/vllm-project/vllm/pull/34285#discussion_r2849573472)
- `2026-03-06T16:54:53Z` `inline` by `BowenBao` `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`:162; signals: fp4, hang, mxfp4, perf, performance; excerpt: "Please see above comment this change is motivated by that 256 padding on MI300X has higher performance than 128 padding." (https://github.com/vllm-project/vllm/pull/34285#discussion_r2896830237)
- `2026-03-06T06:40:41Z` `inline` by `ChuanLi1101` `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`:119; signals: fp4, hang, moe, mxfp4; excerpt: "Mxfp4Backend.NONE passes the isinstance(mxfp4 backend, Mxfp4Backend) check and falls through to the elif current platform.is rocm() or else branch, applying roundup unnecessarily. Since NONE ..." (https://github.com/vllm-project/vllm/pull/34285#discussion_r2894120975)
- `2026-03-26T03:07:49Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:434; signals: hang, kernel, moe, triton; excerpt: "cc @AndreasKaratzas I reverted this part of change. The hidden state shape will be padded, so it won't match with unpadded K w1. I ..." (https://github.com/vllm-project/vllm/pull/34285#discussion_r2992198234)
- `2026-03-26T03:21:33Z` `inline` by `AndreasKaratzas` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:434; signals: hang, kernel, moe, triton; excerpt: "With padding things may certainly change, I'll take a good look over at AMD CI once it's complete :)" (https://github.com/vllm-project/vllm/pull/34285#discussion_r2992231684)
- `2026-03-06T00:23:48Z` `issue` by `BowenBao`; signals: fp4, moe, mxfp4, throughput; excerpt: "@tjtanaa, @ChuanLi1101 please review. Latest part of the PR enables Quark MXFP4 MoE with aiter backend running with padded intermediate size. Tested with MiniMax ..." (https://github.com/vllm-project/vllm/pull/34285#issuecomment-4008661373)
- `2026-03-17T05:46:43Z` `issue` by `tjtanaa`; signals: fp4, moe, mxfp4, throughput; excerpt: "@BowenBao can you also provide the lm-eval score for this model? please review. Latest part of the PR enables Quark MXFP4 MoE with aiter ..." (https://github.com/vllm-project/vllm/pull/34285#issuecomment-4072517015)
- `2026-03-24T01:26:57Z` `issue` by `BowenBao`; signals: accuracy, fp4, fp8, mxfp4; excerpt: "openai/gpt-oss-120b Configuration GPQA Score Std Dev Avg Response Length -------------- ------------ --------- --------------------- TP2 65.59% 0.475 161 chars TP4 65.09% 0.477 155 chars TP8 ..." (https://github.com/vllm-project/vllm/pull/34285#issuecomment-4114769693)
- `2026-02-24T21:48:36Z` `inline` by `BowenBao` `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`:156; signals: fp4, mxfp4, perf; excerpt: "I don't have context of the previous PRs that introduced 256 in layer.py. Do you have perf data on gfx942 showing which one is ..." (https://github.com/vllm-project/vllm/pull/34285#discussion_r2849717739)
- `2026-02-25T21:54:42Z` `inline` by `Rohan138` `vllm/model_executor/layers/quantization/utils/mxfp4_utils.py`:156; signals: alignment, fp4, mxfp4; excerpt: "yeah, confirmed on main: vs setting pad size to 128: @BowenBao can you delete the get padding alignment function as part of this PR ..." (https://github.com/vllm-project/vllm/pull/34285#discussion_r2855710524)
- `2026-03-06T06:42:05Z` `inline` by `ChuanLi1101` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:774; signals: fp4, moe, mxfp4; excerpt: "The guard if self.mxfp4 backend is not None will pass for Mxfp4Backend.NONE (it's an enum value, not None), causing unnecessary roundup when emulating. This ..." (https://github.com/vllm-project/vllm/pull/34285#discussion_r2894125454)
- `2026-03-26T03:35:41Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:434; signals: kernel, moe, triton; excerpt: "thx, I found I need to remove the later part which slices on hidden output too, otherwise it is segfaulting on gpt-oss w4a8. was ..." (https://github.com/vllm-project/vllm/pull/34285#discussion_r2992263059)
