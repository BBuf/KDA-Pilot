# PR Discussion Digest

- Source PR: [NVIDIA/cccl#3588](https://github.com/NVIDIA/cccl/pull/3588)
- Source page: `sources/prs/cccl-cub/PR-3588.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-3588`
- Generated at: `2026-05-20T15:19:34.404385+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-29T22:06:49Z`
- Merged: `2025-02-04T18:39:56Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 15 (approved=5, commented=10)
- Inline review comments: 13
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=7
- Human participants with discussion text: bernhardmgruber, davebayer, fbusato, miscco
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-01-29T22:18:01Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2582495184)
- `2025-01-29T22:32:52Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2582515889)
- `2025-01-30T10:30:56Z` `COMMENTED` by `miscco` - Minor nits (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2583506815)
- `2025-01-30T22:09:10Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2585160151)
- `2025-01-30T22:20:09Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2585175169)
- `2025-01-31T00:40:26Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2585412417)
- `2025-01-31T00:45:00Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2585415312)
- `2025-01-31T06:34:48Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2585773523)
- `2025-01-31T09:37:33Z` `APPROVED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2586117028)
- `2025-01-31T11:50:26Z` `COMMENTED` by `davebayer` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2586390711)
- `2025-01-31T17:46:59Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2587409822)
- `2025-01-31T18:41:43Z` `COMMENTED` by `fbusato` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2587535521)
- `2025-02-03T07:19:56Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2589087716)
- `2025-02-03T19:28:04Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2590819704)
- `2025-02-04T16:52:13Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2593481889)

## Inline Comment Hotspots

- `libcudacxx/include/cuda/std/__cccl/extended_data_types.h`: 6 inline comment(s)
- `cub/cub/util_type.cuh`: 4 inline comment(s)
- `c2h/include/c2h/generators.h`: 2 inline comment(s)
- `cmake/header_test.cu.in`: 1 inline comment(s)

## High-Signal Discussion

- `2025-01-30T22:09:10Z` `inline` by `fbusato` `c2h/include/c2h/generators.h`:56; signals: bf16, cuda, fp8; excerpt: "realized that CUDA FP8 TYPES EXIST , CUDA FP16 TYPES EXIST , CUDA BF16 TYPES EXIST is many places (wrongly)" (https://github.com/NVIDIA/cccl/pull/3588#discussion_r1936360276)
- `2025-01-29T22:32:51Z` `inline` by `fbusato` `libcudacxx/include/cuda/std/__cccl/extended_data_types.h`:50; signals: bf16, cuda; excerpt: "good point. On the other hand, BF16 can be disabled with CUB . Let me make all macros look more uniform" (https://github.com/NVIDIA/cccl/pull/3588#discussion_r1934747365)
- `2025-01-29T22:17:32Z` `inline` by `bernhardmgruber` `libcudacxx/include/cuda/std/__cccl/extended_data_types.h`:50; signals: cuda; excerpt: "Suggestion: the condition could be further simplified. Also why do we need CCCL DISABLE NVFP16 SUPPORT, fi we already check for CCCL DISABLE FP16 ..." (https://github.com/NVIDIA/cccl/pull/3588#discussion_r1934733880)
- `2025-01-31T11:50:26Z` `inline` by `davebayer` `libcudacxx/include/cuda/std/__cccl/extended_data_types.h`:56; signals: cuda; excerpt: "I think we should use the same approach as for the builtins: In my opinion, this approach is clearer and removes the repetitive else ..." (https://github.com/NVIDIA/cccl/pull/3588#discussion_r1937109776)
- `2025-01-31T17:46:59Z` `inline` by `fbusato` `libcudacxx/include/cuda/std/__cccl/extended_data_types.h`:56; signals: cuda; excerpt: "I don't have a strong opinion on that. define/ undef pattern is less common but I agree that it is less verbose" (https://github.com/NVIDIA/cccl/pull/3588#discussion_r1937682124)
- `2025-01-30T10:28:51Z` `inline` by `miscco` `c2h/include/c2h/generators.h`:56; signals: fp8; excerpt: "That should probably also use CCCL HAS FP8()" (https://github.com/NVIDIA/cccl/pull/3588#discussion_r1935371005)
- `2025-01-31T18:41:43Z` `inline` by `fbusato` `libcudacxx/include/cuda/std/__cccl/extended_data_types.h`:56; signals: cuda; excerpt: "done. The condition for CCCL HAS FLOAT128 looks pretty hard to read" (https://github.com/NVIDIA/cccl/pull/3588#discussion_r1937763198)
- `2025-01-30T10:30:56Z` `review` `COMMENTED` by `miscco`; signals: general review; excerpt: "Minor nits" (https://github.com/NVIDIA/cccl/pull/3588#pullrequestreview-2583506815)
- `2025-01-30T10:30:01Z` `inline` by `miscco` `cub/cub/util_type.cuh`:933; signals: general review; excerpt: "missing the endif above" (https://github.com/NVIDIA/cccl/pull/3588#discussion_r1935372663)
- `2025-01-30T22:20:08Z` `inline` by `fbusato` `cub/cub/util_type.cuh`:933; signals: general review; excerpt: "sorry, I don't understand where is the problem here." (https://github.com/NVIDIA/cccl/pull/3588#discussion_r1936369603)
- `2025-01-31T00:40:26Z` `inline` by `bernhardmgruber` `cub/cub/util_type.cuh`:933; signals: general review; excerpt: "Your preceding edit misses a corresponding edit of the endif comment on line 68." (https://github.com/NVIDIA/cccl/pull/3588#discussion_r1936504732)
- `2025-02-03T07:17:35Z` `inline` by `miscco` `cmake/header_test.cu.in`:26; signals: general review; excerpt: "This seems like the foratting has been broken hard here" (https://github.com/NVIDIA/cccl/pull/3588#discussion_r1938891814)
