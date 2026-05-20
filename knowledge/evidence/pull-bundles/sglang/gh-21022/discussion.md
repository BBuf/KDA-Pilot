# PR Discussion Digest

- Source PR: [sgl-project/sglang#21022](https://github.com/sgl-project/sglang/pull/21022)
- Source page: `sources/prs/sglang/PR-21022.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21022`
- Generated at: `2026-05-20T15:29:10.014291+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-20T12:08:10Z`
- Merged: `2026-03-25T10:08:40Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: BBuf, DarkSharpness
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-20T12:11:40Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request refactors the JIT compilation architecture handling by introducing a new ArchInfo dataclass and ... (https://github.com/sgl-project/sglang/pull/21022#pullrequestreview-3981160943)
- `2026-03-22T06:51:19Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21022#pullrequestreview-3987819304)
- `2026-03-22T06:55:23Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21022#pullrequestreview-3987822774)
- `2026-03-22T06:55:27Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/21022#pullrequestreview-3987822814)
- `2026-03-22T07:00:42Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/21022#pullrequestreview-3987831247)
- `2026-03-24T16:26:26Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/21022#pullrequestreview-4000597824)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/__main__.py`: 3 inline comment(s)
- `python/sglang/jit_kernel/utils.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-03-22T06:51:19Z` `inline` by `BBuf` `python/sglang/jit_kernel/__main__.py`:27; signals: compile, kernel; excerpt: "Should we keep -std=c++20 here as well? The JIT build still compiles these headers as C++20, and jit kernel/include/sgl kernel/utils.cuh already uses C++20 headers ..." (https://github.com/sgl-project/sglang/pull/21022#discussion_r2971159960)
- `2026-03-22T07:00:41Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/utils.py`:247; signals: kernel; excerpt: "This environent var is internally used by tvm ffi. For JIT compilation, we choose to force override this flag because we only target current ..." (https://github.com/sgl-project/sglang/pull/21022#discussion_r2971171267)
- `2026-03-22T06:55:23Z` `inline` by `BBuf` `python/sglang/jit_kernel/utils.py`:247; signals: kernel; excerpt: "Has this environment variable been added to the environment variable documentation?" (https://github.com/sgl-project/sglang/pull/21022#discussion_r2971163695)
- `2026-03-24T16:26:26Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/__main__.py`:27; signals: kernel; excerpt: "it's a mistake. I will add it back" (https://github.com/sgl-project/sglang/pull/21022#discussion_r2982826506)
- `2026-03-24T16:35:23Z` `issue` by `DarkSharpness`; signals: kernel; excerpt: "should be ready as long as JIT kernel tests passed @BBuf" (https://github.com/sgl-project/sglang/pull/21022#issuecomment-4119708986)
