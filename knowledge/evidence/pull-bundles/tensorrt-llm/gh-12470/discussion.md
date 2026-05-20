# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#12470](https://github.com/NVIDIA/TensorRT-LLM/pull/12470)
- Source page: `sources/prs/tensorrt-llm/PR-12470.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-12470`
- Generated at: `2026-05-20T15:18:10.404757+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-24T01:34:05Z`
- Merged: `2026-04-19T03:33:27Z`

## Discussion Counts

- Issue comments: 65
- Review submissions: 14 (approved=3, commented=11)
- Inline review comments: 26
- Review threads observed: 18
- Resolved/outdated thread markers: resolved=18, outdated=18
- Human participants with discussion text: PerkzZheng, QiJune, coderabbitai, heyuhhh, lfr-0531, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-24T01:48:46Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 10 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-3995766328)
- `2026-03-30T08:25:55Z` `COMMENTED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4028708516)
- `2026-03-30T08:42:00Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4028975216)
- `2026-03-30T08:42:23Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4028977126)
- `2026-03-30T08:46:04Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4028996680)
- `2026-03-30T08:47:11Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4029003679)
- `2026-03-30T08:47:32Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4029005593)
- `2026-03-30T08:48:11Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4029010012)
- `2026-03-30T08:49:10Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4029016405)
- `2026-03-31T14:41:14Z` `COMMENTED` by `PerkzZheng` (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4037919782)
- `2026-04-08T11:18:42Z` `COMMENTED` by `heyuhhh` (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4074706343)
- `2026-04-08T12:57:44Z` `APPROVED` by `PerkzZheng` (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4075232466)
- `2026-04-13T04:31:43Z` `APPROVED` by `QiJune` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4096409615)
- `2026-04-13T07:37:39Z` `APPROVED` by `lfr-0531` (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-4097080997)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`: 5 inline comment(s)
- `cpp/tensorrt_llm/thop/attentionOp.cpp`: 5 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaRunnerParams.h`: 4 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/sparse/kernel.py`: 2 inline comment(s)
- `tests/unittest/_torch/attention/sparse/test_sparse_attention.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaReduction.cu`: 2 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/trtllm.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/kernelParams.h`: 1 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/trtllm_gen.py`: 1 inline comment(s)
- `tests/unittest/_torch/attention/sparse/test_dsa_indexer.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-24T01:48:40Z` `issue` by `coderabbitai`; signals: attention, block, cache, correctness, hang, kernel, kv cache, layout; excerpt: "📝 Walkthrough Walkthrough This PR refactors sparse attention parameter naming and control flow across C++ kernel dispatchers and Python attention backends. It separates paged-sparse-attention ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#issuecomment-4114830704)
- `2026-03-24T01:48:46Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, hang, kernel, mla, nan, tensorrt; excerpt: "Actionable comments posted: 10 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#pullrequestreview-3995766328)
- `2026-03-24T01:48:44Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/kernelParams.h`:780; signals: attention, fp4, kernel, layout, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major FP4 sparse attention still reads scales from the dense KV layout. This branch flattens K/V into a 2-D sparse ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#discussion_r2978536812)
- `2026-03-24T01:48:44Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/thop/attentionOp.cpp`:378; signals: attention, cache, fp4, kv cache, nvfp4, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Reuse host primary pool pointer for sparse kv cache pool. Line 407 assumes host kv cache pool pointers is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#discussion_r2978536818)
- `2026-03-24T01:48:44Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/attention_backend/sparse/kernel.py`:1858; signals: attention, block, cute, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 122 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#discussion_r2978536832)
- `2026-03-30T08:42:00Z` `inline` by `heyuhhh` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`:353; signals: attention, hang, kernel, mla, tensorrt; excerpt: "We use an enum class to indicate the sparse type: So that different sparse attention will choose specific kernels. We only have sparse mla ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#discussion_r3008371958)
- `2026-03-24T01:48:44Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/attention_backend/sparse/kernel.py`:1910; signals: attention, cache, kernel, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Don’t silently synthesize stride factor from an incomplete formula. The documented page span includes num layers, but the fallback ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#discussion_r2978536837)
- `2026-03-24T01:48:44Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/attention_backend/trtllm_gen.py`:253; signals: attention, flashinfer, tensorrt, tma; excerpt: "⚠️ Potential issue 🟠 Major Don't advertise skip softmax support until this backend actually uses it. Line 243 returns True, but this file never ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#discussion_r2978536840)
- `2026-03-30T08:48:11Z` `inline` by `heyuhhh` `cpp/tensorrt_llm/thop/attentionOp.cpp`:377; signals: attention, cache, kv cache, tensorrt; excerpt: "use kv cache includes this check" (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#discussion_r3008403138)
- `2026-03-24T01:48:44Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/fmha/fmhaKernels.h`:436; signals: attention, kernel, tensorrt; excerpt: "⚠️ Potential issue 🔴 Critical Treat mSparseTopK == 0 as “unknown”, not “attend to zero tokens”. Line 435 collapses the attention window to 0 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#discussion_r2978536806)
- `2026-03-24T01:48:44Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/attention_backend/sparse/dsa.py`:794; signals: attention, benchmark, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Wrap this comparison to clear the lint failure. Flake8 is flagging this continuation with E123; the wrapped form keeps ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#discussion_r2978536820)
- `2026-03-24T01:48:44Z` `inline` by `coderabbitai` `tests/unittest/_torch/attention/sparse/test_dsa_indexer.py`:612; signals: attention, benchmark, block; excerpt: "⚠️ Potential issue 🟡 Minor The generation skip mock still has a dead draft-token adjustment. self.max draft tokens + 1 is a no-op, so ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/12470#discussion_r2978536843)
