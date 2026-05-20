# PR Discussion Digest

- Source PR: [vllm-project/vllm#35448](https://github.com/vllm-project/vllm/pull/35448)
- Source page: `sources/prs/vllm/PR-35448.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-35448`
- Generated at: `2026-05-20T15:40:01.507934+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-26T22:21:06Z`
- Merged: `2026-03-16T22:07:39Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: EdalatiAli, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2026-02-26T22:23:58Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for online MXFP8 MoE quantization. The changes are comprehensive, adding a ... (https://github.com/vllm-project/vllm/pull/35448#pullrequestreview-3863861510)
- `2026-03-10T20:25:25Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/35448#pullrequestreview-3925194381)
- `2026-03-12T18:02:13Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/35448#pullrequestreview-3938481814)
- `2026-03-13T21:05:23Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/35448#pullrequestreview-3946946021)
- `2026-03-13T21:07:20Z` `COMMENTED` by `EdalatiAli` (https://github.com/vllm-project/vllm/pull/35448#pullrequestreview-3946953604)
- `2026-03-16T22:07:26Z` `APPROVED` by `mgoin` - Okay seems reasonable to me to accept. I'm not sure how much we should truly reuse with the ... (https://github.com/vllm-project/vllm/pull/35448#pullrequestreview-3956926413)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/fp8.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/oracle/fp8.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/oracle/mxfp8.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-13T21:05:22Z` `inline` by `EdalatiAli` `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`:360; signals: block, flashinfer, fp8, hang, moe; excerpt: "Yes, it's necessary — the monolithic class serves both block-scale (SILU only, hardcoded in flashinfer) and per-tensor (SILU + RELU2) paths, and supports activation ..." (https://github.com/vllm-project/vllm/pull/35448#discussion_r2933759618)
- `2026-03-13T21:07:20Z` `inline` by `EdalatiAli` `vllm/model_executor/layers/fused_moe/oracle/fp8.py`:237; signals: fp8, hang, moe; excerpt: "Sure, I changed the code to use [ I had to make a few other minor changes to correctly use it." (https://github.com/vllm-project/vllm/pull/35448#discussion_r2933766618)
- `2026-03-12T17:34:14Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/experts/trtllm_fp8_moe.py`:360; signals: fp8, moe; excerpt: "It seems like you assert SILU but don't restrict selection in supports activation, is this necessary?" (https://github.com/vllm-project/vllm/pull/35448#discussion_r2926258483)
- `2026-03-16T22:04:12Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/oracle/mxfp8.py`:26; signals: fp8, moe; excerpt: "It is a bit confusing to use Fp8MoeBackend here and elsewhere for mxfp8, but I guess it is needed to reuse the moe utils" (https://github.com/vllm-project/vllm/pull/35448#discussion_r2943213209)
- `2026-03-12T18:02:04Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/oracle/fp8.py`:237; signals: fp8, moe; excerpt: "We already have an mxfp8 oracle at could we use that rather than overloading fp8?" (https://github.com/vllm-project/vllm/pull/35448#discussion_r2926411954)
- `2026-03-10T20:25:25Z` `inline` by `EdalatiAli` `vllm/model_executor/layers/quantization/fp8.py`:1446; signals: fp8; excerpt: "This issue is resolved by renaming the scale name postfix to weight scale" (https://github.com/vllm-project/vllm/pull/35448#discussion_r2914250317)
- `2026-03-16T22:07:26Z` `review` `APPROVED` by `mgoin`; signals: fp8; excerpt: "Okay seems reasonable to me to accept. I'm not sure how much we should truly reuse with the fp8 methods but it is fair ..." (https://github.com/vllm-project/vllm/pull/35448#pullrequestreview-3956926413)
- `2026-03-04T04:05:04Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @EdalatiAli." (https://github.com/vllm-project/vllm/pull/35448#issuecomment-3995124847)
- `2026-03-12T15:21:40Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @EdalatiAli." (https://github.com/vllm-project/vllm/pull/35448#issuecomment-4047629821)
