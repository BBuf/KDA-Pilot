# PR Discussion Digest

- Source PR: [sgl-project/sglang#12078](https://github.com/sgl-project/sglang/pull/12078)
- Source page: `sources/prs/sglang/PR-12078.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12078`
- Generated at: `2026-05-20T15:27:32.572787+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-24T13:36:14Z`
- Merged: `2025-11-25T11:44:25Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 20 (approved=2, changes_requested=2, commented=16)
- Inline review comments: 29
- Review threads observed: 26
- Resolved/outdated thread markers: resolved=9, outdated=22
- Human participants with discussion text: iforgetmyname, ping1jing2, ssshinigami
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-24T13:39:37Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces several optimizations for Qwen models on Ascend NPUs, including the use of ... (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3376821592)
- `2025-11-01T06:26:56Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3406894542)
- `2025-11-01T06:36:28Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3406903803)
- `2025-11-01T06:46:35Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3406906943)
- `2025-11-01T07:34:35Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3406934089)
- `2025-11-01T07:43:48Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3406937228)
- `2025-11-01T07:48:39Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3406938617)
- `2025-11-02T02:34:26Z` `COMMENTED` by `sglang-bot` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3407991101)
- `2025-11-05T11:29:16Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3421402154)
- `2025-11-05T11:30:23Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3421405593)
- `2025-11-05T11:34:03Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3421417008)
- `2025-11-05T11:34:29Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3421418330)
- `2025-11-05T11:35:29Z` `COMMENTED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3421385837)
- `2025-11-12T08:32:55Z` `COMMENTED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3452220250)
- `2025-11-16T03:25:20Z` `APPROVED` by `sglang-bot` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3469249742)
- `2025-11-19T11:49:10Z` `CHANGES_REQUESTED` by `ssshinigami` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3482266462)
- `2025-11-21T11:19:28Z` `CHANGES_REQUESTED` by `ssshinigami` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3492317437)
- `2025-11-22T10:52:55Z` `COMMENTED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3496587902)
- `2025-11-25T11:25:38Z` `APPROVED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3504634345)
- `2025-11-25T11:37:09Z` `COMMENTED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/12078#pullrequestreview-3504674746)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/topk.py`: 7 inline comment(s)
- `python/sglang/srt/mem_cache/memory_pool.py`: 5 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 5 inline comment(s)
- `python/sglang/srt/utils/common.py`: 3 inline comment(s)
- `python/sglang/srt/layers/rotary_embedding.py`: 3 inline comment(s)
- `python/sglang/srt/models/qwen3_moe.py`: 2 inline comment(s)
- `python/sglang/srt/utils/__init__.py`: 1 inline comment(s)
- `python/sglang/srt/mem_cache/memory_pool_ascend.py`: 1 inline comment(s)
- `python/sglang/srt/model_executor/model_runner.py`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/w8a8_int8.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-19T11:45:59Z` `inline` by `ssshinigami` `python/sglang/srt/models/qwen3_moe.py`:403; signals: hang, kernel, moe; excerpt: "Please try to avoid this model change and create fusion pass for this kernel We have supported fusion pass manager in this PR" (https://github.com/sgl-project/sglang/pull/12078#discussion_r2541662461)
- `2025-11-05T11:28:13Z` `inline` by `iforgetmyname` `python/sglang/srt/mem_cache/memory_pool.py`:1755; signals: cache, hang, memory; excerpt: "revert this change" (https://github.com/sgl-project/sglang/pull/12078#discussion_r2494070210)
- `2025-11-01T07:34:35Z` `inline` by `ping1jing2` `python/sglang/srt/layers/moe/topk.py`:71; signals: hang, moe; excerpt: "please change it. use gating topk fused = get bool env var("SGLANG USE GATING TOPK FUSED") and is npu" (https://github.com/sgl-project/sglang/pull/12078#discussion_r2483178947)
- `2025-11-01T06:46:35Z` `inline` by `ping1jing2` `python/sglang/srt/mem_cache/memory_pool.py`:1764; signals: cache, memory; excerpt: "please remove these code and refer 11510" (https://github.com/sgl-project/sglang/pull/12078#discussion_r2483158896)
- `2025-11-01T07:48:38Z` `inline` by `ping1jing2` `python/sglang/srt/mem_cache/memory_pool.py`:1762; signals: cache, memory; excerpt: "please delete it because we have already done it at the beginning of this file." (https://github.com/sgl-project/sglang/pull/12078#discussion_r2483183470)
- `2025-11-05T11:25:50Z` `inline` by `iforgetmyname` `python/sglang/srt/layers/moe/topk.py`:888; signals: kernel, moe; excerpt: "this kernel has been introduced, pls pull the latest code" (https://github.com/sgl-project/sglang/pull/12078#discussion_r2494062784)
- `2025-11-05T11:26:10Z` `inline` by `iforgetmyname` `python/sglang/srt/layers/moe/topk.py`:71; signals: kernel, moe; excerpt: "we don't need this env var, use this kernel by default if it's robust enough" (https://github.com/sgl-project/sglang/pull/12078#discussion_r2494063767)
- `2025-11-05T11:34:03Z` `inline` by `ping1jing2` `python/sglang/srt/mem_cache/memory_pool_ascend.py`:13; signals: cache, memory; excerpt: "revert" (https://github.com/sgl-project/sglang/pull/12078#discussion_r2494084996)
- `2025-11-12T08:32:55Z` `inline` by `iforgetmyname` `python/sglang/srt/layers/moe/ep_moe/layer.py`:159; signals: moe; excerpt: "implement fused deepep moe as a standalone moe a2a backend instead Take these into consideration: - add DispatchOutputChecker type - how to escape run ..." (https://github.com/sgl-project/sglang/pull/12078#discussion_r2517382887)
- `2025-11-22T10:52:55Z` `inline` by `iforgetmyname` `python/sglang/srt/layers/moe/ep_moe/layer.py`:472; signals: moe; excerpt: "i can't really appreciate anything that does fix this issue there using flatten is just another workaround from my view" (https://github.com/sgl-project/sglang/pull/12078#discussion_r2552972971)
- `2025-11-01T06:26:56Z` `inline` by `ping1jing2` `python/sglang/srt/layers/moe/topk.py`:857; signals: moe; excerpt: "remove these useless code" (https://github.com/sgl-project/sglang/pull/12078#discussion_r2483150308)
- `2025-11-05T11:29:16Z` `inline` by `ping1jing2` `python/sglang/srt/layers/moe/topk.py`:879; signals: moe; excerpt: "same implementation:" (https://github.com/sgl-project/sglang/pull/12078#discussion_r2494072939)
