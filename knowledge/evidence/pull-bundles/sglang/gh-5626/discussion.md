# PR Discussion Digest

- Source PR: [sgl-project/sglang#5626](https://github.com/sgl-project/sglang/pull/5626)
- Source page: `sources/prs/sglang/PR-5626.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5626`
- Generated at: `2026-05-20T15:30:28.040255+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-22T09:31:17Z`
- Merged: `2025-05-08T08:20:34Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 16 (commented=16)
- Inline review comments: 19
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=9, outdated=12
- Human participants with discussion text: Alcanderian, ZhengHSI, ch-wan, fzyzcjy, sleepcoo, xutizhou
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-23T12:40:03Z` `COMMENTED` by `xutizhou` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2786010192)
- `2025-04-25T00:48:32Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2792776998)
- `2025-04-25T03:32:21Z` `COMMENTED` by `sleepcoo` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2792918976)
- `2025-04-25T03:34:22Z` `COMMENTED` by `ZhengHSI` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2792920233)
- `2025-04-25T03:34:48Z` `COMMENTED` by `ZhengHSI` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2792920509)
- `2025-04-25T07:13:08Z` `COMMENTED` by `ZhengHSI` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2793199267)
- `2025-04-25T07:13:13Z` `COMMENTED` by `ZhengHSI` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2793199445)
- `2025-04-25T07:25:36Z` `COMMENTED` by `xutizhou` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2793226247)
- `2025-04-25T07:54:51Z` `COMMENTED` by `xutizhou` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2793291454)
- `2025-04-25T11:21:25Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2793801328)
- `2025-04-26T18:18:14Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2796330473)
- `2025-04-27T04:03:55Z` `COMMENTED` by `ZhengHSI` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2796916142)
- `2025-04-30T07:09:06Z` `COMMENTED` by `xutizhou` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2805994677)
- `2025-04-30T07:09:49Z` `COMMENTED` by `xutizhou` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2806000155)
- `2025-04-30T07:10:31Z` `COMMENTED` by `xutizhou` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2806005580)
- `2025-04-30T07:19:28Z` `COMMENTED` by `xutizhou` (https://github.com/sgl-project/sglang/pull/5626#pullrequestreview-2806038830)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/ep_moe/token_dispatcher.py`: 8 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 6 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/kernels.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-04-24T01:47:35Z` `issue` by `xutizhou`; signals: benchmark, deepgemm, gemm, throughput; excerpt: "I did benchmark for H20 with command Results for Baseline (w/o deepgemm) n isl osl c input throughput mean ttft ms Type ----: ------: ..." (https://github.com/sgl-project/sglang/pull/5626#issuecomment-2825953324)
- `2025-04-23T05:53:41Z` `inline` by `xutizhou` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:19; signals: gemm, kernel, moe; excerpt: "How about replacing it with try: from deep gemm import ceil div except ImportError:xxx" (https://github.com/sgl-project/sglang/pull/5626#discussion_r2055298775)
- `2025-04-30T07:09:06Z` `inline` by `xutizhou` `python/sglang/srt/layers/moe/ep_moe/layer.py`:16; signals: deepgemm, gemm, moe; excerpt: "import ENABLE JIT DEEPGEMM directly to align with" (https://github.com/sgl-project/sglang/pull/5626#discussion_r2068007435)
- `2025-04-30T07:09:49Z` `inline` by `xutizhou` `python/sglang/srt/layers/moe/ep_moe/layer.py`:21; signals: deepgemm, gemm, moe; excerpt: "use ENABLE JIT DEEPGEMM instead of enable jit deepgemm?" (https://github.com/sgl-project/sglang/pull/5626#discussion_r2068011157)
- `2025-04-30T07:10:31Z` `inline` by `xutizhou` `python/sglang/srt/layers/moe/ep_moe/layer.py`:868; signals: deepgemm, gemm, moe; excerpt: "if ENABLE JIT DEEPGEMM?" (https://github.com/sgl-project/sglang/pull/5626#discussion_r2068015152)
- `2025-04-25T03:08:45Z` `issue` by `xutizhou`; signals: cuda, kernel, memory; excerpt: "@fzyzcjy and I confronted cuda illegal memory access in fwd kernel ep scatter 2. Could you please provide the command and commit hash to ..." (https://github.com/sgl-project/sglang/pull/5626#issuecomment-2829275914)
- `2025-04-24T17:57:48Z` `issue` by `ch-wan`; signals: cuda, kernel, memory; excerpt: "@fzyzcjy and I confronted cuda illegal memory access in fwd kernel ep scatter 2." (https://github.com/sgl-project/sglang/pull/5626#issuecomment-2828454308)
- `2025-04-26T18:18:13Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/token_dispatcher.py`:198; signals: fp8, moe; excerpt: "This is a bypass related to sglang per token group quant fp8. We can move this conditional statement to that function." (https://github.com/sgl-project/sglang/pull/5626#discussion_r2061530921)
- `2025-04-25T03:32:21Z` `inline` by `sleepcoo` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:19; signals: kernel, moe; excerpt: "done" (https://github.com/sgl-project/sglang/pull/5626#discussion_r2059510849)
- `2025-04-25T03:34:22Z` `inline` by `ZhengHSI` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:19; signals: kernel, moe; excerpt: "done" (https://github.com/sgl-project/sglang/pull/5626#discussion_r2059511820)
- `2025-04-25T07:54:51Z` `inline` by `xutizhou` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:18; signals: kernel, moe; excerpt: "This part is duplicated with code: just remove it." (https://github.com/sgl-project/sglang/pull/5626#discussion_r2059747128)
- `2025-04-27T04:03:55Z` `inline` by `ZhengHSI` `python/sglang/srt/layers/moe/ep_moe/kernels.py`:18; signals: kernel, moe; excerpt: "done" (https://github.com/sgl-project/sglang/pull/5626#discussion_r2061995868)
