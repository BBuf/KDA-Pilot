# PR Discussion Digest

- Source PR: [sgl-project/sglang#8464](https://github.com/sgl-project/sglang/pull/8464)
- Source page: `sources/prs/sglang/PR-8464.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-8464`
- Generated at: `2026-05-20T15:31:23.669838+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-28T13:52:48Z`
- Merged: `2025-10-25T00:41:16Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 22 (approved=1, commented=21)
- Inline review comments: 32
- Review threads observed: 18
- Resolved/outdated thread markers: resolved=17, outdated=15
- Human participants with discussion text: ayrnb, bird2426, ch-wan, fzyzcjy, pandengyao, qhsc, yunkchen, zhyncs
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-28T13:53:24Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @ayrnb, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3062882401)
- `2025-07-28T13:55:23Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for DeepEP low latency mode for w4a8 models. The changes involve ... (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3062893152)
- `2025-08-01T08:17:05Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3078201228)
- `2025-08-01T15:59:46Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3079764845)
- `2025-08-03T10:20:08Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3082113441)
- `2025-08-04T03:56:25Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3082600346)
- `2025-08-20T14:41:04Z` `COMMENTED` by `fzyzcjy` - LGTM, only some nits (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3136932355)
- `2025-08-22T07:38:49Z` `COMMENTED` by `yunkchen` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3143465369)
- `2025-08-25T04:00:34Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3149837096)
- `2025-08-25T13:05:01Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3151373326)
- `2025-08-25T13:09:48Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3151397075)
- `2025-08-25T13:09:58Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3151398551)
- `2025-08-27T03:50:34Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3158179836)
- `2025-10-21T18:14:25Z` `COMMENTED` by `ch-wan` - It looks good to me in general. I left some comments. Also, we are gradually adopting the new ... (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3362070650)
- `2025-10-23T05:16:53Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3368269496)
- `2025-10-23T05:17:43Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3368270771)
- `2025-10-23T05:17:51Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3368270937)
- `2025-10-23T22:12:00Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3373009119)
- `2025-10-24T00:53:57Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3373751946)
- `2025-10-24T01:10:50Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3373794492)
- `2025-10-24T12:05:00Z` `COMMENTED` by `ayrnb` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3376159254)
- `2025-10-24T21:50:18Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/8464#pullrequestreview-3378997653)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`: 13 inline comment(s)
- `python/sglang/srt/layers/quantization/w4afp8.py`: 6 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/kernels.py`: 4 inline comment(s)
- `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`: 4 inline comment(s)
- `sgl-kernel/csrc/moe/cutlass_moe/w4a8/w4a8_get_group_starts.cuh`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 1 inline comment(s)
- `sgl-kernel/csrc/moe/cutlass_moe/w4a8/w4a8_grouped_mm_c3x.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-25T04:00:34Z` `inline` by `ayrnb` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:167; signals: cutlass, dtype, fp8, hang, kernel, moe; excerpt: "yes, the previous output dtype of the w4afp8 moe kernel was half, so I changed it to BFloat16 before combining, but this processing was ..." (https://github.com/sgl-project/sglang/pull/8464#discussion_r2297067377)
- `2025-10-24T01:10:50Z` `inline` by `ch-wan` `python/sglang/srt/layers/quantization/w4afp8.py`:340; signals: bf16, cutlass, fp8, moe; excerpt: "Then we need to add assertion somewhere to ensure that our users correctly set SGLANG DEEPEP BF16 DISPATCH=1. Also, I'm curious is we can ..." (https://github.com/sgl-project/sglang/pull/8464#discussion_r2458240307)
- `2025-08-22T07:38:48Z` `inline` by `yunkchen` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:167; signals: cutlass, dtype, latency, moe; excerpt: "The input dtype of low latency mode combine should be BFloat16" (https://github.com/sgl-project/sglang/pull/8464#discussion_r2292972444)
- `2025-08-01T15:59:46Z` `inline` by `ayrnb` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:124; signals: cutlass, latency, moe; excerpt: "But how to distinguish between deepep normal and low latency？🤔🤔🤔" (https://github.com/sgl-project/sglang/pull/8464#discussion_r2248332650)
- `2025-08-20T14:38:55Z` `inline` by `fzyzcjy` `sgl-kernel/csrc/moe/cutlass_moe/w4a8/w4a8_get_group_starts.cuh`:92; signals: cutlass, kernel, moe; excerpt: "nit: if we put 2d kernel before 3d kernel, then maybe put 2d define before 3d define" (https://github.com/sgl-project/sglang/pull/8464#discussion_r2288397828)
- `2025-08-20T14:40:22Z` `inline` by `fzyzcjy` `sgl-kernel/csrc/moe/cutlass_moe/w4a8/w4a8_get_group_starts.cuh`:139; signals: cutlass, kernel, moe; excerpt: "would be great to unify two functions, but if it is hard then it looks ok" (https://github.com/sgl-project/sglang/pull/8464#discussion_r2288402123)
- `2025-08-20T14:40:53Z` `inline` by `fzyzcjy` `sgl-kernel/csrc/moe/cutlass_moe/w4a8/w4a8_grouped_mm_c3x.cuh`:187; signals: cutlass, kernel, moe; excerpt: "nit: shall we make it "some cond another cond" instead of commenting out" (https://github.com/sgl-project/sglang/pull/8464#discussion_r2288403682)
- `2025-08-25T13:09:47Z` `inline` by `ayrnb` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:190; signals: cutlass, latency, moe; excerpt: "In normal mode, the increase of mem can be ignored. low latency mode will increase peak mem." (https://github.com/sgl-project/sglang/pull/8464#discussion_r2298065903)
- `2025-08-25T13:09:58Z` `inline` by `ayrnb` `sgl-kernel/csrc/moe/cutlass_moe/w4a8/w4a8_get_group_starts.cuh`:92; signals: cutlass, kernel, moe; excerpt: "Done" (https://github.com/sgl-project/sglang/pull/8464#discussion_r2298066472)
- `2025-08-03T10:20:08Z` `inline` by `ayrnb` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:124; signals: cutlass, moe; excerpt: "How about using MoeA2ABackend and ep size to check ep mode? sorry, I didn't notice that --enable-deepep-moe is deprecated. 🥵🥵🥵🥵" (https://github.com/sgl-project/sglang/pull/8464#discussion_r2249914671)
- `2025-08-04T03:56:25Z` `inline` by `ayrnb` `python/sglang/srt/layers/moe/cutlass_w4a8_moe.py`:124; signals: cutlass, moe; excerpt: "How about using MoeA2ABackend and ep size to check ep mode? I updated the code and used dispatch output.format to check ep mode." (https://github.com/sgl-project/sglang/pull/8464#discussion_r2250342596)
- `2025-10-24T12:05:00Z` `inline` by `ayrnb` `python/sglang/srt/layers/quantization/w4afp8.py`:340; signals: block, fp8; excerpt: "Because w4afp8 uses static quantization, while DeepEP FP8 dispatch uses dynamic per-block quantization, we cannot set a1 scale as hidden states scale. I have ..." (https://github.com/sgl-project/sglang/pull/8464#discussion_r2460081813)
