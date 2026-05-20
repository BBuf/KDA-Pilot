# PR Discussion Digest

- Source PR: [sgl-project/sglang#15631](https://github.com/sgl-project/sglang/pull/15631)
- Source page: `sources/prs/sglang/PR-15631.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15631`
- Generated at: `2026-05-20T15:28:14.851630+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-22T09:49:27Z`
- Merged: `2026-01-18T20:54:36Z`

## Discussion Counts

- Issue comments: 21
- Review submissions: 15 (approved=2, commented=13)
- Inline review comments: 16
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=13, outdated=12
- Human participants with discussion text: BBuf, DarkSharpness, Fridge003, RubiaCx, hebiao064, liz-badada, merrymercy, zhyncs
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-12-22T09:52:44Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new, high-performance CuTe DSL kernel for the GDN decode operation, which ... (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3603400202)
- `2026-01-01T00:57:58Z` `COMMENTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3621557455)
- `2026-01-04T17:42:03Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3625107293)
- `2026-01-05T00:53:45Z` `COMMENTED` by `liz-badada` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3625267436)
- `2026-01-05T04:25:34Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3625454815)
- `2026-01-05T04:26:44Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3625456145)
- `2026-01-13T06:32:54Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3654077320)
- `2026-01-13T06:37:37Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3654091069)
- `2026-01-13T07:02:00Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3654163848)
- `2026-01-13T07:02:08Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3654164179)
- `2026-01-13T07:03:03Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3654166461)
- `2026-01-13T07:04:27Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3654171658)
- `2026-01-14T08:22:28Z` `COMMENTED` by `liz-badada` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3659458045)
- `2026-01-16T05:49:06Z` `APPROVED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3669003731)
- `2026-01-16T06:39:33Z` `APPROVED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/15631#pullrequestreview-3669178276)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`: 7 inline comment(s)
- `python/pyproject.toml`: 4 inline comment(s)
- `sgl-kernel/python/sgl_kernel/__init__.py`: 3 inline comment(s)
- `sgl-kernel/tests/test_cutedsl_gdn.py`: 1 inline comment(s)
- `python/sglang/jit_kernel/cutedsl_gdn.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-15T17:20:53Z` `issue` by `liz-badada`; signals: attention, block, cute, kernel, moe, perf, speedup, triton; excerpt: "Nice work! Could you share a perf comparison vs the current Triton decode path on a few key shapes, plus exact HW/SW configs? From ..." (https://github.com/sgl-project/sglang/pull/15631#issuecomment-3756009221)
- `2026-01-15T17:19:14Z` `issue` by `liz-badada`; signals: b200, h200, kernel, perf, performance; excerpt: "Single kernel performance H200 B200 H20" (https://github.com/sgl-project/sglang/pull/15631#issuecomment-3756002793)
- `2026-01-13T07:02:00Z` `inline` by `hebiao064` `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`:51; signals: attention, cute, kernel; excerpt: "this seems to be too verbose, and we should move this to common utils instead of attention backend. regarding detecting whether is cutedsl gdn ..." (https://github.com/sgl-project/sglang/pull/15631#discussion_r2685106933)
- `2026-01-13T07:04:27Z` `inline` by `hebiao064` `sgl-kernel/python/sgl_kernel/__init__.py`:135; signals: cute, cutlass, kernel; excerpt: "curious do we need to modify anything in pyproject.toml to include dependencies needed for cutlass/cute?" (https://github.com/sgl-project/sglang/pull/15631#discussion_r2685113837)
- `2026-01-13T07:28:35Z` `issue` by `RubiaCx`; signals: kernel, perf, triton; excerpt: "Nice work! Could you share a perf comparison vs the current Triton decode path on a few key shapes, plus exact HW/SW configs? From ..." (https://github.com/sgl-project/sglang/pull/15631#issuecomment-3742486212)
- `2026-01-01T00:57:56Z` `inline` by `merrymercy` `python/sglang/jit_kernel/cutedsl_gdn.py`:1373; signals: cute, kernel; excerpt: "for jit kernels, we can directly put under The sgl-kernel package is mostly for kernels that need AOT" (https://github.com/sgl-project/sglang/pull/15631#discussion_r2656016965)
- `2026-01-04T17:42:03Z` `inline` by `DarkSharpness` `python/pyproject.toml`:41; signals: cutlass, kernel; excerpt: "As far as I know, sgl kernel seems to have some compatibility issue with latest cutlass-dsl. Maybe we should fix this to a tested ..." (https://github.com/sgl-project/sglang/pull/15631#discussion_r2659820262)
- `2026-01-13T07:03:03Z` `inline` by `hebiao064` `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`:65; signals: attention, cute; excerpt: "why cutedsl fused sigmoid gating delta rule update instead of cutedsl fused sigmoid gating delta rule update ? cutedsl fused sigmoid gating delta rule ..." (https://github.com/sgl-project/sglang/pull/15631#discussion_r2685109616)
- `2026-01-14T08:22:28Z` `inline` by `liz-badada` `sgl-kernel/python/sgl_kernel/__init__.py`:135; signals: cutlass, kernel; excerpt: "The only one that need to modify in pyproject.toml is to set "nvidia-cutlass-dsl =4.3.0" or just fixed as 4.3.0, but it seems somehow not ..." (https://github.com/sgl-project/sglang/pull/15631#discussion_r2689442176)
- `2026-01-05T00:53:45Z` `inline` by `liz-badada` `python/pyproject.toml`:41; signals: cutlass; excerpt: "How about nvidia-cutlass-dsl==4.3.0? I checked 4.2.1 doesn't support python function make rmem tensor, I tested with 4.3.0" (https://github.com/sgl-project/sglang/pull/15631#discussion_r2660057341)
- `2026-01-13T06:32:54Z` `inline` by `hebiao064` `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`:942; signals: attention; excerpt: "let's use rank0 log" (https://github.com/sgl-project/sglang/pull/15631#discussion_r2685030743)
- `2026-01-13T06:37:37Z` `inline` by `hebiao064` `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`:45; signals: attention; excerpt: "add env variable to" (https://github.com/sgl-project/sglang/pull/15631#discussion_r2685042431)
