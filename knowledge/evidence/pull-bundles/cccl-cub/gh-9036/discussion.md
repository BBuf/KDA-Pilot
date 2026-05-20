# PR Discussion Digest

- Source PR: [NVIDIA/cccl#9036](https://github.com/NVIDIA/cccl/pull/9036)
- Source page: `sources/prs/cccl-cub/PR-9036.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-9036`
- Generated at: `2026-05-20T15:21:07.482323+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-15T20:11:38Z`
- Merged: `2026-05-18T23:16:44Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 20 (approved=1, changes_requested=1, commented=18)
- Inline review comments: 26
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=8, outdated=4
- Human participants with discussion text: coderabbitai, fbusato, miscco, oleksandr-pavlyk, s-oboyle
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-15T20:15:02Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (1) libcudacxx/include/cuda/std/ complex/hyperbolic functions.h (1) 334-334: ⚡ Quick win suggestion: Missing noexcept specifier on the ... (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4301110457)
- `2026-05-15T21:04:14Z` `COMMENTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4301371493)
- `2026-05-15T21:23:34Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4301489950)
- `2026-05-15T21:23:54Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4301491577)
- `2026-05-15T21:24:48Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4301494888)
- `2026-05-15T21:47:39Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4301581777)
- `2026-05-15T23:45:30Z` `CHANGES_REQUESTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4301996325)
- `2026-05-18T11:46:46Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4309839340)
- `2026-05-18T11:47:27Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4309843685)
- `2026-05-18T12:16:04Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4310025661)
- `2026-05-18T13:43:12Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4310681824)
- `2026-05-18T13:43:52Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4310686615)
- `2026-05-18T13:43:58Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4310687364)
- `2026-05-18T13:47:56Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4310717342)
- `2026-05-18T14:26:31Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4311027445)
- `2026-05-18T18:20:02Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4312653577)
- `2026-05-18T18:21:09Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4312662229)
- `2026-05-18T18:21:24Z` `APPROVED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4312663883)
- `2026-05-18T18:27:05Z` `COMMENTED` by `oleksandr-pavlyk` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4312699842)
- `2026-05-18T23:13:14Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4314591415)

## Inline Comment Hotspots

- `libcudacxx/include/cuda/std/__complex/hyperbolic_functions.h`: 26 inline comment(s)

## High-Signal Discussion

- `2026-05-15T20:15:02Z` `review` `COMMENTED` by `coderabbitai`; signals: cuda, hang; excerpt: "🧹 Nitpick comments (1) libcudacxx/include/cuda/std/ complex/hyperbolic functions.h (1) 334-334: ⚡ Quick win suggestion: Missing noexcept specifier on the main tanh template. The sinh and ..." (https://github.com/NVIDIA/cccl/pull/9036#pullrequestreview-4301110457)
- `2026-05-18T18:20:02Z` `inline` by `fbusato` `libcudacxx/include/cuda/std/__complex/hyperbolic_functions.h`:336; signals: cuda, hang, tile; excerpt: "yes, the change is already in the main branch. 80% of libcu++ functionalities support Tile" (https://github.com/NVIDIA/cccl/pull/9036#discussion_r3261096418)
- `2026-05-15T20:14:59Z` `issue` by `coderabbitai`; signals: cuda, hang, nan; excerpt: "[ with a numerically-stable implementation that range-reduces large real parts, computes sin/cos of the imaginary part, evaluates via expm1+FMA with a composed denominator reciprocal, ..." (https://github.com/NVIDIA/cccl/pull/9036#issuecomment-4463205790)
- `2026-05-18T18:27:05Z` `inline` by `oleksandr-pavlyk` `libcudacxx/include/cuda/std/__complex/hyperbolic_functions.h`:344; signals: cuda, nan; excerpt: "If imag x is NaN, the mapping to signed 0 depends on the value of sign-bit of NaN. This may be withing the spec, ..." (https://github.com/NVIDIA/cccl/pull/9036#discussion_r3261133094)
- `2026-05-15T23:35:24Z` `inline` by `fbusato` `libcudacxx/include/cuda/std/__complex/hyperbolic_functions.h`:336; signals: cuda, tile; excerpt: "very likely that we need to move it to CCCL HOST DEVICE API. CCCL API also means supporting Tile" (https://github.com/NVIDIA/cccl/pull/9036#discussion_r3251511722)
- `2026-05-18T13:47:56Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/hyperbolic_functions.h`:336; signals: cuda, hang; excerpt: "I'd rather update all these functions at the same time, I don't think main has this change yet?" (https://github.com/NVIDIA/cccl/pull/9036#discussion_r3259398287)
- `2026-05-15T21:03:47Z` `inline` by `miscco` `libcudacxx/include/cuda/std/__complex/hyperbolic_functions.h`:392; signals: cuda; excerpt: "Question: Should those rather be else if or is clamp huge values bound larger than large interval bound" (https://github.com/NVIDIA/cccl/pull/9036#discussion_r3250990463)
- `2026-05-15T21:23:34Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/hyperbolic_functions.h`:392; signals: cuda; excerpt: "It's a little hard to see in the templated code, but these all do (necessarily) cascade together (so very large values will hit all ..." (https://github.com/NVIDIA/cccl/pull/9036#discussion_r3251081617)
- `2026-05-15T23:39:52Z` `inline` by `fbusato` `libcudacxx/include/cuda/std/__complex/hyperbolic_functions.h`:357; signals: cuda; excerpt: "do we need static cast here? it should not be a problem at least for the first branch. The second one depends if this ..." (https://github.com/NVIDIA/cccl/pull/9036#discussion_r3251522690)
- `2026-05-18T11:46:45Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/hyperbolic_functions.h`:344; signals: cuda; excerpt: "You are quite correct, something has gone awry translating my usual non-template code into this template code. It needs a little more baking it ..." (https://github.com/NVIDIA/cccl/pull/9036#discussion_r3258616634)
- `2026-05-18T11:47:27Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/hyperbolic_functions.h`:357; signals: cuda; excerpt: "This is true, and happy to remove, it was more just for keeping in line with the other functions. But I do like removing ..." (https://github.com/NVIDIA/cccl/pull/9036#discussion_r3258620792)
- `2026-05-18T12:16:03Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/hyperbolic_functions.h`:344; signals: cuda; excerpt: "Ah, so the copysign does matter, because we overwrite the answer at the end with this value sometimes: Without this we get a incorrectly ..." (https://github.com/NVIDIA/cccl/pull/9036#discussion_r3258789162)
