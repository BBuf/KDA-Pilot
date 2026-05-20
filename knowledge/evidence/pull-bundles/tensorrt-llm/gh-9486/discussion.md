# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#9486](https://github.com/NVIDIA/TensorRT-LLM/pull/9486)
- Source page: `sources/prs/tensorrt-llm/PR-9486.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-9486`
- Generated at: `2026-05-20T15:19:24.864059+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-26T08:22:14Z`
- Merged: `2025-12-01T00:37:07Z`

## Discussion Counts

- Issue comments: 31
- Review submissions: 35 (approved=4, commented=31)
- Inline review comments: 57
- Review threads observed: 29
- Resolved/outdated thread markers: resolved=29, outdated=12
- Human participants with discussion text: QiJune, bobboli, coderabbitai, dongxuy04, kaiyux, nekorobov, syuoni, tensorrt-cicd, tomeras91, xxi-nv
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-26T08:30:47Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3509668859)
- `2025-11-26T10:19:47Z` `COMMENTED` by `nekorobov` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3509815166)
- `2025-11-26T10:23:45Z` `COMMENTED` by `bobboli` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3510241768)
- `2025-11-26T10:24:28Z` `COMMENTED` by `bobboli` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3510244640)
- `2025-11-26T11:21:02Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3510441468)
- `2025-11-26T11:24:21Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3510451968)
- `2025-11-26T11:26:45Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3510459484)
- `2025-11-26T11:27:18Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3510461276)
- `2025-11-26T11:28:23Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3510464891)
- `2025-11-26T11:30:58Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3510475453)
- `2025-11-26T11:31:23Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3510477168)
- `2025-11-26T11:41:28Z` `COMMENTED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3510486274)
- `2025-11-26T12:14:44Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3510649697)
- `2025-11-26T12:18:33Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3510671365)
- `2025-11-27T00:41:50Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3513107572)
- `2025-11-27T00:55:39Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3513132109)
- `2025-11-27T10:24:06Z` `COMMENTED` by `bobboli` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3514024020)
- `2025-11-27T11:07:25Z` `COMMENTED` by `bobboli` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3514472047)
- `2025-11-27T11:09:11Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3514668763)
- `2025-11-27T11:12:48Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3514685461)
- `2025-11-27T11:46:23Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3514842194)
- `2025-11-27T11:46:42Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3514843193)
- `2025-11-27T11:50:03Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3514858540)
- `2025-11-28T05:48:05Z` `APPROVED` by `dongxuy04` (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3517551685)
- ... 11 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`: 23 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/communication/nvlink_one_sided.py`: 9 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_gpt_oss.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/interface.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/communication/communication_factory.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/communication/nvlink_two_sided.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_wide_ep.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/create_moe.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/modules/fused_moe/communication/deep_ep_low_latency.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-26T08:30:47Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, block, cache, correctness, cutlass, deepgemm, dtype, fp4; excerpt: "Actionable comments posted: 0 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#pullrequestreview-3509668859)
- `2025-11-26T08:30:44Z` `issue` by `coderabbitai`; signals: alignment, attention, cache, cutlass, deepgemm, dtype, fp4, fp8; excerpt: "📝 Walkthrough Walkthrough This pull request refactors the MoE framework with a new composition-based ConfigurableMoE class, communication strategy updates renaming MNNVL backends to NVLink ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#issuecomment-3580102213)
- `2025-11-26T12:18:32Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`:765; signals: memory, moe, perf, performance, tensorrt, tiling; excerpt: "I have confirmed with @jinyangyuan-nvidia , the original two stream have no sync, o, it is essentially equivalent to what I did in this ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#discussion_r2564777616)
- `2025-11-26T11:41:00Z` `inline` by `dongxuy04` `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`:765; signals: moe, perf, performance, tensorrt; excerpt: "I am not sure of the overlap performance here, e.g. is this Compute/Comm overlap? But maybe not important since this is not Alltoall case." (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#discussion_r2564654109)
- `2025-11-27T10:39:58Z` `inline` by `bobboli` `tensorrt_llm/_torch/modules/fused_moe/communication/communication_factory.py`:170; signals: latency, moe, tensorrt, throughput; excerpt: "We no longer need such a switch. Just try-catch in the following order (assume that init of Communication may throw RuntimeError): NVLinkOneSided NVLinkTwoSided DeepEP ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#discussion_r2568009097)
- `2025-11-26T10:23:45Z` `inline` by `bobboli` `tensorrt_llm/_torch/modules/fused_moe/communication/nvlink_one_sided.py`:116; signals: benchmark, moe, tensorrt; excerpt: "512 is not enough for some benchmarks in InferenceMax. The size will be automatically decided in the future, without the need to specify a ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#discussion_r2564418238)
- `2025-11-26T11:26:45Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/modules/fused_moe/communication/nvlink_one_sided.py`:170; signals: cutlass, moe, tensorrt; excerpt: "That's right, it is configurable and the parameters could be passed from the ConfigurableMoE. When the ConfigurableMoE supports cutlass as the new backend, it ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#discussion_r2564610515)
- `2025-11-26T11:30:58Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/modules/fused_moe/configurable_moe.py`:932; signals: attention, moe, tensorrt; excerpt: "I override the require routing separation in TRTLLMGenMoE, which will return true only when attention is DP." (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#discussion_r2564624087)
- `2025-11-27T10:28:24Z` `inline` by `bobboli` `tensorrt_llm/_torch/modules/fused_moe/communication/deep_ep_low_latency.py`:83; signals: latency, moe, tensorrt; excerpt: "Should we create an abstract function is platform supported in base class Communication? And call is platform supported in the init of the base ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#discussion_r2567965008)
- `2025-11-27T11:50:02Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/models/modeling_gpt_oss.py`; signals: hang, moe, tensorrt; excerpt: "To parse the MoE weights from the model weights, because after the MoE refactor, the name of the NamedModule is changed. So I need ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#discussion_r2568282011)
- `2025-11-28T15:11:04Z` `inline` by `syuoni` `tensorrt_llm/_torch/modules/fused_moe/communication/nvlink_one_sided.py`:170; signals: cutlass, moe, tensorrt; excerpt: "BTW, -1 should also work in CutlassMoE, any value out of the range [0, num local experts) is recognized as invalid expert ID." (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#discussion_r2571950538)
- `2025-11-29T00:05:04Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cutlass.py`:253; signals: cutlass, moe, tensorrt; excerpt: "Yeah, this is the preparatory work for cutlass. This PR focuses on the TRTLLMGenFusedMoE. I am going to implement the cutlass backend in the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/9486#discussion_r2572675358)
