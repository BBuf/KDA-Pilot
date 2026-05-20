# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12642](https://github.com/NVIDIA/TensorRT-LLM/pull/12642)
- Source page: `sources/prs/tensorrt-llm/PR-12642.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12642`
- Generated at: `2026-05-20T15:18:12.885022+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-01T00:42:58Z`
- Merged: `2026-04-02T20:29:22Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 13
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=6
- Human participants with discussion text: coderabbitai, nvchenghaoz, suyoggupta, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-01T00:49:53Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 4 🧹 Nitpick comments (3) tensorrt llm/ torch/auto deploy/custom ops/attention/triton paged attention.py (2) 126-159: Consider ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#pullrequestreview-4041058158)
- `2026-04-01T17:28:57Z` `COMMENTED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#pullrequestreview-4045815402)
- `2026-04-01T17:29:23Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#pullrequestreview-4045833816)
- `2026-04-01T17:55:18Z` `COMMENTED` by `suyoggupta` (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#pullrequestreview-4045982927)
- `2026-04-01T22:14:22Z` `COMMENTED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#pullrequestreview-4047375733)
- `2026-04-01T22:17:26Z` `APPROVED` by `suyoggupta` (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#pullrequestreview-4047390400)

## Inline Comment Hotspots

- `tests/unittest/auto_deploy/singlegpu/custom_ops/attention/test_triton_paged_attention.py`: 9 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_paged_attention.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-04-01T00:49:53Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, correctness, flashinfer, hang, kernel, latency, nan, tensorrt; excerpt: "Actionable comments posted: 4 🧹 Nitpick comments (3) tensorrt llm/ torch/auto deploy/custom ops/attention/triton paged attention.py (2) 126-159: Consider documenting tensor shapes in docstring. Per ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#pullrequestreview-4041058158)
- `2026-04-01T00:49:48Z` `issue` by `coderabbitai`; signals: attention, cache, correctness, flashinfer, hang, kernel, kv cache, layout; excerpt: "📝 Walkthrough Walkthrough A new Triton-based paged attention implementation for TensorRT-LLM auto-deploy custom ops introduces two-stage FlashDecoding for decode operations, optimized context processing with ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#issuecomment-4166656022)
- `2026-04-01T17:55:18Z` `inline` by `suyoggupta` `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_paged_attention.py`:983; signals: attention, cuda, cudagraph, kernel, perf, tensorrt, triton; excerpt: "It is important we make sure this kernel works with cudagraphs. 2 options: (a) add a e2e model test that uses triton paged attention ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#discussion_r3023684824)
- `2026-04-01T00:49:51Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_paged_attention.py`:60; signals: attention, benchmark, cache, cuda, tensorrt, triton; excerpt: "⚠️ Potential issue 🟡 Minor Hardcoded device index may cause issues in multi-GPU setups. get num sms() always queries device 0, but the code ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#discussion_r3019173102)
- `2026-04-01T00:49:52Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_paged_attention.py`:1175; signals: attention, benchmark, tensorrt, triton; excerpt: "⚠️ Potential issue 🟡 Minor Unsupported attention arguments are logged but not rejected. The code logs a debug message when attn mask is not ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#discussion_r3019173108)
- `2026-04-01T00:49:52Z` `inline` by `coderabbitai` `tests/unittest/auto_deploy/singlegpu/custom_ops/attention/test_triton_paged_attention.py`:581; signals: attention, benchmark, flashinfer, triton; excerpt: "⚠️ Potential issue 🟡 Minor Incorrect pytest.mark.skipif usage causes test to always be skipped. The pytest.importorskip returns the imported module (truthy) on success, or ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#discussion_r3019173112)
- `2026-04-01T22:14:22Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/custom_ops/attention/triton_paged_attention.py`:983; signals: attention, perf, tensorrt, triton; excerpt: "updated and added the perf in the description." (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#discussion_r3024927406)
- `2026-04-01T00:49:52Z` `inline` by `coderabbitai` `tests/unittest/auto_deploy/singlegpu/custom_ops/attention/test_triton_paged_attention.py`:508; signals: attention, flashinfer, triton; excerpt: "⚠️ Potential issue 🟡 Minor Missing FlashInfer import protection in test decode vs flashinfer. Line 507 uses import flashinfer directly without skip protection. If ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#discussion_r3019173110)
- `2026-04-01T17:29:23Z` `inline` by `coderabbitai` `tests/unittest/auto_deploy/singlegpu/custom_ops/attention/test_triton_paged_attention.py`:508; signals: attention, flashinfer, triton; excerpt: "@nvchenghaoz, understood — if FlashInfer is guaranteed to be present in the test environment, the unprotected import is fine. Thanks for the clarification! --- ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#discussion_r3023551643)
- `2026-04-01T17:27:40Z` `inline` by `nvchenghaoz` `tests/unittest/auto_deploy/singlegpu/custom_ops/attention/test_triton_paged_attention.py`:295; signals: attention, nan, triton; excerpt: "compare the output with torch sdpa or other implementation, checking isnan and isinf is useless." (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#discussion_r3023542687)
- `2026-04-01T17:28:19Z` `inline` by `nvchenghaoz` `tests/unittest/auto_deploy/singlegpu/custom_ops/attention/test_triton_paged_attention.py`:508; signals: attention, flashinfer, triton; excerpt: "Not a concern as flashinfer will be installed by default." (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#discussion_r3023546130)
- `2026-04-01T17:26:00Z` `inline` by `nvchenghaoz` `tests/unittest/auto_deploy/singlegpu/custom_ops/attention/test_triton_paged_attention.py`:125; signals: attention, triton; excerpt: "Need more parameter combinations for this test." (https://github.com/NVIDIA/TensorRT-LLM/pull/12642#discussion_r3023534067)
