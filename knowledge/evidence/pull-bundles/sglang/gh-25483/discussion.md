# PR Discussion Digest

- Source PR: [sgl-project/sglang#25483](https://github.com/sgl-project/sglang/pull/25483)
- Source page: `sources/prs/sglang/PR-25483.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-25483`
- Generated at: `2026-05-20T15:29:48.829183+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-16T15:37:52Z`
- Merged: `2026-05-20T01:05:39Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 4 (approved=1, commented=2, dismissed=1)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=3
- Human participants with discussion text: BBuf, ch-wan, mickqian, zijiexia
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2026-05-16T15:43:33Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request transitions Wan2.2 FP8 and NVFP4 models to use official NVIDIA full Diffusers repositories ... (https://github.com/sgl-project/sglang/pull/25483#pullrequestreview-4303844843)
- `2026-05-16T18:11:02Z` `DISMISSED` by `zijiexia` (https://github.com/sgl-project/sglang/pull/25483#pullrequestreview-4304060491)
- `2026-05-17T14:04:31Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/25483#pullrequestreview-4305542279)
- `2026-05-20T01:04:32Z` `APPROVED` by `mickqian` (https://github.com/sgl-project/sglang/pull/25483#pullrequestreview-4324501298)

## Inline Comment Hotspots

- `docs/diffusion/quantization.md`: 4 inline comment(s)

## High-Signal Discussion

- `2026-05-16T16:24:25Z` `issue` by `BBuf`; signals: b200, bf16, compile, fp4, fp8, h100, h200, memory; excerpt: "H200 FP8 vs BF16 follow-up I checked the historical ModelOpt PRs and reran a Wan2.2 FP8-vs-BF16 comparison on H200 to understand the small speedup ..." (https://github.com/sgl-project/sglang/pull/25483#issuecomment-4467424434)
- `2026-05-16T16:36:36Z` `issue` by `BBuf`; signals: attention, b200, bf16, blackwell, compile, flashinfer, fp4, gemm; excerpt: "B200 Wan2.2 NVFP4 no-compile retest I reran the Wan2.2 NVFP4 speed comparison on B200 with torch compile explicitly disabled. This uses the current PR ..." (https://github.com/sgl-project/sglang/pull/25483#issuecomment-4467457898)
- `2026-05-17T05:20:06Z` `issue` by `BBuf`; signals: attention, b200, bf16, compile, fp4, fp8, nvfp4; excerpt: "Repro commands for the Wan2.2 ModelOpt validation table The rendered GIF table in the PR body was generated on ion-b200 GPU 6 with the ..." (https://github.com/sgl-project/sglang/pull/25483#issuecomment-4469438482)
- `2026-05-17T13:43:33Z` `issue` by `BBuf`; signals: b200, block, compile, fp4, hang, layout, nvfp4; excerpt: "Added the FLUX.1 NVFP4 CUDNN scale-layout fix from 25527 into this PR as a minimal targeted change instead of merging the whole draft PR. ..." (https://github.com/sgl-project/sglang/pull/25483#issuecomment-4470859113)
- `2026-05-17T11:01:16Z` `issue` by `BBuf`; signals: b200, fp4, gemm, layout, nvfp4; excerpt: "Follow-up on the garbled NVIDIA NVFP4 video: - Root cause: nvidia/Wan2.2-T2V-A14B-Diffusers-NVFP4 omits SGLang's swap weight nibbles layout knob in both Wan transformer configs. The ..." (https://github.com/sgl-project/sglang/pull/25483#issuecomment-4470367250)
- `2026-05-17T12:52:20Z` `issue` by `BBuf`; signals: b200, compile, fp4, layout, nvfp4; excerpt: "Follow-up update: I replaced the Wan-specific fallback with the generic ModelOpt NVFP4 layout rule. Final behavior: - swap weight nibbles now defaults to false. ..." (https://github.com/sgl-project/sglang/pull/25483#issuecomment-4470723316)
- `2026-05-18T13:29:50Z` `issue` by `BBuf`; signals: fp4, fp8, nvfp4; excerpt: "Updated this PR to enable consistency checks for the six ModelOpt diffusion CI cases: - flux1 modelopt fp8 t2i - flux2 modelopt fp8 t2i ..." (https://github.com/sgl-project/sglang/pull/25483#issuecomment-4478172779)
- `2026-05-16T18:10:55Z` `inline` by `zijiexia` `docs/diffusion/quantization.md`; signals: hang; excerpt: "Hi @BBuf , we've migrated our docs to the new location under docs new. Could you please migrate your changes to docs new accordingly? ..." (https://github.com/sgl-project/sglang/pull/25483#discussion_r3253258347)
- `2026-05-17T14:04:31Z` `inline` by `BBuf` `docs/diffusion/quantization.md`; signals: general review; excerpt: "ok, thanks." (https://github.com/sgl-project/sglang/pull/25483#discussion_r3254756432)
