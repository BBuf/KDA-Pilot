# PR Discussion Digest

- Source PR: [vllm-project/vllm#38960](https://github.com/vllm-project/vllm/pull/38960)
- Source page: `sources/prs/vllm/PR-38960.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38960`
- Generated at: `2026-05-20T15:40:38.439184+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-04T01:39:29Z`
- Merged: `2026-04-07T00:07:54Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 9
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=9
- Human participants with discussion text: mergify, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-04T01:45:46Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the MoE quantization logic by splitting the monolithic compressed tensors moe.py file ... (https://github.com/vllm-project/vllm/pull/38960#pullrequestreview-4057875177)
- `2026-04-06T19:12:11Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/38960#pullrequestreview-4063991830)
- `2026-04-06T19:12:21Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/38960#pullrequestreview-4063992617)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_w4a4_mxfp4.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_w4a4_nvfp4.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_w4a8_fp8.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_w4a8_int8.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_w8a8_fp8.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_w8a8_int8.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_wna16.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe_wna16_marlin.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-04T22:43:38Z` `issue` by `mergify`; signals: general review; excerpt: "Documentation preview:" (https://github.com/vllm-project/vllm/pull/38960#issuecomment-4187867603)
