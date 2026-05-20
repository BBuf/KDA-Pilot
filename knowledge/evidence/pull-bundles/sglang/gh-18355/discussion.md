# PR Discussion Digest

- Source PR: [sgl-project/sglang#18355](https://github.com/sgl-project/sglang/pull/18355)
- Source page: `sources/prs/sglang/PR-18355.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18355`
- Generated at: `2026-05-20T15:28:36.983918+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-06T08:16:01Z`
- Merged: `2026-02-25T19:06:23Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 5 (approved=1, changes_requested=1, commented=3)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: 1am9trash, HaiShaw, hubertlu-tw, yichiche
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2026-02-06T08:17:55Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for Qwen3-Coder-Next on the AMD platform. The changes are well-structured and ... (https://github.com/sgl-project/sglang/pull/18355#pullrequestreview-3761483122)
- `2026-02-25T09:28:59Z` `CHANGES_REQUESTED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/18355#pullrequestreview-3852949458)
- `2026-02-25T11:34:24Z` `COMMENTED` by `yichiche` (https://github.com/sgl-project/sglang/pull/18355#pullrequestreview-3853681890)
- `2026-02-25T11:41:45Z` `COMMENTED` by `yichiche` (https://github.com/sgl-project/sglang/pull/18355#pullrequestreview-3853717350)
- `2026-02-25T16:53:29Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/18355#pullrequestreview-3855515984)

## Inline Comment Hotspots

- `python/sglang/srt/models/qwen3_next.py`: 2 inline comment(s)
- `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`: 1 inline comment(s)
- `python/sglang/srt/layers/attention/aiter_backend.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-25T11:41:46Z` `inline` by `yichiche` `python/sglang/srt/layers/attention/aiter_backend.py`:571; signals: attention, hang, mla; excerpt: "We didn't change the logic in this part; we just moved it to line 799. if self.use mla: self.mla indices updater prefill.update( forward batch.req ..." (https://github.com/sgl-project/sglang/pull/18355#discussion_r2852541655)
- `2026-02-11T02:41:10Z` `issue` by `yichiche`; signals: hang, perf; excerpt: "I see the test uses --chunked-prefill-size 32768 (typically use 131072). Does Qwen3-coder-next tend to perform better with chunk prefill? With the change from --chunked-prefill-size ..." (https://github.com/sgl-project/sglang/pull/18355#issuecomment-3881800980)
- `2026-02-25T11:34:24Z` `inline` by `yichiche` `python/sglang/srt/models/qwen3_next.py`:390; signals: cuda; excerpt: "alt stream = torch.cuda.Stream() if is cuda else None, with the checking of self.alt stream first, we can gurantt it will not fall into ..." (https://github.com/sgl-project/sglang/pull/18355#discussion_r2852509328)
- `2026-02-25T09:28:29Z` `inline` by `HaiShaw` `python/sglang/srt/models/qwen3_next.py`:390; signals: hang; excerpt: "Seems unnecessary changes here?" (https://github.com/sgl-project/sglang/pull/18355#discussion_r2851847449)
- `2026-02-10T15:31:37Z` `issue` by `1am9trash`; signals: perf; excerpt: "I see the test uses --chunked-prefill-size 32768 (typically use 131072). Does Qwen3-coder-next tend to perform better with chunk prefill?" (https://github.com/sgl-project/sglang/pull/18355#issuecomment-3878565960)
