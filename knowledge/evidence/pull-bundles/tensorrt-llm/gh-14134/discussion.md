# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#14134](https://github.com/NVIDIA/TensorRT-LLM/pull/14134)
- Source page: `sources/prs/tensorrt-llm/PR-14134.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-14134`
- Generated at: `2026-05-20T15:19:04.145412+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-14T09:28:48Z`
- Merged: `2026-05-19T08:19:53Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 8 (approved=4, commented=4)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=1
- Human participants with discussion text: 2ez4bz, Hudayday, PerkzZheng, coderabbitai, lancelly, lfr-0531, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-14T09:34:55Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#pullrequestreview-4288898587)
- `2026-05-14T21:23:27Z` `APPROVED` by `2ez4bz` - Approving changes for the modeling files. (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#pullrequestreview-4291598828)
- `2026-05-15T02:34:06Z` `COMMENTED` by `Hudayday` (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#pullrequestreview-4294851376)
- `2026-05-15T02:40:02Z` `COMMENTED` by `Hudayday` (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#pullrequestreview-4294883674)
- `2026-05-15T03:33:17Z` `COMMENTED` by `Hudayday` (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#pullrequestreview-4295157797)
- `2026-05-18T09:45:19Z` `APPROVED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#pullrequestreview-4309036699)
- `2026-05-18T12:28:45Z` `APPROVED` by `lancelly` - Scheduler changes looks good to me (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#pullrequestreview-4310120100)
- `2026-05-19T08:11:15Z` `APPROVED` by `PerkzZheng` (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#pullrequestreview-4317002464)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/models/modeling_gemma4mm.py`: 3 inline comment(s)
- `tensorrt_llm/inputs/registry.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-14T09:34:55Z` `review` `COMMENTED` by `coderabbitai`; signals: alignment, attention, cache, flashinfer, gemm, hang, kv cache, perf; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#pullrequestreview-4288898587)
- `2026-05-14T09:34:51Z` `issue` by `coderabbitai`; signals: alignment, attention, block, cache, flashinfer, gemm, hang, kernel; excerpt: "📝 Walkthrough Walkthrough This PR extends TensorRT-LLM to support multimodal Gemma4 inference with sliding-window attention constraints and scheduler-aware chunk alignment. It adds a window ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#issuecomment-4449500847)
- `2026-05-15T03:33:17Z` `inline` by `Hudayday` `tensorrt_llm/inputs/registry.py`:145; signals: attention, block, gemm, tensorrt; excerpt: "It has been added here as a template for any MM processors. Putting the default on the base class lets any subclass with a ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#discussion_r3245709896)
- `2026-05-14T09:34:54Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/models/modeling_gemma4mm.py`:330; signals: gemm, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Guard audio token counting when AutoProcessor fallback is active. Line 321 assumes self.processor.feature extractor always exists, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#discussion_r3240443904)
- `2026-05-14T09:34:54Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/pyexecutor/scheduler/scheduler_v2.py`:646; signals: block, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Re-check the rounded snap-up boundary before returning it. up block end is rounded past block end ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#discussion_r3240443911)
- `2026-05-14T21:21:57Z` `inline` by `2ez4bz` `tensorrt_llm/_torch/models/modeling_gemma4mm.py`:306; signals: gemm, tensorrt; excerpt: "Based on the code comment, wouldn't this be wrong? If so, should we raise an error instead?" (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#discussion_r3244357450)
- `2026-05-14T21:23:12Z` `inline` by `2ez4bz` `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`:321; signals: hang, tensorrt; excerpt: "Were these just cosmetic changes?" (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#discussion_r3244365109)
- `2026-05-15T02:34:06Z` `inline` by `Hudayday` `tensorrt_llm/_torch/models/modeling_gemma4mm.py`:306; signals: gemm, tensorrt; excerpt: "Yes, we should raise an error here. Thanks for the suggestion, fixed in the following commit." (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#discussion_r3245452701)
- `2026-05-15T02:40:01Z` `inline` by `Hudayday` `tensorrt_llm/_torch/models/modeling_multimodal_utils.py`:321; signals: tensorrt; excerpt: "Yes, those were cosmetic which I added when I was debugging. Reverted tensorrt llm/ torch/models/modeling multimodal utils.py to the original." (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#discussion_r3245479981)
- `2026-05-14T16:28:28Z` `inline` by `2ez4bz` `tensorrt_llm/inputs/registry.py`:145; signals: tensorrt; excerpt: "I might be missing something - why do we need this here if the check is on the instance at line 840?" (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#discussion_r3242778095)
- `2026-05-14T15:06:19Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48351]( [ run ] completed with state SUCCESS. Commit: 2042736 [/LLM/main/L0 MergeRequest PR pipeline 38157]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#issuecomment-4451923226)
- `2026-05-15T21:05:46Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48594]( [ run ] completed with state SUCCESS. Commit: 6b3bef6 [/LLM/main/L0 MergeRequest PR pipeline 38377]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14134#issuecomment-4463638507)
