# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#7937](https://github.com/NVIDIA/TensorRT-LLM/pull/7937)
- Source page: `sources/prs/tensorrt-llm/PR-7937.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-7937`
- Generated at: `2026-05-20T15:19:16.467837+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-23T20:23:21Z`
- Merged: `2025-10-06T20:59:06Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 22 (approved=4, commented=18)
- Inline review comments: 23
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=14, outdated=9
- Human participants with discussion text: PerkzZheng, brb-nv, coderabbitai, djns99, dongfengy, farazkh80, mikeiovine, rnik12, tensorrt-cicd, voipmonitor, zmarty
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-09-24T01:46:38Z` `COMMENTED` by `djns99` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3260298316)
- `2025-09-24T02:27:35Z` `COMMENTED` by `PerkzZheng` - @farazkh80 have [those tests]( been added automatically to sm120 machines ? the changes in fmha v2 LGTM. (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3260377970)
- `2025-09-24T03:25:20Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3260618947)
- `2025-09-24T03:25:39Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3260620526)
- `2025-09-24T03:26:01Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3260622047)
- `2025-09-24T03:26:29Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3260624172)
- `2025-09-24T03:26:54Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3260625926)
- `2025-09-24T04:11:36Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3260796051)
- `2025-09-24T04:12:42Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3260799736)
- `2025-09-24T04:13:03Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3260800835)
- `2025-09-24T23:40:04Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3265024091)
- `2025-10-02T02:15:33Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3291833164)
- `2025-10-02T02:34:17Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3291852805)
- `2025-10-02T20:46:21Z` `APPROVED` by `djns99` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3296341711)
- `2025-10-02T21:49:54Z` `COMMENTED` by `brb-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3296545545)
- `2025-10-02T21:53:10Z` `COMMENTED` by `brb-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3296557386)
- `2025-10-02T21:54:44Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3296562548)
- `2025-10-02T21:56:19Z` `COMMENTED` by `farazkh80` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3296567077)
- `2025-10-02T21:58:25Z` `COMMENTED` by `brb-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3296573596)
- `2025-10-02T21:59:44Z` `APPROVED` by `brb-nv` - Changes under tensorrt llm/ torch/models/ look good to me. (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3296577965)
- `2025-10-06T20:56:17Z` `APPROVED` by `dongfengy` (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3307321599)
- `2025-10-06T20:58:17Z` `APPROVED` by `mikeiovine` - Stamping to unblock, @dongfengy's review should be sufficient for this one (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3307333818)

## Inline Comment Hotspots

- `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch.h`: 7 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_gpt_oss.py`: 5 inline comment(s)
- `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/launchers/moe_gemm_tma_ws_launcher.inl`: 4 inline comment(s)
- `cpp/tests/unit_tests/kernels/mixtureOfExpertsTest.cu`: 2 inline comment(s)
- `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch_tma_ws.h`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_tma_warp_specialized_traits.h`: 1 inline comment(s)
- `cpp/tensorrt_llm/kernels/cutlass_kernels/python/generate_kernels.py`: 1 inline comment(s)
- `cpp/kernels/fmha_v2/src/fmha/fragment.h`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-02T02:34:17Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, attention, benchmark, bf16, block, compile, cuda, cutlass; excerpt: "Actionable comments posted: 1 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#pullrequestreview-3291852805)
- `2025-09-24T01:31:14Z` `inline` by `djns99` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/launchers/moe_gemm_tma_ws_launcher.inl`:427; signals: cutlass, fp4, gemm, kernel, moe, nvfp4, tensorrt, tma; excerpt: "Does NVFP4 also require this?" (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#discussion_r2373827974)
- `2025-10-02T02:34:13Z` `issue` by `coderabbitai`; signals: alignment, attention, bf16, block, cuda, cutlass, dtype, epilogue; excerpt: "📝 Walkthrough Walkthrough Adds optional attention sink handling to FMHA kernels, introduces a bias epilogue path in cuBLASLt wrappers and scaled MM, expands SM120 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#issuecomment-3358804629)
- `2025-09-24T04:13:03Z` `inline` by `farazkh80` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_tma_warp_specialized_traits.h`:88; signals: cutlass, gemm, kernel, moe, tensorrt, tma, warp; excerpt: "@pamelap-nvidia I added this here, let me know if you think it could break sth" (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#discussion_r2374139140)
- `2025-09-24T01:40:19Z` `inline` by `djns99` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch.h`:631; signals: block, cutlass, gemm, kernel, moe, tensorrt; excerpt: "In general, I would prefer to update get candidate configs to do this filtering if we can do it easily. Its not done by ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#discussion_r2373837060)
- `2025-09-24T01:43:31Z` `inline` by `djns99` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch_tma_ws.h`:507; signals: cutlass, gemm, kernel, moe, tensorrt, tma; excerpt: "The pretty function log above should include all the type information in the template expansion. Less readable but also less noise reading the actual ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#discussion_r2373840361)
- `2025-09-24T03:25:20Z` `inline` by `farazkh80` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch.h`:631; signals: cutlass, gemm, kernel, moe, sm120, tensorrt; excerpt: "agreed, I removed it and also stopped ommiting kernels for MX path with CTA shapes other than 128x128x128 in generate kernels.py. Moved the filtering ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#discussion_r2373974725)
- `2025-09-24T01:31:54Z` `inline` by `djns99` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/launchers/moe_gemm_tma_ws_launcher.inl`:454; signals: cutlass, gemm, kernel, moe, tensorrt, tma; excerpt: "Can the default case here still be Auto?" (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#discussion_r2373828606)
- `2025-09-24T03:26:29Z` `inline` by `farazkh80` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/launchers/moe_gemm_tma_ws_launcher.inl`:454; signals: cutlass, gemm, kernel, moe, tensorrt, tma; excerpt: "fixed this, it was a WAR initially but auto works and stage count auto also works" (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#discussion_r2373980436)
- `2025-09-24T03:26:54Z` `inline` by `farazkh80` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/launchers/moe_gemm_tma_ws_launcher.inl`:427; signals: cutlass, gemm, kernel, moe, tensorrt, tma; excerpt: "removed, explained in" (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#discussion_r2373982102)
- `2025-10-02T02:34:17Z` `inline` by `coderabbitai` `cpp/kernels/fmha_v2/src/fmha/fragment.h`:1269; signals: attention, kernel, nan, overflow, tma; excerpt: "⚠️ Potential issue 🔴 Critical Guard update sum when attention sinks are disabled attention sink value is initialized to -FLT MAX when params.attention sinks ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#discussion_r2396464481)
- `2025-09-24T01:34:24Z` `inline` by `djns99` `cpp/tensorrt_llm/kernels/cutlass_kernels/moe_gemm/moe_gemm_template_dispatch.h`:558; signals: cutlass, gemm, kernel, moe, tensorrt; excerpt: "Shouldn't we edit the isValidXXMOESpecialization function with this condition?" (https://github.com/NVIDIA/TensorRT-LLM/pull/7937#discussion_r2373831201)
