# PR Discussion Digest

- Source PR: [vllm-project/vllm#30357](https://github.com/vllm-project/vllm/pull/30357)
- Source page: `sources/prs/vllm/PR-30357.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-30357`
- Generated at: `2026-05-20T15:38:59.294990+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-09T19:49:32Z`
- Merged: `2026-02-26T22:50:16Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 25 (approved=2, changes_requested=1, commented=22)
- Inline review comments: 40
- Review threads observed: 26
- Resolved/outdated thread markers: resolved=18, outdated=20
- Human participants with discussion text: BowenBao, Rohan138, chatgpt-codex-connector, cursor, gshtras, maleksan85, mergify, mgoin, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-09T19:53:19Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for fp8 quantization with static scales for the gpt oss model. ... (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3559403599)
- `2025-12-22T23:44:51Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3606090174)
- `2026-01-12T05:23:38Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3649209925)
- `2026-01-16T23:41:29Z` `COMMENTED` by `cursor` - Cursor Bugbot has reviewed your changes and found 3 potential issues. Bugbot Autofix is OFF. To automatically fix ... (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3673160810)
- `2026-01-20T23:07:19Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3684672552)
- `2026-01-20T23:07:31Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3684672931)
- `2026-01-20T23:07:43Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3684673277)
- `2026-01-28T02:01:23Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3693273731)
- `2026-02-04T05:15:16Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3749035138)
- `2026-02-12T23:37:04Z` `CHANGES_REQUESTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3794233757)
- `2026-02-20T21:04:32Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3834204031)
- `2026-02-20T21:10:59Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3834228760)
- `2026-02-20T22:59:57Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3834542739)
- `2026-02-23T18:38:54Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3842742803)
- `2026-02-23T19:07:57Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3842987314)
- `2026-02-23T19:16:30Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3843033415)
- `2026-02-23T19:55:02Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3843203467)
- `2026-02-24T00:30:49Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3844301808)
- `2026-02-24T17:14:17Z` `APPROVED` by `BowenBao` - LGTM, thank you! (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3849225745)
- `2026-02-24T20:59:16Z` `COMMENTED` by `Rohan138` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3850489780)
- `2026-02-24T21:01:33Z` `COMMENTED` by `Rohan138` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3850501454)
- `2026-02-24T21:07:46Z` `COMMENTED` by `Rohan138` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3850535862)
- `2026-02-25T19:25:02Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3856376507)
- `2026-02-25T19:26:07Z` `APPROVED` by `gshtras` (https://github.com/vllm-project/vllm/pull/30357#pullrequestreview-3856383974)
- ... 1 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/quark/quark_moe.py`: 16 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 7 inline comment(s)
- `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`: 7 inline comment(s)
- `vllm/model_executor/models/gpt_oss.py`: 4 inline comment(s)
- `vllm/_aiter_ops.py`: 4 inline comment(s)
- `vllm/envs.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-01-16T23:41:29Z` `inline` by `cursor` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:458; signals: cache, fp4, kernel, moe, mxfp4, triton; excerpt: "Undefined variable when quant config lacks mxfp4 flags High Severity In triton kernel fused oss experts, when quant config is None, it defaults to ..." (https://github.com/vllm-project/vllm/pull/30357#discussion_r2700335298)
- `2026-02-12T23:28:59Z` `inline` by `BowenBao` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:1007; signals: fp4, fp8, kernel, moe, mxfp4, triton; excerpt: "For wmxfp4 afp8, just need to add the triton kernel dispatch at here. If there are some triton kernel specific setups needed like pre-shuffling, ..." (https://github.com/vllm-project/vllm/pull/30357#discussion_r2801532104)
- `2026-02-23T18:26:49Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:422; signals: fp4, fp8, kernel, moe, mxfp4, triton; excerpt: "ok ithink we should add a flag use mxfp4 w4a8 and use that, 'afp4' was not involved in this case, the inputs are fp16 ..." (https://github.com/vllm-project/vllm/pull/30357#discussion_r2842405657)
- `2026-02-23T18:28:28Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:439; signals: fp4, kernel, moe, mxfp4, triton; excerpt: "ah i see how input scale is passed, through within w1 precision. I think by using mxfp4 w4a8 moe quant config, we can use ..." (https://github.com/vllm-project/vllm/pull/30357#discussion_r2842412149)
- `2026-02-24T20:59:16Z` `inline` by `Rohan138` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:307; signals: fp4, kernel, moe, mxfp4, triton; excerpt: "can we unify this with [triton kernel moe forward]( Currently for this function, we always have quant config.use mxfp4 w4a8 = True; but the ..." (https://github.com/vllm-project/vllm/pull/30357#discussion_r2849513393)
- `2026-02-12T23:33:34Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:422; signals: fp4, kernel, moe, mxfp4, triton; excerpt: "why is it use mxfp4 w4a4 in config but a8w4 kernel" (https://github.com/vllm-project/vllm/pull/30357#discussion_r2801544553)
- `2026-02-20T22:59:57Z` `inline` by `maleksan85` `vllm/model_executor/layers/fused_moe/gpt_oss_triton_kernels_moe.py`:422; signals: fp4, fp8, kernel, moe, triton; excerpt: "there is downcast to static fp8, i.e. conversion from afp4 to afp8" (https://github.com/vllm-project/vllm/pull/30357#discussion_r2835416612)
- `2026-01-28T01:55:22Z` `issue` by `mgoin`; signals: blackwell, fp4, fp8, kernel, mxfp4; excerpt: "We already have w4a8 gpt-oss using mxfp4 and mxfp8 on Blackwell with just a kernel integration using the original checkpoint, why does this need ..." (https://github.com/vllm-project/vllm/pull/30357#issuecomment-3808516052)
- `2026-01-16T23:41:29Z` `inline` by `cursor` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:1097; signals: fp4, moe, mxfp4, register; excerpt: "AttributeError when input scales not registered Medium Severity In QuarkW4MXFp4MoEMethod OSS.process weights after loading, line 1269 accesses layer.w13 input scale and layer.w2 input scale ..." (https://github.com/vllm-project/vllm/pull/30357#discussion_r2700335301)
- `2026-02-12T23:28:03Z` `inline` by `BowenBao` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:57; signals: fp4, fp8, moe, mxfp4; excerpt: "No need to add these two. Both are supported under QuarkOCP MX MoEMethod. Both wmxfp4 amxfp4 and wmxfp4 afp8 are covered under QuarkOCP MX ..." (https://github.com/vllm-project/vllm/pull/30357#discussion_r2801529708)
- `2026-02-23T18:36:13Z` `inline` by `BowenBao` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:97; signals: fp4, fp8, moe, mxfp4; excerpt: "best to avoid conditioning on model type, ideally something like if self.ocp mx scheme == "w mxfp4 a fp8" and not emulate:" (https://github.com/vllm-project/vllm/pull/30357#discussion_r2842444008)
- `2026-02-24T16:48:21Z` `inline` by `BowenBao` `vllm/model_executor/layers/quantization/quark/quark_moe.py`:90; signals: fp4, kernel, moe, mxfp4; excerpt: "nit: for QuarkOCP MX MoEMethod OSS purpose should we just check emulate = not rocm aiter ops.is fused moe enabled()? IIUC both mxfp4 w4a16 ..." (https://github.com/vllm-project/vllm/pull/30357#discussion_r2848340745)
