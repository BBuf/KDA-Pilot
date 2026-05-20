# PR Discussion Digest

- Source PR: [sgl-project/sglang#22204](https://github.com/sgl-project/sglang/pull/22204)
- Source page: `sources/prs/sglang/PR-22204.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22204`
- Generated at: `2026-05-20T15:29:21.829559+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-06T19:48:59Z`
- Merged: `2026-04-13T02:08:46Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: Fridge003, b8zhong, zianglih
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-06T19:50:45Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors weight management for FlashInfer TRT-LLM FP4 MoE by renaming shuffled weight parameters ... (https://github.com/sgl-project/sglang/pull/22204#pullrequestreview-4064187403)
- `2026-04-06T20:04:49Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/22204#pullrequestreview-4064247793)
- `2026-04-07T09:22:44Z` `COMMENTED` by `zianglih` (https://github.com/sgl-project/sglang/pull/22204#pullrequestreview-4067043805)
- `2026-04-10T05:13:08Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/22204#pullrequestreview-4087343939)
- `2026-04-11T03:36:13Z` `APPROVED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/22204#pullrequestreview-4093341749)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 1 inline comment(s)
- `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-07T09:22:44Z` `inline` by `zianglih` `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`:200; signals: flashinfer, moe, register; excerpt: "Set to 0.89 according to 22136" (https://github.com/sgl-project/sglang/pull/22204#discussion_r3044047352)
- `2026-04-06T20:04:49Z` `inline` by `zianglih` `python/sglang/srt/layers/moe/moe_runner/flashinfer_trtllm.py`:286; signals: flashinfer, moe; excerpt: "this only happens during weight load once" (https://github.com/sgl-project/sglang/pull/22204#discussion_r3041425513)
- `2026-04-12T00:24:32Z` `issue` by `Fridge003`; signals: failing; excerpt: "@zianglih Please take a look at this failing test" (https://github.com/sgl-project/sglang/pull/22204#issuecomment-4230434148)
- `2026-04-12T18:22:01Z` `issue` by `zianglih`; signals: b200; excerpt: "@Fridge003 the standalone stage-c-test-4-gpu-b200 passed." (https://github.com/sgl-project/sglang/pull/22204#issuecomment-4232319292)
