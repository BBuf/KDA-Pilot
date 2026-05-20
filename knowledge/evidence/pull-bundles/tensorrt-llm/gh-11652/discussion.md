# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11652](https://github.com/NVIDIA/TensorRT-LLM/pull/11652)
- Source page: `sources/prs/tensorrt-llm/PR-11652.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11652`
- Generated at: `2026-05-20T15:17:48.275504+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-23T13:21:00Z`
- Merged: `2026-03-10T21:48:20Z`

## Discussion Counts

- Issue comments: 32
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 8
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=7
- Human participants with discussion text: MrGeva, StanleySun639, coderabbitai, suyoggupta, tcherckez-nvidia, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-23T13:33:24Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 🧹 Nitpick comments (3) tensorrt llm/ torch/auto deploy/transform/library/fused moe.py (3) 2607-2639: Closure captures loop-scoped ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#pullrequestreview-3841092659)
- `2026-03-05T18:38:12Z` `COMMENTED` by `suyoggupta` (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#pullrequestreview-3898828649)
- `2026-03-08T07:55:31Z` `COMMENTED` by `tcherckez-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#pullrequestreview-3911150204)
- `2026-03-08T11:09:10Z` `COMMENTED` by `MrGeva` (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#pullrequestreview-3911324369)
- `2026-03-08T11:12:31Z` `COMMENTED` by `MrGeva` (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#pullrequestreview-3911326866)
- `2026-03-08T13:56:31Z` `COMMENTED` by `MrGeva` (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#pullrequestreview-3911495228)
- `2026-03-08T14:07:12Z` `APPROVED` by `MrGeva` (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#pullrequestreview-3911503437)
- `2026-03-09T05:18:49Z` `APPROVED` by `StanleySun639` (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#pullrequestreview-3912958416)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/auto_deploy/transform/library/fused_moe.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/trtllm_moe.py`: 3 inline comment(s)
- `extra-llm-api-config.yml`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-23T13:33:24Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, alignment, cache, epilogue, hang, moe, tensorrt, tile; excerpt: "Actionable comments posted: 3 🧹 Nitpick comments (3) tensorrt llm/ torch/auto deploy/transform/library/fused moe.py (3) 2607-2639: Closure captures loop-scoped variables — works but is fragile. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#pullrequestreview-3841092659)
- `2026-02-23T13:33:19Z` `issue` by `coderabbitai`; signals: accuracy, blackwell, cache, fp4, fp8, hang, kernel, kv cache; excerpt: "📝 Walkthrough Walkthrough This change introduces NVFP4 Mixture of Experts optimization using TRTLLM-Gen kernels with specialized weight shuffling and fusion transforms. It adds configuration ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#issuecomment-3944817187)
- `2026-02-23T13:33:23Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/trtllm_moe.py`:682; signals: bf16, cutlass, dtype, hang, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Hardcoded bfloat16 cast for topk weights may break fp16 models. Line 682 unconditionally casts routing weights to torch.bfloat16. If ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#discussion_r2840892459)
- `2026-02-23T13:33:22Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/trtllm_moe.py`:678; signals: cute, fp4, moe, nvfp4, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 840 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#discussion_r2840892448)
- `2026-03-05T18:38:12Z` `inline` by `suyoggupta` `tensorrt_llm/_torch/auto_deploy/transform/library/fused_moe.py`:2638; signals: fp4, moe, nvfp4, tensorrt, triton; excerpt: "couldn't we make part of the existing fuse nvfp4 moe transform, with an additional field "moe backend". I believe we're doing that for other ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#discussion_r2891574719)
- `2026-02-23T13:33:23Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/transform/library/fused_moe.py`:2654; signals: failing, kernel, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Silently defaulting top k=8 is dangerous — prefer failing explicitly. If the FX node doesn't carry shape metadata, the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#discussion_r2840892469)
- `2026-03-08T11:09:10Z` `inline` by `MrGeva` `tensorrt_llm/_torch/auto_deploy/transform/library/fused_moe.py`:2363; signals: kernel, moe, tensorrt; excerpt: "the function silently returns the scales here without shuffling or interleaving. The kernel then receives incorrectly formatted scales and will produce silently wrong output. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#discussion_r2901691460)
- `2026-03-08T11:12:31Z` `inline` by `MrGeva` `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/trtllm_moe.py`:835; signals: failing, moe, tensorrt; excerpt: "would be better to catch it in the transform that added this op, rather than failing here in runtime." (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#discussion_r2901694692)
- `2026-03-08T07:55:31Z` `inline` by `tcherckez-nvidia` `tensorrt_llm/_torch/auto_deploy/transform/library/fused_moe.py`:2638; signals: moe, tensorrt; excerpt: "Done. Thanks." (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#discussion_r2901506126)
- `2026-03-05T15:59:29Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 37857]( [ run ] completed with state SUCCESS. Commit: 4594b7b [/LLM/main/L0 MergeRequest PR pipeline 29311]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#issuecomment-4006097313)
- `2026-03-05T17:43:44Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 37893]( Bot args parsing error: usage: /bot [-h] {run,kill,skip,submit,reviewers,reuse-pipeline,reuse-review} ... /bot: error: unrecognized arguments: -reuse-test [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#issuecomment-4006639142)
- `2026-03-08T10:57:13Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 38132]( [ run ] completed with state SUCCESS. Commit: 6bc928b [/LLM/main/L0 MergeRequest PR pipeline 29540]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11652#issuecomment-4018835850)
