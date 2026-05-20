# PR Discussion Digest

- Source PR: [sgl-project/sglang#9199](https://github.com/sgl-project/sglang/pull/9199)
- Source page: `sources/prs/sglang/PR-9199.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-9199`
- Generated at: `2026-05-20T15:31:32.891260+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-14T20:41:04Z`
- Merged: `2025-09-12T03:18:44Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 24 (approved=3, changes_requested=1, commented=20)
- Inline review comments: 45
- Review threads observed: 32
- Resolved/outdated thread markers: resolved=26, outdated=30
- Human participants with discussion text: fzyzcjy, kaixih, wenscarl
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-14T20:41:28Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @wenscarl, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3122065775)
- `2025-08-14T20:42:30Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for Flashinfer's CuteDSL masked group GEMM for MoE layers. The changes ... (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3122068053)
- `2025-08-17T07:22:36Z` `COMMENTED` by `kaixih` - Thanks for the prompt work! I’ve left some comments mainly about the behavior and scope of the MoE ... (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3126212823)
- `2025-08-17T13:58:27Z` `APPROVED` by `fzyzcjy` - LGTM since this is again only temporary work and will be refined and fused later (and thus there ... (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3126349065)
- `2025-08-17T20:00:49Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3126447700)
- `2025-08-17T20:28:13Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3126453440)
- `2025-08-17T23:46:37Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3126503742)
- `2025-08-25T03:36:44Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3149761435)
- `2025-08-25T08:56:11Z` `CHANGES_REQUESTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3150504843)
- `2025-08-27T23:18:37Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3162115248)
- `2025-08-28T04:27:58Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3163110842)
- `2025-08-28T15:57:26Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3165521516)
- `2025-08-28T23:47:26Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3166927162)
- `2025-09-01T02:42:15Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3171971037)
- `2025-09-01T02:42:45Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3171971418)
- `2025-09-04T03:06:53Z` `COMMENTED` by `fzyzcjy` - briefly checked the code and the code itself roughly LGTM, though it would be great to have a ... (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3183243275)
- `2025-09-05T08:04:12Z` `APPROVED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3188397076)
- `2025-09-05T17:49:27Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3190027874)
- `2025-09-05T17:57:28Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3190319109)
- `2025-09-05T23:40:02Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3191100315)
- `2025-09-05T23:40:16Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3191101340)
- `2025-09-06T00:02:19Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3191146609)
- `2025-09-09T06:07:01Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3199458720)
- `2025-09-10T23:56:13Z` `APPROVED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/9199#pullrequestreview-3208223041)

## Inline Comment Hotspots

- `sgl-kernel/python/sgl_kernel/moe.py`: 17 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 5 inline comment(s)
- `python/sglang/srt/server_args.py`: 5 inline comment(s)
- `sgl-kernel/python/sgl_kernel/gemm.py`: 4 inline comment(s)
- `python/sglang/test/test_flashinfer_cutedsl_scaled_mm.py`: 4 inline comment(s)
- `sgl-kernel/tests/test_flashinfer_cutedsl_scaled_mm.py`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 2 inline comment(s)
- `python/sglang/srt/utils.py`: 1 inline comment(s)
- `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/w4a4_bf16_masked.py`: 1 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 1 inline comment(s)
- `python/sglang/srt/layers/moe/flashinfer_cutedsl_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-28T04:21:02Z` `issue` by `fzyzcjy`; signals: accuracy, attention, b200, benchmark, cute, cutlass, fp4, fp8; excerpt: "Before merging, it would be great to ensure accuracy and performance. More specifically, Accuracy Target benchmarks and thresholds GPQA diamond: need 80% MATH500: need ..." (https://github.com/sgl-project/sglang/pull/9199#issuecomment-3231812859)
- `2025-08-17T07:21:05Z` `inline` by `kaixih` `sgl-kernel/python/sgl_kernel/moe.py`:348; signals: deepgemm, gemm, kernel, latency, moe; excerpt: "I don’t think we need this. I feel it will already be applied in the combine process for DeepEP low-latency, and I don’t see ..." (https://github.com/sgl-project/sglang/pull/9199#discussion_r2280762993)
- `2025-08-25T03:35:29Z` `inline` by `fzyzcjy` `sgl-kernel/python/sgl_kernel/moe.py`; signals: accuracy, kernel, moe, perf, performance; excerpt: "would be great to have a. accuracy numbers gpqa (64k generation, or shorter as long as no truncated answer) math500 (64k generation, or shorter ..." (https://github.com/sgl-project/sglang/pull/9199#discussion_r2297020139)
- `2025-08-17T20:00:49Z` `inline` by `wenscarl` `sgl-kernel/python/sgl_kernel/gemm.py`:463; signals: cutlass, fp4, gemm, kernel, moe; excerpt: "The global scaling at fp32 is to ensure the consistency with current cutlass moe fp4 API." (https://github.com/sgl-project/sglang/pull/9199#discussion_r2281002931)
- `2025-09-05T17:54:57Z` `inline` by `kaixih` `python/sglang/test/test_flashinfer_cutedsl_scaled_mm.py`:27; signals: cute, flashinfer, fp4, moe; excerpt: "can we use the exsting convert swizzled to linear and break fp4 bytes from test fp4 moe.py? or put them into test utils.py?" (https://github.com/sgl-project/sglang/pull/9199#discussion_r2325715701)
- `2025-09-05T17:57:24Z` `inline` by `kaixih` `python/sglang/test/test_flashinfer_cutedsl_scaled_mm.py`:27; signals: cute, flashinfer, fp4, moe; excerpt: "Or, since this is mainly about fp4. Maybe it also reasonable to put the test into test fp4 moe.py?" (https://github.com/sgl-project/sglang/pull/9199#discussion_r2325719866)
- `2025-08-17T06:57:20Z` `inline` by `kaixih` `sgl-kernel/python/sgl_kernel/moe.py`:294; signals: dtype, kernel, moe; excerpt: "Also, can we sth like assert aq sf.dtype == e4m3 and aq.dtype == (u)int8, before setting ab dtype and sf dtype." (https://github.com/sgl-project/sglang/pull/9199#discussion_r2280748640)
- `2025-08-17T13:51:36Z` `inline` by `fzyzcjy` `sgl-kernel/python/sgl_kernel/moe.py`:266; signals: dtype, kernel, moe; excerpt: "nit: maybe we can add a dozen of assertions to ensure shapes and dtypes are what we want, like many other functions do" (https://github.com/sgl-project/sglang/pull/9199#discussion_r2280889797)
- `2025-08-25T08:55:47Z` `inline` by `fzyzcjy` `sgl-kernel/python/sgl_kernel/moe.py`:264; signals: hang, kernel, moe; excerpt: "it seems we should move this to sglang/srt folder instead of sgl-kernel folder (same holds for the tests, etc, i.e. in this PR we ..." (https://github.com/sgl-project/sglang/pull/9199#discussion_r2297513120)
- `2025-09-05T17:47:14Z` `inline` by `kaixih` `python/sglang/srt/server_args.py`:428; signals: cute, flashinfer, moe; excerpt: "we don't need this deprecation warning, right? since the --enable-flashinfer-cutedsl-moe is never a thing before." (https://github.com/sgl-project/sglang/pull/9199#discussion_r2325701363)
- `2025-09-05T17:49:22Z` `inline` by `kaixih` `python/sglang/srt/server_args.py`:2215; signals: cute, flashinfer, moe; excerpt: "i am a bit confused: shouldn't we do --moe-runner-backend flashinfer cutedsl in the first place? why introduce a deprecated flag?" (https://github.com/sgl-project/sglang/pull/9199#discussion_r2325705193)
- `2025-08-17T06:50:34Z` `inline` by `kaixih` `sgl-kernel/python/sgl_kernel/moe.py`:275; signals: dtype, kernel, moe; excerpt: "Nit: could we move the shape/dtype requirements into the function’s docstring?" (https://github.com/sgl-project/sglang/pull/9199#discussion_r2280746688)
