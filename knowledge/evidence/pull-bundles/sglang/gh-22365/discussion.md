# PR Discussion Digest

- Source PR: [sgl-project/sglang#22365](https://github.com/sgl-project/sglang/pull/22365)
- Source page: `sources/prs/sglang/PR-22365.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22365`
- Generated at: `2026-05-20T15:29:25.447373+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-08T13:49:03Z`
- Merged: `2026-04-10T12:56:57Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 4 (commented=4)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: BBuf, mickqian
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-04-08T13:53:26Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request implements support for NVIDIA ModelOpt FP8 and NVFP4 quantization in SGLang Diffusion, introducing ... (https://github.com/sgl-project/sglang/pull/22365#pullrequestreview-4075612756)
- `2026-04-09T06:34:24Z` `COMMENTED` by `mickqian` - some TODOs: 1. adapt quantization doc if necessary 2. add at least one testcase for modelopt fp8 (https://github.com/sgl-project/sglang/pull/22365#pullrequestreview-4080148744)
- `2026-04-09T06:36:34Z` `COMMENTED` by `mickqian` (https://github.com/sgl-project/sglang/pull/22365#pullrequestreview-4080156687)
- `2026-04-10T06:34:18Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/22365#pullrequestreview-4087807097)

## Inline Comment Hotspots

- `python/sglang/multimodal_gen/runtime/layers/quantization/modelopt_quant.py`: 2 inline comment(s)
- `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-10T05:03:10Z` `issue` by `BBuf`; signals: correctness, fp8, hang; excerpt: "Split the ModelOpt FP8 skill and helper tooling out into stacked PR 22492 so this PR stays focused on the runtime / loader / ..." (https://github.com/sgl-project/sglang/pull/22365#issuecomment-4220767774)
- `2026-04-09T06:34:24Z` `review` `COMMENTED` by `mickqian`; signals: fp8; excerpt: "some TODOs: 1. adapt quantization doc if necessary 2. add at least one testcase for modelopt fp8" (https://github.com/sgl-project/sglang/pull/22365#pullrequestreview-4080148744)
- `2026-04-10T12:50:12Z` `issue` by `BBuf`; signals: fp8; excerpt: "FLUX1 main pr (fp8)" (https://github.com/sgl-project/sglang/pull/22365#issuecomment-4223850557)
- `2026-04-09T06:35:59Z` `inline` by `mickqian` `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py`:329; signals: general review; excerpt: "maybe extract to a dedicated function here to better illustrate the quant load logic" (https://github.com/sgl-project/sglang/pull/22365#discussion_r3055897093)
- `2026-04-10T06:34:18Z` `inline` by `BBuf` `python/sglang/multimodal_gen/runtime/loader/transformer_load_utils.py`:329; signals: general review; excerpt: "done" (https://github.com/sgl-project/sglang/pull/22365#discussion_r3062574313)
