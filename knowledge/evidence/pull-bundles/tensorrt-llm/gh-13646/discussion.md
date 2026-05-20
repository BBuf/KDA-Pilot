# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13646](https://github.com/NVIDIA/TensorRT-LLM/pull/13646)
- Source page: `sources/prs/tensorrt-llm/PR-13646.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13646`
- Generated at: `2026-05-20T15:18:49.439061+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-30T05:21:53Z`
- Merged: `2026-05-07T02:34:07Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: 2ez4bz, hyukn, lfr-0531, peihu-nv, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-04T16:18:07Z` `APPROVED` by `2ez4bz` (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#pullrequestreview-4221635434)
- `2026-05-05T23:02:04Z` `APPROVED` by `peihu-nv` - Tested both the accuracy and perf on B200 and GB200 MTP0/MTP1. All looking good. (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#pullrequestreview-4232110300)
- `2026-05-06T00:41:10Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#pullrequestreview-4232459560)
- `2026-05-06T06:56:05Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#pullrequestreview-4233897000)
- `2026-05-06T06:56:11Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#pullrequestreview-4233897538)

## Inline Comment Hotspots

- `tests/unittest/_torch/thop/parallel/test_dsv3_router_gemm.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_deepseekv4.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-05T23:02:04Z` `review` `APPROVED` by `peihu-nv`; signals: accuracy, b200, perf; excerpt: "Tested both the accuracy and perf on B200 and GB200 MTP0/MTP1. All looking good." (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#pullrequestreview-4232110300)
- `2026-05-04T16:16:45Z` `inline` by `2ez4bz` `tensorrt_llm/_torch/models/modeling_deepseekv4.py`:1329; signals: tensorrt; excerpt: "Just checking: is self.weight.t() a view or contiguous? If the former, would it be beneficial to assign the contiguous transpose to a variable that ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#discussion_r3182889802)
- `2026-05-04T16:18:04Z` `inline` by `2ez4bz` `tests/unittest/_torch/thop/parallel/test_dsv3_router_gemm.py`:13; signals: gemm; excerpt: "Just checking: how long does this test take to run? Note that the new parameterization for hidden size double the test execution time for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#discussion_r3182897078)
- `2026-05-06T06:56:11Z` `inline` by `hyukn` `tensorrt_llm/_torch/models/modeling_deepseekv4.py`:1329; signals: tensorrt; excerpt: "Thanks for the mentioning. Because the op wants the B matrix to be column major, .t() here will not introduce any copy. So I ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#discussion_r3193566203)
- `2026-05-06T00:41:09Z` `inline` by `hyukn` `tests/unittest/_torch/thop/parallel/test_dsv3_router_gemm.py`:13; signals: gemm; excerpt: "I think the router GEMM should not take too long to run. I can take some quick validations." (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#discussion_r3192355691)
- `2026-05-06T06:56:05Z` `inline` by `hyukn` `tests/unittest/_torch/thop/parallel/test_dsv3_router_gemm.py`:13; signals: gemm; excerpt: "The test takes less than 1s. It will not be a big deal. Thanks for mentioning." (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#discussion_r3193565785)
- `2026-05-05T16:15:11Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46830]( [ run ] completed with state FAILURE. Commit: 18a1270 [/LLM/main/L0 MergeRequest PR pipeline 36849]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#issuecomment-4381036090)
- `2026-05-05T17:52:38Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46843]( [ run ] completed with state FAILURE. Commit: 18a1270 [/LLM/main/L0 MergeRequest PR pipeline 36861]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#issuecomment-4381705593)
- `2026-05-06T17:24:18Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46851]( [ run ] completed with state SUCCESS. Commit: 591f210 [/LLM/main/L0 MergeRequest PR pipeline 36866]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#issuecomment-4390440813)
- `2026-05-07T02:32:39Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47056]( [ run ] completed with state SUCCESS. Commit: 591f210 [/LLM/main/L0 MergeRequest PR pipeline 37029]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13646#issuecomment-4393768422)
