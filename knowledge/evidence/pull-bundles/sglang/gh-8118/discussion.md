# PR Discussion Digest

- Source PR: [sgl-project/sglang#8118](https://github.com/sgl-project/sglang/pull/8118)
- Source page: `sources/prs/sglang/PR-8118.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-8118`
- Generated at: `2026-05-20T15:31:21.456042+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-17T08:54:38Z`
- Merged: `2025-09-02T05:17:26Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 7
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=4, outdated=5
- Human participants with discussion text: AniZpZ, BBuf, Bruce-x-1997, chenxijun1029, donpromax, huangzl18883, junliu-mde, llc-kc, yangsijia-celina, yuhyao, zhilingjiang
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 9

## Review Decisions

- `2025-07-17T08:55:11Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @chenxijun1029, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/8118#pullrequestreview-3028592735)
- `2025-07-17T08:56:19Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for tensor parallelism (TP) mode for the DeepSeek-R1-W4AFP8 model, which shows ... (https://github.com/sgl-project/sglang/pull/8118#pullrequestreview-3028596823)
- `2025-07-20T14:05:48Z` `COMMENTED` by `yangsijia-celina` (https://github.com/sgl-project/sglang/pull/8118#pullrequestreview-3036024074)
- `2025-07-30T05:53:26Z` `COMMENTED` by `huangzl18883` (https://github.com/sgl-project/sglang/pull/8118#pullrequestreview-3069973966)
- `2025-08-04T12:38:09Z` `COMMENTED` by `donpromax` (https://github.com/sgl-project/sglang/pull/8118#pullrequestreview-3084013348)
- `2025-08-18T09:36:19Z` `COMMENTED` by `AniZpZ` (https://github.com/sgl-project/sglang/pull/8118#pullrequestreview-3127574482)
- `2025-08-20T02:07:30Z` `APPROVED` by `AniZpZ` (https://github.com/sgl-project/sglang/pull/8118#pullrequestreview-3134554062)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/w4afp8.py`: 3 inline comment(s)
- `sgl-kernel/csrc/moe/cutlass_moe/w4a8/w4a8_grouped_mm_c3x.cu`: 2 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 1 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-18T09:30:58Z` `inline` by `AniZpZ` `sgl-kernel/csrc/moe/cutlass_moe/w4a8/w4a8_grouped_mm_c3x.cu`:205; signals: cutlass, kernel, moe; excerpt: "I think it's better to use a template to reduce duplicate code here" (https://github.com/sgl-project/sglang/pull/8118#discussion_r2281844032)
- `2025-08-05T08:46:38Z` `issue` by `yuhyao`; signals: cutlass, kernel, moe; excerpt: "@chenxijun1029 Nice work! Just wondering if there will be any further updates? Also, should the file sgl-kernel/tests/test cutlass w4a8 moe mm.py be updated as ..." (https://github.com/sgl-project/sglang/pull/8118#issuecomment-3154144523)
- `2025-08-15T12:26:40Z` `issue` by `chenxijun1029`; signals: accuracy, perf, performance; excerpt: "Thanks for your great work on this! To help us evaluate the impact of this PR, could you please provide the performance results (like ..." (https://github.com/sgl-project/sglang/pull/8118#issuecomment-3191390244)
- `2025-08-04T12:38:04Z` `inline` by `donpromax` `python/sglang/srt/layers/quantization/w4afp8.py`:11; signals: fp8, moe; excerpt: "Python module and function cannot use the same name, otherwise you will encounter the circular import error. One way to fix this is to ..." (https://github.com/sgl-project/sglang/pull/8118#discussion_r2251363352)
- `2025-07-17T14:22:01Z` `issue` by `AniZpZ`; signals: perf, performance; excerpt: "Thanks for your great work on this! To help us evaluate the impact of this PR, could you please provide the performance results (like ..." (https://github.com/sgl-project/sglang/pull/8118#issuecomment-3084276220)
- `2025-07-20T14:00:24Z` `inline` by `yangsijia-celina` `python/sglang/srt/layers/quantization/w4afp8.py`:418; signals: fp8; excerpt: "just want to confirm if you've checked the contents of the act scales.safetensors file. Are the input scales for w1 and w3 all consistent?" (https://github.com/sgl-project/sglang/pull/8118#discussion_r2217829091)
- `2025-07-20T13:50:40Z` `inline` by `yangsijia-celina` `python/sglang/srt/layers/moe/ep_moe/layer.py`:43; signals: moe; excerpt: "seems this import isn't used" (https://github.com/sgl-project/sglang/pull/8118#discussion_r2217816418)
- `2025-07-30T05:53:25Z` `inline` by `huangzl18883` `python/sglang/srt/layers/quantization/w4afp8.py`:11; signals: fp8; excerpt: "remove python prefix?" (https://github.com/sgl-project/sglang/pull/8118#discussion_r2241598958)
