# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13575](https://github.com/NVIDIA/TensorRT-LLM/pull/13575)
- Source page: `sources/prs/tensorrt-llm/PR-13575.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13575`
- Generated at: `2026-05-20T15:18:47.023245+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-28T21:37:39Z`
- Merged: `2026-05-18T02:18:47Z`

## Discussion Counts

- Issue comments: 30
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 6
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=6
- Human participants with discussion text: jiaganc, lfr-0531, mikeiovine, tensorrt-cicd, yingguo-trt
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-14T19:46:17Z` `COMMENTED` by `mikeiovine` (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#pullrequestreview-4292932140)
- `2026-05-15T02:38:00Z` `APPROVED` by `yingguo-trt` (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#pullrequestreview-4294871855)
- `2026-05-15T02:46:13Z` `APPROVED` by `yingguo-trt` (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#pullrequestreview-4294922478)
- `2026-05-15T05:30:29Z` `COMMENTED` by `jiaganc` (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#pullrequestreview-4295562069)
- `2026-05-16T16:50:15Z` `COMMENTED` by `mikeiovine` (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#pullrequestreview-4303962128)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`: 2 inline comment(s)
- `tests/unittest/_torch/attention/sparse/rocketkv/test_rocketkv.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/model_config.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/modules/attention.py`: 1 inline comment(s)
- `tests/integration/test_lists/waives.txt`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-15T05:16:31Z` `inline` by `jiaganc` `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`:824; signals: attention, cache, dtype, tensorrt; excerpt: "model config.sparse attention config must have indexer k dtype, so you dont have to use getattr. Please use model config.sparse attention config.indexer k dtype ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#discussion_r3246049270)
- `2026-05-15T05:14:12Z` `inline` by `jiaganc` `tensorrt_llm/_torch/attention_backend/sparse/deepseek_v4/cache_manager.py`:204; signals: attention, cache, dtype, tensorrt; excerpt: "Could you move these codes into a new method like self. init indexer dtype()" (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#discussion_r3246041717)
- `2026-05-14T19:46:17Z` `inline` by `mikeiovine` `tests/unittest/_torch/attention/sparse/rocketkv/test_rocketkv.py`:296; signals: attention, hang; excerpt: "Not sure why the linter insisted on applying format changes to this file and a few others, can undo if you want Undid all ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#discussion_r3243870034)
- `2026-05-15T05:24:31Z` `inline` by `jiaganc` `tensorrt_llm/_torch/modules/attention.py`:1071; signals: attention, tensorrt; excerpt: "This line of code does nothing. Maybe remove it?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#discussion_r3246074517)
- `2026-05-15T05:23:30Z` `inline` by `jiaganc` `tensorrt_llm/_torch/model_config.py`:773; signals: tensorrt; excerpt: "Similarly, I don't think getattr is necessary here." (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#discussion_r3246071513)
- `2026-05-16T16:50:15Z` `inline` by `mikeiovine` `tests/integration/test_lists/waives.txt`:90; signals: failing; excerpt: "Confirmed test is failing on trunk locally" (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#discussion_r3253147920)
- `2026-05-14T23:06:33Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48423]( [ run ] completed with state SUCCESS. Commit: 9f6f0d5 [/LLM/main/L0 MergeRequest PR pipeline 38224]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#issuecomment-4455464979)
- `2026-05-15T23:56:26Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48633]( [ run ] completed with state FAILURE. Commit: ba16ae9 [/LLM/main/L0 MergeRequest PR pipeline 38415]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#issuecomment-4464602509)
- `2026-05-16T03:17:51Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48648]( [ run ] completed with state FAILURE. Commit: ba16ae9 [/LLM/main/L0 MergeRequest PR pipeline 38429]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#issuecomment-4465369152)
- `2026-05-16T16:26:17Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48693]( [ run ] completed with state FAILURE. Commit: ba16ae9 [/LLM/main/L0 MergeRequest PR pipeline 38467]( completed with status: 'ABORTED' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#issuecomment-4467429704)
- `2026-05-16T18:12:02Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48701]( [ run ] completed with state FAILURE. Commit: fded951 [/LLM/main/L0 MergeRequest PR pipeline 38472]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#issuecomment-4467714343)
- `2026-05-17T07:40:04Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48734]( [ run ] completed with state SUCCESS. Commit: d07d383 [/LLM/main/L0 MergeRequest PR pipeline 38500]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13575#issuecomment-4469789785)
