# PR Discussion Digest

- Source PR: [vllm-project/vllm#23148](https://github.com/vllm-project/vllm/pull/23148)
- Source page: `sources/prs/vllm/PR-23148.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23148`
- Generated at: `2026-05-20T15:37:21.164631+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-19T04:38:52Z`
- Merged: `2025-09-02T04:06:53Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 18 (approved=2, commented=16)
- Inline review comments: 23
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=5, outdated=12
- Human participants with discussion text: ProExpertProg, bnellnm, jikunshang, mergify, yewentao256, yma11
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-19T04:40:19Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for fp8 online quantization on the XPU platform. The changes involve ... (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3130634004)
- `2025-08-19T14:50:44Z` `COMMENTED` by `yewentao256` - Thanks for the work! Could you also post some E2E results? Eg, showing throughput using vllm bench and ... (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3132696518)
- `2025-08-21T04:41:32Z` `COMMENTED` by `yma11` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3139000765)
- `2025-08-23T12:35:45Z` `COMMENTED` by `yma11` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3148003841)
- `2025-08-25T02:17:57Z` `COMMENTED` by `yma11` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3149678897)
- `2025-08-25T05:34:03Z` `APPROVED` by `jikunshang` - Overall LGTM. thanks! (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3149967944)
- `2025-08-26T21:00:07Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3157260071)
- `2025-08-27T02:38:23Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3158094110)
- `2025-08-28T02:39:18Z` `COMMENTED` by `yma11` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3162866294)
- `2025-08-28T07:12:28Z` `COMMENTED` by `jikunshang` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3163437675)
- `2025-08-28T07:14:21Z` `COMMENTED` by `yma11` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3163526415)
- `2025-08-28T07:14:42Z` `COMMENTED` by `yma11` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3163527389)
- `2025-08-28T07:41:34Z` `COMMENTED` by `yma11` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3163626425)
- `2025-08-28T14:33:16Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3165137820)
- `2025-08-29T03:16:25Z` `COMMENTED` by `yma11` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3167206456)
- `2025-08-29T13:58:56Z` `APPROVED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3168845481)
- `2025-09-02T00:06:02Z` `COMMENTED` by `jikunshang` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3174601518)
- `2025-09-02T01:37:08Z` `COMMENTED` by `yma11` (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3174670381)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/fp8.py`: 7 inline comment(s)
- `vllm/model_executor/layers/quantization/ipex_quant.py`: 7 inline comment(s)
- `vllm/_custom_ops.py`: 4 inline comment(s)
- `vllm/_ipex_ops.py`: 3 inline comment(s)
- `vllm/platforms/xpu.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-28T14:33:16Z` `inline` by `bnellnm` `vllm/model_executor/layers/quantization/ipex_quant.py`:307; signals: fp8, gemm, moe; excerpt: "Thanks for doing the refactoring! Don't you need to call super(). init () here? (this will initialize topk indices type, fused experts and self.moe ..." (https://github.com/vllm-project/vllm/pull/23148#discussion_r2307608233)
- `2025-08-19T14:50:44Z` `review` `COMMENTED` by `yewentao256`; signals: accuracy, throughput; excerpt: "Thanks for the work! Could you also post some E2E results? Eg, showing throughput using vllm bench and accuracy using lm-eval" (https://github.com/vllm-project/vllm/pull/23148#pullrequestreview-3132696518)
- `2025-08-21T04:42:11Z` `issue` by `yma11`; signals: accuracy, benchmark, throughput; excerpt: "Thanks for the work! Could you also post some E2E results? Eg, showing throughput using vllm bench and accuracy using lm-eval benchmark and acc ..." (https://github.com/vllm-project/vllm/pull/23148#issuecomment-3208975274)
- `2025-08-26T20:51:57Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/fp8.py`:997; signals: fp8, moe; excerpt: "cc @bnellnm @tlrmchlsmth @varun-sundar-rabindranath to review the Moe piece, this integration seems pretty intrusive" (https://github.com/vllm-project/vllm/pull/23148#discussion_r2302119573)
- `2025-08-27T02:38:23Z` `inline` by `bnellnm` `vllm/model_executor/layers/quantization/fp8.py`:997; signals: fp8, moe; excerpt: "I think ideally there should be a XPU version of Fp8MoEMethod that is selected by Fp8Config.get quant method so that all the XPU specific ..." (https://github.com/vllm-project/vllm/pull/23148#discussion_r2302697086)
- `2025-08-26T20:46:44Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/fp8.py`:210; signals: cuda, fp8; excerpt: "Should we say not is cuda here?" (https://github.com/vllm-project/vllm/pull/23148#discussion_r2302107109)
- `2025-08-28T06:54:31Z` `inline` by `jikunshang` `vllm/model_executor/layers/quantization/ipex_quant.py`:265; signals: fp8, moe; excerpt: "I prefer to use XPUFp8LinearMethod instead. same for moe method." (https://github.com/vllm-project/vllm/pull/23148#discussion_r2306399937)
- `2025-08-21T04:41:32Z` `inline` by `yma11` `vllm/_custom_ops.py`:1218; signals: kernel; excerpt: "Yes. XPU quantization kernel has problem with empty scale. I separate this value to keep empty for non-xpu path, okay for you?" (https://github.com/vllm-project/vllm/pull/23148#discussion_r2289836246)
- `2025-08-23T12:35:45Z` `inline` by `yma11` `vllm/_custom_ops.py`:1218; signals: hang; excerpt: "I will do a refactor to put xpu related logic in ipex ops so there will no change of these code anymore. Will ping ..." (https://github.com/vllm-project/vllm/pull/23148#discussion_r2295962959)
- `2025-08-28T02:39:18Z` `inline` by `yma11` `vllm/model_executor/layers/quantization/fp8.py`:168; signals: fp8; excerpt: "@ProExpertProg @bnellnm @LucasWilkinson Thanks for your review. I did a further refactor to avoid too many dispatches in current fp8 path and more future ..." (https://github.com/vllm-project/vllm/pull/23148#discussion_r2305991784)
- `2025-08-29T03:16:24Z` `inline` by `yma11` `vllm/model_executor/layers/quantization/ipex_quant.py`:307; signals: moe; excerpt: "Yes, I can inherit directly from FusedMoEMethodBase and makes more sense by calling super(). init (). Updated. Thanks." (https://github.com/vllm-project/vllm/pull/23148#discussion_r2309023509)
- `2025-08-19T14:49:42Z` `inline` by `yewentao256` `vllm/_custom_ops.py`:1218; signals: hang; excerpt: "I remember one previous PR specifically change to empty, will this cause trouble?" (https://github.com/vllm-project/vllm/pull/23148#discussion_r2285521655)
