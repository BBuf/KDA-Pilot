# PR Discussion Digest

- Source PR: [vllm-project/vllm#35986](https://github.com/vllm-project/vllm/pull/35986)
- Source page: `sources/prs/vllm/PR-35986.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35986`
- Generated at: `2026-05-20T15:40:05.330438+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-04T09:36:08Z`
- Merged: `2026-03-08T20:00:05Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 9
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: danisereb, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-04T09:40:43Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for ModelOpt MXFP8 MoE models by integrating a new kernel from ... (https://github.com/vllm-project/vllm/pull/35986#pullrequestreview-3888263054)
- `2026-03-04T10:12:11Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/35986#pullrequestreview-3888439932)
- `2026-03-04T10:21:52Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/35986#pullrequestreview-3888491132)
- `2026-03-08T11:36:22Z` `APPROVED` by `mgoin` - Looks good to me, nice work! Appreciate you setting up the oracle structure cc @robertgshaw2-redhat (https://github.com/vllm-project/vllm/pull/35986#pullrequestreview-3911281064)
- `2026-03-08T12:03:59Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/35986#pullrequestreview-3911368042)
- `2026-03-08T12:14:35Z` `COMMENTED` by `danisereb` (https://github.com/vllm-project/vllm/pull/35986#pullrequestreview-3911377745)

## Inline Comment Hotspots

- `tests/kernels/moe/test_ocp_mx_moe.py`: 4 inline comment(s)
- `vllm/model_executor/layers/quantization/modelopt.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-04T10:21:52Z` `inline` by `danisereb` `tests/kernels/moe/test_ocp_mx_moe.py`:25; signals: fp4, fp8, hang, kernel, moe, mxfp4; excerpt: "I did not use TRTLLM GEN MXFP8 AVAILABLE = TRTLLM GEN MXFP4 AVAILABLE in case the conditions for MXFP4 and MXFP8 are different. But ..." (https://github.com/vllm-project/vllm/pull/35986#discussion_r2882975711)
- `2026-03-08T12:14:35Z` `inline` by `danisereb` `vllm/model_executor/layers/fused_moe/layer.py`:1219; signals: block, fp4, moe, nvfp4; excerpt: "I think I followed what ModelOpt NVFP4 ModelOptNvFp4FusedMoE uses - FusedMoeWeightScaleSupported.BLOCK. I assume NVFP4 would also have to use GROUP since it is (1, ..." (https://github.com/vllm-project/vllm/pull/35986#discussion_r2901752179)
- `2026-03-04T10:12:11Z` `inline` by `danisereb` `vllm/model_executor/layers/quantization/modelopt.py`:1970; signals: flashinfer, fp8, moe; excerpt: "flashinfer 0.6.4 (what vLLM currently uses) does not support TRTLLM MXFP8 non-gated ReLU2 MoE. Support will be added later (in new flashinfer release). So ..." (https://github.com/vllm-project/vllm/pull/35986#discussion_r2882931855)
- `2026-03-08T10:16:47Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/layer.py`:1219; signals: block, fp8, moe; excerpt: "Technically, I think MXFP8 should be a GROUP scale rather than BLOCK since it is (1, 32)" (https://github.com/vllm-project/vllm/pull/35986#discussion_r2901642110)
- `2026-03-08T12:03:59Z` `inline` by `danisereb` `tests/kernels/moe/test_ocp_mx_moe.py`:991; signals: flashinfer, kernel, moe; excerpt: "non-gated MoE is not supported yet (in flashinfer 0.6.4), working on it:" (https://github.com/vllm-project/vllm/pull/35986#discussion_r2901741756)
- `2026-03-08T10:13:40Z` `inline` by `mgoin` `tests/kernels/moe/test_ocp_mx_moe.py`:991; signals: kernel, moe; excerpt: "Is non-gated not supported?" (https://github.com/vllm-project/vllm/pull/35986#discussion_r2901639401)
- `2026-03-04T10:36:47Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @danisereb, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/35986#issuecomment-3996672972)
- `2026-03-08T10:20:17Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/modelopt.py`:1970; signals: general review; excerpt: "Okay understood, you can ignore my comment on the test then" (https://github.com/vllm-project/vllm/pull/35986#discussion_r2901645429)
