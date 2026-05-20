# PR Discussion Digest

- Source PR: [sgl-project/sglang#22136](https://github.com/sgl-project/sglang/pull/22136)
- Source page: `sources/prs/sglang/PR-22136.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22136`
- Generated at: `2026-05-20T15:29:21.828197+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-05T05:42:22Z`
- Merged: `2026-04-23T05:30:55Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 1 (commented=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: zianglih
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-05T05:43:46Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request lowers the GSM8K accuracy baselines for FlashInfer TRT-LLM MoE and DeepSeek-R1 FP4 performance ... (https://github.com/sgl-project/sglang/pull/22136#pullrequestreview-4059155407)

## Inline Comment Hotspots

- `test/registered/backends/test_flashinfer_trtllm_gen_moe_backend.py`: 1 inline comment(s)
- `test/registered/perf/test_dpsk_r1_fp4_4gpu_perf.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-06T21:13:08Z` `issue` by `zianglih`; signals: flashinfer, fp8, moe; excerpt: "Hi, FlashinferTrtllmGenMoeBackendMXFP8Base also regressed similar to FlashinferTrtllmGenMoeBackendFP8Base. We can also set threshold from 0.93 to 0.89 there." (https://github.com/sgl-project/sglang/pull/22136#issuecomment-4195032205)
