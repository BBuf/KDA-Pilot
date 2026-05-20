# PR Discussion Digest

- Source PR: [vllm-project/vllm#12931](https://github.com/vllm-project/vllm/pull/12931)
- Source page: `sources/prs/vllm/PR-12931.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-12931`
- Generated at: `2026-05-20T15:33:54.184387+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-08T02:38:08Z`
- Merged: `2025-03-01T06:30:59Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 12
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=5, outdated=7
- Human participants with discussion text: mgoin, wyajieha
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-02-14T19:15:34Z` `COMMENTED` by `mgoin` - Looks pretty straight-foward, thanks for the nice work! My main questions are on supported hardware for non-Ampere and ... (https://github.com/vllm-project/vllm/pull/12931#pullrequestreview-2618548052)
- `2025-02-26T03:21:01Z` `APPROVED` by `mgoin` - Nicely integrated! I've enabled the full CI to run. I'm just a bit curious why you need the ... (https://github.com/vllm-project/vllm/pull/12931#pullrequestreview-2642940835)
- `2025-02-26T05:16:35Z` `COMMENTED` by `wyajieha` (https://github.com/vllm-project/vllm/pull/12931#pullrequestreview-2643094640)
- `2025-02-27T03:36:43Z` `COMMENTED` by `wyajieha` (https://github.com/vllm-project/vllm/pull/12931#pullrequestreview-2646483832)
- `2025-02-27T15:30:28Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/12931#pullrequestreview-2648196397)
- `2025-02-27T15:57:34Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/12931#pullrequestreview-2648285158)
- `2025-02-28T02:55:54Z` `COMMENTED` by `wyajieha` (https://github.com/vllm-project/vllm/pull/12931#pullrequestreview-2649594917)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/kernels/mixed_precision/allspark.py`: 6 inline comment(s)
- `csrc/quantization/gptq_allspark/allspark_qgemm_a16w8.cu`: 2 inline comment(s)
- `CMakeLists.txt`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/allspark_utils.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/gptq_allspark.py`: 1 inline comment(s)
- `vllm/_custom_ops.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-02-17T12:54:33Z` `issue` by `wyajieha`; signals: accuracy, cuda, hopper, kernel, perf, performance, sm90; excerpt: "Thanks for your detailed reply! The following are some additional points for explanation. 1. Here are full-model evaluation results with Qwen2-7B-Instruct-quantized.w8a16 model using the ..." (https://github.com/vllm-project/vllm/pull/12931#issuecomment-2663040072)
- `2025-02-26T05:16:35Z` `inline` by `wyajieha` `vllm/model_executor/layers/quantization/kernels/mixed_precision/allspark.py`:120; signals: benchmark, gemm, kernel, memory, perf, performance; excerpt: "The weight name pattern is mainly used to save the output tensors of different GEMM layer, which avoids frequent runtime calls to torch::empty for ..." (https://github.com/vllm-project/vllm/pull/12931#discussion_r1970921495)
- `2025-02-14T19:15:34Z` `review` `COMMENTED` by `mgoin`; signals: accuracy, kernel; excerpt: "Looks pretty straight-foward, thanks for the nice work! My main questions are on supported hardware for non-Ampere and if we could move this as ..." (https://github.com/vllm-project/vllm/pull/12931#pullrequestreview-2618548052)
- `2025-02-27T03:36:43Z` `inline` by `wyajieha` `vllm/model_executor/layers/quantization/kernels/mixed_precision/allspark.py`:74; signals: dtype, kernel; excerpt: "Hi @mgoin, I encountered a failure in the CI quantization tests specifically in the test compressed tensors wNa16 case where the assertion assert qkv ..." (https://github.com/vllm-project/vllm/pull/12931#discussion_r1972775157)
- `2025-02-17T20:46:00Z` `issue` by `mgoin`; signals: kernel, throughput; excerpt: "Thank you for the response @wyajieha ! 1. Your evals look good, and we see the throughput improvement! ✅ 2. Appreciate the clarity on ..." (https://github.com/vllm-project/vllm/pull/12931#issuecomment-2664048346)
- `2025-02-14T18:55:21Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/gptq_allspark.py`; signals: kernel; excerpt: "Since you are targeting the GPTQ format, you could likely leverage the existing MPLinearKernel abstraction to plug in GPTQAllSpark as a new possible kernel ..." (https://github.com/vllm-project/vllm/pull/12931#discussion_r1956593464)
- `2025-02-14T19:12:19Z` `inline` by `mgoin` `csrc/quantization/gptq_allspark/allspark_qgemm_a16w8.cu`:714; signals: gemm; excerpt: "Would be good to have a comment quickly describing the arg sweep, especially if it was tuned for a certain GPU/model size" (https://github.com/vllm-project/vllm/pull/12931#discussion_r1956610289)
- `2025-02-27T15:57:33Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/kernels/mixed_precision/allspark.py`:74; signals: kernel; excerpt: "@wyajieha You can simply remove the assertion. These tests are fairly old and made before we expanded the available kernels. We should be doing ..." (https://github.com/vllm-project/vllm/pull/12931#discussion_r1973883568)
- `2025-02-14T18:34:07Z` `inline` by `mgoin` `CMakeLists.txt`:301; signals: sm90; excerpt: "Do we need to support all of these arches? For instance are SM89 and SM90 realistic targets?" (https://github.com/vllm-project/vllm/pull/12931#discussion_r1956572371)
- `2025-02-14T19:11:29Z` `inline` by `mgoin` `csrc/quantization/gptq_allspark/allspark_qgemm_a16w8.cu`:666; signals: gemm; excerpt: "nit: extra ;" (https://github.com/vllm-project/vllm/pull/12931#discussion_r1956609477)
- `2025-02-26T03:19:40Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/kernels/mixed_precision/allspark.py`:120; signals: kernel; excerpt: "What is the purpose of the weight name pattern?" (https://github.com/vllm-project/vllm/pull/12931#discussion_r1970840948)
- `2025-02-27T15:30:28Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/kernels/mixed_precision/allspark.py`:74; signals: kernel; excerpt: "Oh I see.. I'm glad we ran into this. @dsikka do you think we could remove the assertion?" (https://github.com/vllm-project/vllm/pull/12931#discussion_r1973830548)
