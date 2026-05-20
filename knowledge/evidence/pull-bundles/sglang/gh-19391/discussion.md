# PR Discussion Digest

- Source PR: [sgl-project/sglang#19391](https://github.com/sgl-project/sglang/pull/19391)
- Source page: `sources/prs/sglang/PR-19391.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19391`
- Generated at: `2026-05-20T15:28:48.603063+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-26T04:00:56Z`
- Merged: `2026-03-04T22:01:25Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 11 (approved=3, commented=8)
- Inline review comments: 10
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=1
- Human participants with discussion text: ShangmingCai, hlu1, hzh0425, vincentzed, yizhang2077
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-28T06:23:22Z` `COMMENTED` by `ShangmingCai` (https://github.com/sgl-project/sglang/pull/19391#pullrequestreview-3870137050)
- `2026-03-02T08:17:19Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/19391#pullrequestreview-3874681464)
- `2026-03-02T08:25:57Z` `COMMENTED` by `hlu1` (https://github.com/sgl-project/sglang/pull/19391#pullrequestreview-3874718393)
- `2026-03-02T08:27:14Z` `COMMENTED` by `hlu1` (https://github.com/sgl-project/sglang/pull/19391#pullrequestreview-3874723486)
- `2026-03-02T08:30:12Z` `APPROVED` by `ShangmingCai` - LGTM as long as the CI passes. CC: @yizhang2077 Please double check. (https://github.com/sgl-project/sglang/pull/19391#pullrequestreview-3874735062)
- `2026-03-02T08:58:50Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/19391#pullrequestreview-3874857497)
- `2026-03-02T09:01:54Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/19391#pullrequestreview-3874870717)
- `2026-03-02T09:08:46Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/19391#pullrequestreview-3874900405)
- `2026-03-02T09:11:58Z` `APPROVED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/19391#pullrequestreview-3874915052)
- `2026-03-02T09:14:08Z` `COMMENTED` by `hlu1` (https://github.com/sgl-project/sglang/pull/19391#pullrequestreview-3874924701)
- `2026-03-02T09:48:23Z` `APPROVED` by `hzh0425` - LGTM (https://github.com/sgl-project/sglang/pull/19391#pullrequestreview-3875091285)

## Inline Comment Hotspots

- `python/sglang/srt/disaggregation/decode.py`: 4 inline comment(s)
- `test/registered/4-gpu-models/test_qwen35_models.py`: 4 inline comment(s)
- `python/sglang/srt/server_args.py`: 1 inline comment(s)
- `python/sglang/srt/mem_cache/memory_pool.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-02T08:25:56Z` `inline` by `hlu1` `python/sglang/srt/disaggregation/decode.py`:186; signals: accuracy, benchmark, cache, speedup; excerpt: "Why can't it be compatible with no buffer? As I understand it, extra buffer is only needed when you write the ssm/conv states to ..." (https://github.com/sgl-project/sglang/pull/19391#discussion_r2871118069)
- `2026-02-28T06:23:22Z` `inline` by `ShangmingCai` `python/sglang/srt/server_args.py`:1895; signals: cache, hang; excerpt: "Since this change is inside the mamba rafix cache check, I think it is reasonable. Also, we disable radix cache by default for decode ..." (https://github.com/sgl-project/sglang/pull/19391#discussion_r2867127667)
- `2026-03-02T08:27:14Z` `inline` by `hlu1` `test/registered/4-gpu-models/test_qwen35_models.py`:29; signals: fp8, register; excerpt: "The gsm8k tests take a pretty long time when testing with chat template and thinking on. As long as the you are ok with ..." (https://github.com/sgl-project/sglang/pull/19391#discussion_r2871122706)
- `2026-03-02T08:16:23Z` `inline` by `yizhang2077` `python/sglang/srt/mem_cache/memory_pool.py`:460; signals: cache, memory; excerpt: "the same as above" (https://github.com/sgl-project/sglang/pull/19391#discussion_r2871084164)
- `2026-03-02T08:58:50Z` `inline` by `yizhang2077` `test/registered/4-gpu-models/test_qwen35_models.py`:29; signals: fp8, register; excerpt: "I think we could add fp8 test without mtp" (https://github.com/sgl-project/sglang/pull/19391#discussion_r2871243656)
- `2026-03-01T19:26:34Z` `issue` by `vincentzed`; signals: latency, triton; excerpt: "I tested trtllm mha under this as well: Latency (s) Tokens Acc Length Speed (token/s) 3.088 512 3.413 165.82 Triton 2.177 512 3.303 235.23" (https://github.com/sgl-project/sglang/pull/19391#issuecomment-3980835351)
- `2026-03-02T08:16:12Z` `inline` by `yizhang2077` `python/sglang/srt/disaggregation/decode.py`:186; signals: cache; excerpt: "spec v2 can not be compatible with no buffer radix cache， I think we need to add assertion here（but it should be compatible with ..." (https://github.com/sgl-project/sglang/pull/19391#discussion_r2871083516)
- `2026-03-02T09:01:54Z` `inline` by `yizhang2077` `python/sglang/srt/disaggregation/decode.py`:186; signals: cache; excerpt: "if radix cache needs to be compatible with mtp, it needs to support bigram key, which only store keys and values in the range ..." (https://github.com/sgl-project/sglang/pull/19391#discussion_r2871255556)
- `2026-03-02T09:08:46Z` `inline` by `yizhang2077` `python/sglang/srt/disaggregation/decode.py`:186; signals: cache; excerpt: "wait, I think if we use speculative decoding in no buffer mode, radix cache is close, so remove assertion here is ok." (https://github.com/sgl-project/sglang/pull/19391#discussion_r2871282875)
- `2026-03-02T08:17:09Z` `inline` by `yizhang2077` `test/registered/4-gpu-models/test_qwen35_models.py`:29; signals: register; excerpt: "could we add qwen35 original model in this file as well?" (https://github.com/sgl-project/sglang/pull/19391#discussion_r2871086767)
- `2026-03-02T09:14:08Z` `inline` by `hlu1` `test/registered/4-gpu-models/test_qwen35_models.py`:29; signals: register; excerpt: "I'll add them tomorrow in a follow-up PR." (https://github.com/sgl-project/sglang/pull/19391#discussion_r2871304669)
- `2026-03-04T21:33:31Z` `issue` by `hlu1`; signals: register; excerpt: "Both test/registered/4-gpu-models/test qwen3 next models mtp.py and test/registered/4-gpu-models/test qwen35 models.py have passed in the latest CI run." (https://github.com/sgl-project/sglang/pull/19391#issuecomment-4000434783)
