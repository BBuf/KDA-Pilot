# PR Discussion Digest

- Source PR: [sgl-project/sglang#20874](https://github.com/sgl-project/sglang/pull/20874)
- Source page: `sources/prs/sglang/PR-20874.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-20874`
- Generated at: `2026-05-20T15:29:08.002368+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-18T16:39:07Z`
- Merged: `2026-03-20T02:30:05Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 4 (commented=4)
- Inline review comments: 4
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: DarkSharpness, mmangkad, xingsy97
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-18T16:44:55Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/20874#pullrequestreview-3969322314)
- `2026-03-18T16:49:14Z` `COMMENTED` by `mmangkad` (https://github.com/sgl-project/sglang/pull/20874#pullrequestreview-3969354263)
- `2026-03-19T02:36:55Z` `COMMENTED` by `DarkSharpness` (https://github.com/sgl-project/sglang/pull/20874#pullrequestreview-3972343304)
- `2026-03-19T10:15:28Z` `COMMENTED` by `mmangkad` (https://github.com/sgl-project/sglang/pull/20874#pullrequestreview-3974074310)

## Inline Comment Hotspots

- `python/sglang/jit_kernel/nvfp4.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-03-18T16:49:14Z` `inline` by `mmangkad` `python/sglang/jit_kernel/nvfp4.py`:86; signals: cuda, fp4, kernel, nvfp4; excerpt: "Don't we need the a suffix though? get cuda arch list() in utils.py returns major.minor without a, but NVFP4 requires sm a targets" (https://github.com/sgl-project/sglang/pull/20874#discussion_r2954845039)
- `2026-03-18T16:44:55Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/nvfp4.py`:86; signals: fp4, kernel, nvfp4; excerpt: "Can we remove this context? JIT kernel already use current arch major.minor. We just need to check that whether major = 10 here." (https://github.com/sgl-project/sglang/pull/20874#discussion_r2954818547)
- `2026-03-19T02:36:55Z` `inline` by `DarkSharpness` `python/sglang/jit_kernel/nvfp4.py`:86; signals: fp4, kernel, nvfp4; excerpt: "ic. let's just keep it for now." (https://github.com/sgl-project/sglang/pull/20874#discussion_r2957439975)
- `2026-03-19T10:15:28Z` `inline` by `mmangkad` `python/sglang/jit_kernel/nvfp4.py`:86; signals: fp4, kernel, nvfp4; excerpt: "@DarkSharpness shall we land this now or do you still see any issues?" (https://github.com/sgl-project/sglang/pull/20874#discussion_r2959052597)
- `2026-03-18T17:03:06Z` `issue` by `xingsy97`; signals: general review; excerpt: "LGTM for mitigating the issue. It seems that the JIT multi-arch build logic was copied from AOT build logic, but JIT only targets the ..." (https://github.com/sgl-project/sglang/pull/20874#issuecomment-4084132525)
