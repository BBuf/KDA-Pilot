# PR Discussion Digest

- Source PR: [sgl-project/sglang#17480](https://github.com/sgl-project/sglang/pull/17480)
- Source page: `sources/prs/sglang/PR-17480.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-17480`
- Generated at: `2026-05-20T15:28:29.142318+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-21T08:50:57Z`
- Merged: `2026-01-30T07:19:43Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 6 (approved=1, changes_requested=1, commented=4)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: McZyWu, iforgetmyname, ping1jing2
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-01-21T08:57:26Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to enhance the accuracy for the kimi-vl-instruct-a3b model on NPU backends. The ... (https://github.com/sgl-project/sglang/pull/17480#pullrequestreview-3686047233)
- `2026-01-26T10:48:58Z` `COMMENTED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/17480#pullrequestreview-3705513544)
- `2026-01-26T11:01:17Z` `COMMENTED` by `McZyWu` (https://github.com/sgl-project/sglang/pull/17480#pullrequestreview-3705552398)
- `2026-01-28T12:41:09Z` `CHANGES_REQUESTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/17480#pullrequestreview-3716483735)
- `2026-01-29T01:13:23Z` `COMMENTED` by `McZyWu` (https://github.com/sgl-project/sglang/pull/17480#pullrequestreview-3719969072)
- `2026-01-30T07:17:44Z` `APPROVED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/17480#pullrequestreview-3726755163)

## Inline Comment Hotspots

- `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`: 5 inline comment(s)
- `python/sglang/srt/hardware_backend/npu/moe/topk.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-26T10:48:27Z` `inline` by `iforgetmyname` `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`:107; signals: attention, mla; excerpt: "add comments" (https://github.com/sgl-project/sglang/pull/17480#discussion_r2727143214)
- `2026-01-28T12:36:13Z` `inline` by `ping1jing2` `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`:108; signals: attention, mla; excerpt: "it would be better to do it like below" (https://github.com/sgl-project/sglang/pull/17480#discussion_r2736441625)
- `2026-01-29T01:13:23Z` `inline` by `McZyWu` `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`:108; signals: attention, mla; excerpt: "sure thanks" (https://github.com/sgl-project/sglang/pull/17480#discussion_r2739309942)
- `2026-01-26T10:48:42Z` `inline` by `iforgetmyname` `python/sglang/srt/hardware_backend/npu/moe/topk.py`:45; signals: moe; excerpt: "add comments on router logits.shape[-1] <= 2048" (https://github.com/sgl-project/sglang/pull/17480#discussion_r2727143949)
- `2026-01-26T11:01:17Z` `inline` by `McZyWu` `python/sglang/srt/hardware_backend/npu/modules/deepseek_v2_attention_mla_npu.py`:107; signals: attention, mla; excerpt: "Thank you!" (https://github.com/sgl-project/sglang/pull/17480#discussion_r2727179852)
