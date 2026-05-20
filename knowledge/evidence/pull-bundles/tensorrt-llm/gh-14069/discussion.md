# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#14069](https://github.com/NVIDIA/TensorRT-LLM/pull/14069)
- Source page: `sources/prs/tensorrt-llm/PR-14069.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-14069`
- Generated at: `2026-05-20T15:19:02.321886+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-13T02:58:45Z`
- Merged: `2026-05-17T19:20:51Z`

## Discussion Counts

- Issue comments: 30
- Review submissions: 12 (approved=2, changes_requested=1, commented=9)
- Inline review comments: 11
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: coderabbitai, dongfengy, jieli-matrix, tensorrt-cicd, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-13T03:02:13Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (1) tests/integration/defs/accuracy/test llm api pytorch.py (1) 5334-5335: QA list update is unnecessary for this PR. ... (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4277910482)
- `2026-05-15T03:16:08Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4295079873)
- `2026-05-15T03:24:42Z` `COMMENTED` by `dongfengy` (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4295117480)
- `2026-05-15T04:39:24Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4295435546)
- `2026-05-15T05:57:20Z` `COMMENTED` by `dongfengy` (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4295742096)
- `2026-05-15T06:09:24Z` `CHANGES_REQUESTED` by `jieli-matrix` - LGTM, but some comments from SDET perspective: The test-skip logic for H20+TRITON MXFP4 currently uses inline if … ... (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4295716726)
- `2026-05-15T06:28:32Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4295909831)
- `2026-05-15T06:28:42Z` `APPROVED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4295910461)
- `2026-05-15T22:43:22Z` `COMMENTED` by `dongfengy` (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4301805805)
- `2026-05-15T22:44:10Z` `COMMENTED` by `dongfengy` (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4301809465)
- `2026-05-15T22:44:33Z` `COMMENTED` by `dongfengy` (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4301811549)
- `2026-05-17T12:00:19Z` `APPROVED` by `jieli-matrix` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4305391670)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`: 9 inline comment(s)
- `tests/integration/defs/accuracy/test_llm_api_pytorch.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-13T03:02:10Z` `issue` by `coderabbitai`; signals: accuracy, cuda, fp4, h200, hang, layout, memory, moe; excerpt: "📝 Walkthrough Walkthrough This PR refines MXFP4 swizzling support in TensorRT-LLM by introducing a device-aware compatibility check and fixing tensor storage management. A new ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#issuecomment-4436771449)
- `2026-05-13T03:02:13Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, hang, moe, tensorrt, triton; excerpt: "🧹 Nitpick comments (1) tests/integration/defs/accuracy/test llm api pytorch.py (1) 5334-5335: QA list update is unnecessary for this PR. This patch only adjusts skip gating ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4277910482)
- `2026-05-15T06:09:24Z` `review` `CHANGES_REQUESTED` by `jieli-matrix`; signals: fp4, hang, layout, mxfp4, triton; excerpt: "LGTM, but some comments from SDET perspective: The test-skip logic for H20+TRITON MXFP4 currently uses inline if … pytest.skip() calls inside test method bodies. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#pullrequestreview-4295716726)
- `2026-05-15T05:51:19Z` `inline` by `jieli-matrix` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`:693; signals: fp4, moe, mxfp4, tensorrt, triton; excerpt: "actually the function imply the logic -- "skip on H20 since MXFP4 swizzle not supported". I suggest replace the current implementation with a marker ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#discussion_r3246165929)
- `2026-05-15T22:43:22Z` `inline` by `dongfengy` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`:734; signals: accuracy, kernel, moe, tensorrt, triton; excerpt: "This code is still needed. So we turn off swizzling due to H20 kernel issue here so that the test won't get accuracy = ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#discussion_r3251361064)
- `2026-05-15T22:44:10Z` `inline` by `dongfengy` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`:693; signals: fp4, moe, mxfp4, tensorrt, triton; excerpt: "skip no mxfp4 swizzle has been added." (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#discussion_r3251363825)
- `2026-05-15T03:24:41Z` `inline` by `dongfengy` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`:1155; signals: hang, moe, tensorrt, triton; excerpt: "The code here is more general and future-proof. For now we know that the old data is reused when not swizzling. But in the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#discussion_r3245675571)
- `2026-05-15T03:16:08Z` `inline` by `yuxianq` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`:1155; signals: moe, tensorrt, triton; excerpt: "We replace two tensors weight/scale here, for H20, don't need to replace both of them. So why don't we just skip the whole replacement ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#discussion_r3245644498)
- `2026-05-15T04:39:24Z` `inline` by `yuxianq` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`:1155; signals: moe, tensorrt, triton; excerpt: "If so, we can use if new weight.untyped storage().data ptr() != weight data.untyped storage().data ptr() instead of if not is swizzling supported(), is it ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#discussion_r3245936565)
- `2026-05-15T05:57:20Z` `inline` by `dongfengy` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`:1155; signals: moe, tensorrt, triton; excerpt: "I am not sure this can be further simplified. Could you clarify? This is supposed to be a best effort clean up of not ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#discussion_r3246187026)
- `2026-05-15T06:02:58Z` `inline` by `jieli-matrix` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`:734; signals: moe, tensorrt, triton; excerpt: "Given the new test skip decorator, I think the original code is okay since only skipping on H20?" (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#discussion_r3246208753)
- `2026-05-15T06:28:32Z` `inline` by `yuxianq` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`:1155; signals: moe, tensorrt, triton; excerpt: "Got it." (https://github.com/NVIDIA/TensorRT-LLM/pull/14069#discussion_r3246319237)
