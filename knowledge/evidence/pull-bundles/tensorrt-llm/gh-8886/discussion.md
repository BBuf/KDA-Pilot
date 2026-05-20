# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#8886](https://github.com/NVIDIA/TensorRT-LLM/pull/8886)
- Source page: `sources/prs/tensorrt-llm/PR-8886.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-8886`
- Generated at: `2026-05-20T15:19:19.682372+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-03T13:51:07Z`
- Merged: `2025-11-12T20:30:28Z`

## Discussion Counts

- Issue comments: 64
- Review submissions: 32 (approved=4, changes_requested=1, commented=27)
- Inline review comments: 37
- Review threads observed: 20
- Resolved/outdated thread markers: resolved=20, outdated=8
- Human participants with discussion text: bobboli, coderabbitai, dongxuy04, nekorobov, syuoni, tensorrt-cicd, xxi-nv, yuxianq
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-05T09:59:21Z` `COMMENTED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3420694552)
- `2025-11-06T08:09:29Z` `COMMENTED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3426799139)
- `2025-11-06T11:15:42Z` `COMMENTED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3427646711)
- `2025-11-06T11:25:19Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3427684207)
- `2025-11-07T01:40:56Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3431151197)
- `2025-11-07T03:42:48Z` `COMMENTED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3431476194)
- `2025-11-07T03:43:28Z` `COMMENTED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3431477075)
- `2025-11-07T03:43:42Z` `COMMENTED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3431477416)
- `2025-11-07T03:48:07Z` `COMMENTED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3431484151)
- `2025-11-07T04:21:23Z` `CHANGES_REQUESTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3431229650)
- `2025-11-07T06:24:21Z` `COMMENTED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3431650164)
- `2025-11-07T07:33:00Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3432064503)
- `2025-11-08T16:15:44Z` `APPROVED` by `bobboli` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3438465678)
- `2025-11-10T03:33:40Z` `APPROVED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3440679823)
- `2025-11-10T07:38:54Z` `COMMENTED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3441326902)
- `2025-11-10T07:38:59Z` `COMMENTED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3441327261)
- `2025-11-10T07:57:36Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3441406516)
- `2025-11-10T07:59:10Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3441413162)
- `2025-11-10T08:09:40Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3441451866)
- `2025-11-10T08:09:55Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3441452555)
- `2025-11-10T08:13:02Z` `COMMENTED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3441465567)
- `2025-11-10T08:25:43Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3441523085)
- `2025-11-10T08:27:01Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3441531997)
- `2025-11-10T08:27:09Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3441533170)
- ... 8 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/quantization.py`: 14 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`: 8 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/moe_load_balancer.py`: 5 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`: 4 inline comment(s)
- `cpp/tensorrt_llm/thop/mxFp4BlockScaleMoe.cpp`: 2 inline comment(s)
- `tests/integration/test_lists/test-db/l0_rtx_pro_6000.yml`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`: 1 inline comment(s)
- `tests/integration/test_lists/qa/llm_function_core.txt`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-06T11:25:19Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, alignment, b200, blackwell, cache, cute, cutlass, dtype; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#pullrequestreview-3427684207)
- `2025-11-05T09:07:55Z` `inline` by `nekorobov` `cpp/tensorrt_llm/thop/mxFp4BlockScaleMoe.cpp`:203; signals: block, fp4, fp8, moe, mxfp4, nvfp4, perf, tensorrt; excerpt: "Have you measured the perf impact of this? Also, do you need to do the same for other accuracies. I.e. DS FP8, FP8, NVFP4?" (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#discussion_r2493598431)
- `2025-11-06T11:25:15Z` `issue` by `coderabbitai`; signals: accuracy, aligned, attention, b200, block, cache, correctness, cute; excerpt: "📝 Walkthrough Walkthrough Integrates load-balancer support across MoE backends with slot-based token routing, GPU/CPU stage synchronization, and expert statistics tracking. Refactors weight loading for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#issuecomment-3496697184)
- `2025-11-06T11:15:42Z` `inline` by `dongxuy04` `cpp/tensorrt_llm/thop/mxFp4BlockScaleMoe.cpp`:203; signals: autotune, block, fp4, moe, mxfp4, tensorrt; excerpt: "It is just a temp fix of AutoTuner to verify EPLB works for2 88 case works. I think maybe we need separate PR to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#discussion_r2498561050)
- `2025-11-07T04:58:42Z` `inline` by `dongxuy04` `tensorrt_llm/_torch/modules/fused_moe/quantization.py`:1999; signals: block, hang, memory, moe, perf, tensorrt; excerpt: "I think different quantization has different weights loading method, and may need different transformations. So my judgement for now is keep them inside each ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#discussion_r2501687486)
- `2025-11-08T16:15:27Z` `inline` by `bobboli` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`:256; signals: cutlass, hang, moe, tensorrt, throughput; excerpt: "MnnvlThroughput doesn't support EPLB now. We can add this change either in this PR or in" (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#discussion_r2506999826)
- `2025-11-07T03:42:48Z` `inline` by `dongxuy04` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`:705; signals: cutlass, latency, moe, tensorrt; excerpt: "It is to avoid using multi-stream when using multi-chunk for MnnvlLatency, since MnnvlLatency need separate workspaces if we want to use multi-stream, but not ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#discussion_r2501574039)
- `2025-11-07T04:14:14Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/modules/fused_moe/quantization.py`:1999; signals: block, dtype, moe, tensorrt; excerpt: "Do you need to unify the behaviour in the weights loading in the base class? The non blocking is always True for now. dst ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#discussion_r2501622070)
- `2025-11-07T04:15:13Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/modules/fused_moe/quantization.py`:2001; signals: fp4, moe, mxfp4, tensorrt; excerpt: "It seems that the MXFP4 did not do the same logic here, could you help to explain why this is different?" (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#discussion_r2501623070)
- `2025-11-10T09:07:44Z` `inline` by `dongxuy04` `tensorrt_llm/_torch/modules/fused_moe/quantization.py`:1960; signals: block, hang, moe, tensorrt; excerpt: "Thanks a lot @yuxianq . I agree with you that it has no effect. But since many weights loading in quantization.py are using non ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#discussion_r2509430417)
- `2025-11-07T03:43:28Z` `inline` by `dongxuy04` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:359; signals: moe, perf, performance, tensorrt; excerpt: "Yes, it should have better performance if we move before routing method.apply(), moved, thanks." (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#discussion_r2501574764)
- `2025-11-08T16:14:34Z` `inline` by `bobboli` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_trtllm_gen.py`:185; signals: hang, moe, tensorrt, throughput; excerpt: "MnnvlThroughput doesn't support EPLB now. We can add this change either in this PR or in" (https://github.com/NVIDIA/TensorRT-LLM/pull/8886#discussion_r2506999499)
