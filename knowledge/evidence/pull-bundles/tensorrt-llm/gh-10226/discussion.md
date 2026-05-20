# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#10226](https://github.com/NVIDIA/TensorRT-LLM/pull/10226)
- Source page: `sources/prs/tensorrt-llm/PR-10226.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-10226`
- Generated at: `2026-05-20T15:17:36.995432+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-23T08:36:13Z`
- Merged: `2025-12-24T06:39:12Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 10 (approved=1, commented=9)
- Inline review comments: 11
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=2
- Human participants with discussion text: coderabbitai, lfr-0531, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-23T08:41:45Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 🧹 Nitpick comments (1) tests/unittest/ torch/attention/sparse/test dsa indexer.py (1) 1026-1033: Redundant assignment and minor ... (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#pullrequestreview-3607122157)
- `2025-12-23T10:15:28Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#pullrequestreview-3607457412)
- `2025-12-23T10:17:56Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#pullrequestreview-3607464531)
- `2025-12-23T15:03:33Z` `COMMENTED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#pullrequestreview-3608370212)
- `2025-12-23T15:08:10Z` `COMMENTED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#pullrequestreview-3608386764)
- `2025-12-23T15:16:00Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#pullrequestreview-3608410523)
- `2025-12-23T15:16:23Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#pullrequestreview-3608412122)
- `2025-12-24T01:57:48Z` `COMMENTED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#pullrequestreview-3609723870)
- `2025-12-24T02:18:52Z` `COMMENTED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#pullrequestreview-3609750784)
- `2025-12-24T03:22:00Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#pullrequestreview-3609816964)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`: 7 inline comment(s)
- `tests/unittest/_torch/attention/sparse/test_dsa_indexer.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-12-23T08:41:45Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, block, deepgemm, fp8, gemm, hang, kernel, tensorrt; excerpt: "Actionable comments posted: 3 🧹 Nitpick comments (1) tests/unittest/ torch/attention/sparse/test dsa indexer.py (1) 1026-1033: Redundant assignment and minor suggestion. Line 1027 q fp8 = ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#pullrequestreview-3607122157)
- `2025-12-23T08:38:05Z` `issue` by `coderabbitai`; signals: attention, cache, deepgemm, gemm, hang, kernel, kv cache, sm100; excerpt: "📝 Walkthrough Walkthrough This change introduces SM version-aware MTP (Multi-Token Prediction) expanded buffer handling in sparse attention. A new use expanded buffers for mtp ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#issuecomment-3685736588)
- `2025-12-24T02:18:52Z` `inline` by `lfr-0531` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:748; signals: attention, deepgemm, fp8, gemm, sm100, sm90, tensorrt; excerpt: "Updated. There is another ongoing to update the DeepGEMM. After that PR, the fp8 paged mqa logits can also support max draft tokens = ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#discussion_r2644631508)
- `2025-12-23T15:08:10Z` `inline` by `lfr-0531` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:748; signals: attention, deepgemm, gemm, sm100, sm90, tensorrt; excerpt: "We also want to support max draft tokens 3. So for sm90, only when max draft tokens == 0/1, we don't need to use ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#discussion_r2643501853)
- `2025-12-23T08:41:44Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:749; signals: attention, sm100, sm90, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Operator precedence bug: the == 90 comparison is applied incorrectly. The expression (self.max draft tokens 1 and get sm ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#discussion_r2642408843)
- `2025-12-23T08:41:44Z` `inline` by `coderabbitai` `tests/unittest/_torch/attention/sparse/test_dsa_indexer.py`:523; signals: attention, benchmark; excerpt: "⚠️ Potential issue 🟠 Major Same operator precedence bug as in production code. The test mock mirrors the production code bug where == 90 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#discussion_r2642408848)
- `2025-12-23T10:17:56Z` `inline` by `yuxianq` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:748; signals: attention, tensorrt; excerpt: "Why we use self.max draft tokens 1 when the comment says "seq len == 1/2", and use self.max draft tokens == 2 or self.max ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#discussion_r2642688770)
- `2025-12-23T15:16:00Z` `inline` by `yuxianq` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:748; signals: attention, tensorrt; excerpt: "Got it. Can we also add the max draft tokens part to the comment? E.g., "seq len == 1/2/4" - "seq len == 1/2/4 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#discussion_r2643522413)
- `2025-12-24T01:57:48Z` `inline` by `lfr-0531` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:748; signals: attention, tensorrt; excerpt: "Sure, will do." (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#discussion_r2644607433)
- `2025-12-23T08:41:45Z` `inline` by `coderabbitai` `tests/unittest/_torch/attention/sparse/test_dsa_indexer.py`:544; signals: attention; excerpt: "⚠️ Potential issue 🟠 Major Bug: Comparing boolean to integer. use expanded buffers for mtp is a boolean, so 1 will always be False ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#discussion_r2642408851)
- `2025-12-23T10:15:28Z` `inline` by `yuxianq` `tests/unittest/_torch/attention/sparse/test_dsa_indexer.py`:544; signals: attention; excerpt: "self.use expanded buffers for mtp 1 - self.use expanded buffers for mtp" (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#discussion_r2642682355)
- `2025-12-23T15:03:33Z` `inline` by `lfr-0531` `tests/unittest/_torch/attention/sparse/test_dsa_indexer.py`:544; signals: attention; excerpt: "Thanks, Yuxian! Fixed." (https://github.com/NVIDIA/TensorRT-LLM/pull/10226#discussion_r2643489935)
