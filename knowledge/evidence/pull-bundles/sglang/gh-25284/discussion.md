# PR Discussion Digest

- Source PR: [sgl-project/sglang#25284](https://github.com/sgl-project/sglang/pull/25284)
- Source page: `sources/prs/sglang/PR-25284.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-25284`
- Generated at: `2026-05-20T15:29:47.124735+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-14T13:44:37Z`
- Merged: `2026-05-19T14:40:12Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 10 (approved=1, commented=9)
- Inline review comments: 10
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=3
- Human participants with discussion text: BBuf, kpham-sgl, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-14T13:47:05Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces Pipeline Parallelism (PP) support for Gemma4 causal and multimodal models by implementing ... (https://github.com/sgl-project/sglang/pull/25284#pullrequestreview-4290437588)
- `2026-05-14T13:48:58Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25284#pullrequestreview-4290455428)
- `2026-05-14T13:50:01Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25284#pullrequestreview-4290464885)
- `2026-05-14T13:50:15Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25284#pullrequestreview-4290466899)
- `2026-05-19T00:34:48Z` `COMMENTED` by `kpham-sgl` - PP and Gemma 4 MTP likely won't work together as the MTP is quite If it doesn't work, ... (https://github.com/sgl-project/sglang/pull/25284#pullrequestreview-4314906716)
- `2026-05-19T01:46:34Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/25284#pullrequestreview-4315133622)
- `2026-05-19T01:46:43Z` `COMMENTED` by `BBuf` - Could we add a PP=2 smoke test for a Gemma4 PLE variant such as E2B/E4B? The current coverage ... (https://github.com/sgl-project/sglang/pull/25284#pullrequestreview-4315133983)
- `2026-05-19T02:34:43Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25284#pullrequestreview-4315284715)
- `2026-05-19T02:40:28Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/25284#pullrequestreview-4315304935)
- `2026-05-19T07:20:16Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/25284#pullrequestreview-4316646469)

## Inline Comment Hotspots

- `python/sglang/srt/models/gemma4_causal.py`: 6 inline comment(s)
- `python/sglang/srt/models/gemma4_mm.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-05-19T00:31:11Z` `inline` by `kpham-sgl` `python/sglang/srt/models/gemma4_causal.py`:973; signals: cuda, cudagraph, gemm; excerpt: "Cudagraph capture part is ignoring proxy["per layer inputs"] Only E2B and E4B models have PLE so you probably missed this during testing of the ..." (https://github.com/sgl-project/sglang/pull/25284#discussion_r3262977649)
- `2026-05-19T01:46:43Z` `review` `COMMENTED` by `BBuf`; signals: cuda, gemm; excerpt: "Could we add a PP=2 smoke test for a Gemma4 PLE variant such as E2B/E4B? The current coverage uses 26B-A4B, which likely misses the ..." (https://github.com/sgl-project/sglang/pull/25284#pullrequestreview-4315133983)
- `2026-05-19T03:32:58Z` `issue` by `yuan-luo`; signals: accuracy, cuda, gemm; excerpt: "Could we add a PP=2 smoke test for a Gemma4 PLE variant such as E2B/E4B? The current coverage uses 26B-A4B, which likely misses the ..." (https://github.com/sgl-project/sglang/pull/25284#issuecomment-4484163946)
- `2026-05-19T02:34:43Z` `inline` by `yuan-luo` `python/sglang/srt/models/gemma4_causal.py`:973; signals: cuda, gemm; excerpt: "Good catch. Updated and added a guard in Gemma4TextModel. init (gemma4 causal.py) that raises when pp size 1 + hidden size per layer input ..." (https://github.com/sgl-project/sglang/pull/25284#discussion_r3263323714)
- `2026-05-19T00:34:48Z` `review` `COMMENTED` by `kpham-sgl`; signals: gemm; excerpt: "PP and Gemma 4 MTP likely won't work together as the MTP is quite If it doesn't work, can you update server args to ..." (https://github.com/sgl-project/sglang/pull/25284#pullrequestreview-4314906716)
- `2026-05-19T02:31:53Z` `issue` by `yuan-luo`; signals: gemm, pipeline; excerpt: "PP and Gemma 4 MTP likely won't work together as the MTP is quite If it doesn't work, can you update server args to ..." (https://github.com/sgl-project/sglang/pull/25284#issuecomment-4483915287)
- `2026-05-14T13:48:58Z` `inline` by `yuan-luo` `python/sglang/srt/models/gemma4_causal.py`:949; signals: gemm; excerpt: "Reject. This is a false positive. make layers returns a ModuleList of length num hidden layers with PPMissingLayer placeholders at indices [0, start layer) ..." (https://github.com/sgl-project/sglang/pull/25284#discussion_r3241781597)
- `2026-05-19T01:46:34Z` `inline` by `BBuf` `python/sglang/srt/models/gemma4_mm.py`:856; signals: gemm; excerpt: "Can we extract this logic into a common function? It seems this part also exists in gemma4 causal.py." (https://github.com/sgl-project/sglang/pull/25284#discussion_r3263186728)
- `2026-05-14T13:50:01Z` `inline` by `yuan-luo` `python/sglang/srt/models/gemma4_causal.py`:1121; signals: gemm; excerpt: "Same as above." (https://github.com/sgl-project/sglang/pull/25284#discussion_r3241788394)
- `2026-05-14T13:50:15Z` `inline` by `yuan-luo` `python/sglang/srt/models/gemma4_mm.py`:864; signals: gemm; excerpt: "Save as above." (https://github.com/sgl-project/sglang/pull/25284#discussion_r3241789907)
- `2026-05-19T02:40:28Z` `inline` by `yuan-luo` `python/sglang/srt/models/gemma4_mm.py`:856; signals: gemm; excerpt: "Adopted." (https://github.com/sgl-project/sglang/pull/25284#discussion_r3263341560)
