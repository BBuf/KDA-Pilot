# PR Discussion Digest

- Source PR: [vllm-project/vllm#38325](https://github.com/vllm-project/vllm/pull/38325)
- Source page: `sources/prs/vllm/PR-38325.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38325`
- Generated at: `2026-05-20T15:40:30.400783+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-27T06:11:31Z`
- Merged: `2026-04-03T13:49:59Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: Nekofish-L, claude, johnnynunez, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-27T06:11:34Z` `COMMENTED` by `claude` - Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer ... (https://github.com/vllm-project/vllm/pull/38325#pullrequestreview-4019084158)
- `2026-03-27T06:13:10Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a mechanism to swap the A and B matrices in the CUTLASS ... (https://github.com/vllm-project/vllm/pull/38325#pullrequestreview-4019089132)
- `2026-03-27T23:26:25Z` `APPROVED` by `mgoin` - Nice work, the changes look solid to me for using swapAB with cutlass. I really appreciate you taking ... (https://github.com/vllm-project/vllm/pull/38325#pullrequestreview-4024142960)

## Inline Comment Hotspots

- `csrc/quantization/w8a8/cutlass/c3x/scaled_mm_blockwise_sm120_fp8_dispatch.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-27T23:26:25Z` `review` `APPROVED` by `mgoin`; signals: cutlass, hang, sm120; excerpt: "Nice work, the changes look solid to me for using swapAB with cutlass. I really appreciate you taking the time to optimize SM120!" (https://github.com/vllm-project/vllm/pull/38325#pullrequestreview-4024142960)
- `2026-03-27T06:11:34Z` `review` `COMMENTED` by `claude`; signals: general review; excerpt: "Claude Code Review This pull request is from a fork — automated review is disabled. A repository maintainer can comment @claude review to run ..." (https://github.com/vllm-project/vllm/pull/38325#pullrequestreview-4019084158)
- `2026-03-30T18:44:24Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @Nekofish-L." (https://github.com/vllm-project/vllm/pull/38325#issuecomment-4157319817)
- `2026-04-02T06:11:56Z` `issue` by `Nekofish-L`; signals: general review; excerpt: "Hi @mgoin , I've rebased the branch to resolve the merge conflicts. It looks like the rebase disabled the auto-merge. Could you please take ..." (https://github.com/vllm-project/vllm/pull/38325#issuecomment-4174910813)
