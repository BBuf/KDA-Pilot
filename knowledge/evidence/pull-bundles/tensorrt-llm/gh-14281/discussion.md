# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#14281](https://github.com/NVIDIA/TensorRT-LLM/pull/14281)
- Source page: `sources/prs/tensorrt-llm/PR-14281.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-14281`
- Generated at: `2026-05-20T15:19:07.690711+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-19T01:50:45Z`
- Merged: `2026-05-19T21:37:59Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: bmarimuthu-nv, coderabbitai, nvchenghaoz, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-19T03:06:24Z` `COMMENTED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#pullrequestreview-4315375973)
- `2026-05-19T04:05:11Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#pullrequestreview-4315541693)
- `2026-05-19T04:08:29Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#pullrequestreview-4315551702)
- `2026-05-19T04:09:39Z` `COMMENTED` by `bmarimuthu-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#pullrequestreview-4315554712)
- `2026-05-19T20:08:07Z` `APPROVED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#pullrequestreview-4322771333)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/auto_deploy/custom_ops/fla/delta_rule/chunk.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/triton_moe.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/quantization/torch_quant.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-19T01:54:15Z` `issue` by `coderabbitai`; signals: block, gemm, hang, moe, nan, tensorrt, triton; excerpt: "ℹ️ Recent review info ⚙️ Run configuration Configuration used : Path: .coderabbit.yaml Review profile : CHILL Plan : Enterprise Run ID : d2c54d78-4b56-4d26-ad0f-8a10bfcf9b52 📥 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#issuecomment-4483764870)
- `2026-05-19T03:04:54Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/triton_moe.py`:1; signals: kernel, moe, tensorrt, triton; excerpt: "I remember when I ported this kernel, it is from sgLang project. Are we sure that vllm related code is being used?" (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#discussion_r3263410730)
- `2026-05-19T04:09:39Z` `inline` by `bmarimuthu-nv` `tensorrt_llm/_torch/auto_deploy/custom_ops/quantization/torch_quant.py`:3; signals: block, fp8, kernel, tensorrt; excerpt: "This is because the comment at [line 520 says]( "Adapted from sgl-project/sglang fp8 block matmul kernel"." (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#discussion_r3263579696)
- `2026-05-19T04:08:29Z` `inline` by `bmarimuthu-nv` `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/triton_moe.py`:1; signals: moe, tensorrt, triton; excerpt: "No direct vLLM code, but there are comments mentioning inspired from vLLM [here]( and [here](" (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#discussion_r3263576617)
- `2026-05-19T03:03:48Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/custom_ops/fla/delta_rule/chunk.py`:1; signals: tensorrt; excerpt: "The copyright is different from" (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#discussion_r3263407992)
- `2026-05-19T03:06:18Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/custom_ops/quantization/torch_quant.py`:3; signals: tensorrt; excerpt: "I cannot find torch quant file under sglang... Is sglang the source? cc + @Fridah-nv" (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#discussion_r3263414625)
- `2026-05-19T04:05:11Z` `inline` by `bmarimuthu-nv` `tensorrt_llm/_torch/auto_deploy/custom_ops/fla/delta_rule/chunk.py`:1; signals: tensorrt; excerpt: "thanks, fixed it!" (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#discussion_r3263567420)
- `2026-05-19T01:51:36Z` `issue` by `coderabbitai`; signals: perf; excerpt: "✅ Actions performed Summary regeneration triggered." (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#issuecomment-4483752477)
- `2026-05-19T20:21:43Z` `issue` by `tensorrt-cicd`; signals: general review; excerpt: "[PR Github 49259]( [ skip ] completed with state SUCCESS. Commit: 8bf53dd Skipping testing for commit 8bf53dd [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#issuecomment-4491715355)
- `2026-05-19T20:34:31Z` `issue` by `tensorrt-cicd`; signals: general review; excerpt: "[PR Github 49260]( [ skip ] completed with state SUCCESS. Commit: 8bf53dd Skipping testing for commit 8bf53dd [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/14281#issuecomment-4491811509)
