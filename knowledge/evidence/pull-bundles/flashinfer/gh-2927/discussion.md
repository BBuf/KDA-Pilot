# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2927](https://github.com/flashinfer-ai/flashinfer/pull/2927)
- Source page: `sources/prs/flashinfer/PR-2927.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2927`
- Generated at: `2026-05-20T15:25:53.845106+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-31T18:29:26Z`
- Merged: `2026-04-03T23:39:32Z`

## Discussion Counts

- Issue comments: 30
- Review submissions: 12 (approved=3, commented=9)
- Inline review comments: 10
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=3, outdated=6
- Human participants with discussion text: aleozlx, askliar, coderabbitai, djns99, eugr, johnnynunez
- Automation comments/reviews omitted from high-signal summary: 15
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-31T18:31:28Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for the SM121 (GB10) architecture, primarily focusing on managing its reduced ... (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4039302872)
- `2026-03-31T18:34:59Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (1) csrc/nv internal/tensorrt llm/kernels/cutlass kernels/cutlass heuristic.cpp (1) 152-154: Potential edge case: SIMT on SM121 returns ... (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4039319682)
- `2026-03-31T20:23:39Z` `APPROVED` by `djns99` (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4039925256)
- `2026-03-31T21:17:17Z` `COMMENTED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4040225653)
- `2026-03-31T21:18:04Z` `COMMENTED` by `aleozlx` - lgtm overall posted one comment (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4040229000)
- `2026-04-01T09:21:18Z` `COMMENTED` by `askliar` (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4042852682)
- `2026-04-01T11:25:04Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4043488444)
- `2026-04-01T13:51:44Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4044366201)
- `2026-04-01T13:58:40Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces shared memory (SMEM) limit checks for CUTLASS kernels to prevent invalid tile ... (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4044412040)
- `2026-04-01T16:47:01Z` `COMMENTED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4045567407)
- `2026-04-01T16:49:11Z` `APPROVED` by `aleozlx` - approved with some non-blocking questions (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4045585556)
- `2026-04-02T21:35:26Z` `APPROVED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4053337341)

## Inline Comment Hotspots

- `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`: 8 inline comment(s)
- `flashinfer/autotuner.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-31T18:34:59Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, cutlass, flashinfer, gemm, hang, kernel, tensorrt, vector; excerpt: "🧹 Nitpick comments (1) csrc/nv internal/tensorrt llm/kernels/cutlass kernels/cutlass heuristic.cpp (1) 152-154: Potential edge case: SIMT on SM121 returns empty candidates. For CutlassGemmType::Simt on SM121, ..." (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4039319682)
- `2026-04-01T11:25:03Z` `inline` by `coderabbitai` `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`:676; signals: b200, blackwell, block, cuda, cutlass, hang, kernel, memory; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🌐 Web query: What is the maximum shared memory per block for NVIDIA GB10 (SM 12.1) ..." (https://github.com/flashinfer-ai/flashinfer/pull/2927#discussion_r3021461745)
- `2026-04-01T13:51:44Z` `review` `COMMENTED` by `coderabbitai`; signals: bf16, cutlass, hang, kernel, pipeline, tensorrt, tile; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (1) csrc/nv internal/tensorrt ..." (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4044366201)
- `2026-03-31T18:29:40Z` `issue` by `coderabbitai`; signals: autotune, cache, cuda, cutlass, flashinfer, fp8, gemm, hang; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/flashinfer-ai/flashinfer/pull/2927#issuecomment-4164587772)
- `2026-04-01T11:25:03Z` `inline` by `coderabbitai` `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`:619; signals: cutlass, gemm, hang, kernel, pipeline, sm120, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor Fix clang-format issues flagged by CI. The pipeline failure indicates clang-format modified this section. Please run clang-format on this ..." (https://github.com/flashinfer-ai/flashinfer/pull/2927#discussion_r3021461743)
- `2026-04-01T11:25:04Z` `review` `COMMENTED` by `coderabbitai`; signals: cutlass, flashinfer, hang, kernel, tensorrt; excerpt: "Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/flashinfer-ai/flashinfer/pull/2927#pullrequestreview-4043488444)
- `2026-03-31T21:17:17Z` `inline` by `aleozlx` `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`:134; signals: cutlass, kernel, tensorrt; excerpt: "@askliar i suggest const &configs" (https://github.com/flashinfer-ai/flashinfer/pull/2927#discussion_r3018452609)
- `2026-04-01T16:47:01Z` `inline` by `aleozlx` `csrc/nv_internal/tensorrt_llm/kernels/cutlass_kernels/cutlass_heuristic.cpp`:597; signals: cutlass, kernel, tensorrt; excerpt: "may be cutlass has some util function we can query" (https://github.com/flashinfer-ai/flashinfer/pull/2927#discussion_r3023313727)
- `2026-04-02T09:16:46Z` `issue` by `johnnynunez`; signals: autotune, hang, regression; excerpt: "@askliar - btw, is MTP supposed to work with Nemotron with this PR? Getting this error: Works fine without MTP. This PR is to ..." (https://github.com/flashinfer-ai/flashinfer/pull/2927#issuecomment-4175850489)
- `2026-03-31T20:22:21Z` `inline` by `djns99` `flashinfer/autotuner.py`:777; signals: autotune, flashinfer; excerpt: "Should this maybe be warning or info and remove the error and just say enable debug logs to see more information. Its the full ..." (https://github.com/flashinfer-ai/flashinfer/pull/2927#discussion_r3018181684)
- `2026-04-01T09:21:18Z` `inline` by `askliar` `flashinfer/autotuner.py`:777; signals: autotune, flashinfer; excerpt: "That makes sense, added!" (https://github.com/flashinfer-ai/flashinfer/pull/2927#discussion_r3020860817)
- `2026-04-03T00:38:09Z` `issue` by `askliar`; signals: compile, flashinfer; excerpt: "@eugr I did run with and without! General serve command: With MTP, I've used uvx llama-benchy --base-url --model nemotron-3-super --pp 2048 --depth 4096 16000 ..." (https://github.com/flashinfer-ai/flashinfer/pull/2927#issuecomment-4181176536)
