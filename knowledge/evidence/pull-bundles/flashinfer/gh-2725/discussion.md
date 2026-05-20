# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2725](https://github.com/flashinfer-ai/flashinfer/pull/2725)
- Source page: `sources/prs/flashinfer/PR-2725.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2725`
- Generated at: `2026-05-20T15:25:25.935511+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-09T05:25:21Z`
- Merged: `2026-03-20T04:26:28Z`

## Discussion Counts

- Issue comments: 25
- Review submissions: 11 (approved=3, changes_requested=2, commented=6)
- Inline review comments: 9
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=7, outdated=7
- Human participants with discussion text: aleozlx, brandonmmusic-max, coderabbitai, geraldstanje, jasl, kahyunnam, nv-yunzheq
- Automation comments/reviews omitted from high-signal summary: 10
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-09T05:27:22Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for SM120 (RTX Blackwell desktop) GPUs to the NVFP4 MoE kernels. ... (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3912982178)
- `2026-03-09T05:33:01Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ ... (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3912995894)
- `2026-03-09T05:48:28Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ ... (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3913032547)
- `2026-03-10T12:29:41Z` `COMMENTED` by `jasl` (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3922027553)
- `2026-03-11T22:46:35Z` `CHANGES_REQUESTED` by `kahyunnam` - Left one comment here; cc @aleozlx since he is team PIC for MoE operations. (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3932925485)
- `2026-03-12T00:49:45Z` `COMMENTED` by `brandonmmusic-max` - Thanks — that makes sense. I restricted the f suffix normalization to SM120 specifically to avoid possible regressions ... (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3933293148)
- `2026-03-12T00:52:08Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ ... (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3933298594)
- `2026-03-13T18:46:33Z` `APPROVED` by `kahyunnam` - LGTM, thanks for the contribution! (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3946265382)
- `2026-03-13T21:02:42Z` `APPROVED` by `nv-yunzheq` - LGTM (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3946934649)
- `2026-03-13T21:12:20Z` `CHANGES_REQUESTED` by `kahyunnam` - One last comment, thanks! (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3946974707)
- `2026-03-18T00:02:54Z` `APPROVED` by `kahyunnam` (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3964329069)

## Inline Comment Hotspots

- `csrc/trtllm_fused_moe_kernel_launcher.cu`: 4 inline comment(s)
- `flashinfer/compilation_context.py`: 4 inline comment(s)
- `flashinfer/jit/fused_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-09T05:33:00Z` `inline` by `coderabbitai` `flashinfer/jit/fused_moe.py`:63; signals: blackwell, cuda, cute, flashinfer, fp4, gemm, moe, nvfp4; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length of output: 1484 --- 🏁 Script executed: Repository: flashinfer-ai/flashinfer Length ..." (https://github.com/flashinfer-ai/flashinfer/pull/2725#discussion_r2903306315)
- `2026-03-09T05:25:39Z` `issue` by `coderabbitai`; signals: benchmark, blackwell, block, cuda, flashinfer, fp4, hang, kernel; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/flashinfer-ai/flashinfer/pull/2725#issuecomment-4021249876)
- `2026-03-11T23:05:55Z` `issue` by `geraldstanje`; signals: attention, blackwell, flash attention, flashinfer, kernel, moe, sm120, triton; excerpt: "hi @brandonmmusic-max does that mean after merging this pr sm120 for nvidia rtx 6000 pro blackwell can also run the MoE kernel from FlashInfer ..." (https://github.com/flashinfer-ai/flashinfer/pull/2725#issuecomment-4042794833)
- `2026-03-11T22:44:02Z` `inline` by `kahyunnam` `flashinfer/compilation_context.py`:49; signals: b200, flashinfer, fp4, nvfp4, perf, regression, sm120; excerpt: "@brandonmmusic-max can you explain your rationale for patching all major =10 with "f"? I understand there's the 120a bug for nvfp4, so we prefer ..." (https://github.com/flashinfer-ai/flashinfer/pull/2725#discussion_r2921371892)
- `2026-03-09T05:33:01Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, hang, kernel, moe; excerpt: "Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ Run configuration Configuration used : defaults ..." (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3912995894)
- `2026-03-09T05:48:28Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, hang, kernel, moe; excerpt: "Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info ⚙️ Run configuration Configuration used : defaults ..." (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3913032547)
- `2026-03-12T00:49:45Z` `review` `COMMENTED` by `brandonmmusic-max`; signals: b200, regression, sm100, sm120; excerpt: "Thanks — that makes sense. I restricted the f suffix normalization to SM120 specifically to avoid possible regressions on SM100/B200. The PR has been ..." (https://github.com/flashinfer-ai/flashinfer/pull/2725#pullrequestreview-3933293148)
- `2026-03-10T04:32:15Z` `issue` by `geraldstanje`; signals: blackwell, flashinfer, kernel, moe, sm120; excerpt: "hi @brandonmmusic-max does that mean after merging this pr sm120 for nvidia rtx 6000 pro blackwell can also run the MoE kernel from FlashInfer ..." (https://github.com/flashinfer-ai/flashinfer/pull/2725#issuecomment-4028589967)
- `2026-03-10T13:27:23Z` `issue` by `brandonmmusic-max`; signals: blackwell, flashinfer, kernel, moe, sm120; excerpt: "hi @brandonmmusic-max does that mean after merging this pr sm120 for nvidia rtx 6000 pro blackwell can also run the MoE kernel from FlashInfer ..." (https://github.com/flashinfer-ai/flashinfer/pull/2725#issuecomment-4031383007)
- `2026-03-14T00:03:32Z` `issue` by `brandonmmusic-max`; signals: cuda, flashinfer, fp4, hang, sm120; excerpt: "Sounds like a great idea to me. The more compatible the merrier. Brandon M. Music W. Jeffrey Scott, P.S.C. Pronouns He, Him, His On ..." (https://github.com/flashinfer-ai/flashinfer/pull/2725#issuecomment-4058821986)
- `2026-03-14T03:26:35Z` `issue` by `brandonmmusic-max`; signals: cuda, flashinfer, fp4, hang, sm120; excerpt: "Hi Ka-Hyun, I have made the requested changes and pushed them. I also updated the docstring to reflect these updates, as I thought that ..." (https://github.com/flashinfer-ai/flashinfer/pull/2725#issuecomment-4059337652)
- `2026-03-09T05:48:27Z` `inline` by `coderabbitai` `flashinfer/compilation_context.py`:47; signals: blackwell, cuda, cute, flashinfer; excerpt: "⚠️ Potential issue 🟠 Major Normalize FLASHINFER CUDA ARCH LIST with the same suffix mapping. This only fixes autodetected devices. If a build sets ..." (https://github.com/flashinfer-ai/flashinfer/pull/2725#discussion_r2903344308)
