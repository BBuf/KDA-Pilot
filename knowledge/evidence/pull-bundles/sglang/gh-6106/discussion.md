# PR Discussion Digest

- Source PR: [sgl-project/sglang#6106](https://github.com/sgl-project/sglang/pull/6106)
- Source page: `sources/prs/sglang/PR-6106.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6106`
- Generated at: `2026-05-20T15:30:36.128420+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-08T02:07:35Z`
- Merged: `2025-06-11T18:47:25Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 8 (approved=3, changes_requested=3, commented=2)
- Inline review comments: 6
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=2
- Human participants with discussion text: JustinTong0323, Lyken17, futrime, lifuhuang, mickqian
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-29T20:21:12Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This pull request introduces support for VILA models, including the necessary processor and model generation classes. ... (https://github.com/sgl-project/sglang/pull/6106#pullrequestreview-2879512887)
- `2025-05-29T21:09:49Z` `CHANGES_REQUESTED` by `JustinTong0323` (https://github.com/sgl-project/sglang/pull/6106#pullrequestreview-2879549374)
- `2025-06-03T17:37:08Z` `COMMENTED` by `JustinTong0323` (https://github.com/sgl-project/sglang/pull/6106#pullrequestreview-2893465152)
- `2025-06-04T13:03:25Z` `COMMENTED` by `futrime` (https://github.com/sgl-project/sglang/pull/6106#pullrequestreview-2896648560)
- `2025-06-07T07:50:21Z` `CHANGES_REQUESTED` by `mickqian` (https://github.com/sgl-project/sglang/pull/6106#pullrequestreview-2907095510)
- `2025-06-08T03:38:02Z` `APPROVED` by `mickqian` (https://github.com/sgl-project/sglang/pull/6106#pullrequestreview-2908078769)
- `2025-06-08T07:24:23Z` `APPROVED` by `JustinTong0323` (https://github.com/sgl-project/sglang/pull/6106#pullrequestreview-2908208080)
- `2025-06-09T07:00:48Z` `APPROVED` by `lifuhuang` (https://github.com/sgl-project/sglang/pull/6106#pullrequestreview-2890862017)

## Inline Comment Hotspots

- `python/sglang/srt/models/vila.py`: 5 inline comment(s)
- `python/sglang/bench_serving.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-06T11:35:58Z` `issue` by `futrime`; signals: attention, flash attention, flashinfer; excerpt: "Here are the evaluation results of our local branch: Model & Impl TextVQA VQAv2 --- --- --- NVILA-Lite-2B (HuggingFace Transformers & Flash Attention 2) ..." (https://github.com/sgl-project/sglang/pull/6106#issuecomment-2948973110)
- `2025-06-05T06:37:04Z` `issue` by `futrime`; signals: benchmark, hang; excerpt: "I forgot to mention, can you also post the MMMU benchmark of your local branch? Thanks! --max-concurrency 1 --num-prompts 50: --max-concurrency 8 --num-prompts 50: ..." (https://github.com/sgl-project/sglang/pull/6106#issuecomment-2942946961)
- `2025-06-07T01:53:06Z` `issue` by `JustinTong0323`; signals: accuracy, kernel; excerpt: "It is strange that even though we set temperature to zero, it will still yield different accuracy on different runs ( 0.03%) cc @mickqian ..." (https://github.com/sgl-project/sglang/pull/6106#issuecomment-2951450811)
- `2025-05-29T20:36:21Z` `inline` by `JustinTong0323` `python/sglang/srt/models/vila.py`:209; signals: hang; excerpt: "We have our own version of siglip now: sglang/python/sglang/srt/models/siglip.py, could we change to it?" (https://github.com/sgl-project/sglang/pull/6106#discussion_r2114710522)
- `2025-06-03T17:37:07Z` `inline` by `JustinTong0323` `python/sglang/srt/models/vila.py`:11; signals: hang; excerpt: "Could we change to from sglang.srt.models.siglip import SiglipVisionModel here?" (https://github.com/sgl-project/sglang/pull/6106#discussion_r2124503900)
- `2025-06-04T13:01:39Z` `issue` by `futrime`; signals: benchmark; excerpt: "I forgot to mention, can you also post the MMMU benchmark of your local branch? Thanks! --max-concurrency 1 --num-prompts 50: --max-concurrency 8 --num-prompts 50:" (https://github.com/sgl-project/sglang/pull/6106#issuecomment-2939956375)
- `2025-06-05T04:10:17Z` `issue` by `lifuhuang`; signals: benchmark; excerpt: "I forgot to mention, can you also post the MMMU benchmark of your local branch? Thanks! --max-concurrency 1 --num-prompts 50: --max-concurrency 8 --num-prompts 50: ..." (https://github.com/sgl-project/sglang/pull/6106#issuecomment-2942673331)
- `2025-06-05T14:31:07Z` `issue` by `Lyken17`; signals: benchmark; excerpt: "the behavior is bit strange... The SGL result (0.467) is much higher than HF original impl (0.392) @futrime can you also test other benchmarks ..." (https://github.com/sgl-project/sglang/pull/6106#issuecomment-2944757336)
- `2025-06-06T11:38:45Z` `issue` by `futrime`; signals: accuracy; excerpt: "It is strange that even though we set temperature to zero, it will still yield different accuracy on different runs ( 0.03%)" (https://github.com/sgl-project/sglang/pull/6106#issuecomment-2948980759)
- `2025-06-07T01:48:26Z` `issue` by `JustinTong0323`; signals: benchmark; excerpt: "the behavior is bit strange... The SGL result (0.467) is much higher than HF original impl (0.392) @futrime can you also test other benchmarks ..." (https://github.com/sgl-project/sglang/pull/6106#issuecomment-2951446829)
- `2025-06-04T02:32:48Z` `issue` by `lifuhuang`; signals: benchmark; excerpt: "I forgot to mention, can you also post the MMMU benchmark of your local branch? Thanks!" (https://github.com/sgl-project/sglang/pull/6106#issuecomment-2938129764)
- `2025-06-04T13:03:25Z` `inline` by `futrime` `python/sglang/srt/models/vila.py`:11; signals: general review; excerpt: "It seems that the siglip vision model in sglang.srt.models.siglip does not output a BaseModelOutputWithPooling containing intermediate hidden states, which is required by NVILA." (https://github.com/sgl-project/sglang/pull/6106#discussion_r2126549191)
