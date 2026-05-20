# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2993](https://github.com/flashinfer-ai/flashinfer/pull/2993)
- Source page: `sources/prs/flashinfer/PR-2993.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2993`
- Generated at: `2026-05-20T15:26:04.675269+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-06T10:26:10Z`
- Merged: `2026-04-13T04:03:28Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 12 (approved=2, commented=10)
- Inline review comments: 15
- Review threads observed: 11
- Resolved/outdated thread markers: resolved=11, outdated=7
- Human participants with discussion text: ChristinaZ, aleozlx, coderabbitai, jiahanc, nvpohanh
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-06T10:30:47Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a dynamic block kernel for MoE routing to handle a wider range ... (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4061500483)
- `2026-04-06T10:38:52Z` `COMMENTED` by `jiahanc` (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4061531199)
- `2026-04-06T10:46:33Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 4 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4061560925)
- `2026-04-06T10:50:32Z` `COMMENTED` by `ChristinaZ` (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4061572417)
- `2026-04-06T23:40:11Z` `APPROVED` by `jiahanc` - LGTM. Thanks for contribution! (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4065052548)
- `2026-04-07T14:17:37Z` `COMMENTED` by `ChristinaZ` (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4068803486)
- `2026-04-11T13:12:45Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🧹 Nitpick comments (1) tests/moe/test trtllm gen fused moe.py (1) 4048-4063: Add one MiniMax2 ... (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4093755041)
- `2026-04-11T14:34:23Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4093870721)
- `2026-04-12T03:12:59Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 ♻️ Duplicate comments (1) csrc/fused moe/trtllm backend/trtllm fused moe routing custom.cu (1) 895-917: ⚠️ ... (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4094469538)
- `2026-04-12T03:46:10Z` `COMMENTED` by `ChristinaZ` (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4094491646)
- `2026-04-12T03:46:32Z` `COMMENTED` by `coderabbitai` (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4094491835)
- `2026-04-13T04:03:26Z` `APPROVED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4096337690)

## Inline Comment Hotspots

- `csrc/fused_moe/trtllm_backend/trtllm_fused_moe_routing_custom.cu`: 5 inline comment(s)
- `tests/moe/test_trtllm_gen_fused_moe.py`: 4 inline comment(s)
- `include/flashinfer/trtllm/fused_moe/RoutingCustomPolicy.cuh`: 3 inline comment(s)
- `flashinfer/fused_moe/core.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-04-11T14:34:23Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, bf16, block, dtype, flashinfer, fp4, fp8, hang; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4093870721)
- `2026-04-11T14:34:22Z` `inline` by `coderabbitai` `flashinfer/fused_moe/core.py`:1226; signals: autotune, bf16, cache, cuda, cute, flashinfer, fp4, fp8; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 78 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2993#discussion_r3068155472)
- `2026-04-06T10:26:31Z` `issue` by `coderabbitai`; signals: autotune, block, dtype, flashinfer, hang, kernel, memory, moe; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/flashinfer-ai/flashinfer/pull/2993#issuecomment-4191693058)
- `2026-04-12T03:12:59Z` `review` `COMMENTED` by `coderabbitai`; signals: block, flashinfer, hang, kernel, moe, tile; excerpt: "Actionable comments posted: 1 ♻️ Duplicate comments (1) csrc/fused moe/trtllm backend/trtllm fused moe routing custom.cu (1) 895-917: ⚠️ Potential issue 🟠 Major Gate dyn-block ..." (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4094469538)
- `2026-04-06T10:46:32Z` `inline` by `coderabbitai` `csrc/fused_moe/trtllm_backend/trtllm_fused_moe_routing_custom.cu`:562; signals: cuda, cute, flashinfer, kernel, moe, race; excerpt: "⚠️ Potential issue 🔴 Critical 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 132 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2993#discussion_r3039065600)
- `2026-04-06T10:46:33Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, hang, kernel, moe, pipeline; excerpt: "Actionable comments posted: 4 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4061560925)
- `2026-04-11T13:12:45Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, flashinfer, hang, moe, regression; excerpt: "Actionable comments posted: 1 🧹 Nitpick comments (1) tests/moe/test trtllm gen fused moe.py (1) 4048-4063: Add one MiniMax2 case above 512 experts. This config ..." (https://github.com/flashinfer-ai/flashinfer/pull/2993#pullrequestreview-4093755041)
- `2026-04-06T10:46:32Z` `inline` by `coderabbitai` `csrc/fused_moe/trtllm_backend/trtllm_fused_moe_routing_custom.cu`:525; signals: block, gemm, kernel, moe, tile; excerpt: "⚠️ Potential issue 🟠 Major Restore the cluster-size CTA expansion from the static block kernel. numCtaPerExpert is now left in cluster units, and MnLimit ..." (https://github.com/flashinfer-ai/flashinfer/pull/2993#discussion_r3039065597)
- `2026-04-06T10:46:32Z` `inline` by `coderabbitai` `include/flashinfer/trtllm/fused_moe/RoutingCustomPolicy.cuh`:635; signals: cute, flashinfer, moe; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 129 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2993#discussion_r3039065604)
- `2026-04-11T14:34:22Z` `inline` by `coderabbitai` `csrc/fused_moe/trtllm_backend/trtllm_fused_moe_routing_custom.cu`:910; signals: block, kernel, moe; excerpt: "⚠️ Potential issue 🟠 Major Gate useDynBlock on the dispatched tier size. The new Tier fallback lets queryDispatchedMaxExperts() return 1024 even when data.mNumExperts == ..." (https://github.com/flashinfer-ai/flashinfer/pull/2993#discussion_r3068155469)
- `2026-04-12T03:12:59Z` `inline` by `coderabbitai` `csrc/fused_moe/trtllm_backend/trtllm_fused_moe_routing_custom.cu`:585; signals: memory, moe, shared memory; excerpt: "⚠️ Potential issue 🟡 Minor Don't load smemOffset for non-local experts. smemOffset is only written in Phase 2 for local experts, but Line 583 ..." (https://github.com/flashinfer-ai/flashinfer/pull/2993#discussion_r3068897527)
- `2026-04-07T05:39:43Z` `issue` by `nvpohanh`; signals: block, kernel, tensorrt; excerpt: "Add dynamic block kernel (routingIndicesDynBlockKernel) comes from the TensorRT-LLM. . Made related modification by refactoring LAUNCH ROUTING CUSTOM with dispatchRoutingPolicy and queryDispatchedMaxExperts Simplify PDL ..." (https://github.com/flashinfer-ai/flashinfer/pull/2993#issuecomment-4196793408)
