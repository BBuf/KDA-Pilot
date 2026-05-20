# PR Discussion Digest

- Source PR: [sgl-project/sglang#6338](https://github.com/sgl-project/sglang/pull/6338)
- Source page: `sources/prs/sglang/PR-6338.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6338`
- Generated at: `2026-05-20T15:30:39.759861+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-16T00:54:55Z`
- Merged: `2025-07-28T03:42:30Z`

## Discussion Counts

- Issue comments: 17
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 10
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=4
- Human participants with discussion text: Edenzzzz, Fridge003, Qiaolin-Yu, Ximingwang-09, hnyls2002, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 8

## Review Decisions

- `2025-05-16T01:52:01Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6338#pullrequestreview-2845307983)
- `2025-05-16T05:09:03Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/6338#pullrequestreview-2845507695)
- `2025-05-17T04:57:32Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/6338#pullrequestreview-2847983304)
- `2025-05-17T06:00:02Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6338#pullrequestreview-2848026794)
- `2025-05-21T01:54:37Z` `COMMENTED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/6338#pullrequestreview-2856001065)
- `2025-05-21T03:46:56Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6338#pullrequestreview-2856145951)
- `2025-07-28T03:03:17Z` `APPROVED` by `hnyls2002` (https://github.com/sgl-project/sglang/pull/6338#pullrequestreview-3060134404)

## Inline Comment Hotspots

- `python/sglang/srt/model_executor/model_runner.py`: 7 inline comment(s)
- `python/sglang/srt/model_executor/cuda_graph_runner.py`: 1 inline comment(s)
- `test/srt/test_hybrid_attn_backend.py`: 1 inline comment(s)
- `python/sglang/srt/layers/attention/hybrid_attn_backend.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-05-18T02:18:19Z` `issue` by `Fridge003`; signals: attention, benchmark, flashinfer, h200, mla, throughput, triton; excerpt: "Some benchmark results on DeepSeek-V3 TP8 on H200, with hybrid attention backends. Benchmark command: Prefill + Decode Median TTFT (ms) Median ITL (ms) Total ..." (https://github.com/sgl-project/sglang/pull/6338#issuecomment-2888715750)
- `2025-05-17T05:44:28Z` `inline` by `Fridge003` `test/srt/test_hybrid_attn_backend.py`:17; signals: accuracy, compile, mla; excerpt: "We need end-to-end accuracy tests on different settings (mla, torch compile, speculative decoding etc.) You can imitate the tests in test fa3.py. But this ..." (https://github.com/sgl-project/sglang/pull/6338#discussion_r2093944499)
- `2025-05-18T01:46:06Z` `issue` by `Fridge003`; signals: accuracy, kernel, triton; excerpt: "Profile on DeepSeek-V3: FA3 kernel during prefill: Triton kernel during decode: Accuracy on DeepSeek-V3:" (https://github.com/sgl-project/sglang/pull/6338#issuecomment-2888701098)
- `2025-07-24T18:18:54Z` `issue` by `Edenzzzz`; signals: attention, flashinfer, h100; excerpt: "Hi will this get merged anytime soon? Also, I tested on H100 to see that Flashinfer P+D beats FA3 in the mixed chunk case. ..." (https://github.com/sgl-project/sglang/pull/6338#issuecomment-3114411797)
- `2025-07-26T05:27:13Z` `issue` by `Qiaolin-Yu`; signals: attention, flashinfer, h100; excerpt: "Hi will this get merged anytime soon? Also, I tested on H100 to see that Flashinfer P+D beats FA3 in the mixed chunk case. ..." (https://github.com/sgl-project/sglang/pull/6338#issuecomment-3121313395)
- `2025-05-17T05:46:53Z` `inline` by `Fridge003` `python/sglang/srt/model_executor/model_runner.py`:922; signals: attention; excerpt: "You can create a MockModelRunner. See python/sglang/test/attention/test flashattn backend.py for some reference." (https://github.com/sgl-project/sglang/pull/6338#discussion_r2093947219)
- `2025-05-16T01:45:00Z` `inline` by `Fridge003` `python/sglang/srt/model_executor/cuda_graph_runner.py`:220; signals: cuda; excerpt: "We can add a util function that checks current prefill backend/decode backend" (https://github.com/sgl-project/sglang/pull/6338#discussion_r2092190381)
- `2025-05-17T05:48:02Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/hybrid_attn_backend.py`:100; signals: attention; excerpt: "Support of speculative decoding can be left for future PR." (https://github.com/sgl-project/sglang/pull/6338#discussion_r2093949315)
- `2025-05-17T04:57:31Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/model_executor/model_runner.py`:922; signals: general review; excerpt: "I added the end-to-end test for the hybrid backend. However, it's very hard to verify if the test is actually using the correct backend ..." (https://github.com/sgl-project/sglang/pull/6338#discussion_r2093917648)
- `2025-05-16T01:50:08Z` `inline` by `Fridge003` `python/sglang/srt/model_executor/model_runner.py`:993; signals: general review; excerpt: "Why not "fa3" here?" (https://github.com/sgl-project/sglang/pull/6338#discussion_r2092193745)
- `2025-05-16T01:51:38Z` `inline` by `Fridge003` `python/sglang/srt/model_executor/model_runner.py`:922; signals: general review; excerpt: "We need a test for hybrid backend" (https://github.com/sgl-project/sglang/pull/6338#discussion_r2092194732)
- `2025-05-16T05:09:03Z` `inline` by `Qiaolin-Yu` `python/sglang/srt/model_executor/model_runner.py`:993; signals: general review; excerpt: "Ohh, it's typo generated by cursor. Fixed." (https://github.com/sgl-project/sglang/pull/6338#discussion_r2092329855)
