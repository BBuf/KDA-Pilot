# PR Discussion Digest

- Source PR: [vllm-project/vllm#18321](https://github.com/vllm-project/vllm/pull/18321)
- Source page: `sources/prs/vllm/PR-18321.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-18321`
- Generated at: `2026-05-20T15:35:18.363084+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-18T12:05:48Z`
- Merged: `2025-07-29T10:13:27Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 1 (approved=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: DarkLight1337, Isotr0py, mergify, noooop
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-29T07:36:56Z` `APPROVED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/18321#pullrequestreview-3065980339)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-05-28T07:10:29Z` `issue` by `Isotr0py`; signals: hang, moe; excerpt: "Personally, is gated is better than is act and mul Yes, I have considered is gated at first. But since we're using "gating" in ..." (https://github.com/vllm-project/vllm/pull/18321#issuecomment-2915222610)
- `2025-05-24T12:54:21Z` `issue` by `noooop`; signals: attention; excerpt: "Fix: Respect is causal=False config in forward to enable bidirectional attention The test failure is related to this, and after a year, it has ..." (https://github.com/vllm-project/vllm/pull/18321#issuecomment-2906818186)
- `2025-05-28T01:31:43Z` `issue` by `noooop`; signals: kernel; excerpt: "sorry for late response language-models-test-extended has verified the model's results on mteb/STS12 I tested a larger mteb/T2Reranking dataset. There can still be significant speed ..." (https://github.com/vllm-project/vllm/pull/18321#issuecomment-2914612239)
- `2025-05-24T10:12:51Z` `issue` by `DarkLight1337`; signals: block; excerpt: "Since this model already has a test in CI, I'll just unblock it and see if it passes" (https://github.com/vllm-project/vllm/pull/18321#issuecomment-2906739943)
- `2025-07-29T06:10:23Z` `issue` by `DarkLight1337`; signals: compile; excerpt: "Any update on this? It would help with getting the model to support V1 with torch.compile" (https://github.com/vllm-project/vllm/pull/18321#issuecomment-3130833964)
- `2025-07-29T07:07:53Z` `issue` by `Isotr0py`; signals: moe; excerpt: "Let me update this PR to catch recent MoE refactoring." (https://github.com/vllm-project/vllm/pull/18321#issuecomment-3130999319)
- `2025-05-26T03:29:20Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @Isotr0py." (https://github.com/vllm-project/vllm/pull/18321#issuecomment-2908411849)
