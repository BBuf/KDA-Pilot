# PR Discussion Digest

- Source PR: [sgl-project/sglang#16892](https://github.com/sgl-project/sglang/pull/16892)
- Source page: `sources/prs/sglang/PR-16892.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-16892`
- Generated at: `2026-05-20T15:28:23.538665+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-11T08:24:02Z`
- Merged: `2026-01-25T16:15:53Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 13
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=3, outdated=0
- Human participants with discussion text: HandH1998, ispobock
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-11T08:42:41Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for mxint4 quantization with the flashinfer trtllm backend for Mixture-of-Experts (MoE) ... (https://github.com/sgl-project/sglang/pull/16892#pullrequestreview-3647521341)
- `2026-01-13T04:16:29Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/16892#pullrequestreview-3653735772)
- `2026-01-13T08:33:24Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/16892#pullrequestreview-3654523393)
- `2026-01-13T10:21:31Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/16892#pullrequestreview-3655035462)
- `2026-01-13T10:24:42Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/16892#pullrequestreview-3655048683)
- `2026-01-13T10:33:33Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/16892#pullrequestreview-3655083038)
- `2026-01-13T10:39:04Z` `COMMENTED` by `HandH1998` (https://github.com/sgl-project/sglang/pull/16892#pullrequestreview-3655103954)
- `2026-01-13T15:18:20Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/16892#pullrequestreview-3656374779)
- `2026-01-13T15:18:54Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/16892#pullrequestreview-3656377418)
- `2026-01-14T01:47:58Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/16892#pullrequestreview-3658533488)
- `2026-01-25T16:15:40Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/16892#pullrequestreview-3704018901)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 13 inline comment(s)

## High-Signal Discussion

- `2026-01-13T15:18:20Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:91; signals: flashinfer, moe; excerpt: "Yes, we may need a seperate PR to upgrade flashinfer. It's a major version update and may introduce issues." (https://github.com/sgl-project/sglang/pull/16892#discussion_r2686877974)
- `2026-01-13T08:30:35Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:91; signals: flashinfer, moe; excerpt: "What flashinfer version do we need? Is it alrady released?" (https://github.com/sgl-project/sglang/pull/16892#discussion_r2685384963)
- `2026-01-13T10:33:33Z` `inline` by `HandH1998` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:91; signals: flashinfer, moe; excerpt: "We need to upgrade flashinfer to v0.6.0 then run the CI again." (https://github.com/sgl-project/sglang/pull/16892#discussion_r2685805491)
- `2026-01-13T04:16:28Z` `inline` by `HandH1998` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:1900; signals: moe; excerpt: "We can keep these for debugging and better understanding." (https://github.com/sgl-project/sglang/pull/16892#discussion_r2684750589)
- `2026-01-13T08:29:40Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:59; signals: moe; excerpt: "It seems will be overrided in L80?" (https://github.com/sgl-project/sglang/pull/16892#discussion_r2685381885)
- `2026-01-13T08:32:44Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:1800; signals: moe; excerpt: "Maybe we can update the usage in [cookbook]( for kimi-k2-thinking." (https://github.com/sgl-project/sglang/pull/16892#discussion_r2685392943)
- `2026-01-13T10:21:31Z` `inline` by `HandH1998` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:91; signals: moe; excerpt: "v0.6.0, yes it is released" (https://github.com/sgl-project/sglang/pull/16892#discussion_r2685762865)
- `2026-01-13T10:24:42Z` `inline` by `HandH1998` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:59; signals: moe; excerpt: "It is a function and is called in L80." (https://github.com/sgl-project/sglang/pull/16892#discussion_r2685774093)
- `2026-01-13T10:39:04Z` `inline` by `HandH1998` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:1800; signals: moe; excerpt: "It seems the cookbook only provides basic usage. I'm not sure if it should be put into the cookbook." (https://github.com/sgl-project/sglang/pull/16892#discussion_r2685825183)
- `2026-01-13T15:18:54Z` `inline` by `ispobock` `python/sglang/srt/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:1800; signals: moe; excerpt: "Maybe we can add a note in the Configuration Tips" (https://github.com/sgl-project/sglang/pull/16892#discussion_r2686880305)
- `2026-01-19T08:05:08Z` `issue` by `ispobock`; signals: flashinfer; excerpt: "@HandH1998 The flashinfer is already updated to 0.6.1. Could you rebase the PR and rerun the ci for testing?" (https://github.com/sgl-project/sglang/pull/16892#issuecomment-3766983685)
- `2026-01-19T08:17:04Z` `issue` by `HandH1998`; signals: flashinfer; excerpt: "@HandH1998 The flashinfer is already updated to 0.6.1. Could you rebase the PR and rerun the ci for testing? ok" (https://github.com/sgl-project/sglang/pull/16892#issuecomment-3767023534)
