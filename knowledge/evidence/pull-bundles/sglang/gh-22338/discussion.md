# PR Discussion Digest

- Source PR: [sgl-project/sglang#22338](https://github.com/sgl-project/sglang/pull/22338)
- Source page: `sources/prs/sglang/PR-22338.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22338`
- Generated at: `2026-05-20T15:29:25.442414+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-08T07:57:30Z`
- Merged: `2026-05-19T04:46:52Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: OrangeRedeng, TallMessiWu, TheKonka, ping1jing2
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-08T07:59:40Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for MXFP4 and MXFP8 quantization on Ascend NPUs, including both offline ... (https://github.com/sgl-project/sglang/pull/22338#pullrequestreview-4073599343)
- `2026-05-18T09:13:11Z` `COMMENTED` by `OrangeRedeng` (https://github.com/sgl-project/sglang/pull/22338#pullrequestreview-4308803894)
- `2026-05-18T10:24:23Z` `COMMENTED` by `TallMessiWu` (https://github.com/sgl-project/sglang/pull/22338#pullrequestreview-4309297294)
- `2026-05-18T13:40:27Z` `COMMENTED` by `OrangeRedeng` (https://github.com/sgl-project/sglang/pull/22338#pullrequestreview-4310659095)
- `2026-05-19T04:46:05Z` `APPROVED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/22338#pullrequestreview-4315780852)

## Inline Comment Hotspots

- `python/sglang/multimodal_gen/runtime/server_args.py`: 3 inline comment(s)
- `python/sglang/multimodal_gen/runtime/layers/quantization/modelslim_mxfp4_scheme.py`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-18T10:34:26Z` `issue` by `TallMessiWu`; signals: benchmark, compile, failing, fp4, hang, kernel, latency, mxfp4; excerpt: "CI Failure Analysis I went through all failing jobs in the latest run. None of the failures are related to this PR's changes. This ..." (https://github.com/sgl-project/sglang/pull/22338#issuecomment-4476800766)
- `2026-05-18T10:24:23Z` `inline` by `TallMessiWu` `python/sglang/multimodal_gen/runtime/server_args.py`:1297; signals: bf16, fp4, fp8, mxfp4, perf; excerpt: "Hi! Great question. The distinction is between online quantization and offline (pre-quantized) loading . - modelslim is the entry point for offline pre-quantized checkpoints ..." (https://github.com/sgl-project/sglang/pull/22338#discussion_r3258119929)
- `2026-05-14T00:57:13Z` `issue` by `TheKonka`; signals: latency, perf, performance; excerpt: "Performance Comparison Report 1. High-level Summary Metric Baseline online.json offline.json :--- :--- :--- :--- E2E Latency 1447979.04 ms 1238595.17 ms (-14.5%) ✅ 1280412.90 ms ..." (https://github.com/sgl-project/sglang/pull/22338#issuecomment-4446397239)
- `2026-05-17T02:37:57Z` `issue` by `TheKonka`; signals: latency, perf, performance; excerpt: "Performance Comparison Report 1. High-level Summary Metric Baseline online.json offline.json :--- :--- :--- :--- E2E Latency 1447860.88 ms 1240433.51 ms (-14.3%) ✅ 1280435.48 ms ..." (https://github.com/sgl-project/sglang/pull/22338#issuecomment-4468965270)
- `2026-05-18T09:13:11Z` `inline` by `OrangeRedeng` `python/sglang/multimodal_gen/runtime/server_args.py`:1297; signals: fp8; excerpt: "Hi! Why are new quantization entities like mxfp8 or mxpf4 npu being created, shouldn't it be related to modelslim and handled in modelslim config?" (https://github.com/sgl-project/sglang/pull/22338#discussion_r3257682832)
- `2026-05-18T13:40:27Z` `inline` by `OrangeRedeng` `python/sglang/multimodal_gen/runtime/server_args.py`:1297; signals: general review; excerpt: "Got it! Thank you for your answer!" (https://github.com/sgl-project/sglang/pull/22338#discussion_r3259348184)
