# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12055](https://github.com/NVIDIA/TensorRT-LLM/pull/12055)
- Source page: `sources/prs/tensorrt-llm/PR-12055.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12055`
- Generated at: `2026-05-20T15:17:56.823863+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-09T23:39:41Z`
- Merged: `2026-03-18T06:01:54Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: coderabbitai, peihu-nv, pengbowang-nv, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-18T04:46:57Z` `APPROVED` by `pengbowang-nv` - LGTM. Leaving a minor question. (https://github.com/NVIDIA/TensorRT-LLM/pull/12055#pullrequestreview-3965007110)
- `2026-03-18T05:36:20Z` `COMMENTED` by `peihu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/12055#pullrequestreview-3965199458)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-09T23:46:27Z` `issue` by `coderabbitai`; signals: accuracy, attention, gemm, hang, mla, tensorrt; excerpt: "📝 Walkthrough Walkthrough The changes refactor the Indexer weight fusion mechanism by introducing a post-load-weights method that fuses wk and weights proj tensors. The ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12055#issuecomment-4027666241)
- `2026-03-18T05:36:20Z` `inline` by `peihu-nv` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:1034; signals: attention, hang, memory, tensorrt; excerpt: "I actually considered cleaning up the original weights. Then after the change, I noticed that there are tests directly access wk.weight and weights proj.weight ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12055#discussion_r2951039364)
- `2026-03-18T04:46:12Z` `inline` by `pengbowang-nv` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:1034; signals: attention, tensorrt; excerpt: "nit: Do we need to cleanup the original weight? (should be 300mb for dsv3.2)" (https://github.com/NVIDIA/TensorRT-LLM/pull/12055#discussion_r2950855786)
- `2026-03-17T10:33:36Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 39188]( [ run ] completed with state SUCCESS. Commit: c7049ce [/LLM/main/L0 MergeRequest PR pipeline 30442]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12055#issuecomment-4073945499)
- `2026-03-17T20:18:39Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 39282]( [ run ] completed with state SUCCESS. Commit: 6f744c1 [/LLM/main/L0 MergeRequest PR pipeline 30540]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12055#issuecomment-4077757531)
