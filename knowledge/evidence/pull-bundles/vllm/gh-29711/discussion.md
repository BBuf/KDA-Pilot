# PR Discussion Digest

- Source PR: [vllm-project/vllm#29711](https://github.com/vllm-project/vllm/pull/29711)
- Source page: `sources/prs/vllm/PR-29711.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29711`
- Generated at: `2026-05-20T15:38:47.432646+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-29T02:07:02Z`
- Merged: `2025-12-02T01:24:19Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 3 (approved=1, changes_requested=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: ApostaC, ProExpertProg, bbrowning, chatgpt-codex-connector, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-29T02:08:49Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces runtime SM dispatch for cutlass scaled fp4 mm, which is a solid ... (https://github.com/vllm-project/vllm/pull/29711#pullrequestreview-3520340172)
- `2025-12-01T20:32:55Z` `CHANGES_REQUESTED` by `ProExpertProg` - The diff seems polluted, can you rebase/merge from main? (https://github.com/vllm-project/vllm/pull/29711#pullrequestreview-3526869786)
- `2025-12-02T01:24:05Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/29711#pullrequestreview-3527731564)

## Inline Comment Hotspots

- `csrc/quantization/fp4/nvfp4_scaled_mm_entry.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-01T23:58:12Z` `issue` by `bbrowning`; signals: compile, cuda, failing, fp4, nvfp4; excerpt: "I tested this on my DGX Spark (sm121), was able to reproduce the original issue, and confirm that this fixes the failing tests in ..." (https://github.com/vllm-project/vllm/pull/29711#issuecomment-3599498107)
- `2025-12-01T20:17:19Z` `issue` by `ApostaC`; signals: tma; excerpt: "Hey @hholtmann , should this PR be merged to the main branch instead of releases/v0.11.2? In the mean time, cc @mgoin @tlrmchlsmth" (https://github.com/vllm-project/vllm/pull/29711#issuecomment-3598664273)
- `2025-12-01T20:28:50Z` `issue` by `mergify`; signals: tma; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @hholtmann." (https://github.com/vllm-project/vllm/pull/29711#issuecomment-3598700769)
- `2025-12-01T20:32:55Z` `review` `CHANGES_REQUESTED` by `ProExpertProg`; signals: general review; excerpt: "The diff seems polluted, can you rebase/merge from main?" (https://github.com/vllm-project/vllm/pull/29711#pullrequestreview-3526869786)
- `2025-11-29T02:07:10Z` `issue` by `chatgpt-codex-connector`; signals: general review; excerpt: "Codex usage limits have been reached for code reviews. Please check with the admins of this repo to increase the limits by adding credits." (https://github.com/vllm-project/vllm/pull/29711#issuecomment-3590862217)
