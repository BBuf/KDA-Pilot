# PR Discussion Digest

- Source PR: [vllm-project/vllm#16038](https://github.com/vllm-project/vllm/pull/16038)
- Source page: `sources/prs/vllm/PR-16038.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16038`
- Generated at: `2026-05-20T15:34:48.684838+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-03T22:49:21Z`
- Merged: `2025-04-10T07:08:47Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: houseroad, luccafong, mgoin
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-09T19:29:26Z` `COMMENTED` by `luccafong` (https://github.com/vllm-project/vllm/pull/16038#pullrequestreview-2754574399)
- `2025-04-09T19:32:39Z` `COMMENTED` by `luccafong` (https://github.com/vllm-project/vllm/pull/16038#pullrequestreview-2754586569)
- `2025-04-09T19:34:10Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/16038#pullrequestreview-2754591198)
- `2025-04-09T19:45:26Z` `COMMENTED` by `houseroad` - Didn't see obvious wrong things. Is it possible to add some unittest? (https://github.com/vllm-project/vllm/pull/16038#pullrequestreview-2754615329)
- `2025-04-09T20:39:22Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/16038#pullrequestreview-2754760488)
- `2025-04-10T07:03:46Z` `APPROVED` by `luccafong` - Looks good to me, thanks for adding the integration! (https://github.com/vllm-project/vllm/pull/16038#pullrequestreview-2755562224)
- `2025-04-10T07:07:32Z` `APPROVED` by `houseroad` (https://github.com/vllm-project/vllm/pull/16038#pullrequestreview-2755571195)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-04-09T19:34:10Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:57; signals: cuda, gemm, kernel, moe, triton; excerpt: "It starts off low, basically equal at 16 experts but exponentially gets worse as experts increase such that at 100 experts it is essentially ..." (https://github.com/vllm-project/vllm/pull/16038#discussion_r2036026973)
- `2025-04-09T19:29:26Z` `inline` by `luccafong` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:57; signals: moe, perf; excerpt: "what's the perf gap on marlin when =16" (https://github.com/vllm-project/vllm/pull/16038#discussion_r2036018042)
- `2025-04-09T19:32:39Z` `inline` by `luccafong` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:62; signals: moe; excerpt: "not weight quant.actorder != "dynamic" based on comment?" (https://github.com/vllm-project/vllm/pull/16038#discussion_r2036024552)
- `2025-04-09T20:39:22Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:62; signals: moe; excerpt: "group is an alias for dynamic, but good point let me add both!" (https://github.com/vllm-project/vllm/pull/16038#discussion_r2036110467)
- `2025-04-09T19:45:26Z` `review` `COMMENTED` by `houseroad`; signals: general review; excerpt: "Didn't see obvious wrong things. Is it possible to add some unittest?" (https://github.com/vllm-project/vllm/pull/16038#pullrequestreview-2754615329)
