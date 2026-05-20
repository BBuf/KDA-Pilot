# PR Discussion Digest

- Source PR: [sgl-project/sglang#22594](https://github.com/sgl-project/sglang/pull/22594)
- Source page: `sources/prs/sglang/PR-22594.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22594`
- Generated at: `2026-05-20T15:29:27.571404+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-11T15:59:45Z`
- Merged: `2026-04-13T00:01:55Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: BBuf, mickqian, yhyang201
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-11T16:02:23Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables dit layerwise offload for ModelOpt FP8 checkpoints by updating the LayerwiseOffloadManager to ... (https://github.com/sgl-project/sglang/pull/22594#pullrequestreview-4093938498)
- `2026-04-12T07:04:03Z` `COMMENTED` by `mickqian` (https://github.com/sgl-project/sglang/pull/22594#pullrequestreview-4094730072)
- `2026-04-12T14:04:19Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/22594#pullrequestreview-4095113112)
- `2026-04-12T14:27:37Z` `APPROVED` by `mickqian` (https://github.com/sgl-project/sglang/pull/22594#pullrequestreview-4095134694)

## Inline Comment Hotspots

- `docs/diffusion/quantization.md`: 2 inline comment(s)
- `python/sglang/multimodal_gen/runtime/utils/layerwise_offload.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-12T02:00:50Z` `issue` by `BBuf`; signals: cache, fp4, fp8, h100, memory, nvfp4, perf; excerpt: "Layerwise-offload VRAM comparison for the validated ModelOpt paths, using the same smoke configs as the bring-up runs and reading memory checkpoints.after forward from --perf-dump-path. ..." (https://github.com/sgl-project/sglang/pull/22594#issuecomment-4230550586)
- `2026-04-12T07:02:32Z` `inline` by `mickqian` `docs/diffusion/quantization.md`:53; signals: fp4, fp8, nvfp4; excerpt: "nit: remove: Keep the FP8 and NVFP4 rows here instead of duplicating them in workflow skills." (https://github.com/sgl-project/sglang/pull/22594#discussion_r3069125633)
- `2026-04-12T14:04:19Z` `inline` by `BBuf` `docs/diffusion/quantization.md`:53; signals: general review; excerpt: "done" (https://github.com/sgl-project/sglang/pull/22594#discussion_r3069562138)
