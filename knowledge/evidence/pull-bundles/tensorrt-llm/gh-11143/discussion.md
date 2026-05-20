# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11143](https://github.com/NVIDIA/TensorRT-LLM/pull/11143)
- Source page: `sources/prs/tensorrt-llm/PR-11143.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11143`
- Generated at: `2026-05-20T15:17:39.919221+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-30T18:43:28Z`
- Merged: `2026-02-04T03:25:18Z`

## Discussion Counts

- Issue comments: 22
- Review submissions: 6 (approved=3, commented=3)
- Inline review comments: 10
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=6, outdated=2
- Human participants with discussion text: coderabbitai, litaotju, longlee0622, nekorobov, tensorrt-cicd, xxi-nv, yizhang-nv
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-02-03T03:37:52Z` `APPROVED` by `xxi-nv` - Overall, LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#pullrequestreview-3742610148)
- `2026-02-03T05:39:20Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#pullrequestreview-3743064706)
- `2026-02-03T13:55:32Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 6 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#pullrequestreview-3745423170)
- `2026-02-03T15:15:14Z` `COMMENTED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#pullrequestreview-3745362914)
- `2026-02-04T03:10:20Z` `APPROVED` by `litaotju` (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#pullrequestreview-3748704126)
- `2026-02-04T03:12:26Z` `APPROVED` by `yizhang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#pullrequestreview-3748707893)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_deepseekv3.py`: 2 inline comment(s)
- `tests/unittest/_torch/thop/serial/test_moe.py`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingDeepSeek.cu`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/runner.cu`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/runner.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-03T13:55:32Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, block, cache, cute, fp4, fp8, hang, kernel; excerpt: "Actionable comments posted: 6 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#pullrequestreview-3745423170)
- `2026-02-03T13:55:27Z` `issue` by `coderabbitai`; signals: autotune, block, cuda, cute, fp4, fp8, gemm, hang; excerpt: "📝 Walkthrough Walkthrough This pull request adds comprehensive fused shared expert support to TensorRT-LLM's MoE routing pipeline. Changes span CUDA kernels, C++ runners and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#issuecomment-3841477162)
- `2026-02-03T13:55:30Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/RoutingDeepSeek.cu`:721; signals: benchmark, block, hang, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Fix the fused‑shared expert limit error message. The current message is malformed and doesn’t report the actual fused-expert count, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#discussion_r2759214088)
- `2026-02-03T13:55:30Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/runner.cu`:129; signals: benchmark, block, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Guard against divide-by-zero and uneven expert partitioning. numDevices divides by localNumExperts; add validation to prevent undefined behavior if misconfigured. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#discussion_r2759214117)
- `2026-02-03T05:39:21Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:229; signals: moe, perf, performance, tensorrt; excerpt: "It appears that you're overriding the original behavior. The new method will invariably attempt to fuse the shared expert. Could I confirm whether this ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#discussion_r2757290970)
- `2026-02-03T13:55:30Z` `inline` by `coderabbitai` `cpp/tensorrt_llm/kernels/trtllmGenKernels/blockScaleMoe/runner.h`:156; signals: block, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Add Doxygen for the new numFusedSharedExpert parameter. Header prototypes should document newly introduced parameters to keep the API clear. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#discussion_r2759214130)
- `2026-02-03T13:55:31Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:178; signals: block, fp8, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Set num fused shared expert before create weights(). create weights() now sizes FP8 block‑scale weights based on num fused ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#discussion_r2759214136)
- `2026-02-03T13:55:31Z` `inline` by `coderabbitai` `tests/unittest/_torch/thop/serial/test_moe.py`:174; signals: benchmark, moe; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🌐 Web query: torch.range deprecated PyTorch torch.arange replacement 💡 Result: torch.range(start, end, step) is deprecated (and ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#discussion_r2759214145)
- `2026-02-03T13:43:39Z` `inline` by `nekorobov` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:229; signals: moe, tensorrt; excerpt: "Yes, @lishicheng1996 to confirm." (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#discussion_r2759162176)
- `2026-02-03T13:55:31Z` `inline` by `coderabbitai` `tests/unittest/_torch/thop/serial/test_moe.py`:1051; signals: moe; excerpt: "⚠️ Potential issue 🟡 Minor Remove or gate debug prints in tests. Unconditional prints can flood CI logs; consider guarding with an env flag ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#discussion_r2759214157)
- `2026-02-03T02:37:36Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/models/modeling_deepseekv3.py`:1209; signals: tensorrt; excerpt: "Is this a debug code? You are overriding the line 1203." (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#discussion_r2756914169)
- `2026-02-03T13:44:43Z` `inline` by `nekorobov` `tensorrt_llm/_torch/models/modeling_deepseekv3.py`:1209; signals: tensorrt; excerpt: "Great catch, let me remove this!" (https://github.com/NVIDIA/TensorRT-LLM/pull/11143#discussion_r2759167521)
