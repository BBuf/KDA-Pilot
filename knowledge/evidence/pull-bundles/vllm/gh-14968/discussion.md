# PR Discussion Digest

- Source PR: [vllm-project/vllm#14968](https://github.com/vllm-project/vllm/pull/14968)
- Source page: `sources/prs/vllm/PR-14968.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14968`
- Generated at: `2026-05-20T15:34:33.205276+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-17T15:33:00Z`
- Merged: `2025-05-14T02:08:21Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 8 (approved=2, commented=6)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: DarkLight1337, ProExpertProg, SageMoore, houseroad, mergify, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-31T15:29:08Z` `COMMENTED` by `SageMoore` - This generally looks fine. What models are you all using this kernel with? If there are any models ... (https://github.com/vllm-project/vllm/pull/14968#pullrequestreview-2729696157)
- `2025-04-23T00:55:51Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/14968#pullrequestreview-2785697813)
- `2025-04-23T01:57:32Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/14968#pullrequestreview-2785760686)
- `2025-05-12T20:35:54Z` `COMMENTED` by `SageMoore` - In general this looks fine, but let's iron out this "is cutlass supported logic" ironed out before landing. (https://github.com/vllm-project/vllm/pull/14968#pullrequestreview-2834422054)
- `2025-05-13T02:16:05Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/14968#pullrequestreview-2835097298)
- `2025-05-13T03:30:33Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/14968#pullrequestreview-2835180722)
- `2025-05-13T14:00:46Z` `APPROVED` by `SageMoore` - Looks reasonable. Thanks for the contribution! (https://github.com/vllm-project/vllm/pull/14968#pullrequestreview-2836915748)
- `2025-05-13T14:31:55Z` `APPROVED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14968#pullrequestreview-2837036675)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/fp8_utils.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-05-12T20:33:32Z` `inline` by `SageMoore` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:34; signals: block, fp8; excerpt: "If that's the case can we just return False? Or move the current platform.is rocm() check to apply w8a8 block fp8 linear?" (https://github.com/vllm-project/vllm/pull/14968#discussion_r2085414387)
- `2025-03-31T15:29:08Z` `review` `COMMENTED` by `SageMoore`; signals: kernel; excerpt: "This generally looks fine. What models are you all using this kernel with? If there are any models that we would like to claim ..." (https://github.com/vllm-project/vllm/pull/14968#pullrequestreview-2729696157)
- `2025-05-12T20:35:54Z` `review` `COMMENTED` by `SageMoore`; signals: cutlass; excerpt: "In general this looks fine, but let's iron out this "is cutlass supported logic" ironed out before landing." (https://github.com/vllm-project/vllm/pull/14968#pullrequestreview-2834422054)
- `2025-04-23T01:57:32Z` `inline` by `tjtanaa` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:122; signals: fp8; excerpt: "@houseroad We have cross-checked with main. It seems they have implemented and removed the comment. Thus, we have removed the TODO comment." (https://github.com/vllm-project/vllm/pull/14968#discussion_r2055132668)
- `2025-04-23T00:55:51Z` `inline` by `houseroad` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:122; signals: fp8; excerpt: "can we add the github id or create an issue for this for tracking purpose." (https://github.com/vllm-project/vllm/pull/14968#discussion_r2055092714)
- `2025-05-13T02:16:05Z` `inline` by `tjtanaa` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:34; signals: fp8; excerpt: "@SageMoore I think we could." (https://github.com/vllm-project/vllm/pull/14968#discussion_r2085801267)
- `2025-05-13T03:30:33Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:34; signals: fp8; excerpt: "Just make sure you have a look at 14397 as it describes how this is currently a bug." (https://github.com/vllm-project/vllm/pull/14968#discussion_r2085858005)
- `2025-04-16T18:24:38Z` `issue` by `tjtanaa`; signals: register; excerpt: "@SageMoore We have updated the PR description and wrap the function in direct register custom op to make it also V1 compatible. It is ..." (https://github.com/vllm-project/vllm/pull/14968#issuecomment-2810380370)
- `2025-03-24T15:58:13Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @vllmellm." (https://github.com/vllm-project/vllm/pull/14968#issuecomment-2748626784)
- `2025-03-31T15:29:52Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @vllmellm." (https://github.com/vllm-project/vllm/pull/14968#issuecomment-2766602594)
- `2025-04-22T10:03:44Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @vllmellm." (https://github.com/vllm-project/vllm/pull/14968#issuecomment-2820822831)
- `2025-05-13T11:19:29Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @vllmellm." (https://github.com/vllm-project/vllm/pull/14968#issuecomment-2876095044)
