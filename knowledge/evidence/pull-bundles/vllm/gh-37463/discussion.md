# PR Discussion Digest

- Source PR: [vllm-project/vllm#37463](https://github.com/vllm-project/vllm/pull/37463)
- Source page: `sources/prs/vllm/PR-37463.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-37463`
- Generated at: `2026-05-20T15:40:21.423132+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-18T17:01:03Z`
- Merged: `2026-04-17T23:42:32Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 7 (commented=7)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=3, outdated=4
- Human participants with discussion text: dsikka, eugr, geraldstanje, mergify, mgoin, yzong-rh, zyongye
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2026-03-18T17:06:54Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request introduces MXFP4 W4A4 MoE kernel support for SM100, including a new grouped GEMM ... (https://github.com/vllm-project/vllm/pull/37463#pullrequestreview-3969480455)
- `2026-03-19T22:11:02Z` `COMMENTED` by `dsikka` (https://github.com/vllm-project/vllm/pull/37463#pullrequestreview-3978266193)
- `2026-03-20T01:18:31Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/37463#pullrequestreview-3978832014)
- `2026-03-20T17:39:56Z` `COMMENTED` by `dsikka` (https://github.com/vllm-project/vllm/pull/37463#pullrequestreview-3983064201)
- `2026-03-20T18:20:21Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/37463#pullrequestreview-3983297344)
- `2026-04-16T20:43:21Z` `COMMENTED` by `zyongye` - LGTM. (https://github.com/vllm-project/vllm/pull/37463#pullrequestreview-4124306311)
- `2026-04-17T23:39:04Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/37463#pullrequestreview-4132812880)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a16_mxfp4.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/config.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/utils/quant_utils.py`: 1 inline comment(s)
- `csrc/quantization/fp4/mxfp4_blockwise_moe_kernel.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-24T01:52:13Z` `issue` by `geraldstanje`; signals: cutlass, flashinfer, fp4, fp8, kernel, moe, mxfp4, sm120; excerpt: "hi @Tib-Gridello will this pr also work for rtx 6000 pro (sm120) for gpt oss 20b? i used VLLM USE FLASHINFER MOE MXFP4 MXFP8 ..." (https://github.com/vllm-project/vllm/pull/37463#issuecomment-4114840015)
- `2026-04-01T14:45:07Z` `issue` by `mgoin`; signals: fp4, kernel, nvfp4, sm100, sm120; excerpt: "@geraldstanje no, this PR only adds a kernel for SM100. I think it would not be difficult to produce a similar SM120 version, like ..." (https://github.com/vllm-project/vllm/pull/37463#issuecomment-4170609910)
- `2026-03-19T22:10:56Z` `inline` by `dsikka` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:157; signals: fp4, moe, nvfp4; excerpt: "We'll need to update this, similar to nvfp4" (https://github.com/vllm-project/vllm/pull/37463#discussion_r2962974095)
- `2026-04-16T20:42:59Z` `inline` by `zyongye` `vllm/model_executor/layers/fused_moe/config.py`:766; signals: dtype, moe; excerpt: "Just want to clarify, if we don't specify a that means we are using the same dtype for weight and activation right?" (https://github.com/vllm-project/vllm/pull/37463#discussion_r3096250784)
- `2026-03-20T17:39:56Z` `inline` by `dsikka` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a16_mxfp4.py`:33; signals: fp4, mxfp4; excerpt: "why did you remove" (https://github.com/vllm-project/vllm/pull/37463#discussion_r2967106625)
- `2026-03-20T18:20:21Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_w4a16_mxfp4.py`:33; signals: fp4, mxfp4; excerpt: "I don't feel like we need so many of these "debug-like" messages, I can add it back" (https://github.com/vllm-project/vllm/pull/37463#discussion_r2967300179)
- `2026-03-18T19:31:04Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @mgoin, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/37463#issuecomment-4085089923)
- `2026-03-18T20:12:05Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @mgoin, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/37463#issuecomment-4085297376)
- `2026-04-13T20:30:56Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @mgoin, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/37463#issuecomment-4239426826)
- `2026-03-20T14:48:11Z` `issue` by `yzong-rh`; signals: fp4, mxfp4; excerpt: "cc @zyongye as this would conflict with your MXFP4 refactor: 37128" (https://github.com/vllm-project/vllm/pull/37463#issuecomment-4098580985)
- `2026-03-20T01:18:31Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:157; signals: moe; excerpt: "We can do in follow up" (https://github.com/vllm-project/vllm/pull/37463#discussion_r2963512955)
- `2026-04-17T23:39:00Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/config.py`:766; signals: moe; excerpt: "Correct" (https://github.com/vllm-project/vllm/pull/37463#discussion_r3103906858)
