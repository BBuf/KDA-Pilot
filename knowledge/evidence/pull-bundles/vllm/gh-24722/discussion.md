# PR Discussion Digest

- Source PR: [vllm-project/vllm#24722](https://github.com/vllm-project/vllm/pull/24722)
- Source page: `sources/prs/vllm/PR-24722.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-24722`
- Generated at: `2026-05-20T15:37:49.708157+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-12T05:45:41Z`
- Merged: `2025-11-29T15:19:34Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 21 (approved=1, commented=20)
- Inline review comments: 37
- Review threads observed: 25
- Resolved/outdated thread markers: resolved=23, outdated=16
- Human participants with discussion text: elvircrn, jinzhen-lin, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-12T05:48:27Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces significant enhancements to the Marlin kernels by adding W4A8 quantization support, which ... (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3214749834)
- `2025-09-18T22:19:05Z` `COMMENTED` by `elvircrn` - Great work! @mgoin asked me to take a look at this. Just a short question for now and ... (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3241979431)
- `2025-10-24T09:30:05Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3375349786)
- `2025-10-24T11:05:38Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3375793975)
- `2025-10-24T11:10:02Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3375814799)
- `2025-10-24T11:43:53Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3376022173)
- `2025-10-24T11:46:35Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3376040500)
- `2025-10-24T11:49:04Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3376059248)
- `2025-11-08T23:41:53Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3438985724)
- `2025-11-10T08:40:39Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3441614848)
- `2025-11-10T08:51:31Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3441684329)
- `2025-11-13T08:42:53Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3458426861)
- `2025-11-14T10:37:50Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3464283689)
- `2025-11-14T10:44:06Z` `COMMENTED` by `elvircrn` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3464317631)
- `2025-11-17T01:51:34Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3470682287)
- `2025-11-17T23:20:17Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3474898207)
- `2025-11-27T02:22:33Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3513334686)
- `2025-11-27T02:51:30Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3513383541)
- `2025-11-28T21:44:52Z` `COMMENTED` by `mgoin` - On the Blackwell lm-eval I see there is an accuracy issue - I ran twice to confirm Since ... (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3520053532)
- `2025-11-29T03:31:57Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3520455111)
- `2025-11-29T15:19:23Z` `APPROVED` by `mgoin` - Excellent work Jinzhen! Thank you for the diligent work on this w4a8 enhancement and general improvements to the ... (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3520734392)

## Inline Comment Hotspots

- `csrc/moe/marlin_moe_wna16/marlin_template.h`: 12 inline comment(s)
- `csrc/moe/marlin_moe_wna16/ops.cu`: 4 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_marlin_moe.py`: 4 inline comment(s)
- `vllm/envs.py`: 3 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/marlin_utils_fp4.py`: 3 inline comment(s)
- `csrc/moe/marlin_moe_wna16/generate_kernels.py`: 2 inline comment(s)
- `csrc/quantization/gptq_marlin/marlin_template.h`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/marlin_utils.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/fp8.py`: 2 inline comment(s)
- `csrc/quantization/gptq_marlin/generate_kernels.py`: 1 inline comment(s)
- `csrc/quantization/gptq_marlin/dequant.h`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-10T08:51:31Z` `inline` by `jinzhen-lin` `vllm/model_executor/layers/fused_moe/fused_marlin_moe.py`:146; signals: compile, moe, perf, performance, sm90, tile; excerpt: "atomic add only provides benefits when both m tiles and n tiles are extremely small. In the MoE scenario, m tiles will at least ..." (https://github.com/vllm-project/vllm/pull/24722#discussion_r2509363420)
- `2025-10-24T11:05:37Z` `inline` by `jinzhen-lin` `csrc/moe/marlin_moe_wna16/marlin_template.h`:528; signals: kernel, moe, perf, performance; excerpt: "Previously, I found that this logic could make w4a16-pr slower than w4a16-main in certain cases, so I temporarily removed it for debugging. However, in ..." (https://github.com/vllm-project/vllm/pull/24722#discussion_r2459834005)
- `2025-11-08T23:35:14Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/marlin_utils.py`:510; signals: compile, cuda, fp8, kernel; excerpt: "We should try to use the QuantFP8 class so we can dispatch between using the CUDA kernel or torch impl for custom or automatic ..." (https://github.com/vllm-project/vllm/pull/24722#discussion_r2507361172)
- `2025-11-10T08:40:39Z` `inline` by `jinzhen-lin` `csrc/moe/marlin_moe_wna16/generate_kernels.py`:264; signals: compile, kernel, moe, sm120; excerpt: "I specified in the CMakeLists.txt that the corresponding files should only be compiled for sm89 and sm120." (https://github.com/vllm-project/vllm/pull/24722#discussion_r2509315110)
- `2025-09-12T05:46:09Z` `issue` by `jinzhen-lin`; signals: accuracy, fp8, kernel, moe; excerpt: "Kernel Bench Test Dense Marlin Kernel Bench Test (on RTX 4090) MoE Marlin Kernel Bench Test E2E Bench Test E2E Accuracy Test GSM8K Metric ..." (https://github.com/vllm-project/vllm/pull/24722#issuecomment-3283767387)
- `2025-11-17T01:51:34Z` `inline` by `jinzhen-lin` `csrc/moe/marlin_moe_wna16/marlin_template.h`:1443; signals: compile, cuda, moe; excerpt: "It seems that the CUDA compiler cannot recognize that matmul only runs under the !is a 8bit branch. If we don’t add that check, ..." (https://github.com/vllm-project/vllm/pull/24722#discussion_r2532428493)
- `2025-11-08T22:59:41Z` `inline` by `mgoin` `csrc/moe/marlin_moe_wna16/generate_kernels.py`:264; signals: kernel, moe, sm90; excerpt: "Will sm90 and 100 still resolve to this?" (https://github.com/vllm-project/vllm/pull/24722#discussion_r2507345124)
- `2025-11-28T21:44:52Z` `review` `COMMENTED` by `mgoin`; signals: accuracy, blackwell; excerpt: "On the Blackwell lm-eval I see there is an accuracy issue - I ran twice to confirm Since it ran fine for lm-eval on ..." (https://github.com/vllm-project/vllm/pull/24722#pullrequestreview-3520053532)
- `2025-10-24T11:10:02Z` `inline` by `jinzhen-lin` `csrc/moe/marlin_moe_wna16/marlin_template.h`:597; signals: moe, warp; excerpt: "I have add the warp-level parallelized implement. There is a slight improvement when n and k are small, while for larger n and k, ..." (https://github.com/vllm-project/vllm/pull/24722#discussion_r2459848601)
- `2025-10-24T11:46:35Z` `inline` by `jinzhen-lin` `csrc/moe/marlin_moe_wna16/marlin_template.h`:597; signals: attention, moe; excerpt: "I didn’t pay attention to your advice earlier, so I only made the update just now after you reminded me again hh" (https://github.com/vllm-project/vllm/pull/24722#discussion_r2459999429)
- `2025-11-17T23:20:15Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:196; signals: failing, moe; excerpt: "I think you need to update the docs reference of CompressedTensorsW4A4MoeMethod to CompressedTensorsW4A4MoEMethod, I see the docs build failing" (https://github.com/vllm-project/vllm/pull/24722#discussion_r2535797280)
- `2025-09-18T20:25:28Z` `inline` by `elvircrn` `csrc/moe/marlin_moe_wna16/marlin_template.h`:597; signals: moe, warp; excerpt: "Can this search be warp-level parallelized?" (https://github.com/vllm-project/vllm/pull/24722#discussion_r2361088956)
