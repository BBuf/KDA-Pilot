# PR Discussion Digest

- Source PR: [sgl-project/sglang#17707](https://github.com/sgl-project/sglang/pull/17707)
- Source page: `sources/prs/sglang/PR-17707.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-17707`
- Generated at: `2026-05-20T15:28:31.268608+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-25T13:34:46Z`
- Merged: `2026-04-04T08:18:01Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 38 (approved=5, changes_requested=1, commented=32)
- Inline review comments: 39
- Review threads observed: 16
- Resolved/outdated thread markers: resolved=9, outdated=12
- Human participants with discussion text: Fridge003, b8zhong, harrisonlimh, leejnau, nv-yunzheq, nvpohanh
- Automation comments/reviews omitted from high-signal summary: 8
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2026-01-25T13:36:33Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds a new benchmark script to compare the performance of dsv3 router gemm ... (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3703881557)
- `2026-01-29T18:26:43Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3724349821)
- `2026-02-03T18:20:49Z` `COMMENTED` by `leejnau` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3746833690)
- `2026-02-04T00:57:17Z` `COMMENTED` by `nv-yunzheq` - @harrisonlimh Could you help fix the issues of tensor creation, pdl issue and rerun the benchmark? I think ... (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3748394555)
- `2026-02-04T11:03:49Z` `COMMENTED` by `harrisonlimh` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3750398623)
- `2026-02-09T17:32:08Z` `COMMENTED` by `leejnau` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3774459237)
- `2026-02-09T17:44:14Z` `COMMENTED` by `leejnau` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3774515831)
- `2026-02-09T17:56:38Z` `COMMENTED` by `leejnau` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3774569804)
- `2026-02-09T18:19:26Z` `COMMENTED` by `leejnau` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3774682623)
- `2026-02-11T23:30:53Z` `COMMENTED` by `harrisonlimh` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3788024856)
- `2026-02-12T00:19:17Z` `COMMENTED` by `leejnau` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3788131291)
- `2026-02-12T00:47:38Z` `COMMENTED` by `harrisonlimh` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3788202827)
- `2026-02-12T01:09:41Z` `COMMENTED` by `harrisonlimh` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3788265187)
- `2026-02-12T01:09:58Z` `COMMENTED` by `harrisonlimh` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3788265755)
- `2026-02-12T01:11:23Z` `COMMENTED` by `harrisonlimh` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3788268702)
- `2026-02-12T12:26:40Z` `COMMENTED` by `nvpohanh` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3790730157)
- `2026-02-12T15:48:45Z` `COMMENTED` by `leejnau` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3791829657)
- `2026-02-12T15:52:44Z` `COMMENTED` by `leejnau` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3791852259)
- `2026-02-12T19:27:37Z` `COMMENTED` by `harrisonlimh` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3793188700)
- `2026-02-13T05:57:51Z` `COMMENTED` by `leejnau` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3795212535)
- `2026-02-13T07:57:32Z` `COMMENTED` by `nvpohanh` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3795605899)
- `2026-02-22T05:36:58Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3836769955)
- `2026-02-23T02:13:41Z` `COMMENTED` by `harrisonlimh` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3838836615)
- `2026-02-23T03:47:07Z` `COMMENTED` by `harrisonlimh` (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3839039613)
- ... 14 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 19 inline comment(s)
- `benchmark/kernels/deepseek/benchmark_deepgemm_dsv3_router_gemm_blackwell.py`: 10 inline comment(s)
- `python/sglang/srt/environ.py`: 8 inline comment(s)
- `sglang`: 2 inline comment(s)

## High-Signal Discussion

- `2026-02-04T11:03:48Z` `inline` by `harrisonlimh` `benchmark/kernels/deepseek/benchmark_deepgemm_dsv3_router_gemm_blackwell.py`:28; signals: benchmark, blackwell, deepgemm, flashinfer, gemm, hang, kernel, perf; excerpt: "Hi! Thank you for the feedback! Please see below for follow ups!: Made the suggested change and attached the result that compares PDL enabled ..." (https://github.com/sgl-project/sglang/pull/17707#discussion_r2763433370)
- `2026-01-29T18:26:38Z` `inline` by `Fridge003` `benchmark/kernels/deepseek/benchmark_deepgemm_dsv3_router_gemm_blackwell.py`:6; signals: benchmark, blackwell, deepgemm, flashinfer, gemm, kernel; excerpt: "I feel you are importing a specific kernel from flashinfer, which is not expected? There should be a general interface in flashinfer I guess, ..." (https://github.com/sgl-project/sglang/pull/17707#discussion_r2742961478)
- `2026-02-03T18:20:49Z` `inline` by `leejnau` `benchmark/kernels/deepseek/benchmark_deepgemm_dsv3_router_gemm_blackwell.py`:6; signals: benchmark, blackwell, deepgemm, flashinfer, gemm, kernel; excerpt: "I feel you are importing a specific kernel from flashinfer, which is not expected? There should be a general interface in flashinfer I guess, ..." (https://github.com/sgl-project/sglang/pull/17707#discussion_r2760391105)
- `2026-02-04T00:53:58Z` `inline` by `nv-yunzheq` `benchmark/kernels/deepseek/benchmark_deepgemm_dsv3_router_gemm_blackwell.py`:28; signals: benchmark, blackwell, deepgemm, gemm, kernel; excerpt: "As benchmark script, output should not be created with randn, as it introduce addtional overhead. We should use empty just like how SGLang function ..." (https://github.com/sgl-project/sglang/pull/17707#discussion_r2761674117)
- `2026-02-04T00:57:17Z` `review` `COMMENTED` by `nv-yunzheq`; signals: benchmark, kernel, perf, performance; excerpt: "@harrisonlimh Could you help fix the issues of tensor creation, pdl issue and rerun the benchmark? I think on kernel-level, two kernel should be ..." (https://github.com/sgl-project/sglang/pull/17707#pullrequestreview-3748394555)
- `2026-02-04T10:57:29Z` `issue` by `harrisonlimh`; signals: benchmark, flashinfer, kernel, perf, performance; excerpt: "Flashinfer vs. SGLang kernel performance comparison Performance is essentially on par between two kernels as explained by the team, especially when using PDL. 1. ..." (https://github.com/sgl-project/sglang/pull/17707#issuecomment-3846741514)
- `2026-02-12T01:11:23Z` `inline` by `harrisonlimh` `python/sglang/srt/models/deepseek_v2.py`:358; signals: flashinfer, kernel, perf, performance; excerpt: "Removed it for now, but as PDL is off by default, it will always be disabled when using flashinfer, which would result in worse ..." (https://github.com/sgl-project/sglang/pull/17707#discussion_r2796300861)
- `2026-01-25T13:51:43Z` `issue` by `harrisonlimh`; signals: flashinfer, kernel, perf, performance; excerpt: "The result seems to suggest that the new flashinfer kernel only boosts the performance for m=6 and is limited to 0.365% gain. As I ..." (https://github.com/sgl-project/sglang/pull/17707#issuecomment-3796695107)
- `2026-02-03T18:24:57Z` `issue` by `leejnau`; signals: flashinfer, kernel, perf, performance; excerpt: "The result seems to suggest that the new flashinfer kernel only boosts the performance for m=6 and is limited to 0.365% gain. As I ..." (https://github.com/sgl-project/sglang/pull/17707#issuecomment-3842932476)
- `2026-02-03T23:48:47Z` `issue` by `nv-yunzheq`; signals: hang, perf, performance, regression; excerpt: "@harrisonlimh I think we should not compare the native implementation with launch with pdl set to False. To get it comparable with native integration, ..." (https://github.com/sgl-project/sglang/pull/17707#issuecomment-3844423146)
- `2026-02-04T19:34:23Z` `issue` by `leejnau`; signals: flashinfer, gemm, perf, performance; excerpt: "@harrisonlimh I discussed with @nv-yunzheq and based on your current findings with PDL enabled showing performance parity, it is safe to proceed with integrating ..." (https://github.com/sgl-project/sglang/pull/17707#issuecomment-3849361686)
- `2026-02-12T00:47:14Z` `issue` by `harrisonlimh`; signals: benchmark, flashinfer, hang; excerpt: "E2E benchmark results. Both runs are done with PDL and confirm that they are on par for ITL. Before change With Flashinfer" (https://github.com/sgl-project/sglang/pull/17707#issuecomment-3888042415)
