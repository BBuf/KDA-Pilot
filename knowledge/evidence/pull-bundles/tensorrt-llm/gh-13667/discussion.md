# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13667](https://github.com/NVIDIA/TensorRT-LLM/pull/13667)
- Source page: `sources/prs/tensorrt-llm/PR-13667.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13667`
- Generated at: `2026-05-20T15:18:51.725244+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-30T14:50:31Z`
- Merged: `2026-05-08T13:29:42Z`

## Discussion Counts

- Issue comments: 49
- Review submissions: 6 (approved=3, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: SimengLiu-nv, coderabbitai, hyukn, rosenrodt, tensorrt-cicd, xxi-nv
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-03T07:49:48Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#pullrequestreview-4216041645)
- `2026-05-08T04:02:36Z` `APPROVED` by `hyukn` - LGTM overall. Thanks a lot for the improvements. We still need to figure out a better way of ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#pullrequestreview-4249406788)
- `2026-05-08T08:54:44Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#pullrequestreview-4250914590)
- `2026-05-08T08:54:49Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#pullrequestreview-4250915962)
- `2026-05-08T08:54:58Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#pullrequestreview-4250916775)
- `2026-05-08T09:59:20Z` `COMMENTED` by `rosenrodt` (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#pullrequestreview-4251363664)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-03T07:49:48Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, block, cache, fp4, fp8, hang, moe, mxfp4; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (3) tensorrt llm/ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#pullrequestreview-4216041645)
- `2026-05-03T07:49:45Z` `issue` by `coderabbitai`; signals: autotune, bf16, block, cache, cute, flashinfer, fp4, fp8; excerpt: "📝 Walkthrough Walkthrough The PR extends MoE autotuning infrastructure to support configurable dummy top-k generation modes (balanced or random) via environment variable, and propagates ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#issuecomment-4365688234)
- `2026-05-08T04:22:19Z` `issue` by `rosenrodt`; signals: autotune, flashinfer, hang, kernel, moe, regression; excerpt: "We still need to figure out a better way of preparing tuning data, and how to map the kernel correctly between warm-up and real ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#issuecomment-4403315336)
- `2026-05-03T16:50:17Z` `issue` by `SimengLiu-nv`; signals: cache, hang, kv cache; excerpt: "kv cache/test prefix aware scheduling.py::TestServePrefixAwareScheduling::test multi round qa shared prefix[swa-chunked] is a new test I added. Trying to understand if the failure is related ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#issuecomment-4366671660)
- `2026-05-03T16:59:30Z` `issue` by `SimengLiu-nv`; signals: cache, hang, kv cache; excerpt: "kv cache/test prefix aware scheduling.py::TestServePrefixAwareScheduling::test multi round qa shared prefix[swa-chunked] is a new test I added. Trying to understand if the failure is related ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#issuecomment-4366688935)
- `2026-05-04T05:13:14Z` `issue` by `rosenrodt`; signals: cache, hang, kv cache; excerpt: "kv cache/test prefix aware scheduling.py::TestServePrefixAwareScheduling::test multi round qa shared prefix[swa-chunked] is a new test I added. Trying to understand if the failure is related ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#issuecomment-4368436237)
- `2026-05-08T08:54:35Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:707; signals: moe, tensorrt; excerpt: "Do you need to update use dp for other quantization recipe?" (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#discussion_r3207540323)
- `2026-05-08T09:59:20Z` `inline` by `rosenrodt` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:707; signals: moe, tensorrt; excerpt: "Yep. Thanks for catching. I will enable them in next PR (pushing through the CI is really hard :))" (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#discussion_r3207901958)
- `2026-05-08T04:02:36Z` `review` `APPROVED` by `hyukn`; signals: kernel, regression; excerpt: "LGTM overall. Thanks a lot for the improvements. We still need to figure out a better way of preparing tuning data, and how to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#pullrequestreview-4249406788)
- `2026-05-01T03:20:02Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46394]( [ run ] completed with state SUCCESS. Commit: 7ebca22 [/LLM/main/L0 MergeRequest PR pipeline 36473]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#issuecomment-4357620483)
- `2026-05-03T11:06:38Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46586]( [ run ] completed with state SUCCESS. Commit: 665506c [/LLM/main/L0 MergeRequest PR pipeline 36635]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#issuecomment-4366015948)
- `2026-05-03T16:31:02Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46595]( [ run ] completed with state SUCCESS. Commit: 665506c [/LLM/main/L0 MergeRequest PR pipeline 36642]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13667#issuecomment-4366635865)
