# PR Discussion Digest

- Source PR: [NVIDIA/cutlass#3091](https://github.com/NVIDIA/cutlass/pull/3091)
- Source page: `sources/prs/cutlass/PR-3091.md`
- Evidence bundle: `evidence/pull-bundles/cutlass/gh-3091`
- Generated at: `2026-05-20T15:21:25.667260+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-06T22:30:09Z`
- Merged: `2026-03-18T04:40:16Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 12
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=3
- Human participants with discussion text: Johnsonms, depaulmillz, hwu36
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-12T23:06:01Z` `COMMENTED` by `depaulmillz` (https://github.com/NVIDIA/cutlass/pull/3091#pullrequestreview-3940351075)
- `2026-03-13T20:27:52Z` `COMMENTED` by `Johnsonms` (https://github.com/NVIDIA/cutlass/pull/3091#pullrequestreview-3946801202)
- `2026-03-13T20:28:14Z` `COMMENTED` by `Johnsonms` (https://github.com/NVIDIA/cutlass/pull/3091#pullrequestreview-3946803214)
- `2026-03-13T20:28:29Z` `COMMENTED` by `Johnsonms` (https://github.com/NVIDIA/cutlass/pull/3091#pullrequestreview-3946804630)
- `2026-03-13T20:28:35Z` `COMMENTED` by `Johnsonms` (https://github.com/NVIDIA/cutlass/pull/3091#pullrequestreview-3946805284)
- `2026-03-13T20:28:37Z` `COMMENTED` by `Johnsonms` (https://github.com/NVIDIA/cutlass/pull/3091#pullrequestreview-3946805531)
- `2026-03-13T20:28:40Z` `COMMENTED` by `Johnsonms` (https://github.com/NVIDIA/cutlass/pull/3091#pullrequestreview-3946805798)
- `2026-03-18T04:38:15Z` `APPROVED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/3091#pullrequestreview-3964987583)

## Inline Comment Hotspots

- `examples/python/CuTeDSL/hopper/grouped_gemm.py`: 6 inline comment(s)
- `pyproject.toml`: 2 inline comment(s)
- `examples/python/CuTeDSL/hopper/verify_tensormap_modes.sh`: 2 inline comment(s)
- `test/examples/CuTeDSL/hopper/test_grouped_gemm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-13T20:28:34Z` `inline` by `Johnsonms` `examples/python/CuTeDSL/hopper/grouped_gemm.py`:1094; signals: cuda, cute, gemm, hopper, kernel; excerpt: "No standalone reproducer yet — found it running this kernel on sm 90a (CUDA ERROR ILLEGAL INSTRUCTION / 715). Can add one as a ..." (https://github.com/NVIDIA/cutlass/pull/3091#discussion_r2933619512)
- `2026-03-13T20:28:40Z` `inline` by `Johnsonms` `examples/python/CuTeDSL/hopper/grouped_gemm.py`:2149; signals: cute, cutlass, gemm, hopper, ptx; excerpt: "Good catch! CUTE DSL KEEP PTX is the correct variable — the DSL prefix is "CUTE DSL" (set in cutlass dsl/cutlass.py), and EnvironmentVarManager constructs ..." (https://github.com/NVIDIA/cutlass/pull/3091#discussion_r2933620102)
- `2026-03-12T23:01:45Z` `inline` by `depaulmillz` `examples/python/CuTeDSL/hopper/grouped_gemm.py`:2295; signals: benchmark, cute, gemm, hopper; excerpt: "I think we can remove the bench grouped gemm.py before merging because we have the benchmark code in this file." (https://github.com/NVIDIA/cutlass/pull/3091#discussion_r2927897652)
- `2026-03-13T20:28:37Z` `inline` by `Johnsonms` `examples/python/CuTeDSL/hopper/grouped_gemm.py`:2295; signals: benchmark, cute, gemm, hopper; excerpt: "Agreed, removed bench grouped gemm.py to keep things simple. We can add back a more structured benchmark as a follow-up." (https://github.com/NVIDIA/cutlass/pull/3091#discussion_r2933619804)
- `2026-03-12T23:00:17Z` `inline` by `depaulmillz` `examples/python/CuTeDSL/hopper/grouped_gemm.py`:2149; signals: cute, gemm, hopper, ptx; excerpt: "Is CUTE DSL KEEP PTX not working?" (https://github.com/NVIDIA/cutlass/pull/3091#discussion_r2927891129)
- `2026-03-12T23:03:14Z` `inline` by `depaulmillz` `examples/python/CuTeDSL/hopper/grouped_gemm.py`:1094; signals: cute, gemm, hopper; excerpt: "Is there a minimal reproducer for this? Its fine if not" (https://github.com/NVIDIA/cutlass/pull/3091#discussion_r2927903882)
- `2026-03-12T23:05:38Z` `inline` by `depaulmillz` `test/examples/CuTeDSL/hopper/test_grouped_gemm.py`:1; signals: cute, gemm, hopper; excerpt: "Could you move this to test/examples/CuTeDSL similar to the sm 100a tests? Thanks" (https://github.com/NVIDIA/cutlass/pull/3091#discussion_r2927913694)
- `2026-03-13T20:27:52Z` `inline` by `Johnsonms` `test/examples/CuTeDSL/hopper/test_grouped_gemm.py`:1; signals: cute, gemm, hopper; excerpt: "Moved. Thanks" (https://github.com/NVIDIA/cutlass/pull/3091#discussion_r2933615954)
- `2026-03-12T23:04:22Z` `inline` by `depaulmillz` `examples/python/CuTeDSL/hopper/verify_tensormap_modes.sh`:1; signals: cute, hopper; excerpt: "Could you also remove this before merging? Thanks" (https://github.com/NVIDIA/cutlass/pull/3091#discussion_r2927908541)
- `2026-03-13T20:28:13Z` `inline` by `Johnsonms` `examples/python/CuTeDSL/hopper/verify_tensormap_modes.sh`:1; signals: cute, hopper; excerpt: "Definitely sure. Thanks @depaulmillz" (https://github.com/NVIDIA/cutlass/pull/3091#discussion_r2933617733)
- `2026-03-12T23:03:58Z` `inline` by `depaulmillz` `pyproject.toml`:30; signals: general review; excerpt: "Could you remove this before merging? Thanks" (https://github.com/NVIDIA/cutlass/pull/3091#discussion_r2927906769)
- `2026-03-13T20:28:29Z` `inline` by `Johnsonms` `pyproject.toml`:30; signals: general review; excerpt: "Sure, done. Thanks" (https://github.com/NVIDIA/cutlass/pull/3091#discussion_r2933619035)
