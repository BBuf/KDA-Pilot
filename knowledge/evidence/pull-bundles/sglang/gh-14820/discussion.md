# PR Discussion Digest

- Source PR: [sgl-project/sglang#14820](https://github.com/sgl-project/sglang/pull/14820)
- Source page: `sources/prs/sglang/PR-14820.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14820`
- Generated at: `2026-05-20T15:28:05.927946+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-10T12:34:35Z`
- Merged: `2025-12-15T18:25:13Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 7 (approved=3, commented=4)
- Inline review comments: 15
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=5, outdated=12
- Human participants with discussion text: Liwansi, ZhongsJie, iforgetmyname, ping1jing2, xueliangyang-oeuler
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 4

## Review Decisions

- `2025-12-10T12:37:22Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for Qwen Eagle3 models on NPU. The main changes include adding ... (https://github.com/sgl-project/sglang/pull/14820#pullrequestreview-3562351904)
- `2025-12-11T03:11:38Z` `COMMENTED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/14820#pullrequestreview-3565403802)
- `2025-12-11T03:15:23Z` `COMMENTED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/14820#pullrequestreview-3565417973)
- `2025-12-12T06:06:51Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/14820#pullrequestreview-3570440872)
- `2025-12-15T01:07:48Z` `APPROVED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/14820#pullrequestreview-3576042776)
- `2025-12-15T01:21:24Z` `APPROVED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/14820#pullrequestreview-3576083840)
- `2025-12-15T18:24:56Z` `APPROVED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/14820#pullrequestreview-3579574667)

## Inline Comment Hotspots

- `python/sglang/srt/speculative/eagle_info_v2.py`: 3 inline comment(s)
- `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`: 2 inline comment(s)
- `docs/platforms/ascend_npu_qwen3_examples.md`: 2 inline comment(s)
- `python/sglang/srt/model_loader/loader.py`: 2 inline comment(s)
- `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_extend_npu_graph_runner.py`: 1 inline comment(s)
- `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`: 1 inline comment(s)
- `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py`: 1 inline comment(s)
- `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`: 1 inline comment(s)
- `python/sglang/srt/speculative/eagle_worker_v2.py`: 1 inline comment(s)
- `python/sglang/srt/configs/model_config.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-12T08:56:17Z` `issue` by `xueliangyang-oeuler`; signals: attention, cache, register; excerpt: "export SGLANG ENABLE OVERLAP PLAN STREAM=1 export SGLANG ENABLE SPEC V2=1 --speculative-algorithm EAGLE3 --speculative-draft-model-path xxx/Qwen3-32B-Eagle3 --speculative-num-steps 1 --speculative-eagle-topk 1 --speculative-num-draft-tokens 2 Thank you, but ..." (https://github.com/sgl-project/sglang/pull/14820#issuecomment-3645549333)
- `2025-12-12T11:39:55Z` `issue` by `Liwansi`; signals: attention, cache, register; excerpt: "export SGLANG ENABLE OVERLAP PLAN STREAM=1 export SGLANG ENABLE SPEC V2=1 --speculative-algorithm EAGLE3 --speculative-draft-model-path xxx/Qwen3-32B-Eagle3 --speculative-num-steps 1 --speculative-eagle-topk 1 --speculative-num-draft-tokens 2 Thank you, but ..." (https://github.com/sgl-project/sglang/pull/14820#issuecomment-3646138103)
- `2025-12-11T13:08:35Z` `issue` by `xueliangyang-oeuler`; signals: perf, performance; excerpt: "@Liwansi Hi, could you write your start up parameters and hardware infos to one README？ I'm working on this pr to test some performance. ..." (https://github.com/sgl-project/sglang/pull/14820#issuecomment-3641849572)
- `2025-12-12T01:20:58Z` `issue` by `Liwansi`; signals: perf, performance; excerpt: "@Liwansi Hi, could you write your start up parameters and hardware infos to one README？ I'm working on this pr to test some performance. ..." (https://github.com/sgl-project/sglang/pull/14820#issuecomment-3644496062)
- `2025-12-11T03:06:02Z` `inline` by `iforgetmyname` `python/sglang/srt/speculative/eagle_draft_cuda_graph_runner.py`:138; signals: cuda; excerpt: "ditto" (https://github.com/sgl-project/sglang/pull/14820#discussion_r2608950115)
- `2025-12-11T03:06:15Z` `inline` by `iforgetmyname` `python/sglang/srt/speculative/eagle_draft_extend_cuda_graph_runner.py`:211; signals: cuda; excerpt: "ditto" (https://github.com/sgl-project/sglang/pull/14820#discussion_r2608950346)
- `2025-12-12T06:06:52Z` `inline` by `ping1jing2` `python/sglang/srt/hardware_backend/npu/attention/ascend_backend.py`:889; signals: attention; excerpt: "pls update related document docs\platforms\ascend npu qwen3 examples.md" (https://github.com/sgl-project/sglang/pull/14820#discussion_r2613042977)
- `2025-12-15T01:21:21Z` `inline` by `iforgetmyname` `python/sglang/srt/configs/model_config.py`:251; signals: general review; excerpt: "quantization = server args.speculative draft model quantization if is draft model else server args.quantization" (https://github.com/sgl-project/sglang/pull/14820#discussion_r2617685894)
- `2025-12-11T03:04:55Z` `inline` by `iforgetmyname` `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_extend_npu_graph_runner.py`:42; signals: general review; excerpt: "make this a public function that can be called outside" (https://github.com/sgl-project/sglang/pull/14820#discussion_r2608948657)
- `2025-12-11T03:05:34Z` `inline` by `iforgetmyname` `python/sglang/srt/hardware_backend/npu/graph_runner/eagle_draft_npu_graph_runner.py`:114; signals: general review; excerpt: "ditto" (https://github.com/sgl-project/sglang/pull/14820#discussion_r2608949580)
- `2025-12-11T03:11:19Z` `inline` by `iforgetmyname` `python/sglang/srt/speculative/eagle_worker_v2.py`:109; signals: general review; excerpt: "should rework this modification here can we read quant config from eagle model config files?" (https://github.com/sgl-project/sglang/pull/14820#discussion_r2608956611)
- `2025-12-11T03:15:19Z` `inline` by `iforgetmyname` `python/sglang/srt/speculative/eagle_info_v2.py`:529; signals: general review; excerpt: "remove this import as well, theoretically import once during startup should work" (https://github.com/sgl-project/sglang/pull/14820#discussion_r2608961685)
