# PR Discussion Digest

- Source PR: [vllm-project/vllm#36728](https://github.com/vllm-project/vllm/pull/36728)
- Source page: `sources/prs/vllm/PR-36728.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36728`
- Generated at: `2026-05-20T15:40:16.127038+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-11T01:27:03Z`
- Merged: `2026-03-23T21:02:57Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 5 (approved=3, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: bnellnm, mergify, robertgshaw2-redhat, yewentao256, yzong-rh
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-11T01:39:22Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly strengthens device support checks for several MoE experts by verifying the availability ... (https://github.com/vllm-project/vllm/pull/36728#pullrequestreview-3926372912)
- `2026-03-17T14:55:15Z` `COMMENTED` by `yzong-rh` (https://github.com/vllm-project/vllm/pull/36728#pullrequestreview-3961445834)
- `2026-03-17T21:14:25Z` `APPROVED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/36728#pullrequestreview-3963810467)
- `2026-03-21T19:24:19Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36728#pullrequestreview-3986525572)
- `2026-03-23T15:06:22Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/36728#pullrequestreview-3992459404)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-17T14:55:15Z` `inline` by `yzong-rh` `vllm/model_executor/layers/fused_moe/experts/flashinfer_cutedsl_moe.py`:68; signals: cute, flashinfer, moe; excerpt: "Fixed" (https://github.com/vllm-project/vllm/pull/36728#discussion_r2947389173)
- `2026-03-21T23:23:36Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @yzong-rh." (https://github.com/vllm-project/vllm/pull/36728#issuecomment-4104817402)
