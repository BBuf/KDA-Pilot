# PR Discussion Digest

- Source PR: [NVIDIA/cutlass#1350](https://github.com/NVIDIA/cutlass/pull/1350)
- Source page: `sources/prs/cutlass/PR-1350.md`
- Evidence bundle: `evidence/pull-bundles/cutlass/gh-1350`
- Generated at: `2026-05-20T15:21:10.038694+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-02-16T18:55:31Z`
- Merged: `2024-08-16T04:59:29Z`

## Discussion Counts

- Issue comments: 22
- Review submissions: 8 (approved=3, commented=5)
- Inline review comments: 6
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: alexsamardzic, hwu36, manishucsd
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2024-07-11T18:27:06Z` `COMMENTED` by `manishucsd` - Let us debug the failing unit test a litter deeper. Some notes on where to start on debugging ... (https://github.com/NVIDIA/cutlass/pull/1350#pullrequestreview-2172704851)
- `2024-07-11T19:02:07Z` `COMMENTED` by `alexsamardzic` (https://github.com/NVIDIA/cutlass/pull/1350#pullrequestreview-2172793817)
- `2024-07-11T21:18:31Z` `APPROVED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/1350#pullrequestreview-2173065546)
- `2024-07-11T21:18:52Z` `APPROVED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/1350#pullrequestreview-2173066462)
- `2024-07-11T21:50:41Z` `COMMENTED` by `alexsamardzic` (https://github.com/NVIDIA/cutlass/pull/1350#pullrequestreview-2173128209)
- `2024-07-11T22:28:09Z` `COMMENTED` by `manishucsd` (https://github.com/NVIDIA/cutlass/pull/1350#pullrequestreview-2173190565)
- `2024-07-12T14:52:55Z` `COMMENTED` by `alexsamardzic` (https://github.com/NVIDIA/cutlass/pull/1350#pullrequestreview-2175110115)
- `2024-08-16T04:54:51Z` `APPROVED` by `hwu36` (https://github.com/NVIDIA/cutlass/pull/1350#pullrequestreview-2241811093)

## Inline Comment Hotspots

- `test/unit/gemm/device/CMakeLists.txt`: 6 inline comment(s)

## High-Signal Discussion

- `2024-07-11T18:26:02Z` `inline` by `manishucsd` `test/unit/gemm/device/CMakeLists.txt`:267; signals: bf16, failing, gemm, hang, kernel, tile; excerpt: "So gemm universal s8t bf16n bf16t mixed input tensor op f32 sm80 Passes but gemm universal u8t bf16n bf16t mixed input tensor op f32 ..." (https://github.com/NVIDIA/cutlass/pull/1350#discussion_r1674483382)
- `2024-02-21T20:15:15Z` `issue` by `alexsamardzic`; signals: compile, cutlass, gemm, kernel, tile; excerpt: "Thanks for the clarification. I've updated gemm fp mixed input.cu in my PR. W.r.t. verification - is there an "official" way to do it? ..." (https://github.com/NVIDIA/cutlass/pull/1350#issuecomment-1957829884)
- `2024-07-11T18:27:06Z` `review` `COMMENTED` by `manishucsd`; signals: bf16, failing, gemm; excerpt: "Let us debug the failing unit test a litter deeper. Some notes on where to start on debugging gemm universal u8t bf16n bf16t mixed ..." (https://github.com/NVIDIA/cutlass/pull/1350#pullrequestreview-2172704851)
- `2024-02-20T12:56:30Z` `issue` by `alexsamardzic`; signals: hang, memory, shared memory, tile; excerpt: "By symmetry, I meant on math instructions list within given generator methods: I was thinking that, if GenerateSM80 SparseTensorOp 16832 method has for example ..." (https://github.com/NVIDIA/cutlass/pull/1350#issuecomment-1954160968)
- `2024-03-07T22:05:29Z` `issue` by `alexsamardzic`; signals: cutlass, gemm, hang, kernel; excerpt: "Thanks for the clarifications. PR is updated with the changes suggested: Added number of tests, so that it should be all consistent now between ..." (https://github.com/NVIDIA/cutlass/pull/1350#issuecomment-1984581115)
- `2024-07-11T11:47:32Z` `issue` by `alexsamardzic`; signals: compile, cutlass, gemm, hang; excerpt: "@hwu36: Thanks for the test fix! The problem with the configurations added in your commit is that they won't work - one could try ..." (https://github.com/NVIDIA/cutlass/pull/1350#issuecomment-2222720157)
- `2024-07-11T22:28:01Z` `inline` by `manishucsd` `test/unit/gemm/device/CMakeLists.txt`:267; signals: bf16, gemm, hang; excerpt: "So this an initialization issue with u8 and bf16 mixed-input. Can you tailor the initialization inside the testbed test::gemm::device::TestAllGemmUniversal when initializingbf16 and other operand ..." (https://github.com/NVIDIA/cutlass/pull/1350#discussion_r1674783999)
- `2024-03-05T03:37:54Z` `issue` by `manishucsd`; signals: compile, cutlass, kernel; excerpt: "1. For your mixed-input case, add a device-level unit test. Track similar unit test from [here]( 2. You should also test if the profiler ..." (https://github.com/NVIDIA/cutlass/pull/1350#issuecomment-1977910775)
- `2024-07-11T12:27:41Z` `issue` by `hwu36`; signals: alignment, epilogue, hang; excerpt: "I did not change unit test. The reason that profiler cannot do 128x32 is due to epilogue alignment. I fixed that. So 128x32 is ..." (https://github.com/NVIDIA/cutlass/pull/1350#issuecomment-2222805798)
- `2024-07-11T12:52:50Z` `issue` by `alexsamardzic`; signals: alignment, epilogue, hang; excerpt: "I did not change unit test. I meant on fixing the test name :-) The reason that profiler cannot do 128x32 is due to ..." (https://github.com/NVIDIA/cutlass/pull/1350#issuecomment-2222861996)
- `2024-07-11T18:20:27Z` `issue` by `manishucsd`; signals: cutlass, gemm, hang; excerpt: "Thank you for the change. Overall looks good. Can do the following? 1. CUTLASS Profiler Output for All the mixed input GEMMs Dump the ..." (https://github.com/NVIDIA/cutlass/pull/1350#issuecomment-2223601983)
- `2024-07-11T19:02:07Z` `inline` by `alexsamardzic` `test/unit/gemm/device/CMakeLists.txt`:267; signals: bf16, gemm; excerpt: "Here is the test file (please rename to .cu): [gemm universal u8t bf16n bf16t mixed input tensor op f32 sm80.txt]( And here is the ..." (https://github.com/NVIDIA/cutlass/pull/1350#discussion_r1674534241)
