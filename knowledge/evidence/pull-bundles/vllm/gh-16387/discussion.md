# PR Discussion Digest

- Source PR: [vllm-project/vllm#16387](https://github.com/vllm-project/vllm/pull/16387)
- Source page: `sources/prs/vllm/PR-16387.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16387`
- Generated at: `2026-05-20T15:34:54.594549+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-10T04:05:22Z`
- Merged: `2025-04-14T21:41:48Z`

## Discussion Counts

- Issue comments: 43
- Review submissions: 10 (approved=3, commented=7)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=2
- Human participants with discussion text: DarkLight1337, Husamx, Isotr0py, courage17340, guihonghao, nicoeiris11, yushuiwx, ywang96, zhouzaida
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 20

## Review Decisions

- `2025-04-10T04:51:18Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/16387#pullrequestreview-2755311250)
- `2025-04-10T04:57:07Z` `COMMENTED` by `courage17340` (https://github.com/vllm-project/vllm/pull/16387#pullrequestreview-2755317700)
- `2025-04-10T06:29:11Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/16387#pullrequestreview-2755479428)
- `2025-04-10T07:06:19Z` `COMMENTED` by `courage17340` (https://github.com/vllm-project/vllm/pull/16387#pullrequestreview-2755568374)
- `2025-04-14T05:48:08Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/16387#pullrequestreview-2763195944)
- `2025-04-14T07:46:41Z` `APPROVED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/16387#pullrequestreview-2763426061)
- `2025-04-14T07:48:35Z` `COMMENTED` by `courage17340` (https://github.com/vllm-project/vllm/pull/16387#pullrequestreview-2763430756)
- `2025-04-14T08:01:16Z` `APPROVED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/16387#pullrequestreview-2763469709)
- `2025-04-14T08:06:26Z` `APPROVED` by `ywang96` - Sorry for the late review - overall LGTM and I just left one comment (https://github.com/vllm-project/vllm/pull/16387#pullrequestreview-2763350860)
- `2025-04-14T08:24:32Z` `COMMENTED` by `courage17340` (https://github.com/vllm-project/vllm/pull/16387#pullrequestreview-2763533174)

## Inline Comment Hotspots

- `vllm/v1/worker/gpu_model_runner.py`: 2 inline comment(s)
- `vllm/transformers_utils/processors/processing_kimi_vl.py`: 2 inline comment(s)
- `tests/models/decoder_only/vision_language/test_models.py`: 2 inline comment(s)
- `vllm/model_executor/models/kimi_vl.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-10T04:48:50Z` `issue` by `ywang96`; signals: cache, memory; excerpt: "Hey @courage17340 thanks for the contribution! Before I review the PR just one quick question: It seems that recent versions of vllm have cpu ..." (https://github.com/vllm-project/vllm/pull/16387#issuecomment-2791541617)
- `2025-04-10T06:21:43Z` `issue` by `courage17340`; signals: cache, memory; excerpt: "Hey @courage17340 thanks for the contribution! Before I review the PR just one quick question: It seems that recent versions of vllm have cpu ..." (https://github.com/vllm-project/vllm/pull/16387#issuecomment-2791676458)
- `2025-04-11T02:59:07Z` `issue` by `courage17340`; signals: memory, oom; excerpt: "Edit: What GPU are you running this on? I get OOM even on A800 (80 GB) I'm running this on H800 (80GB too). It ..." (https://github.com/vllm-project/vllm/pull/16387#issuecomment-2795717938)
- `2025-04-11T04:36:21Z` `issue` by `DarkLight1337`; signals: memory, oom; excerpt: "I'm running this on H800 (80GB too). It seems that you are getting GPU OOM? In that case, you should check whether flash-attn (vllm-flash-attn ..." (https://github.com/vllm-project/vllm/pull/16387#issuecomment-2795811758)
- `2025-04-11T07:56:31Z` `issue` by `courage17340`; signals: cache, memory; excerpt: "Can you try VLLM ENABLE V1 MULTIPROCESSING=0 and see if it resolves the memory issue? This env doesn't help. I guess maybe it's not ..." (https://github.com/vllm-project/vllm/pull/16387#issuecomment-2796138389)
- `2025-04-11T09:03:58Z` `issue` by `DarkLight1337`; signals: cache, memory; excerpt: "I think it's just that the cache limit is multiplied unexpectedly. When I run your command, the memory usage plateaus out at approx. 224G ..." (https://github.com/vllm-project/vllm/pull/16387#issuecomment-2796294323)
- `2025-04-14T07:38:33Z` `issue` by `DarkLight1337`; signals: cache, memory; excerpt: "I think it's just that the cache limit is multiplied unexpectedly. When I run your command, the memory usage plateaus out at approx. 224G ..." (https://github.com/vllm-project/vllm/pull/16387#issuecomment-2800744270)
- `2025-04-10T06:28:09Z` `inline` by `Isotr0py` `vllm/transformers_utils/processors/processing_kimi_vl.py`:60; signals: register; excerpt: ""auto map": { "AutoImageProcessor": "image processing kimi vl.KimiVLImageProcessor", "AutoProcessor": "processing kimi vl.KimiVLProcessor" }, If the processor has been implemented and registered in model repo ..." (https://github.com/vllm-project/vllm/pull/16387#discussion_r2036597636)
- `2025-04-10T04:14:37Z` `issue` by `ywang96`; signals: memory; excerpt: "Hey @courage17340 thanks for the contribution! Before I review the PR just one quick question: It seems that recent versions of vllm have cpu ..." (https://github.com/vllm-project/vllm/pull/16387#issuecomment-2791503367)
- `2025-04-10T04:40:33Z` `issue` by `courage17340`; signals: memory; excerpt: "Hey @courage17340 thanks for the contribution! Before I review the PR just one quick question: It seems that recent versions of vllm have cpu ..." (https://github.com/vllm-project/vllm/pull/16387#issuecomment-2791531972)
- `2025-04-10T08:16:32Z` `issue` by `DarkLight1337`; signals: memory; excerpt: "Could you elaborate on the memory leak when caching is enabled? Does the memory usage grow without bound or does it stabilize after a ..." (https://github.com/vllm-project/vllm/pull/16387#issuecomment-2791941201)
- `2025-04-10T09:43:24Z` `issue` by `courage17340`; signals: memory; excerpt: "Could you elaborate on the memory leak when caching is enabled? Does the memory usage grow without bound or does it stabilize after a ..." (https://github.com/vllm-project/vllm/pull/16387#issuecomment-2792172798)
