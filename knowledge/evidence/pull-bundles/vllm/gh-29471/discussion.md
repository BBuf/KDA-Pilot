# PR Discussion Digest

- Source PR: [vllm-project/vllm#29471](https://github.com/vllm-project/vllm/pull/29471)
- Source page: `sources/prs/vllm/PR-29471.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29471`
- Generated at: `2026-05-20T15:38:44.101733+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-26T02:26:43Z`
- Merged: `2025-11-28T13:52:42Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: Victor49152, chatgpt-codex-connector, mgoin, tjtanaa, ywang96
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-26T02:28:58Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/29471#pullrequestreview-3508118938)
- `2025-11-26T02:28:59Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to remove upstream flash-attention checks. While most of the changes correctly remove ... (https://github.com/vllm-project/vllm/pull/29471#pullrequestreview-3508119024)
- `2025-11-26T03:25:04Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/29471#pullrequestreview-3508374105)
- `2025-11-26T03:28:12Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/29471#pullrequestreview-3508386362)
- `2025-11-26T03:28:27Z` `COMMENTED` by `Victor49152` (https://github.com/vllm-project/vllm/pull/29471#pullrequestreview-3508387383)
- `2025-11-26T03:29:36Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/29471#pullrequestreview-3508391589)
- `2025-11-26T05:14:15Z` `COMMENTED` by `Victor49152` (https://github.com/vllm-project/vllm/pull/29471#pullrequestreview-3508776858)
- `2025-11-28T01:35:18Z` `APPROVED` by `ywang96` - I fixed the precommit error but otherwise LGTM cc @tjtanaa for final check on the changes for resolving ... (https://github.com/vllm-project/vllm/pull/29471#pullrequestreview-3517235948)

## Inline Comment Hotspots

- `vllm/attention/layer.py`: 5 inline comment(s)
- `vllm/attention/ops/vit_attn_wrappers.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-26T02:28:58Z` `inline` by `chatgpt-codex-connector` `vllm/attention/layer.py`:82; signals: attention, cuda, flash attention, kernel; excerpt: "![P1 Badge]( Restore CUDA path in vit flash-attn selection maybe get vit flash attn backend now returns TORCH SDPA for any platform that is ..." (https://github.com/vllm-project/vllm/pull/29471#discussion_r2562587100)
- `2025-11-26T03:28:27Z` `inline` by `Victor49152` `vllm/attention/layer.py`:64; signals: attention, hang; excerpt: "Just pushed this changes, thanks and please comment if there is anything else you notice" (https://github.com/vllm-project/vllm/pull/29471#discussion_r2562820380)
- `2025-11-28T13:51:45Z` `issue` by `tjtanaa`; signals: attention, flash attention; excerpt: "@ywang96 Thanks. LGTM. It is using the flash attention and aiter flash attention. And the code path on ROCm is working, ChartQA score of ..." (https://github.com/vllm-project/vllm/pull/29471#issuecomment-3589420199)
- `2025-11-26T03:25:04Z` `inline` by `tjtanaa` `vllm/attention/layer.py`:64; signals: attention; excerpt: "we need to add back the on gfx9() condition here to differentiate between Radeon and Instinct GPUs. On Radeon, only TORCH SDPA is supported." (https://github.com/vllm-project/vllm/pull/29471#discussion_r2562807472)
- `2025-11-26T03:28:11Z` `inline` by `tjtanaa` `vllm/attention/layer.py`:91; signals: attention; excerpt: "vllm/attention/utils/fa utils.py does not have the logic for ROCm, flash attn varlen func will be a None object if imported this way. We can ..." (https://github.com/vllm-project/vllm/pull/29471#discussion_r2562819390)
- `2025-11-26T03:29:35Z` `inline` by `tjtanaa` `vllm/attention/ops/vit_attn_wrappers.py`:34; signals: attention; excerpt: "like wise, vllm/attention/utils/fa utils.py does not have the logic for ROCm, flash attn varlen func will be a None object if imported this way. ..." (https://github.com/vllm-project/vllm/pull/29471#discussion_r2562824696)
- `2025-11-26T05:14:15Z` `inline` by `Victor49152` `vllm/attention/layer.py`:91; signals: attention; excerpt: "I added this import to fa utils as it looks like the most simple way of it. And except message tells user to install ..." (https://github.com/vllm-project/vllm/pull/29471#discussion_r2563170650)
- `2025-11-26T02:28:58Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/29471#pullrequestreview-3508118938)
- `2025-11-28T01:35:18Z` `review` `APPROVED` by `ywang96`; signals: hang; excerpt: "I fixed the precommit error but otherwise LGTM cc @tjtanaa for final check on the changes for resolving FA import on ROCM platform." (https://github.com/vllm-project/vllm/pull/29471#pullrequestreview-3517235948)
