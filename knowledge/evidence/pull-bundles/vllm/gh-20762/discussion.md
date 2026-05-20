# PR Discussion Digest

- Source PR: [vllm-project/vllm#20762](https://github.com/vllm-project/vllm/pull/20762)
- Source page: `sources/prs/vllm/PR-20762.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-20762`
- Generated at: `2026-05-20T15:36:14.671358+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-10T14:49:38Z`
- Merged: `2025-07-17T13:56:44Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: ElizaWszola, mergify, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-10T14:50:31Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @ElizaWszola, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/20762#pullrequestreview-3006088683)
- `2025-07-10T14:52:04Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces performance improvements for non-blockwise fp8 CUTLASS MoE. The main changes include pre-calculating ... (https://github.com/vllm-project/vllm/pull/20762#pullrequestreview-3006096795)
- `2025-07-15T15:33:14Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/20762#pullrequestreview-3020994778)
- `2025-07-15T15:45:19Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/20762#pullrequestreview-3021048255)
- `2025-07-15T15:46:03Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/20762#pullrequestreview-3021050570)
- `2025-07-15T15:52:57Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/20762#pullrequestreview-3021073279)
- `2025-07-15T15:54:35Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/20762#pullrequestreview-3021078590)

## Inline Comment Hotspots

- `tests/kernels/moe/test_cutlass_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/cutlass_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 1 inline comment(s)
- `csrc/moe/moe_permute_unpermute_op.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-15T15:45:19Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:160; signals: cute, cutlass, kernel, moe, speedup; excerpt: "Does the speedup mentioned in this statement Faster kernels for shuffling hidden states, input scales and outputs of the function that executes CUTLASS MoE ..." (https://github.com/vllm-project/vllm/pull/20762#discussion_r2207889365)
- `2025-07-15T15:33:13Z` `inline` by `tlrmchlsmth` `tests/kernels/moe/test_cutlass_moe.py`:449; signals: cutlass, kernel, memory, moe; excerpt: "Could we save on memory by using the same tensor for both ab strides1 and cstrides2?" (https://github.com/vllm-project/vllm/pull/20762#discussion_r2207857711)
- `2025-07-15T15:54:34Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:160; signals: cutlass, kernel, moe; excerpt: "It comes from using these custom kernels instead of the pytorch index-based function. The "slow" kernels are expected to only be run to shuffle ..." (https://github.com/vllm-project/vllm/pull/20762#discussion_r2207908359)
- `2025-07-15T15:52:57Z` `inline` by `ElizaWszola` `tests/kernels/moe/test_cutlass_moe.py`:449; signals: cutlass, kernel, moe; excerpt: "Yes, this should be possible. I'll push an update" (https://github.com/vllm-project/vllm/pull/20762#discussion_r2207905261)
- `2025-07-10T14:50:26Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @ElizaWszola." (https://github.com/vllm-project/vllm/pull/20762#issuecomment-3057794932)
- `2025-07-11T03:27:15Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @ElizaWszola." (https://github.com/vllm-project/vllm/pull/20762#issuecomment-3060236835)
- `2025-07-13T02:45:46Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @ElizaWszola." (https://github.com/vllm-project/vllm/pull/20762#issuecomment-3066358467)
- `2025-07-16T03:15:59Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @ElizaWszola." (https://github.com/vllm-project/vllm/pull/20762#issuecomment-3076573371)
