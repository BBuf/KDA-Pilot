# PR Discussion Digest

- Source PR: [sgl-project/sglang#7327](https://github.com/sgl-project/sglang/pull/7327)
- Source page: `sources/prs/sglang/PR-7327.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7327`
- Generated at: `2026-05-20T15:31:11.551768+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-18T21:30:31Z`
- Merged: `2025-06-22T20:38:48Z`

## Discussion Counts

- Issue comments: 17
- Review submissions: 19 (approved=1, commented=18)
- Inline review comments: 20
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=10, outdated=10
- Human participants with discussion text: Alcanderian, ch-wan, ispobock, pyc96, trevor-m, wenscarl, zhyncs
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-06-18T21:31:11Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @trevor-m, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2940738351)
- `2025-06-18T21:32:00Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request integrates the Flashinfer NVFP4 CUTLASS MoE kernel and adds support for Expert Parallelism ... (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2940740569)
- `2025-06-19T00:56:30Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2941124655)
- `2025-06-19T04:15:54Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2941491154)
- `2025-06-19T13:31:28Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2943035364)
- `2025-06-20T03:59:58Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2944485065)
- `2025-06-20T04:03:02Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2944488453)
- `2025-06-20T04:06:44Z` `COMMENTED` by `wenscarl` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2944491549)
- `2025-06-20T19:00:34Z` `COMMENTED` by `trevor-m` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2947066020)
- `2025-06-21T04:38:23Z` `COMMENTED` by `pyc96` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2947559806)
- `2025-06-21T14:22:35Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2947781058)
- `2025-06-21T18:08:07Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2947916204)
- `2025-06-21T18:31:10Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2947926738)
- `2025-06-21T18:32:25Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2947926958)
- `2025-06-22T09:01:17Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2948108702)
- `2025-06-22T09:20:49Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2948112819)
- `2025-06-22T09:21:55Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2948113664)
- `2025-06-22T10:19:52Z` `COMMENTED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2948128984)
- `2025-06-22T11:11:44Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/7327#pullrequestreview-2948142096)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 8 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 7 inline comment(s)
- `python/sglang/srt/models/deepseek_v2.py`: 4 inline comment(s)
- `python/sglang/srt/server_args.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-20T04:06:44Z` `inline` by `wenscarl` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:747; signals: attention, moe, triton; excerpt: "Does this PR work naturely for DP-attention? I think you may consider quantization - collective- fused moe - collective pattern." (https://github.com/sgl-project/sglang/pull/7327#discussion_r2157997841)
- `2025-06-21T04:35:57Z` `inline` by `pyc96` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:334; signals: flashinfer, moe, triton; excerpt: "I think we will need to handle MTP which is not quantized. Can we just disable flashinfer moe and ep moe for MTP module ..." (https://github.com/sgl-project/sglang/pull/7327#discussion_r2159861879)
- `2025-06-20T04:03:02Z` `inline` by `wenscarl` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:747; signals: attention, moe, triton; excerpt: "I think if DP attention is on, reduce-scatter is sufficient here instead of all-reduce." (https://github.com/sgl-project/sglang/pull/7327#discussion_r2157995838)
- `2025-06-20T18:54:16Z` `issue` by `trevor-m`; signals: accuracy, flashinfer, moe; excerpt: "@zhyncs Hi Yineng, thank you for checking and letting me know. I made a mistake while cleaning up for the code for the PR. ..." (https://github.com/sgl-project/sglang/pull/7327#issuecomment-2992539906)
- `2025-06-21T18:08:07Z` `inline` by `Alcanderian` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:335; signals: moe, triton; excerpt: "@trevor-m Why we have to do reduce here? There is an reduce op at [here]( We can find all reduce is called twice in ..." (https://github.com/sgl-project/sglang/pull/7327#discussion_r2160104117)
- `2025-06-21T18:32:25Z` `inline` by `Alcanderian` `python/sglang/srt/layers/quantization/modelopt_quant.py`:795; signals: perf, performance; excerpt: "Should be only called once or call at initial phase for performance purpose" (https://github.com/sgl-project/sglang/pull/7327#discussion_r2160111876)
- `2025-06-22T09:01:17Z` `inline` by `Alcanderian` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:747; signals: moe, triton; excerpt: "should not enable reduce here, fixed" (https://github.com/sgl-project/sglang/pull/7327#discussion_r2160271767)
- `2025-06-19T01:05:15Z` `issue` by `trevor-m`; signals: kernel, moe; excerpt: "Great job! But it is quite confused to integrate ep moe in FusedMoE. Could you move it into EPMoE? Thanks! @Alcanderian Thank you for ..." (https://github.com/sgl-project/sglang/pull/7327#issuecomment-2986183295)
- `2025-06-22T09:21:55Z` `inline` by `ispobock` `python/sglang/srt/models/deepseek_v2.py`:352; signals: cache; excerpt: "In prefill stage, one stream can saturate compute resources due to the large problem size while two stream may cause contentions (e.g. L2 cache)." (https://github.com/sgl-project/sglang/pull/7327#discussion_r2160276388)
- `2025-06-19T00:58:41Z` `issue` by `Alcanderian`; signals: moe; excerpt: "Great job! But it is quite confused to integrate ep moe in FusedMoE. Could you move it into EPMoE? Thanks!" (https://github.com/sgl-project/sglang/pull/7327#issuecomment-2986175351)
- `2025-06-20T07:47:43Z` `issue` by `zhyncs`; signals: accuracy; excerpt: "![]( @trevor-m The three options you provided all have accuracy issues, especially the first one, with an accuracy of 0." (https://github.com/sgl-project/sglang/pull/7327#issuecomment-2990159857)
