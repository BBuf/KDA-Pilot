# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12503](https://github.com/NVIDIA/TensorRT-LLM/pull/12503)
- Source page: `sources/prs/tensorrt-llm/PR-12503.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12503`
- Generated at: `2026-05-20T15:18:10.419786+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-24T14:03:21Z`
- Merged: `2026-03-31T12:53:37Z`

## Discussion Counts

- Issue comments: 24
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=2
- Human participants with discussion text: coderabbitai, hyukn, liji-nv, longlee0622, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-24T14:18:27Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#pullrequestreview-3999600551)
- `2026-03-31T01:57:22Z` `APPROVED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#pullrequestreview-4034175375)
- `2026-03-31T02:36:56Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#pullrequestreview-4034263638)
- `2026-03-31T02:56:08Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#pullrequestreview-4034323596)
- `2026-03-31T03:03:19Z` `COMMENTED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#pullrequestreview-4034344563)
- `2026-03-31T03:27:05Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#pullrequestreview-4034426287)
- `2026-03-31T03:32:32Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#pullrequestreview-4034445973)
- `2026-03-31T03:46:16Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#pullrequestreview-4034493631)
- `2026-03-31T05:12:54Z` `COMMENTED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#pullrequestreview-4034717948)
- `2026-03-31T05:55:56Z` `COMMENTED` by `liji-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#pullrequestreview-4034860485)
- `2026-03-31T07:09:33Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#pullrequestreview-4035188005)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/attention.py`: 6 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-24T14:06:28Z` `issue` by `coderabbitai`; signals: attention, block, cache, cuda, hang, mla, tensorrt; excerpt: "📝 Walkthrough Walkthrough The changes introduce DSA (Dynamic Sparse Attention) support for MLA by adding two new TRTLLM custom ops (mla dsa proj and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#issuecomment-4118592380)
- `2026-03-24T14:18:27Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, block, hang, mla, tensorrt; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (2) tensorrt llm/ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#pullrequestreview-3999600551)
- `2026-03-31T03:27:05Z` `inline` by `yuxianq` `tensorrt_llm/_torch/modules/attention.py`:2754; signals: attention, compile, hang, mla, tensorrt; excerpt: "2. We switch to mla dsa proj/mla dsa attn inplace in dsa case unconditionally, so we also disable short mha opt when torch compile ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#discussion_r3013272172)
- `2026-03-31T02:56:08Z` `inline` by `yuxianq` `tensorrt_llm/_torch/modules/attention.py`:2754; signals: attention, mla, perf, tensorrt; excerpt: "1. We dispatch dsa to mla dsa proj/mla dsa attn inplace here, but mla custom op inplace also dispatch dsa internally, are they duplicated? ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#discussion_r3013182073)
- `2026-03-31T05:12:54Z` `inline` by `liji-nv` `tensorrt_llm/_torch/modules/attention.py`:2754; signals: attention, compile, mla, tensorrt; excerpt: "mla dsa proj/mla dsa attn inplace it self supports short mha when torch compile disabled." (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#discussion_r3013547102)
- `2026-03-31T03:03:14Z` `inline` by `liji-nv` `tensorrt_llm/_torch/modules/attention.py`:2754; signals: attention, compile, tensorrt; excerpt: "1. I think yes, but we may remove it latter if merging this PR is urgent. 2. Yes when torch compile is enabled. The ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#discussion_r3013201169)
- `2026-03-31T02:36:57Z` `inline` by `yuxianq` `tensorrt_llm/_torch/modules/attention.py`:2764; signals: attention, tensorrt; excerpt: "proj outputs[:4] is enough." (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#discussion_r3013124383)
- `2026-03-31T03:32:32Z` `inline` by `yuxianq` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:1677; signals: attention, tensorrt; excerpt: "Should we move this assertion to the new forward instead of removing it?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#discussion_r3013289135)
- `2026-03-31T03:46:16Z` `inline` by `yuxianq` `tensorrt_llm/_torch/modules/attention.py`:999; signals: attention, tensorrt; excerpt: "Should we align with to use 1 instead of indexer.head dim // 128?" (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#discussion_r3013329501)
- `2026-03-31T05:55:56Z` `inline` by `liji-nv` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:1677; signals: attention, tensorrt; excerpt: "Moved to sparse attn indexer" (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#discussion_r3013676682)
- `2026-03-25T17:29:21Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 40315]( [ run ] completed with state SUCCESS. Commit: 55980ee [/LLM/main/L0 MergeRequest PR pipeline 31425]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#issuecomment-4128411421)
- `2026-03-26T00:25:41Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 40392]( Bot args parsing error: usage: /bot [-h] {run,kill,skip,submit,reviewers,reuse-pipeline,reuse-review} ... /bot: error: unrecognized arguments: —disable-fail-fast [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/12503#issuecomment-4130708616)
