# PR Discussion Digest

- Source PR: [vllm-project/vllm#29901](https://github.com/vllm-project/vllm/pull/29901)
- Source page: `sources/prs/vllm/PR-29901.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29901`
- Generated at: `2026-05-20T15:38:51.124846+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-02T16:55:01Z`
- Merged: `2025-12-16T22:35:28Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 5 (commented=5)
- Inline review comments: 6
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=4
- Human participants with discussion text: chatgpt-codex-connector, gesong2077, jinzhen-lin, mergify, mgoin, mokieli, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-12-02T16:57:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for the Turing architecture (sm75) to the Marlin kernels, including both ... (https://github.com/vllm-project/vllm/pull/29901#pullrequestreview-3531215676)
- `2025-12-02T17:01:29Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/29901#pullrequestreview-3531237596)
- `2025-12-09T03:00:01Z` `COMMENTED` by `mgoin` - This looks really solid. It seems the added complexity isn't much, just the emulation and fp16 accum. Am ... (https://github.com/vllm-project/vllm/pull/29901#pullrequestreview-3555064870)
- `2025-12-09T03:23:17Z` `COMMENTED` by `jinzhen-lin` (https://github.com/vllm-project/vllm/pull/29901#pullrequestreview-3555176956)
- `2025-12-16T22:31:49Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/29901#pullrequestreview-3585230599)

## Inline Comment Hotspots

- `csrc/moe/marlin_moe_wna16/generate_kernels.py`: 2 inline comment(s)
- `csrc/quantization/gptq_marlin/marlin_mma.h`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/mxfp4.py`: 1 inline comment(s)
- `CMakeLists.txt`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/modelopt.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-02T17:01:29Z` `inline` by `chatgpt-codex-connector` `csrc/quantization/gptq_marlin/marlin_mma.h`:167; signals: aligned, block, cuda, kernel, perf, performance, throughput; excerpt: "&& CUDA ARCH == 750 true, which is always true, so even on Ampere/Ada we always take the sm75 path that issues two mma.sync.aligned.m16n8k8 ..." (https://github.com/vllm-project/vllm/pull/29901#discussion_r2582089709)
- `2025-12-16T22:31:46Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/modelopt.py`; signals: fp4, fp8, kernel, moe, nvfp4; excerpt: "Don't we need to update other places as well? Such as vllm/model executor/layers/quantization/kernels/mixed precision/marlin.py, vllm/model executor/layers/quantization/compressed tensors/schemes/compressed tensors w8a16 fp8.py, vllm/model executor/layers/quantization/compressed tensors/schemes/compressed tensors ..." (https://github.com/vllm-project/vllm/pull/29901#discussion_r2624964381)
- `2025-12-16T03:02:51Z` `issue` by `jinzhen-lin`; signals: benchmark, gemm, kernel, moe, speedup; excerpt: "Could you show a benchmark comparing the original GPTQ to this Marlin gemm on turing? I'm curious if there is a large speedup. Also ..." (https://github.com/vllm-project/vllm/pull/29901#issuecomment-3658516156)
- `2025-12-02T17:01:29Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/quantization/mxfp4.py`:188; signals: bf16, fp4, kernel, mxfp4; excerpt: "to 75 makes MXFP4 appear supported on Turing GPUs, but the marlin kernels explicitly reject any sm75 activation that is not FP16 or INT8 ..." (https://github.com/vllm-project/vllm/pull/29901#discussion_r2582089733)
- `2025-12-15T22:59:31Z` `issue` by `mgoin`; signals: benchmark, gemm, moe, speedup; excerpt: "Could you show a benchmark comparing the original GPTQ to this Marlin gemm on turing? I'm curious if there is a large speedup. Also ..." (https://github.com/vllm-project/vllm/pull/29901#issuecomment-3657954615)
- `2025-12-09T03:19:53Z` `issue` by `jinzhen-lin`; signals: bf16, fp4, mxfp4; excerpt: "This looks really solid. It seems the added complexity isn't much, just the emulation and fp16 accum. Am I correct that it supports all ..." (https://github.com/vllm-project/vllm/pull/29901#issuecomment-3630060061)
- `2025-12-15T22:55:58Z` `issue` by `mgoin`; signals: bf16, fp4, mxfp4; excerpt: "@jinzhen-lin Personally I think supporting MXFP4 x FP16 is too confusing, especially since MXFP4 is still hardcoded for GPT-OSS at the moment with BF16 ..." (https://github.com/vllm-project/vllm/pull/29901#issuecomment-3657946710)
- `2025-12-16T03:06:15Z` `issue` by `jinzhen-lin`; signals: bf16, fp4, mxfp4; excerpt: "@jinzhen-lin Personally I think supporting MXFP4 x FP16 is too confusing, especially since MXFP4 is still hardcoded for GPT-OSS at the moment with BF16 ..." (https://github.com/vllm-project/vllm/pull/29901#issuecomment-3658522576)
- `2025-12-09T02:55:54Z` `inline` by `mgoin` `csrc/moe/marlin_moe_wna16/generate_kernels.py`:170; signals: kernel, moe; excerpt: "Is this intentional? It seems like it removes bfloat16 from the regular result dict" (https://github.com/vllm-project/vllm/pull/29901#discussion_r2600887662)
- `2025-12-09T03:23:17Z` `inline` by `jinzhen-lin` `csrc/moe/marlin_moe_wna16/generate_kernels.py`:170; signals: kernel, moe; excerpt: "I removed that part during the testing phase and later forgot to add it back." (https://github.com/vllm-project/vllm/pull/29901#discussion_r2600937146)
- `2025-12-12T05:42:02Z` `issue` by `jinzhen-lin`; signals: fp4, mxfp4; excerpt: "@mgoin I have added MXFP4 x FP16 support (and added necessray check). If you think this support is inappropriate, I can revert it." (https://github.com/vllm-project/vllm/pull/29901#issuecomment-3645001550)
- `2025-12-12T05:43:20Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @jinzhen-lin, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/29901#issuecomment-3645004091)
