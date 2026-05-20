# PR Discussion Digest

- Source PR: [vllm-project/vllm#28840](https://github.com/vllm-project/vllm/pull/28840)
- Source page: `sources/prs/vllm/PR-28840.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28840`
- Generated at: `2026-05-20T15:38:35.354064+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-17T07:15:29Z`
- Merged: `2025-11-28T23:52:12Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: LucasWilkinson, chatgpt-codex-connector, heheda12345, hl475, mergify, staugust
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-11-17T07:16:37Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly addresses the issue of FlashInfer using base 2 for its log-sum-exp calculations ... (https://github.com/vllm-project/vllm/pull/28840#pullrequestreview-3471304894)
- `2025-11-27T19:17:11Z` `APPROVED` by `LucasWilkinson` - LGTM ( @pavanimajety should look at too though since im not as familiar with when FlashInfer is base2 ... (https://github.com/vllm-project/vllm/pull/28840#pullrequestreview-3516722214)

## Inline Comment Hotspots

- `vllm/attention/ops/common.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-17T07:18:49Z` `issue` by `chatgpt-codex-connector`; signals: attention; excerpt: "💡 Codex Review . Without converting the base‑2 LSEs (e.g., multiply by math.log(2) for both lse context and the lse query returned from new ..." (https://github.com/vllm-project/vllm/pull/28840#issuecomment-3540303785)
- `2025-11-19T07:20:02Z` `issue` by `staugust`; signals: flashinfer; excerpt: "@pavanimajety Would you like to take a look at this issue? I'm wondering which repo to fix this, flashinfer or vllm." (https://github.com/vllm-project/vllm/pull/28840#issuecomment-3551168253)
- `2025-11-27T19:17:11Z` `review` `APPROVED` by `LucasWilkinson`; signals: flashinfer; excerpt: "LGTM ( @pavanimajety should look at too though since im not as familiar with when FlashInfer is base2 )" (https://github.com/vllm-project/vllm/pull/28840#pullrequestreview-3516722214)
- `2025-11-28T03:13:55Z` `issue` by `staugust`; signals: flashinfer; excerpt: "@LucasWilkinson @heheda12345 @pavanimajety From [state.cuh:45]( ,we can figure that flashinfer use 2 as base for all lse computation." (https://github.com/vllm-project/vllm/pull/28840#issuecomment-3587781648)
- `2025-11-19T21:34:53Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @staugust." (https://github.com/vllm-project/vllm/pull/28840#issuecomment-3554724914)
