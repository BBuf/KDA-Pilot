# PR Discussion Digest

- Source PR: [vllm-project/vllm#28346](https://github.com/vllm-project/vllm/pull/28346)
- Source page: `sources/prs/vllm/PR-28346.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28346`
- Generated at: `2026-05-20T15:38:27.949345+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-08T11:47:55Z`
- Merged: `2025-11-21T12:55:43Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 18 (approved=3, commented=15)
- Inline review comments: 15
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=2, outdated=3
- Human participants with discussion text: DarkLight1337, SageMoore, apinge, chatgpt-codex-connector, fsx950223, maleksan85, mergify, sammysun0711, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-08T11:50:13Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to add cross-attention support to the Triton attention backend. While the intent ... (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3438296020)
- `2025-11-08T11:52:01Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3438296425)
- `2025-11-08T17:30:20Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3438496897)
- `2025-11-08T19:05:24Z` `APPROVED` by `maleksan85` - LGTM! Thanks! (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3438537532)
- `2025-11-12T03:41:52Z` `COMMENTED` by `fsx950223` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3451203570)
- `2025-11-12T20:19:39Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3455330130)
- `2025-11-12T20:22:38Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to add cross-attention support to the Triton attention backend. While the changes ... (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3455342284)
- `2025-11-13T08:41:49Z` `COMMENTED` by `apinge` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3458420820)
- `2025-11-18T03:33:15Z` `COMMENTED` by `sammysun0711` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3475332777)
- `2025-11-19T07:33:42Z` `COMMENTED` by `fsx950223` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3481225052)
- `2025-11-19T15:55:49Z` `COMMENTED` by `SageMoore` - Looks reasonable. Just one question. (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3483520978)
- `2025-11-20T02:15:42Z` `COMMENTED` by `fsx950223` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3485410596)
- `2025-11-20T15:53:56Z` `COMMENTED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3488605597)
- `2025-11-20T15:56:49Z` `COMMENTED` by `fsx950223` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3488618258)
- `2025-11-20T15:56:51Z` `COMMENTED` by `fsx950223` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3488618359)
- `2025-11-20T15:56:51Z` `COMMENTED` by `fsx950223` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3488618412)
- `2025-11-20T16:03:00Z` `APPROVED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3488644887)
- `2025-11-21T01:08:37Z` `APPROVED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/28346#pullrequestreview-3490734419)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/triton_attn.py`: 14 inline comment(s)
- `vllm/v1/worker/utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-08T11:52:01Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/triton_attn.py`:353; signals: attention, hang, kernel, triton; excerpt: ". Cross-attention builders explicitly set attn metadata.causal = False so that queries can see the full encoder sequence. For batches where multiple decoder queries ..." (https://github.com/vllm-project/vllm/pull/28346#discussion_r2506872415)
- `2025-11-13T08:41:49Z` `inline` by `apinge` `vllm/v1/attention/backends/triton_attn.py`:313; signals: accuracy, attention, triton; excerpt: "I found that this additional condition self.attn type == AttentionType.DECODER causes a drop in Whisper's accuracy. In these two basic examples( the outputs are ..." (https://github.com/vllm-project/vllm/pull/28346#discussion_r2522346427)
- `2025-11-18T03:33:15Z` `inline` by `sammysun0711` `vllm/v1/attention/backends/triton_attn.py`:313; signals: accuracy, attention, triton; excerpt: "@fsx950223 may I know if any update for whisper accuracy drop issue cause by self.attn type == AttentionType.DECODER mentioned above?" (https://github.com/vllm-project/vllm/pull/28346#discussion_r2536186198)
- `2025-11-19T15:54:44Z` `inline` by `SageMoore` `vllm/v1/attention/backends/triton_attn.py`:350; signals: attention, hang, triton; excerpt: "This change is a noop right? We are just getting the num kv heads from a different spot? Is there some subtle difference that ..." (https://github.com/vllm-project/vllm/pull/28346#discussion_r2542621231)
- `2025-11-08T17:30:20Z` `inline` by `DarkLight1337` `vllm/v1/attention/backends/triton_attn.py`:251; signals: attention, triton; excerpt: "Is this valid?" (https://github.com/vllm-project/vllm/pull/28346#discussion_r2507033671)
- `2025-11-12T03:41:52Z` `inline` by `fsx950223` `vllm/v1/attention/backends/triton_attn.py`:251; signals: attention, triton; excerpt: "Yes" (https://github.com/vllm-project/vllm/pull/28346#discussion_r2516611271)
- `2025-11-19T07:33:42Z` `inline` by `fsx950223` `vllm/v1/attention/backends/triton_attn.py`:313; signals: attention, triton; excerpt: "It's already reverted" (https://github.com/vllm-project/vllm/pull/28346#discussion_r2540867812)
- `2025-11-20T02:15:42Z` `inline` by `fsx950223` `vllm/v1/attention/backends/triton_attn.py`:350; signals: attention, triton; excerpt: "No" (https://github.com/vllm-project/vllm/pull/28346#discussion_r2544119585)
- `2025-11-20T15:53:56Z` `inline` by `SageMoore` `vllm/v1/attention/backends/triton_attn.py`:350; signals: attention, triton; excerpt: "Can we just leave the original code then?" (https://github.com/vllm-project/vllm/pull/28346#discussion_r2546634353)
- `2025-11-20T15:56:49Z` `inline` by `fsx950223` `vllm/v1/attention/backends/triton_attn.py`:350; signals: attention, triton; excerpt: "No, key may be None." (https://github.com/vllm-project/vllm/pull/28346#discussion_r2546644369)
- `2025-11-20T15:56:50Z` `inline` by `fsx950223` `vllm/v1/attention/backends/triton_attn.py`:350; signals: attention, triton; excerpt: "No" (https://github.com/vllm-project/vllm/pull/28346#discussion_r2546644463)
- `2025-11-20T15:56:51Z` `inline` by `fsx950223` `vllm/v1/attention/backends/triton_attn.py`:350; signals: attention, triton; excerpt: "No" (https://github.com/vllm-project/vllm/pull/28346#discussion_r2546644518)
