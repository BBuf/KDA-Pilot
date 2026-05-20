# PR Discussion Digest

- Source PR: [vllm-project/vllm#28561](https://github.com/vllm-project/vllm/pull/28561)
- Source page: `sources/prs/vllm/PR-28561.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28561`
- Generated at: `2026-05-20T15:38:29.439718+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-12T15:23:32Z`
- Merged: `2025-11-13T02:40:59Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: ProExpertProg, benchislett, chatgpt-codex-connector, elvischenv
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-12T15:24:35Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a regression on Blackwell (SM100) GPUs where models utilizing attention sinks were ... (https://github.com/vllm-project/vllm/pull/28561#pullrequestreview-3454027313)
- `2025-11-12T15:26:37Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28561#pullrequestreview-3454039935)
- `2025-11-12T15:42:55Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/28561#pullrequestreview-3454131024)
- `2025-11-12T17:49:46Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/28561#pullrequestreview-3454713255)
- `2025-11-12T18:28:24Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/28561#pullrequestreview-3454883439)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/flashinfer.py`: 2 inline comment(s)
- `vllm/utils/flashinfer.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-12T15:26:37Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/flashinfer.py`:244; signals: attention, flashinfer, hang, sm100, triton; excerpt: "advertises FlashInfer as sink-capable whenever supports trtllm attention() returns true, but supports trtllm attention only checks hardware capability and cubin availability. If the user ..." (https://github.com/vllm-project/vllm/pull/28561#discussion_r2518759903)
- `2025-11-12T17:49:46Z` `inline` by `benchislett` `vllm/v1/attention/backends/flashinfer.py`:244; signals: attention, flashinfer; excerpt: "I agree with the bot. What if VLLM USE TRTLLM ATTENTION=0 is set? The other case is when (num qo heads % num kv ..." (https://github.com/vllm-project/vllm/pull/28561#discussion_r2519248919)
- `2025-11-12T18:28:18Z` `inline` by `elvischenv` `vllm/utils/flashinfer.py`:246; signals: attention, flashinfer; excerpt: "@mgoin Since you are modifying this, should we place into use trtllm attention() and before the I feel like vllm is batch invariant() is ..." (https://github.com/vllm-project/vllm/pull/28561#discussion_r2519367065)
- `2025-11-12T15:26:37Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub [Your team has set up Codex ..." (https://github.com/vllm-project/vllm/pull/28561#pullrequestreview-3454039935)
