# PR Discussion Digest

- Source PR: [vllm-project/vllm#29067](https://github.com/vllm-project/vllm/pull/29067)
- Source page: `sources/prs/vllm/PR-29067.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29067`
- Generated at: `2026-05-20T15:38:36.683376+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-20T03:57:29Z`
- Merged: `2025-11-24T18:38:04Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 8
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: LucasWilkinson, bnellnm, chatgpt-codex-connector, mergify, mgoin
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-20T16:25:54Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/29067#pullrequestreview-3488757416)
- `2025-11-21T19:40:07Z` `APPROVED` by `LucasWilkinson` - Overall looks like a very nice cleanup! thanks! LGTM, left a couple nits (https://github.com/vllm-project/vllm/pull/29067#pullrequestreview-3494121938)
- `2025-11-21T20:21:11Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/29067#pullrequestreview-3494242232)
- `2025-11-21T20:23:00Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/29067#pullrequestreview-3494248361)
- `2025-11-22T01:51:49Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/29067#pullrequestreview-3495118485)
- `2025-11-22T02:51:35Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/29067#pullrequestreview-3495300876)
- `2025-11-24T13:51:00Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/29067#pullrequestreview-3500486353)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 8 inline comment(s)

## High-Signal Discussion

- `2025-11-20T16:25:54Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/fused_moe/layer.py`:1476; signals: flashinfer, hang, kernel, moe; excerpt: "and only the hidden states and router logits, but existing call sites still invoke it as a class method with the old argument list ..." (https://github.com/vllm-project/vllm/pull/29067#discussion_r2546753737)
- `2025-11-22T02:51:34Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:1496; signals: kernel, moe; excerpt: "Right now, for all the quant methods that support eplb, all the implementation kernels support it also. I've left individual eplb checks in the ..." (https://github.com/vllm-project/vllm/pull/29067#discussion_r2551826222)
- `2025-11-24T13:51:00Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:1496; signals: kernel, moe; excerpt: "Currently only three quant methods support eplb and they all seems to unconditionally support it (at least according to the code in main). The ..." (https://github.com/vllm-project/vllm/pull/29067#discussion_r2556369200)
- `2025-11-22T01:51:49Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/layer.py`:1496; signals: kernel, moe; excerpt: "How does this handle methods where not all kernels support eplb?" (https://github.com/vllm-project/vllm/pull/29067#discussion_r2551650590)
- `2025-11-21T20:23:00Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:1452; signals: moe; excerpt: "The last output of select experts is for the zero expert output. In most cases it is None. Hopefully, this will get cleaned up ..." (https://github.com/vllm-project/vllm/pull/29067#discussion_r2550873451)
- `2025-11-20T16:25:54Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/29067#pullrequestreview-3488757416)
- `2025-11-21T19:37:39Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/fused_moe/layer.py`:1476; signals: moe; excerpt: "@bnellnm is this real?" (https://github.com/vllm-project/vllm/pull/29067#discussion_r2550776825)
- `2025-11-21T19:38:30Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/fused_moe/layer.py`:1452; signals: moe; excerpt: "nit cruft" (https://github.com/vllm-project/vllm/pull/29067#discussion_r2550779376)
- `2025-11-21T20:21:11Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:1476; signals: moe; excerpt: "Yeah, I've fixed these but haven't updated the PR yet." (https://github.com/vllm-project/vllm/pull/29067#discussion_r2550869459)
- `2025-11-20T03:58:34Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @bnellnm." (https://github.com/vllm-project/vllm/pull/29067#issuecomment-3555659031)
