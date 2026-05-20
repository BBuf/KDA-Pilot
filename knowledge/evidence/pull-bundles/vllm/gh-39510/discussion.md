# PR Discussion Digest

- Source PR: [vllm-project/vllm#39510](https://github.com/vllm-project/vllm/pull/39510)
- Source page: `sources/prs/vllm/PR-39510.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-39510`
- Generated at: `2026-05-20T13:27:11.299236+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-10T15:56:57Z`
- Merged: `2026-04-14T18:49:56Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 9
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=2, outdated=3
- Human participants with discussion text: amirkl94, danielafrimi, juhi10071998, mgoin
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-04-10T15:59:52Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces weight padding for TRTLLM NVFP4 MoE kernels to ensure hidden dimensions are ... (https://github.com/vllm-project/vllm/pull/39510#pullrequestreview-4090885840)
- `2026-04-10T16:06:41Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/39510#pullrequestreview-4090934840)
- `2026-04-12T07:58:15Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/39510#pullrequestreview-4094791258)
- `2026-04-12T08:08:11Z` `COMMENTED` by `amirkl94` (https://github.com/vllm-project/vllm/pull/39510#pullrequestreview-4094798422)
- `2026-04-12T09:35:24Z` `COMMENTED` by `danielafrimi` (https://github.com/vllm-project/vllm/pull/39510#pullrequestreview-4094871118)
- `2026-04-12T09:36:09Z` `COMMENTED` by `danielafrimi` (https://github.com/vllm-project/vllm/pull/39510#pullrequestreview-4094871670)
- `2026-04-12T10:00:42Z` `COMMENTED` by `danielafrimi` (https://github.com/vllm-project/vllm/pull/39510#pullrequestreview-4094890596)
- `2026-04-12T12:24:26Z` `COMMENTED` by `danielafrimi` (https://github.com/vllm-project/vllm/pull/39510#pullrequestreview-4095021001)
- `2026-04-14T18:48:20Z` `APPROVED` by `mgoin` - LGTM now, thanks! (https://github.com/vllm-project/vllm/pull/39510#pullrequestreview-4108361434)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`: 6 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-12T09:35:24Z` `inline` by `danielafrimi` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:122; signals: aligned, alignment, fp4, hang, moe, nvfp4, perf, performance; excerpt: "Weights are zero-padded to 256-alignment at load time and the MoE runner pads activations via maybe pad hidden states, so any hidden dim is ..." (https://github.com/vllm-project/vllm/pull/39510#discussion_r3069274495)
- `2026-04-12T10:00:42Z` `inline` by `danielafrimi` `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`:287; signals: flashinfer, fp4, hang, moe, nvfp4; excerpt: "Thanks, will change it. Since we're adding this warning and we're always padding the hidden dim in the trtllm MoE nvfp4 path, I think ..." (https://github.com/vllm-project/vllm/pull/39510#discussion_r3069299341)
- `2026-04-12T12:24:26Z` `inline` by `danielafrimi` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:201; signals: fp4, fp8, moe, nvfp4; excerpt: "@robertgshaw2-redhat removed the return hidden states like the FP8 path Now it will only return since we create and allocate the output tensor outside ..." (https://github.com/vllm-project/vllm/pull/39510#discussion_r3069448816)
- `2026-04-12T09:36:09Z` `inline` by `danielafrimi` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:201; signals: autotune, fp4, moe, nvfp4; excerpt: "Yes, since this is a dummy run, we can remove it for the autotuner. I'll remove it. thanks" (https://github.com/vllm-project/vllm/pull/39510#discussion_r3069275345)
- `2026-04-10T16:06:37Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/utils/flashinfer_utils.py`:287; signals: flashinfer, perf, performance; excerpt: "Should this be a performance warning due to needing activation slicing?" (https://github.com/vllm-project/vllm/pull/39510#discussion_r3065409966)
- `2026-04-12T07:58:16Z` `inline` by `amirkl94` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:122; signals: fp4, moe, nvfp4; excerpt: "@danielafrimi Isn't it required that hidden dim % 256 == 0 ?" (https://github.com/vllm-project/vllm/pull/39510#discussion_r3069179694)
- `2026-04-12T08:08:11Z` `inline` by `amirkl94` `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`:201; signals: fp4, moe, nvfp4; excerpt: "@danielafrimi Why is this zeroing needed here?" (https://github.com/vllm-project/vllm/pull/39510#discussion_r3069188501)
