# PR Discussion Digest

- Source PR: [vllm-project/vllm#14568](https://github.com/vllm-project/vllm/pull/14568)
- Source page: `sources/prs/vllm/PR-14568.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14568`
- Generated at: `2026-05-20T15:34:28.833132+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-10T14:26:17Z`
- Merged: `2025-05-02T18:31:55Z`

## Discussion Counts

- Issue comments: 27
- Review submissions: 30 (approved=2, commented=28)
- Inline review comments: 27
- Review threads observed: 21
- Resolved/outdated thread markers: resolved=14, outdated=19
- Human participants with discussion text: CalebDu, bnellnm, gzy19990617, mergify, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-17T17:47:22Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776524565)
- `2025-04-17T17:49:41Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776529129)
- `2025-04-17T17:55:13Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776540037)
- `2025-04-17T18:01:29Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776552276)
- `2025-04-17T18:03:17Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776555711)
- `2025-04-17T18:05:20Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776559669)
- `2025-04-17T18:07:45Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776564604)
- `2025-04-17T18:08:51Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776566689)
- `2025-04-17T18:13:23Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776575872)
- `2025-04-17T18:14:57Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776578821)
- `2025-04-17T18:22:33Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776593357)
- `2025-04-17T18:41:58Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776630306)
- `2025-04-17T18:54:24Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776653993)
- `2025-04-17T18:54:30Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776654176)
- `2025-04-17T18:55:44Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776656521)
- `2025-04-17T18:59:47Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776664011)
- `2025-04-17T19:00:11Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776664744)
- `2025-04-17T19:05:34Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2776674647)
- `2025-04-18T10:48:43Z` `COMMENTED` by `CalebDu` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2778317519)
- `2025-04-18T11:14:43Z` `COMMENTED` by `CalebDu` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2778349105)
- `2025-04-18T12:16:28Z` `COMMENTED` by `CalebDu` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2778424768)
- `2025-04-18T12:20:56Z` `COMMENTED` by `CalebDu` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2778431117)
- `2025-04-18T17:18:33Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2779048027)
- `2025-04-28T16:57:16Z` `COMMENTED` by `bnellnm` - There seems to be a few lint errors that need to be fixed but looks good otherwise! (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2800030815)
- ... 6 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `CMakeLists.txt`: 8 inline comment(s)
- `csrc/moe/permute_unpermute_kernels/moe_permute_unpermute_kernel.h`: 7 inline comment(s)
- `csrc/moe/moe_permute_unpermute_op.cu`: 4 inline comment(s)
- `tests/kernels/test_moe_permute_unpermute.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/moe_permute_unpermute.py`: 2 inline comment(s)
- `csrc/moe/torch_bindings.cpp`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 1 inline comment(s)
- `csrc/moe/permute_unpermute_kernels/moe_permute_unpermute_kernel.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-27T05:02:12Z` `issue` by `CalebDu`; signals: aligned, bf16, block, correctness, deepgemm, fp8, gemm, moe; excerpt: "@CalebDu , thanks for adding the blocking support! I've been working on integrating the new version with DeepGemm but I'm running into problems with ..." (https://github.com/vllm-project/vllm/pull/14568#issuecomment-2756686361)
- `2025-03-27T13:14:09Z` `issue` by `bnellnm`; signals: aligned, bf16, block, correctness, deepgemm, fp8, gemm, moe; excerpt: "@CalebDu , thanks for adding the blocking support! I've been working on integrating the new version with DeepGemm but I'm running into problems with ..." (https://github.com/vllm-project/vllm/pull/14568#issuecomment-2758003179)
- `2025-03-27T13:51:13Z` `issue` by `CalebDu`; signals: block, deepgemm, gemm, kernel, memory, moe; excerpt: "The -1 in the original DeepGemm documentation was a bug. They never actually supported it (I ran into this while doing the initial integration). ..." (https://github.com/vllm-project/vllm/pull/14568#issuecomment-2758136194)
- `2025-03-27T14:59:57Z` `issue` by `bnellnm`; signals: block, deepgemm, gemm, kernel, memory, moe; excerpt: "The -1 in the original DeepGemm documentation was a bug. They never actually supported it (I ran into this while doing the initial integration). ..." (https://github.com/vllm-project/vllm/pull/14568#issuecomment-2758384533)
- `2025-04-18T02:27:20Z` `issue` by `CalebDu`; signals: aligned, bf16, cuda, fp8, kernel, vector; excerpt: "@CalebDu overall the PR looks good. I mostly had minor comments. I was wondering if there were any size restrictions on the new kernels, ..." (https://github.com/vllm-project/vllm/pull/14568#issuecomment-2814375413)
- `2025-03-27T02:00:09Z` `issue` by `bnellnm`; signals: block, correctness, deepgemm, gemm, moe; excerpt: "@CalebDu , thanks for adding the blocking support! I've been working on integrating the new version with DeepGemm but I'm running into problems with ..." (https://github.com/vllm-project/vllm/pull/14568#issuecomment-2756265582)
- `2025-03-26T14:30:00Z` `issue` by `CalebDu`; signals: aligned, block, deepgemm, gemm; excerpt: "Add align block size support for contiguous group gemm in deepgemm. Round up token amount in each expert to align block size and scan ..." (https://github.com/vllm-project/vllm/pull/14568#issuecomment-2754637844)
- `2025-05-02T08:04:56Z` `issue` by `CalebDu`; signals: benchmark, gemm, kernel, moe; excerpt: "@tlrmchlsmth I update code with your review. And fix ci failed in calling FusedMoE.select experts. I add benchmark for comparison permute/unpermte customized kernel in ..." (https://github.com/vllm-project/vllm/pull/14568#issuecomment-2846612852)
- `2025-05-02T00:37:52Z` `inline` by `tlrmchlsmth` `csrc/moe/permute_unpermute_kernels/moe_permute_unpermute_kernel.cu`:115; signals: kernel, moe, overflow; excerpt: "I think this should be: I think the way it is now, it won't cast until after the multiplication, which would allow for overflowing ..." (https://github.com/vllm-project/vllm/pull/14568#discussion_r2070963101)
- `2025-05-02T00:47:35Z` `review` `COMMENTED` by `tlrmchlsmth`; signals: benchmark, overflow; excerpt: "The implementation looks nice and clean. Are there any benchmark results? (I did spot one potential overflow that should be addressed)" (https://github.com/vllm-project/vllm/pull/14568#pullrequestreview-2810991987)
- `2025-03-12T08:57:13Z` `issue` by `gzy19990617`; signals: gemm, kernel, moe; excerpt: "请问预计什么时候会支持呐 ---- Replied Message ---- From @ . Date 03/12/2025 16:54 To vllm-project/vllm @ . Cc gaoziyuan @ . , Comment @ . Subject ..." (https://github.com/vllm-project/vllm/pull/14568#issuecomment-2717116678)
- `2025-03-12T11:23:44Z` `issue` by `CalebDu`; signals: gemm, kernel, moe; excerpt: "请问预计什么时候会支持呐 ---- Replied Message ---- From @ . Date 03/12/2025 16:54 To vllm-project/vllm @ . Cc gaoziyuan @ . , Comment @ . Subject ..." (https://github.com/vllm-project/vllm/pull/14568#issuecomment-2717547933)
