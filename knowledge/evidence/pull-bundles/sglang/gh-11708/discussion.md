# PR Discussion Digest

- Source PR: [sgl-project/sglang#11708](https://github.com/sgl-project/sglang/pull/11708)
- Source page: `sources/prs/sglang/PR-11708.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-11708`
- Generated at: `2026-05-20T15:27:25.292367+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-16T08:39:06Z`
- Merged: `2025-10-28T00:37:49Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 10 (approved=1, commented=8, dismissed=1)
- Inline review comments: 12
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=2
- Human participants with discussion text: FlamingoPg, Fridge003, nvpohanh, weireweire
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-16T08:41:20Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for running FP4 Deepseek on SM120 (Blackwell) GPUs. The changes primarily ... (https://github.com/sgl-project/sglang/pull/11708#pullrequestreview-3343700025)
- `2025-10-17T01:43:16Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/11708#pullrequestreview-3347673390)
- `2025-10-17T05:33:41Z` `DISMISSED` by `FlamingoPg` - @weireweire I think still use is sm100 supported may a good idea, can change logic inner (https://github.com/sgl-project/sglang/pull/11708#pullrequestreview-3344119385)
- `2025-10-17T06:04:28Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/11708#pullrequestreview-3348425935)
- `2025-10-20T02:22:06Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/11708#pullrequestreview-3354857189)
- `2025-10-22T07:04:36Z` `COMMENTED` by `nvpohanh` (https://github.com/sgl-project/sglang/pull/11708#pullrequestreview-3363971045)
- `2025-10-24T06:29:29Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/11708#pullrequestreview-3374723942)
- `2025-10-24T06:55:52Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/11708#pullrequestreview-3374789662)
- `2025-10-24T06:59:35Z` `COMMENTED` by `weireweire` (https://github.com/sgl-project/sglang/pull/11708#pullrequestreview-3374798150)
- `2025-10-27T06:50:10Z` `APPROVED` by `Fridge003` - Thanks for your great work (https://github.com/sgl-project/sglang/pull/11708#pullrequestreview-3382029633)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 5 inline comment(s)
- `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`: 5 inline comment(s)
- `python/sglang/srt/utils/common.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-24T06:26:23Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:28; signals: attention, blackwell, flashinfer, hang, kernel, mla, sm100, sm120; excerpt: "Agree with @nvpohanh. We can change is sm100 supported to is blackwell supported for kernels that support both sm100 and sm120" (https://github.com/sgl-project/sglang/pull/11708#discussion_r2459027057)
- `2025-10-22T07:04:35Z` `inline` by `nvpohanh` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:28; signals: attention, blackwell, flashinfer, kernel, mla, sm100, sm120; excerpt: "@FlamingoPg Could you provide suggestion? SM100 and SM120 are both "blackwell". These kernels can run on both SM100 and SM120, so using is sm100 ..." (https://github.com/sgl-project/sglang/pull/11708#discussion_r2450644018)
- `2025-10-17T06:04:28Z` `inline` by `weireweire` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:28; signals: attention, blackwell, flashinfer, mla, sm100, sm120; excerpt: "there is place that we need to distinguish sm100 and sm120, e.g. TRTLLM backend in flashinfer only support sm100f. Currently I kept both is ..." (https://github.com/sgl-project/sglang/pull/11708#discussion_r2438481636)
- `2025-10-20T02:22:06Z` `inline` by `weireweire` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:28; signals: attention, blackwell, flashinfer, mla, sm100, sm120; excerpt: "Do you have suggestion? Another solution is use is sm100 supported and is sm120 supported to represent is blackwell supported." (https://github.com/sgl-project/sglang/pull/11708#discussion_r2443666208)
- `2025-10-24T06:55:52Z` `inline` by `weireweire` `python/sglang/srt/layers/quantization/modelopt_quant.py`:872; signals: flashinfer, fp4, hang, kernel, moe, sm120; excerpt: "The old kernel don't support sm120, so I changed to flashinfer version here. Although is going to upgrade the kernel for SM120, but I ..." (https://github.com/sgl-project/sglang/pull/11708#discussion_r2459079527)
- `2025-10-16T10:30:41Z` `inline` by `FlamingoPg` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:28; signals: attention, flashinfer, hang, mla, sm100; excerpt: "I think still use is sm100 supported may a good idea, can change logic inner" (https://github.com/sgl-project/sglang/pull/11708#discussion_r2435390105)
- `2025-10-17T01:43:16Z` `inline` by `weireweire` `python/sglang/srt/utils/common.py`:200; signals: sm100, sm90; excerpt: "this consult is sm90 supported 'is sm100 supported`" (https://github.com/sgl-project/sglang/pull/11708#discussion_r2437993265)
- `2025-10-17T05:33:41Z` `review` `DISMISSED` by `FlamingoPg`; signals: hang, sm100; excerpt: "@weireweire I think still use is sm100 supported may a good idea, can change logic inner" (https://github.com/sgl-project/sglang/pull/11708#pullrequestreview-3344119385)
- `2025-10-24T06:27:36Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/modelopt_quant.py`:872; signals: hang; excerpt: "Why doing this change here?" (https://github.com/sgl-project/sglang/pull/11708#discussion_r2459028907)
- `2025-10-17T02:07:38Z` `issue` by `weireweire`; signals: hang; excerpt: "CI failure seems unrelated to my change. please review." (https://github.com/sgl-project/sglang/pull/11708#issuecomment-3413504932)
- `2025-10-24T06:28:22Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/modelopt_quant.py`:1062; signals: general review; excerpt: "Will removing these imports case ImportError?" (https://github.com/sgl-project/sglang/pull/11708#discussion_r2459030201)
- `2025-10-24T06:59:34Z` `inline` by `weireweire` `python/sglang/srt/layers/quantization/modelopt_quant.py`:1062; signals: general review; excerpt: "These imports were not used. Both IDE and string search suggest that." (https://github.com/sgl-project/sglang/pull/11708#discussion_r2459086801)
