# PR Discussion Digest

- Source PR: [vllm-project/vllm#24673](https://github.com/vllm-project/vllm/pull/24673)
- Source page: `sources/prs/vllm/PR-24673.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-24673`
- Generated at: `2026-05-20T15:37:49.696958+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-11T15:54:14Z`
- Merged: `2025-10-01T17:50:54Z`

## Discussion Counts

- Issue comments: 36
- Review submissions: 23 (approved=6, changes_requested=2, commented=15)
- Inline review comments: 31
- Review threads observed: 17
- Resolved/outdated thread markers: resolved=15, outdated=14
- Human participants with discussion text: Aidyn-A, DrStone1971, Jakub227, ProExpertProg, eugeneswalker, hmellor, huydhn, jasl, johnnynunez, mgoin, pavanimajety, simon-mo, youkaichao
- Automation comments/reviews omitted from high-signal summary: 13
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-09-11T15:56:25Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the CMake configuration to support the new NVIDIA Blackwell architecture family, aligning ... (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3212513120)
- `2025-09-13T13:43:52Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3220784018)
- `2025-09-13T18:21:37Z` `COMMENTED` by `DrStone1971` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3221222748)
- `2025-09-13T18:23:48Z` `COMMENTED` by `johnnynunez` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3221225212)
- `2025-09-13T18:29:35Z` `COMMENTED` by `DrStone1971` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3221231108)
- `2025-09-13T18:36:04Z` `COMMENTED` by `johnnynunez` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3221237099)
- `2025-09-13T20:57:49Z` `COMMENTED` by `johnnynunez` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3221385678)
- `2025-09-15T14:26:22Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3224931595)
- `2025-09-15T15:19:15Z` `COMMENTED` by `johnnynunez` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3225177542)
- `2025-09-15T20:19:59Z` `COMMENTED` by `johnnynunez` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3226150834)
- `2025-09-15T20:42:28Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3226270438)
- `2025-09-18T07:23:59Z` `CHANGES_REQUESTED` by `Aidyn-A` - I have left some of the comments. I would like you to test the build, make sure it ... (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3237481720)
- `2025-09-18T15:33:22Z` `COMMENTED` by `Aidyn-A` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3240525353)
- `2025-09-19T16:41:15Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3245832528)
- `2025-09-25T15:26:07Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3268333681)
- `2025-09-25T17:13:24Z` `APPROVED` by `Aidyn-A` - I am happy, as long as the CI is green. (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3268745045)
- `2025-09-25T17:31:53Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3268773036)
- `2025-09-25T19:50:10Z` `CHANGES_REQUESTED` by `mgoin` - We are trying to cut a release today, so will land this after the cut to be conservative (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3269255086)
- `2025-09-25T22:25:49Z` `APPROVED` by `huydhn` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3269621226)
- `2025-09-28T21:29:06Z` `APPROVED` by `Jakub227` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3277409815)
- `2025-10-01T14:57:35Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3289671234)

## Inline Comment Hotspots

- `CMakeLists.txt`: 31 inline comment(s)

## High-Signal Discussion

- `2025-09-19T17:17:10Z` `issue` by `DrStone1971`; signals: cache, compile, cuda, cutlass, fp4, fp8, mla, moe; excerpt: "when compile with latest version have this problem: [28/419] Building CUDA object CMakeFiles/ C.dir/csrc/quantization/cutlass w8a8/scaled mm entry.cu.o FAILED: [code=2] CMakeFiles/ C.dir/csrc/quantization/cutlass w8a8/scaled mm entry.cu.o ..." (https://github.com/vllm-project/vllm/pull/24673#issuecomment-3313041835)
- `2025-09-19T17:27:59Z` `issue` by `johnnynunez`; signals: attention, cache, compile, cuda, cute, cutlass, fp4, fp8; excerpt: "when compile with latest version have this problem: [28/419] Building CUDA object CMakeFiles/ C.dir/csrc/quantization/cutlass w8a8/scaled mm entry.cu.o FAILED: [code=2] CMakeFiles/ C.dir/csrc/quantization/cutlass w8a8/scaled mm entry.cu.o ..." (https://github.com/vllm-project/vllm/pull/24673#issuecomment-3313094610)
- `2025-09-28T19:44:09Z` `issue` by `DrStone1971`; signals: block, cache, compile, cuda, cutlass, fp4, fp8, kernel; excerpt: "Sorry for being absent from this activity, various issues. I built on my machine and got this error. I remember for all i have: ..." (https://github.com/vllm-project/vllm/pull/24673#issuecomment-3344190557)
- `2025-09-19T21:07:53Z` `issue` by `DrStone1971`; signals: attention, blackwell, compile, cutlass, kernel, sm100, sm120; excerpt: "1. Cutlass 4.2.0 in this moment i have sudo apt list grep cutlass libcutlass-dev/noble,noble,now 3.1.0+ds-2 all and into Nvidia Cutlass there is "Note: The ..." (https://github.com/vllm-project/vllm/pull/24673#issuecomment-3313807247)
- `2025-09-18T07:23:59Z` `review` `CHANGES_REQUESTED` by `Aidyn-A`; signals: cuda, cutlass, failing, kernel; excerpt: "I have left some of the comments. I would like you to test the build, make sure it is 100% successful and double test ..." (https://github.com/vllm-project/vllm/pull/24673#pullrequestreview-3237481720)
- `2025-09-29T07:35:55Z` `issue` by `DrStone1971`; signals: cuda, cutlass, moe, sm100, sm120; excerpt: "Does cutlass moe mm sm100 work on SM120? is strange this code: if defined CUDA VERSION if (cuda device capability = 100) { return ..." (https://github.com/vllm-project/vllm/pull/24673#issuecomment-3345460076)
- `2025-09-29T07:50:27Z` `issue` by `jasl`; signals: cutlass, kernel, moe, sm100, sm120; excerpt: "@DrStone71 My testing machine is an x86 with RTX Pro 6000 (SM120) I'm not sure this kernel labeled sm100 will work on SM120. Looking ..." (https://github.com/vllm-project/vllm/pull/24673#issuecomment-3345512696)
- `2025-09-18T06:44:30Z` `inline` by `Aidyn-A` `CMakeLists.txt`:481; signals: blackwell, cutlass, kernel, sm100; excerpt: "From the comment above I see The cutlass scaled mm kernels for Blackwell SM100 (c3x, i.e. CUTLASS 3.x) I do not think 12.0f is ..." (https://github.com/vllm-project/vllm/pull/24673#discussion_r2357695458)
- `2025-09-24T11:48:46Z` `issue` by `johnnynunez`; signals: attention, cuda, cutlass, flash attention; excerpt: "@ProExpertProg @pavanimajety @Aidyn-A good news! With this PR from here + flash attention PR: i'm available to build with CUDA 13 + cutlass v4.2.1" (https://github.com/vllm-project/vllm/pull/24673#issuecomment-3328026872)
- `2025-09-18T06:50:50Z` `inline` by `Aidyn-A` `CMakeLists.txt`:591; signals: cuda, hang, kernel; excerpt: "Have you tested these kernels on 11.0f and 12.0f? Why not add 10.1a and 12.0a to the CUDA < 13.0? Same comment for the ..." (https://github.com/vllm-project/vllm/pull/24673#discussion_r2357714549)
- `2025-09-28T21:41:59Z` `issue` by `jasl`; signals: cutlass, moe, sm100, sm120; excerpt: "Does cutlass moe mm sm100 work on SM120?" (https://github.com/vllm-project/vllm/pull/24673#issuecomment-3344287670)
- `2025-09-13T18:21:37Z` `inline` by `DrStone1971` `CMakeLists.txt`:89; signals: cuda, hang; excerpt: "Maybe @ProExpertProg is right. Many people are still using BW on 12.8. We should only force the change when CUDA 13 is being used." (https://github.com/vllm-project/vllm/pull/24673#discussion_r2346884347)
