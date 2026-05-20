# PR Discussion Digest

- Source PR: [sgl-project/sglang#6769](https://github.com/sgl-project/sglang/pull/6769)
- Source page: `sources/prs/sglang/PR-6769.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6769`
- Generated at: `2026-05-20T15:30:46.488941+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-30T08:02:43Z`
- Merged: `2025-06-28T02:04:29Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 17 (approved=3, changes_requested=2, commented=12)
- Inline review comments: 19
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=6, outdated=8
- Human participants with discussion text: Alcanderian, chunyuan-w, mickqian, mingfeima, zhyncs
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 7

## Review Decisions

- `2025-05-30T08:03:20Z` `COMMENTED` by `gemini-code-assist` - Hello @chunyuan-w, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post my feedback shortly. ... (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2880508028)
- `2025-05-30T08:05:09Z` `CHANGES_REQUESTED` by `gemini-code-assist` - Code Review This PR adds valuable CPU optimizations for DeepSeek models using Intel AMX for INT8 and FP8. ... (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2880511937)
- `2025-06-05T02:45:47Z` `CHANGES_REQUESTED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2898700629)
- `2025-06-05T06:25:26Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2899018780)
- `2025-06-05T06:25:41Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2899019235)
- `2025-06-05T06:27:28Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2899023124)
- `2025-06-05T06:30:35Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2899029252)
- `2025-06-05T07:07:37Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2899110103)
- `2025-06-09T05:27:16Z` `APPROVED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2908949957)
- `2025-06-09T05:30:03Z` `APPROVED` by `mingfeima` (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2908954675)
- `2025-06-26T01:04:03Z` `COMMENTED` by `mickqian` (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2960085850)
- `2025-06-26T03:00:19Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2960391404)
- `2025-06-26T04:39:18Z` `COMMENTED` by `chunyuan-w` (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2960520974)
- `2025-06-26T08:08:25Z` `APPROVED` by `mickqian` (https://github.com/sgl-project/sglang/pull/6769#pullrequestreview-2961153964)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 11 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8.py`: 4 inline comment(s)
- `python/sglang/srt/layers/quantization/w8a8_int8.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-05T02:40:02Z` `inline` by `mingfeima` `python/sglang/srt/models/deepseek_v2.py`:291; signals: dtype; excerpt: "can we skip the checks here? gate up proj.weight.dtype should be the same as gate down proj.weight.dtype, do we have exceptions? if we can ..." (https://github.com/sgl-project/sglang/pull/6769#discussion_r2127830210)
- `2025-06-05T02:44:49Z` `inline` by `mingfeima` `python/sglang/srt/models/deepseek_v2.py`:358; signals: general review; excerpt: "call forward cpu from forward normal?" (https://github.com/sgl-project/sglang/pull/6769#discussion_r2127833898)
- `2025-06-05T02:45:41Z` `inline` by `mingfeima` `python/sglang/srt/models/deepseek_v2.py`:1995; signals: general review; excerpt: "put a TODO here" (https://github.com/sgl-project/sglang/pull/6769#discussion_r2127834483)
- `2025-06-05T06:25:26Z` `inline` by `chunyuan-w` `python/sglang/srt/models/deepseek_v2.py`:272; signals: general review; excerpt: "Fixed" (https://github.com/sgl-project/sglang/pull/6769#discussion_r2128047781)
- `2025-06-05T06:25:40Z` `inline` by `chunyuan-w` `python/sglang/srt/models/deepseek_v2.py`:1995; signals: general review; excerpt: "TODO has been added" (https://github.com/sgl-project/sglang/pull/6769#discussion_r2128048091)
- `2025-06-05T06:27:28Z` `inline` by `chunyuan-w` `python/sglang/srt/models/deepseek_v2.py`:358; signals: general review; excerpt: "I updated this in Could you check if the updated code is good now?" (https://github.com/sgl-project/sglang/pull/6769#discussion_r2128050713)
- `2025-06-05T06:30:35Z` `inline` by `chunyuan-w` `python/sglang/srt/models/deepseek_v2.py`:291; signals: general review; excerpt: "Yes they should be the same. Let me remove this check." (https://github.com/sgl-project/sglang/pull/6769#discussion_r2128054911)
- `2025-06-05T07:07:37Z` `inline` by `chunyuan-w` `python/sglang/srt/models/deepseek_v2.py`:291; signals: general review; excerpt: "Updated the code in Could you check if the updated code is good now?" (https://github.com/sgl-project/sglang/pull/6769#discussion_r2128109865)
- `2025-06-26T01:03:41Z` `inline` by `mickqian` `python/sglang/srt/layers/quantization/w8a8_int8.py`:80; signals: general review; excerpt: "Hi, what's the difference from this with is cpu?" (https://github.com/sgl-project/sglang/pull/6769#discussion_r2167888236)
- `2025-06-26T03:00:19Z` `inline` by `chunyuan-w` `python/sglang/srt/layers/quantization/w8a8_int8.py`:80; signals: general review; excerpt: "They're the same. Let me unify all these checks to use is cpu to make it clearer." (https://github.com/sgl-project/sglang/pull/6769#discussion_r2168001387)
- `2025-06-26T04:39:18Z` `inline` by `chunyuan-w` `python/sglang/srt/layers/quantization/w8a8_int8.py`:80; signals: general review; excerpt: "Code has been updated to use is cpu." (https://github.com/sgl-project/sglang/pull/6769#discussion_r2168089005)
- `2025-06-18T05:26:05Z` `issue` by `chunyuan-w`; signals: general review; excerpt: "I have fixed the conflicts. One thing is that needs to be landed first. I need to rebase the current PR after lands." (https://github.com/sgl-project/sglang/pull/6769#issuecomment-2982734223)
