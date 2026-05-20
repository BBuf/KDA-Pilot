# PR Discussion Digest

- Source PR: [sgl-project/sglang#16171](https://github.com/sgl-project/sglang/pull/16171)
- Source page: `sources/prs/sglang/PR-16171.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-16171`
- Generated at: `2026-05-20T15:28:20.412097+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-30T13:40:11Z`
- Merged: `2026-01-01T02:10:36Z`

## Discussion Counts

- Issue comments: 20
- Review submissions: 14 (approved=2, commented=12)
- Inline review comments: 11
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=2
- Human participants with discussion text: BBuf, DarkSharpness, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-30T13:42:40Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to optimize the Vision Language Model's VisionAttention by adopting a JIT kernel ... (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3618278900)
- `2025-12-31T05:58:33Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3620306257)
- `2025-12-31T06:03:25Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3620311101)
- `2025-12-31T06:11:06Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3620318011)
- `2025-12-31T06:40:11Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3620346106)
- `2025-12-31T06:50:08Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3620356340)
- `2025-12-31T06:53:32Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3620359271)
- `2025-12-31T09:27:24Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3620539383)
- `2025-12-31T09:34:02Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3620548224)
- `2025-12-31T09:54:00Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3620580901)
- `2025-12-31T09:54:55Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3620582577)
- `2025-12-31T11:20:45Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3620719754)
- `2025-12-31T11:31:23Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3620732200)
- `2025-12-31T15:41:15Z` `APPROVED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/16171#pullrequestreview-3621070247)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/vision.py`: 5 inline comment(s)
- `python/sglang/jit_kernel/benchmark/bench_qknorm.py`: 4 inline comment(s)
- `python/sglang/jit_kernel/norm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-31T06:40:11Z` `inline` by `BBuf` `python/sglang/jit_kernel/benchmark/bench_qknorm.py`:32; signals: benchmark, hang, kernel; excerpt: "Why we change this?" (https://github.com/sgl-project/sglang/pull/16171#discussion_r2654893911)
- `2025-12-31T06:53:32Z` `inline` by `yuan-luo` `python/sglang/jit_kernel/benchmark/bench_qknorm.py`:32; signals: benchmark, cuda, kernel; excerpt: "current stream = torch.cuda.current stream() has a large CPU overhead." (https://github.com/sgl-project/sglang/pull/16171#discussion_r2654906835)
- `2025-12-31T01:52:49Z` `issue` by `yuan-luo`; signals: compile, hang, sm90; excerpt: "I think it's related with this change recently. It goes DEFAULT ENABLE BELOW SM90=on branch. So it appends -gencode=arch=compute 89,code=sm 89 in ccmake flag. ..." (https://github.com/sgl-project/sglang/pull/16171#issuecomment-3701158757)
- `2025-12-31T04:50:52Z` `issue` by `yuan-luo`; signals: cuda, h100, kernel; excerpt: "@yuan-luo JIT kernel compilation won't use the CMake config in sgl-kernel. JIT kernels builds on tvm-ffi, which gets cuda arch fromTVM FFI CUDA ARCH ..." (https://github.com/sgl-project/sglang/pull/16171#issuecomment-3701441196)
- `2025-12-31T05:58:33Z` `inline` by `DarkSharpness` `python/sglang/srt/layers/attention/vision.py`:808; signals: attention, kernel; excerpt: "the reshape and contiguous can be even slower than qk norm, so try to eliminate this if possible. If there're still cases where num ..." (https://github.com/sgl-project/sglang/pull/16171#discussion_r2654856028)
- `2025-12-31T06:50:08Z` `inline` by `yuan-luo` `python/sglang/jit_kernel/benchmark/bench_qknorm.py`:32; signals: benchmark, kernel; excerpt: "This is a suggestion from @merrymercy as below:" (https://github.com/sgl-project/sglang/pull/16171#discussion_r2654903876)
- `2025-12-31T09:34:02Z` `inline` by `DarkSharpness` `python/sglang/srt/layers/attention/vision.py`:808; signals: attention, memory; excerpt: "is this reshape really needed? I think we should try to avoid any unnecessary memory copy" (https://github.com/sgl-project/sglang/pull/16171#discussion_r2655090469)
- `2025-12-31T11:20:45Z` `inline` by `BBuf` `python/sglang/jit_kernel/benchmark/bench_qknorm.py`:32; signals: benchmark, kernel; excerpt: "Ok." (https://github.com/sgl-project/sglang/pull/16171#discussion_r2655240145)
- `2025-12-30T15:18:46Z` `issue` by `DarkSharpness`; signals: compile, hopper; excerpt: "@yuan-luo The following error you get should be a bug of the function is arch support pdl. On your machine (sm 89), the PDL ..." (https://github.com/sgl-project/sglang/pull/16171#issuecomment-3699680313)
- `2025-12-31T01:40:54Z` `issue` by `yuan-luo`; signals: compile, hopper; excerpt: "@yuan-luo The following error you get should be a bug of the function is arch support pdl. On your machine (sm 89), the PDL ..." (https://github.com/sgl-project/sglang/pull/16171#issuecomment-3701106277)
- `2025-12-31T04:28:42Z` `issue` by `DarkSharpness`; signals: cuda, kernel; excerpt: "@yuan-luo JIT kernel compilation won't use the CMake config in sgl-kernel. JIT kernels builds on tvm-ffi, which gets cuda arch fromTVM FFI CUDA ARCH ..." (https://github.com/sgl-project/sglang/pull/16171#issuecomment-3701418565)
- `2025-12-31T10:04:39Z` `issue` by `yuan-luo`; signals: h100, kernel; excerpt: "@DarkSharpness @BBuf In H20 I encountered another jit kernel compilation failure issue, not related with this PR, it might be an environmental issue related ..." (https://github.com/sgl-project/sglang/pull/16171#issuecomment-3701881203)
