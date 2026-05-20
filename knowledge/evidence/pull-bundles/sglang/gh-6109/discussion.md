# PR Discussion Digest

- Source PR: [sgl-project/sglang#6109](https://github.com/sgl-project/sglang/pull/6109)
- Source page: `sources/prs/sglang/PR-6109.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6109`
- Generated at: `2026-05-20T15:30:36.130329+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-08T03:57:09Z`
- Merged: `2025-05-15T07:48:12Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 9
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: Fridge003, PopSoda2002, mahaocong90, neiltian-tencent, quinnrong94, sleepcoo, zhaochenyang20
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-05-08T19:11:44Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6109#pullrequestreview-2825993717)
- `2025-05-09T03:09:09Z` `COMMENTED` by `neiltian-tencent` (https://github.com/sgl-project/sglang/pull/6109#pullrequestreview-2826872390)
- `2025-05-09T03:09:23Z` `COMMENTED` by `neiltian-tencent` (https://github.com/sgl-project/sglang/pull/6109#pullrequestreview-2826872556)
- `2025-05-09T03:09:30Z` `COMMENTED` by `neiltian-tencent` (https://github.com/sgl-project/sglang/pull/6109#pullrequestreview-2826872665)
- `2025-05-09T03:15:30Z` `COMMENTED` by `neiltian-tencent` (https://github.com/sgl-project/sglang/pull/6109#pullrequestreview-2826877515)
- `2025-05-12T07:13:21Z` `APPROVED` by `sleepcoo` (https://github.com/sgl-project/sglang/pull/6109#pullrequestreview-2832076976)
- `2025-05-15T01:33:14Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/6109#pullrequestreview-2841891116)

## Inline Comment Hotspots

- `test/srt/test_mla_flashmla.py`: 5 inline comment(s)
- `test/srt/test_eagle_infer.py`: 2 inline comment(s)
- `python/sglang/srt/model_executor/cuda_graph_runner.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-05-08T18:27:22Z` `inline` by `Fridge003` `test/srt/test_mla_flashmla.py`:1; signals: cache, fp8, kv cache, mla; excerpt: "Add a test for fp8 kv cache and move it to test flashmla.py" (https://github.com/sgl-project/sglang/pull/6109#discussion_r2080239904)
- `2025-05-09T13:05:52Z` `issue` by `quinnrong94`; signals: accuracy, benchmark, cache, fp8; excerpt: "Do you have the results of the accuracy test? The accuracy loss of MTP and FP8 kv-cache is relatively small in our tests. For ..." (https://github.com/sgl-project/sglang/pull/6109#issuecomment-2866468605)
- `2025-05-08T18:31:19Z` `inline` by `Fridge003` `python/sglang/srt/model_executor/cuda_graph_runner.py`:214; signals: attention, cuda, mla; excerpt: "No need to import FlashMLABackend here. Instead, import global server args dict at the top of this file: Then attention backend can be checked ..." (https://github.com/sgl-project/sglang/pull/6109#discussion_r2080255818)
- `2025-05-08T18:24:57Z` `inline` by `Fridge003` `test/srt/test_mla_flashmla.py`:44; signals: cuda, mla; excerpt: "Cuda graph should be opened in test." (https://github.com/sgl-project/sglang/pull/6109#discussion_r2080233132)
- `2025-05-08T19:14:13Z` `issue` by `Fridge003`; signals: perf, performance; excerpt: "It's recommended to compare the performance between enabling and disabling MTP with the following script: Please paste the results" (https://github.com/sgl-project/sglang/pull/6109#issuecomment-2864035645)
- `2025-05-09T06:46:07Z` `issue` by `quinnrong94`; signals: perf, performance; excerpt: "It's recommended to compare the performance between enabling and disabling MTP with the following script: Please paste the results The speed-up ratio of enabling ..." (https://github.com/sgl-project/sglang/pull/6109#issuecomment-2865339586)
- `2025-05-08T18:22:57Z` `inline` by `Fridge003` `test/srt/test_mla_flashmla.py`:17; signals: mla; excerpt: "Please move this test to test flashmla.py" (https://github.com/sgl-project/sglang/pull/6109#discussion_r2080230363)
- `2025-05-08T18:23:36Z` `inline` by `Fridge003` `test/srt/test_eagle_infer.py`:572; signals: mla; excerpt: "TestEAGLEServerFlashMLA is not needed. This test can be covered by TestFlashMLAMTP test." (https://github.com/sgl-project/sglang/pull/6109#discussion_r2080231253)
- `2025-05-09T03:09:09Z` `inline` by `neiltian-tencent` `test/srt/test_mla_flashmla.py`:17; signals: mla; excerpt: "done" (https://github.com/sgl-project/sglang/pull/6109#discussion_r2080830953)
- `2025-05-09T03:09:30Z` `inline` by `neiltian-tencent` `test/srt/test_mla_flashmla.py`:44; signals: mla; excerpt: "done" (https://github.com/sgl-project/sglang/pull/6109#discussion_r2080831184)
- `2025-05-09T03:15:30Z` `inline` by `neiltian-tencent` `python/sglang/srt/model_executor/cuda_graph_runner.py`:214; signals: cuda; excerpt: "done" (https://github.com/sgl-project/sglang/pull/6109#discussion_r2080835090)
- `2025-05-14T23:13:26Z` `issue` by `PopSoda2002`; signals: mla; excerpt: "Hi @quinnrong94 , can you take a look at this CI fail? Hi @Fridge003 , I saw flashMLA test failed in CI, I wonder ..." (https://github.com/sgl-project/sglang/pull/6109#issuecomment-2881799707)
