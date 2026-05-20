# PR Discussion Digest

- Source PR: [sgl-project/sglang#13873](https://github.com/sgl-project/sglang/pull/13873)
- Source page: `sources/prs/sglang/PR-13873.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13873`
- Generated at: `2026-05-20T15:27:53.136876+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-25T02:35:29Z`
- Merged: `2025-12-01T03:33:18Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=3
- Human participants with discussion text: BBuf, Kevin-XiongC, ShangmingCai, UranusSeven, jimmy-evo, sysia48
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-11-25T02:38:27Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces an optimization to fuse shared experts for GLM-4 MoE models, which can ... (https://github.com/sgl-project/sglang/pull/13873#pullrequestreview-3503047328)
- `2025-11-25T03:02:27Z` `COMMENTED` by `UranusSeven` (https://github.com/sgl-project/sglang/pull/13873#pullrequestreview-3503090994)
- `2025-11-26T07:12:20Z` `COMMENTED` by `ShangmingCai` - Looks great. CC: @zRzRzRzRzRzRzR can you help review this PR? (https://github.com/sgl-project/sglang/pull/13873#pullrequestreview-3509303431)
- `2025-11-27T12:40:55Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/13873#pullrequestreview-3515121642)
- `2025-11-27T12:44:20Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/13873#pullrequestreview-3515140894)
- `2025-11-27T12:46:57Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/13873#pullrequestreview-3515156469)
- `2025-11-28T14:38:37Z` `COMMENTED` by `jimmy-evo` (https://github.com/sgl-project/sglang/pull/13873#pullrequestreview-3519228609)
- `2025-11-28T14:39:25Z` `COMMENTED` by `jimmy-evo` (https://github.com/sgl-project/sglang/pull/13873#pullrequestreview-3519230790)
- `2025-12-01T03:31:13Z` `APPROVED` by `BBuf` - LGTM. (https://github.com/sgl-project/sglang/pull/13873#pullrequestreview-3523037529)

## Inline Comment Hotspots

- `python/sglang/srt/models/glm4_moe.py`: 8 inline comment(s)

## High-Signal Discussion

- `2025-11-25T03:02:27Z` `inline` by `UranusSeven` `python/sglang/srt/models/glm4_moe.py`:363; signals: moe; excerpt: "Crash is preferred if the config is incorrect." (https://github.com/sgl-project/sglang/pull/13873#discussion_r2558399267)
- `2025-11-27T12:40:55Z` `inline` by `BBuf` `python/sglang/srt/models/glm4_moe.py`:1031; signals: moe; excerpt: "self.num fused shared experts = 0 can be moved down." (https://github.com/sgl-project/sglang/pull/13873#discussion_r2568486857)
- `2025-11-27T12:44:19Z` `inline` by `BBuf` `python/sglang/srt/models/glm4_moe.py`:1114; signals: moe; excerpt: "Don't add logs inside forward; put them in init instead." (https://github.com/sgl-project/sglang/pull/13873#discussion_r2568501061)
- `2025-11-28T14:38:36Z` `inline` by `jimmy-evo` `python/sglang/srt/models/glm4_moe.py`:1139; signals: moe; excerpt: "assert self.config.n shared experts == 1 this assertion is in determine num fused shared experts" (https://github.com/sgl-project/sglang/pull/13873#discussion_r2571872935)
- `2025-11-28T14:39:25Z` `inline` by `jimmy-evo` `python/sglang/srt/models/glm4_moe.py`:1031; signals: moe; excerpt: "set in init as deepseek v2 does so" (https://github.com/sgl-project/sglang/pull/13873#discussion_r2571874926)
- `2025-11-26T07:12:20Z` `review` `COMMENTED` by `ShangmingCai`; signals: general review; excerpt: "Looks great. CC: @zRzRzRzRzRzRzR can you help review this PR?" (https://github.com/sgl-project/sglang/pull/13873#pullrequestreview-3509303431)
