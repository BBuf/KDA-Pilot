# PR Discussion Digest

- Source PR: [sgl-project/sglang#6771](https://github.com/sgl-project/sglang/pull/6771)
- Source page: `sources/prs/sglang/PR-6771.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6771`
- Generated at: `2026-05-20T15:30:46.490499+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-30T08:16:24Z`
- Merged: `2025-07-03T16:51:38Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 17 (approved=2, changes_requested=2, commented=13)
- Inline review comments: 25
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=12, outdated=13
- Human participants with discussion text: Alcanderian, chunyuan-w, mingfeima, yanbing-j, zhyncs
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-30T08:16:47Z` `COMMENTED` by `gemini-code-assist` - Hello @chunyuan-w, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2880538318)
- `2025-05-30T08:18:05Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This PR introduces crucial support for CPU tensor parallelism when model dimensions are not evenly divisible ... (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2880541203)
- `2025-06-03T02:51:47Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2890424477)
- `2025-06-03T02:51:56Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2890424627)
- `2025-06-03T02:52:08Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2890424800)
- `2025-06-03T02:53:24Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2890426271)
- `2025-06-13T01:41:34Z` `CHANGES_REQUESTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2923184764)
- `2025-06-13T01:56:13Z` `COMMENTED` by `yanbing-j` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2923206228)
- `2025-06-13T05:26:29Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2923456533)
- `2025-06-17T02:56:04Z` `APPROVED` by `mingfeima` - LGTM now. Let's align the methd for checking cpu device, use use cpu (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2933994523)
- `2025-06-30T17:06:42Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2971954327)
- `2025-07-03T03:05:54Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2981405186)
- `2025-07-03T03:06:10Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2981406316)
- `2025-07-03T03:06:26Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2981407411)
- `2025-07-03T05:40:14Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2981777009)
- `2025-07-03T14:32:07Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2983433715)
- `2025-07-03T14:35:44Z` `APPROVED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6771#pullrequestreview-2983446809)

## Inline Comment Hotspots

- `python/sglang/srt/utils.py`: 9 inline comment(s)
- `python/sglang/srt/layers/parameter.py`: 6 inline comment(s)
- `python/sglang/srt/layers/linear.py`: 3 inline comment(s)
- `python/sglang/srt/model_executor/model_runner.py`: 2 inline comment(s)
- `python/sglang/srt/models/qwen2.py`: 2 inline comment(s)
- `python/sglang/srt/models/mllama4.py`: 2 inline comment(s)
- `python/sglang/srt/layers/vocab_parallel_embedding.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-03T02:53:24Z` `inline` by `chunyuan-w` `python/sglang/srt/model_executor/model_runner.py`:562; signals: hang; excerpt: "We want to limit this change to CPU only." (https://github.com/sgl-project/sglang/pull/6771#discussion_r2122518867)
- `2025-06-30T16:39:58Z` `inline` by `Alcanderian` `python/sglang/srt/utils.py`:2610; signals: aligned; excerpt: "Move into srt/configs/update config.py and rename it to adjust config with unaligned cpu tp" (https://github.com/sgl-project/sglang/pull/6771#discussion_r2175492796)
- `2025-06-13T05:26:29Z` `inline` by `chunyuan-w` `python/sglang/srt/layers/linear.py`:414; signals: general review; excerpt: "I updated the code to use the API that will be added in to do device check. We need to wait for to land ..." (https://github.com/sgl-project/sglang/pull/6771#discussion_r2144231310)
- `2025-06-30T17:06:15Z` `inline` by `Alcanderian` `python/sglang/srt/models/mllama4.py`:116; signals: general review; excerpt: "There is a potential risk of these code spreading to various models. And could we make original total num kv heads must be available ..." (https://github.com/sgl-project/sglang/pull/6771#discussion_r2175536274)
- `2025-06-03T02:51:46Z` `inline` by `chunyuan-w` `python/sglang/srt/layers/parameter.py`:103; signals: general review; excerpt: "Fixed" (https://github.com/sgl-project/sglang/pull/6771#discussion_r2122517296)
- `2025-06-03T02:51:56Z` `inline` by `chunyuan-w` `python/sglang/srt/layers/parameter.py`:145; signals: general review; excerpt: "Fixed" (https://github.com/sgl-project/sglang/pull/6771#discussion_r2122517404)
- `2025-06-03T02:52:08Z` `inline` by `chunyuan-w` `python/sglang/srt/layers/parameter.py`:228; signals: general review; excerpt: "Fixed" (https://github.com/sgl-project/sglang/pull/6771#discussion_r2122517573)
- `2025-06-13T01:41:24Z` `inline` by `mingfeima` `python/sglang/srt/layers/linear.py`:414; signals: general review; excerpt: "@yanbing-j do we have better approach to do the device check ?" (https://github.com/sgl-project/sglang/pull/6771#discussion_r2144042371)
- `2025-06-13T01:56:12Z` `inline` by `yanbing-j` `python/sglang/srt/layers/linear.py`:414; signals: general review; excerpt: "Yes, I have added use cpu in utils.py to do the device check. Please go to for detailed info." (https://github.com/sgl-project/sglang/pull/6771#discussion_r2144058283)
- `2025-06-30T16:41:19Z` `inline` by `Alcanderian` `python/sglang/srt/utils.py`:2685; signals: general review; excerpt: "Move into srt/model loader/weight utils.py" (https://github.com/sgl-project/sglang/pull/6771#discussion_r2175495164)
- `2025-06-30T16:58:54Z` `inline` by `Alcanderian` `python/sglang/srt/utils.py`:2623; signals: general review; excerpt: "Be careful that for some models head dim != hidden size / num attn heads (such as DeepSeek)" (https://github.com/sgl-project/sglang/pull/6771#discussion_r2175525324)
- `2025-07-03T03:05:54Z` `inline` by `chunyuan-w` `python/sglang/srt/utils.py`:2685; signals: general review; excerpt: "Done" (https://github.com/sgl-project/sglang/pull/6771#discussion_r2181479308)
