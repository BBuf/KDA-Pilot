# PR Discussion Digest

- Source PR: [sgl-project/sglang#7392](https://github.com/sgl-project/sglang/pull/7392)
- Source page: `sources/prs/sglang/PR-7392.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7392`
- Generated at: `2026-05-20T15:31:13.785723+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-20T11:04:06Z`
- Merged: `2026-01-14T09:44:41Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 14 (approved=1, changes_requested=1, commented=12)
- Inline review comments: 19
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=11, outdated=11
- Human participants with discussion text: BowenBao, HaiShaw, fxmarty-amd, yctseng0211
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-20T11:04:37Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @fxmarty-amd, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-2945649441)
- `2025-06-20T11:06:29Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces quark int4fp8 moe online quantization, primarily targeting ROCm. It adds new configuration ... (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-2945655181)
- `2025-06-25T09:05:49Z` `COMMENTED` by `fxmarty-amd` (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-2957329597)
- `2025-06-25T09:10:10Z` `COMMENTED` by `fxmarty-amd` (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-2957344203)
- `2025-06-25T09:10:31Z` `COMMENTED` by `fxmarty-amd` (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-2957345375)
- `2025-06-25T09:15:56Z` `COMMENTED` by `fxmarty-amd` (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-2957364505)
- `2025-06-25T09:16:18Z` `COMMENTED` by `fxmarty-amd` (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-2957365624)
- `2025-06-25T09:17:25Z` `COMMENTED` by `fxmarty-amd` (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-2957369229)
- `2025-06-25T09:17:49Z` `COMMENTED` by `fxmarty-amd` (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-2957370522)
- `2025-07-07T08:39:06Z` `CHANGES_REQUESTED` by `HaiShaw` - int4fp8 for Linear layer shall be out of the scope. projections in the attention layers have their weights ... (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-2992620369)
- `2025-08-11T20:40:35Z` `COMMENTED` by `BowenBao` (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-3107713162)
- `2026-01-05T17:16:35Z` `COMMENTED` by `yctseng0211` (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-3627728440)
- `2026-01-06T13:59:42Z` `COMMENTED` by `fxmarty-amd` (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-3631004549)
- `2026-01-14T09:43:52Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-3659790654)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/quark_w4a8_int4fp8.py`: 10 inline comment(s)
- `python/sglang/srt/layers/quark_utils.py`: 5 inline comment(s)
- `python/sglang/srt/layers/quantization/int4fp8_moe.py`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/__init__.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-07-07T08:39:06Z` `review` `CHANGES_REQUESTED` by `HaiShaw`; signals: accuracy, attention, fp8; excerpt: "int4fp8 for Linear layer shall be out of the scope. projections in the attention layers have their weights quantized online to float8 directly, shall ..." (https://github.com/sgl-project/sglang/pull/7392#pullrequestreview-2992620369)
- `2025-08-11T20:39:53Z` `inline` by `BowenBao` `python/sglang/srt/layers/quantization/int4fp8_moe.py`:143; signals: fp8, moe, perf; excerpt: "IIUC the Int4Fp8 in name only refers to the overall quant method name, For linear layers this just performs fp8 quantization and no int4 ..." (https://github.com/sgl-project/sglang/pull/7392#discussion_r2267972563)
- `2025-08-11T22:30:11Z` `issue` by `BowenBao`; signals: accuracy, attention, fp8; excerpt: "int4fp8 for Linear layer shall be out of the scope. projections in the attention layers have their weights quantized online to float8 directly, shall ..." (https://github.com/sgl-project/sglang/pull/7392#issuecomment-3177082624)
- `2025-12-15T12:23:29Z` `issue` by `fxmarty-amd`; signals: benchmark, fp8, moe; excerpt: "Hi! Re-running python -m sglang.launch server --model-path lmzheng/grok-1--port 30000 --tensor-parallel-size 8 --quantization quark int4fp8 moe and cd benchmark/gsm8k && python3 bench sglang.py --num-questions 2000 ..." (https://github.com/sgl-project/sglang/pull/7392#issuecomment-3655335395)
- `2025-12-20T04:25:07Z` `issue` by `yctseng0211`; signals: block, fp8, moe; excerpt: "@HaiShaw @fxmarty-amd seems the test files "test int4fp8 moe.py" in this PR should be added into 'not in ci' block or '"per-commit-amd"' [sglang/test/srt/run suite.py ..." (https://github.com/sgl-project/sglang/pull/7392#issuecomment-3677363272)
- `2026-01-09T14:01:53Z` `issue` by `fxmarty-amd`; signals: failing, memory, oom; excerpt: "The failing tests come from startup errors as DeepEP error: CPU recv timeout, TimeoutError: Server failed to start within the timeout period, The action ..." (https://github.com/sgl-project/sglang/pull/7392#issuecomment-3729032030)
- `2025-08-11T20:37:50Z` `inline` by `BowenBao` `python/sglang/srt/layers/quantization/int4fp8_moe.py`:298; signals: fp8, moe; excerpt: "int4?" (https://github.com/sgl-project/sglang/pull/7392#discussion_r2267968895)
- `2026-01-14T09:43:36Z` `issue` by `HaiShaw`; signals: fp8, moe; excerpt: "Updated int4fp8 moe to quark int4fp8 moe in PR body" (https://github.com/sgl-project/sglang/pull/7392#issuecomment-3748669916)
- `2025-06-25T09:10:10Z` `inline` by `fxmarty-amd` `python/sglang/srt/layers/quantization/quark_w4a8_int4fp8.py`:123; signals: fp8; excerpt: "fixed in 3df5e1ec241728f3e2397a2e7ee27e57c7ca9cb2" (https://github.com/sgl-project/sglang/pull/7392#discussion_r2166222474)
- `2025-06-25T09:10:31Z` `inline` by `fxmarty-amd` `python/sglang/srt/layers/quantization/quark_w4a8_int4fp8.py`:139; signals: fp8; excerpt: "outdated" (https://github.com/sgl-project/sglang/pull/7392#discussion_r2166223163)
- `2025-06-25T09:15:56Z` `inline` by `fxmarty-amd` `python/sglang/srt/layers/quantization/quark_w4a8_int4fp8.py`:629; signals: fp8; excerpt: "fixed in a4757098793501156b68f6f48c5a6582f2365e94" (https://github.com/sgl-project/sglang/pull/7392#discussion_r2166234778)
- `2025-06-25T09:16:18Z` `inline` by `fxmarty-amd` `python/sglang/srt/layers/quantization/quark_w4a8_int4fp8.py`:380; signals: fp8; excerpt: "irrelevant" (https://github.com/sgl-project/sglang/pull/7392#discussion_r2166235505)
