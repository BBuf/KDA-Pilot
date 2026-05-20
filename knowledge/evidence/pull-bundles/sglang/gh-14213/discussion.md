# PR Discussion Digest

- Source PR: [sgl-project/sglang#14213](https://github.com/sgl-project/sglang/pull/14213)
- Source page: `sources/prs/sglang/PR-14213.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14213`
- Generated at: `2026-05-20T15:27:58.824156+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-01T10:06:59Z`
- Merged: `2025-12-04T12:00:06Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 15 (approved=2, commented=13)
- Inline review comments: 18
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=3, outdated=8
- Human participants with discussion text: JustinTong0323, Wangzheee, dcampora, elvischenv, fzyzcjy, hnyls2002, ishandhanani, ispobock, slin1237
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 6

## Review Decisions

- `2025-12-01T10:12:16Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for Mistral Large 3 and related models like Pixtral and Eagle. ... (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3524213476)
- `2025-12-01T15:19:06Z` `APPROVED` by `slin1237` (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3525556766)
- `2025-12-01T15:27:24Z` `COMMENTED` by `dcampora` (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3525607844)
- `2025-12-03T02:22:49Z` `COMMENTED` by `ispobock` - The dsv3 FP4 ci cannot pass: (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3532898057)
- `2025-12-03T09:38:01Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3534087433)
- `2025-12-03T12:14:34Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3534769232)
- `2025-12-03T13:39:43Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3534933853)
- `2025-12-04T05:16:10Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3538148385)
- `2025-12-04T05:18:41Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3538158078)
- `2025-12-04T05:54:02Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3538258095)
- `2025-12-04T06:27:19Z` `COMMENTED` by `elvischenv` (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3538346618)
- `2025-12-04T08:58:29Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3538815905)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 5 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8.py`: 3 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 3 inline comment(s)
- `python/sglang/srt/layers/attention/trtllm_mla_backend.py`: 2 inline comment(s)
- `python/sglang/srt/utils/hf_transformers_utils.py`: 1 inline comment(s)
- `python/sglang/srt/models/mistral_large_3.py`: 1 inline comment(s)
- `python/sglang/srt/models/mistral_large_3_eagle.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-03T16:56:41Z` `issue` by `dcampora`; signals: deepgemm, flashinfer, fp4, gemm, moe; excerpt: "@ispobock let's tackle Eagle3, DeepGEMM, flashinfer trtllm moe and FP4 support in follow-up MRs. We have removed the Eagle3 code from the PR." (https://github.com/sgl-project/sglang/pull/14213#issuecomment-3607838475)
- `2025-12-03T09:38:00Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:384; signals: aligned, dtype, moe, tma; excerpt: "The scale dtype is int32 after requant, it will throw this error in get mn major tma aligned tensor:" (https://github.com/sgl-project/sglang/pull/14213#discussion_r2584345915)
- `2025-12-03T12:14:34Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:384; signals: deepgemm, gemm, moe; excerpt: "Add SGLANG ENABLE JIT DEEPGEMM=0 to disable DeepGEMM can avoid this issue." (https://github.com/sgl-project/sglang/pull/14213#discussion_r2584880550)
- `2025-12-03T13:38:30Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/fp8.py`:920; signals: flashinfer, fp8, moe; excerpt: "For flashinfer trtllm moe, do we need to seperate a PR to support it?" (https://github.com/sgl-project/sglang/pull/14213#discussion_r2585155737)
- `2025-12-03T13:39:24Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_w8a8_fp8.py`:220; signals: deepgemm, fp8, gemm; excerpt: "TODO: add DeepGEMM support" (https://github.com/sgl-project/sglang/pull/14213#discussion_r2585158497)
- `2025-12-03T12:24:01Z` `issue` by `ispobock`; signals: attention, benchmark, fp8; excerpt: "gsm8k benchmark results: w/ FP8 attention: w/o FP8 attention:" (https://github.com/sgl-project/sglang/pull/14213#issuecomment-3606614230)
- `2025-12-04T05:54:02Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:805; signals: attention, mla; excerpt: "if we add this logic here, we will have to do the same thing for a ton of attn backends and sync them. thus ..." (https://github.com/sgl-project/sglang/pull/14213#discussion_r2587675334)
- `2025-12-04T06:27:19Z` `inline` by `elvischenv` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:805; signals: attention, mla; excerpt: "From Mistral's implementation in vLLM, the scaling is applied between RoPE and attention, so it implements inside the mla layer: In SGLang, for trtllm ..." (https://github.com/sgl-project/sglang/pull/14213#discussion_r2587740688)
- `2025-12-03T02:22:49Z` `review` `COMMENTED` by `ispobock`; signals: fp4; excerpt: "The dsv3 FP4 ci cannot pass:" (https://github.com/sgl-project/sglang/pull/14213#pullrequestreview-3532898057)
- `2025-12-04T05:16:04Z` `inline` by `ispobock` `python/sglang/srt/models/deepseek_v2.py`:1477; signals: hang; excerpt: "There are too many changes for introducing llama 4 scaling parameter here. Is there a better way to handle it?" (https://github.com/sgl-project/sglang/pull/14213#discussion_r2587584561)
- `2025-12-01T15:27:24Z` `inline` by `dcampora` `python/sglang/srt/layers/quantization/fp8.py`:989; signals: fp8; excerpt: "Fixed." (https://github.com/sgl-project/sglang/pull/14213#discussion_r2577556931)
- `2025-12-01T15:38:37Z` `issue` by `dcampora`; signals: nan; excerpt: "May I get clarification on some of the failures? For instance, what does [this one]( mean? CC @ishandhanani" (https://github.com/sgl-project/sglang/pull/14213#issuecomment-3597253307)
