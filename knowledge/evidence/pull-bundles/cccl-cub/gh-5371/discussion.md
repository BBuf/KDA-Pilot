# PR Discussion Digest

- Source PR: [NVIDIA/cccl#5371](https://github.com/NVIDIA/cccl/pull/5371)
- Source page: `sources/prs/cccl-cub/PR-5371.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-5371`
- Generated at: `2026-05-20T15:19:46.440744+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-25T23:46:55Z`
- Merged: `2025-08-18T17:27:48Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 30 (approved=3, changes_requested=4, commented=23)
- Inline review comments: 45
- Review threads observed: 20
- Resolved/outdated thread markers: resolved=18, outdated=18
- Human participants with discussion text: davebayer, fbusato, miscco, s-oboyle
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-26T17:02:51Z` `CHANGES_REQUESTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3058309171)
- `2025-07-28T09:43:38Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3061601602)
- `2025-08-04T08:12:46Z` `CHANGES_REQUESTED` by `miscco` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3083150810)
- `2025-08-04T18:41:15Z` `CHANGES_REQUESTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3085333987)
- `2025-08-06T18:19:48Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3093730403)
- `2025-08-06T18:25:22Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3093747668)
- `2025-08-06T18:40:15Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3093786341)
- `2025-08-06T18:45:38Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3093802549)
- `2025-08-06T18:47:38Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3093810938)
- `2025-08-06T18:54:03Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3093829419)
- `2025-08-06T19:02:39Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3093856392)
- `2025-08-06T22:06:13Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3094460256)
- `2025-08-07T16:10:44Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3097848424)
- `2025-08-07T16:16:02Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3097870557)
- `2025-08-13T15:33:13Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3116567336)
- `2025-08-13T16:00:13Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3116661250)
- `2025-08-13T16:06:13Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3116680872)
- `2025-08-13T16:20:04Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3116732097)
- `2025-08-15T05:47:37Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3122969547)
- `2025-08-15T09:40:22Z` `CHANGES_REQUESTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3123472562)
- `2025-08-15T13:39:15Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3123880046)
- `2025-08-15T14:00:57Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3123929356)
- `2025-08-15T16:28:32Z` `APPROVED` by `fbusato` - looks good. A minor comment on inf check (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3124474902)
- `2025-08-15T19:12:15Z` `COMMENTED` by `s-oboyle` (https://github.com/NVIDIA/cccl/pull/5371#pullrequestreview-3124885046)
- ... 6 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `libcudacxx/include/cuda/std/__complex/roots.h`: 45 inline comment(s)

## High-Signal Discussion

- `2025-08-06T18:19:48Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/roots.h`:55; signals: compile, cuda, fp4, hang; excerpt: "That change should be ok here, it might be the case in other functions that we want to delete eg the float128/fp4/6/8 versions at ..." (https://github.com/NVIDIA/cccl/pull/5371#discussion_r2257939715)
- `2025-08-06T18:47:38Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/roots.h`:48; signals: compile, cuda, hang; excerpt: "I think this errors for some combinations of compiler/toolkit/etc. If it is changed to a single function as Dave suggested above however if could ..." (https://github.com/NVIDIA/cccl/pull/5371#discussion_r2257997154)
- `2025-08-06T19:02:39Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/roots.h`:98; signals: accuracy, cuda, nan; excerpt: "If z is (x,+∞), the result is (+∞,+∞) even if x is NaN 2) std::sqrt(std::conj(z)) == std::conj(std::sqrt(z)) I'll leave the generic constants up to ..." (https://github.com/NVIDIA/cccl/pull/5371#discussion_r2258027267)
- `2025-08-15T19:12:15Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/roots.h`:159; signals: cuda, nan, perf; excerpt: "Doing it this way is possible, however the inf checks here are a little more complicated than inf checks in other functions. (Most of ..." (https://github.com/NVIDIA/cccl/pull/5371#discussion_r2279714478)
- `2025-08-06T18:45:38Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/roots.h`:53; signals: cuda, hang; excerpt: "We can change this, I was victim of a macro bug a some time ago that made my keep as little in it as ..." (https://github.com/NVIDIA/cccl/pull/5371#discussion_r2257991732)
- `2025-08-13T15:33:13Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/roots.h`:96; signals: cuda, hang; excerpt: "Ah, I did not know about the lack of constexpr for bit cast with older GCC's, thanks. Will make the change." (https://github.com/NVIDIA/cccl/pull/5371#discussion_r2273840916)
- `2025-08-15T19:20:30Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/roots.h`:85; signals: cuda, fp8; excerpt: "Ah, apologies. A lesson in reading feedback when very sleepy. So this would have fp explicit bit mask == 0 for say fp32/64, while ..." (https://github.com/NVIDIA/cccl/pull/5371#discussion_r2279727172)
- `2025-08-15T21:19:36Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/roots.h`:60; signals: cuda, nan; excerpt: "I meant to swing back round to this. Do these assertions cause program halt? There are no "bad values" that break these functions, every ..." (https://github.com/NVIDIA/cccl/pull/5371#discussion_r2279909627)
- `2025-08-06T18:25:22Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/roots.h`:55; signals: cuda; excerpt: "Re adding rqsrt into a cuda:: namespace, there are a lot of other cuda only functions you may want to do at the same ..." (https://github.com/NVIDIA/cccl/pull/5371#discussion_r2257952724)
- `2025-08-06T18:40:15Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/roots.h`:96; signals: cuda; excerpt: "Does fp from storage make sure the sizes of the input and output types are the same? Having to understand the fp storage system ..." (https://github.com/NVIDIA/cccl/pull/5371#discussion_r2257980962)
- `2025-08-06T18:54:03Z` `inline` by `s-oboyle` `libcudacxx/include/cuda/std/__complex/roots.h`:60; signals: cuda; excerpt: "For CUDA that usually belongs to the higher level calling functions, as there is no exceptions or flags in the CUDA math functions. If ..." (https://github.com/NVIDIA/cccl/pull/5371#discussion_r2258009796)
- `2025-08-07T16:10:44Z` `inline` by `davebayer` `libcudacxx/include/cuda/std/__complex/roots.h`:55; signals: cuda; excerpt: "I think it would be better to keep this internal version for now and we can introduce + use the cuda::rsqrt function later" (https://github.com/NVIDIA/cccl/pull/5371#discussion_r2260795437)
