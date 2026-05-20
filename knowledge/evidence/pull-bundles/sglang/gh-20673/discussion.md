# PR Discussion Digest

- Source PR: [sgl-project/sglang#20673](https://github.com/sgl-project/sglang/pull/20673)
- Source page: `sources/prs/sglang/PR-20673.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-20673`
- Generated at: `2026-05-20T15:29:06.552763+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-16T08:18:31Z`
- Merged: `2026-04-13T12:29:47Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 11
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=5, outdated=4
- Human participants with discussion text: BBuf, DarkSharpness, nvpohanh, trevor-m
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-03-16T08:36:21Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a significant performance optimization by adding a JIT-compiled fused kernel for tensor-parallel ... (https://github.com/sgl-project/sglang/pull/20673#pullrequestreview-3952212918)
- `2026-03-26T08:23:29Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20673#pullrequestreview-4012227364)
- `2026-03-26T08:24:48Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20673#pullrequestreview-4012233432)
- `2026-03-26T08:41:35Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20673#pullrequestreview-4012323193)
- `2026-03-26T08:42:13Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20673#pullrequestreview-4012326218)
- `2026-03-26T13:41:30Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/20673#pullrequestreview-4014264984)
- `2026-03-26T13:45:45Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/20673#pullrequestreview-4014300291)
- `2026-03-26T13:47:18Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/20673#pullrequestreview-4014312201)
- `2026-03-27T03:49:48Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20673#pullrequestreview-4018702779)
- `2026-03-27T03:50:10Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/20673#pullrequestreview-4018703481)
- `2026-04-10T17:44:31Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/20673#pullrequestreview-4091483579)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/csrc/distributed/tp_qknorm.cuh`: 5 inline comment(s)
- `python/sglang/srt/models/minimax_m2.py`: 4 inline comment(s)
- `python/sglang/jit_kernel/benchmark/bench_tp_qknorm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-26T13:47:18Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/benchmark/bench_tp_qknorm.py`:112; signals: benchmark, kernel, perf, performance; excerpt: "not inplace. should be fixed (though this is just a benchmark, the performance result is still correct)" (https://github.com/sgl-project/sglang/pull/20673#discussion_r2995028636)
- `2026-03-16T08:24:36Z` `issue` by `DarkSharpness`; signals: b200, h200, perf, performance; excerpt: "Performance result (q dim = 6144, k dim = 1024, TP=4): H200 q dim k dim batch fused us baseline us --- --- --- ..." (https://github.com/sgl-project/sglang/pull/20673#issuecomment-4065919823)
- `2026-03-26T08:23:29Z` `inline` by `BBuf` `python/sglang/jit_kernel/benchmark/bench_tp_qknorm.py`:112; signals: benchmark, kernel; excerpt: "Is this custom all reduce op a inplace op?" (https://github.com/sgl-project/sglang/pull/20673#discussion_r2993210156)
- `2026-03-26T08:41:35Z` `inline` by `BBuf` `python/sglang/jit_kernel/csrc/distributed/tp_qknorm.cuh`:194; signals: kernel; excerpt: "I think eps is being applied in the wrong place here. Right now it is added before the cross-GPU reduction, so the final formula ..." (https://github.com/sgl-project/sglang/pull/20673#discussion_r2993291961)
- `2026-03-26T13:41:29Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/csrc/distributed/tp_qknorm.cuh`:194; signals: kernel; excerpt: "We already scale the eps at host side params.eps = eps / kNumGPU; // scale down eps by number of GPUs which is documented ..." (https://github.com/sgl-project/sglang/pull/20673#discussion_r2994988805)
- `2026-03-27T03:49:47Z` `inline` by `BBuf` `python/sglang/jit_kernel/csrc/distributed/tp_qknorm.cuh`:194; signals: kernel; excerpt: "Ok" (https://github.com/sgl-project/sglang/pull/20673#discussion_r2998822107)
- `2026-03-26T08:42:13Z` `inline` by `BBuf` `python/sglang/srt/models/minimax_m2.py`:368; signals: general review; excerpt: "This fused path seems to hard-code a 1 MB push buffer, but the required buffer size grows with num tokens. For larger batches / ..." (https://github.com/sgl-project/sglang/pull/20673#discussion_r2993295282)
- `2026-03-26T13:45:45Z` `inline` by `DarkSharpness` `python/sglang/srt/models/minimax_m2.py`:368; signals: general review; excerpt: "It's hard to pass the max global tokens here. 1MB is actually quite a large buffer, since the each token which only consume 8 ..." (https://github.com/sgl-project/sglang/pull/20673#discussion_r2995018476)
- `2026-03-26T08:24:48Z` `inline` by `BBuf` `python/sglang/srt/models/minimax_m2.py`:348; signals: general review; excerpt: "Should we add this environment variable to doc?" (https://github.com/sgl-project/sglang/pull/20673#discussion_r2993215857)
- `2026-04-10T17:44:31Z` `inline` by `trevor-m` `python/sglang/srt/models/minimax_m2.py`:348; signals: general review; excerpt: "Can this be a server arg instead of an env var?" (https://github.com/sgl-project/sglang/pull/20673#discussion_r3065870439)
