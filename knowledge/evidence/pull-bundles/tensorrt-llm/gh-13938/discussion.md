# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13938](https://github.com/NVIDIA/TensorRT-LLM/pull/13938)
- Source page: `sources/prs/tensorrt-llm/PR-13938.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13938`
- Generated at: `2026-05-20T15:18:58.025078+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-09T09:53:02Z`
- Merged: `2026-05-10T07:37:50Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: lfr-0531, lishicheng1996-nv, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-09T12:40:57Z` `COMMENTED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/13938#pullrequestreview-4257783188)
- `2026-05-09T13:49:22Z` `COMMENTED` by `lishicheng1996-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13938#pullrequestreview-4257853957)
- `2026-05-09T15:16:00Z` `COMMENTED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/13938#pullrequestreview-4257959811)
- `2026-05-09T15:25:54Z` `APPROVED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/13938#pullrequestreview-4257972566)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/attention.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/custom_ops/__init__.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-09T13:49:22Z` `inline` by `lishicheng1996-nv` `tensorrt_llm/_torch/modules/attention.py`:1635; signals: attention, bf16, block, cute, sm100, tensorrt; excerpt: "Thanks for the review! Do we need keep the bf16 path for non-sm100 or use cute dsl blockscaling bmm=False (which is by default)? Side ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13938#discussion_r3213229710)
- `2026-05-09T12:35:38Z` `inline` by `lfr-0531` `tensorrt_llm/_torch/modules/attention.py`:469; signals: attention, block, cute, fp8, tensorrt; excerpt: "We already have use cute dsl blockscaling bmm in llm args, and we can enable it by setting use cute dsl blockscaling bmm: true ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13938#discussion_r3213150020)
- `2026-05-09T12:36:54Z` `inline` by `lfr-0531` `tensorrt_llm/_torch/modules/attention.py`:1635; signals: attention, bf16, fp8, tensorrt; excerpt: "Looks like we can drop this bf16 path now and keep only the FP8 one." (https://github.com/NVIDIA/TensorRT-LLM/pull/13938#discussion_r3213151329)
- `2026-05-09T15:16:00Z` `inline` by `lfr-0531` `tensorrt_llm/_torch/modules/attention.py`:1635; signals: attention, bf16, hopper, tensorrt; excerpt: "Ah, you're right. Let's keep this BF16 path for future Hopper support." (https://github.com/NVIDIA/TensorRT-LLM/pull/13938#discussion_r3213335879)
- `2026-05-09T12:40:48Z` `inline` by `lfr-0531` `tensorrt_llm/_torch/custom_ops/__init__.py`:1; signals: attention, tensorrt; excerpt: "We can simplify these comments, including the ones in attention.py." (https://github.com/NVIDIA/TensorRT-LLM/pull/13938#discussion_r3213155355)
- `2026-05-09T12:02:39Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47512]( [ run ] completed with state SUCCESS. Commit: 14b970b [/LLM/main/L0 MergeRequest PR pipeline 37430]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13938#issuecomment-4412471772)
- `2026-05-09T17:07:52Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47529]( [ run ] completed with state SUCCESS. Commit: cf8ec49 [/LLM/main/L0 MergeRequest PR pipeline 37446]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13938#issuecomment-4413075182)
- `2026-05-10T05:50:48Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47549]( [ run ] completed with state SUCCESS. Commit: 6997a88 [/LLM/main/L0 MergeRequest PR pipeline 37464]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13938#issuecomment-4414558222)
