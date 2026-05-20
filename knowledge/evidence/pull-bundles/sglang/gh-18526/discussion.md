# PR Discussion Digest

- Source PR: [sgl-project/sglang#18526](https://github.com/sgl-project/sglang/pull/18526)
- Source page: `sources/prs/sglang/PR-18526.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18526`
- Generated at: `2026-05-20T15:28:39.897056+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-10T08:31:11Z`
- Merged: `2026-02-27T21:18:32Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: HaiShaw, hubertlu-tw, kkHuang-amd, wufann
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-10T08:35:56Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables CUDA graph capturing for the aiter NSA decode backend and adds a ... (https://github.com/sgl-project/sglang/pull/18526#pullrequestreview-3777493529)
- `2026-02-10T17:50:11Z` `APPROVED` by `hubertlu-tw` - LGTM (https://github.com/sgl-project/sglang/pull/18526#pullrequestreview-3780599845)
- `2026-02-11T06:44:05Z` `COMMENTED` by `kkHuang-amd` (https://github.com/sgl-project/sglang/pull/18526#pullrequestreview-3783104847)
- `2026-02-11T08:53:01Z` `COMMENTED` by `wufann` (https://github.com/sgl-project/sglang/pull/18526#pullrequestreview-3783542405)
- `2026-02-27T21:17:47Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/18526#pullrequestreview-3869125909)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/nsa_backend.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-02-27T09:46:13Z` `issue` by `wufann`; signals: hang, memory, oom; excerpt: "@wufann @bingxche I checked this failed case and it is not related to my changes. I was unable to reproduce the issue on local ..." (https://github.com/sgl-project/sglang/pull/18526#issuecomment-3971877143)
- `2026-02-11T06:44:05Z` `inline` by `kkHuang-amd` `python/sglang/srt/layers/attention/nsa_backend.py`:1798; signals: attention; excerpt: "Line 1798 will have potential issue. The kv indices size is total valid, but get valid kv indices needs the kv indices size is ..." (https://github.com/sgl-project/sglang/pull/18526#discussion_r2791670441)
- `2026-02-11T08:53:01Z` `inline` by `wufann` `python/sglang/srt/layers/attention/nsa_backend.py`:1798; signals: attention; excerpt: "Fixed. Pre allocate kv indices with size (bs topk) for safety." (https://github.com/sgl-project/sglang/pull/18526#discussion_r2792088196)
- `2026-02-26T09:41:44Z` `issue` by `wufann`; signals: mla; excerpt: "Need adapt to the new aiter mla decode fwd api." (https://github.com/sgl-project/sglang/pull/18526#issuecomment-3965386205)
