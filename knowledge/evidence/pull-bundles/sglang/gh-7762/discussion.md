# PR Discussion Digest

- Source PR: [sgl-project/sglang#7762](https://github.com/sgl-project/sglang/pull/7762)
- Source page: `sources/prs/sglang/PR-7762.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7762`
- Generated at: `2026-05-20T15:31:21.451741+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-04T03:21:18Z`
- Merged: `2025-07-07T21:47:21Z`

## Discussion Counts

- Issue comments: 17
- Review submissions: 5 (commented=5)
- Inline review comments: 8
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: AniZpZ, Hongbosherlock, XiaotaoChen, chenxijun1029, huangzl18883, junliu-mde, pengyao96, seanxcwang, whybeyoung, yangsijia-celina, zhyncs
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 9

## Review Decisions

- `2025-07-04T03:22:10Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yangsijia-serena, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7762#pullrequestreview-2985297707)
- `2025-07-04T03:23:28Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for the DeepSeek-R1-W4AFP8 model, which involves a new w4afp8 mixed-precision quantization ... (https://github.com/sgl-project/sglang/pull/7762#pullrequestreview-2985298931)
- `2025-07-07T10:26:13Z` `COMMENTED` by `AniZpZ` (https://github.com/sgl-project/sglang/pull/7762#pullrequestreview-2993102068)
- `2025-07-07T11:36:03Z` `COMMENTED` by `yangsijia-celina` (https://github.com/sgl-project/sglang/pull/7762#pullrequestreview-2993415059)
- `2025-07-07T11:46:34Z` `COMMENTED` by `yangsijia-celina` (https://github.com/sgl-project/sglang/pull/7762#pullrequestreview-2993462364)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/w4afp8.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`: 2 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/kernels.py`: 1 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-04T07:43:13Z` `issue` by `seanxcwang`; signals: deepgemm, fp8, gemm, perf, performance; excerpt: "Are there any performance data comparisons on grouped gemm between w4af8 and deepgemm fp8?" (https://github.com/sgl-project/sglang/pull/7762#issuecomment-3034856032)
- `2025-07-07T10:11:51Z` `inline` by `AniZpZ` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:173; signals: cutlass, fp8, hopper, moe; excerpt: "noticed that chunk size is hard-coded to 128 here. wondering if only g128 is valid for w4fp8 in your test on hopper arch for ..." (https://github.com/sgl-project/sglang/pull/7762#discussion_r2189587221)
- `2025-07-06T14:03:51Z` `issue` by `yangsijia-celina`; signals: benchmark, perf, performance, throughput; excerpt: "@yangsijia-serena Hi, Congratulation for the great work. I'm trying to re-produce the profiling data on 8 H20, but my profiling data is too bad, ..." (https://github.com/sgl-project/sglang/pull/7762#issuecomment-3041706911)
- `2025-07-07T11:36:02Z` `inline` by `yangsijia-celina` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:173; signals: cutlass, fp8, moe; excerpt: "Actually we just test w4afp8 on DeepSeek-R1-W4AFP8 model now, where the moe weight is quantized with group size=128. We can also implement dynamic passing ..." (https://github.com/sgl-project/sglang/pull/7762#discussion_r2189797426)
- `2025-07-07T11:46:34Z` `inline` by `yangsijia-celina` `python/sglang/srt/layers/quantization/w4afp8.py`:69; signals: fp8, moe; excerpt: "The same reason as another comment: the limitation of this quantization scheme is consistent with the DeepSeek-R1-W4AFP8 model. To support other w4a8 models, we ..." (https://github.com/sgl-project/sglang/pull/7762#discussion_r2189824469)
- `2025-07-07T10:25:06Z` `inline` by `AniZpZ` `python/sglang/srt/layers/quantization/w4afp8.py`:69; signals: fp8; excerpt: "just wonder if the quantization scheme is limited for now?" (https://github.com/sgl-project/sglang/pull/7762#discussion_r2189613117)
- `2025-07-06T13:45:40Z` `issue` by `XiaotaoChen`; signals: throughput; excerpt: "@yangsijia-serena Hi, Congratulation for the great work. I'm trying to re-produce the profiling data on 8 H20, but my profiling data is too bad, ..." (https://github.com/sgl-project/sglang/pull/7762#issuecomment-3041622413)
- `2025-07-04T07:14:03Z` `issue` by `huangzl18883`; signals: moe; excerpt: "Are there any bench results available for the Qwen3-moe series?" (https://github.com/sgl-project/sglang/pull/7762#issuecomment-3034784394)
