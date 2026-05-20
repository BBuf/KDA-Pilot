# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13570](https://github.com/NVIDIA/TensorRT-LLM/pull/13570)
- Source page: `sources/prs/tensorrt-llm/PR-13570.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13570`
- Generated at: `2026-05-20T15:18:47.011459+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-28T17:50:09Z`
- Merged: `2026-05-12T04:58:16Z`

## Discussion Counts

- Issue comments: 69
- Review submissions: 25 (approved=3, commented=22)
- Inline review comments: 39
- Review threads observed: 18
- Resolved/outdated thread markers: resolved=18, outdated=8
- Human participants with discussion text: NVShreyas, PerkzZheng, chang-l, coderabbitai, tburt-nv, tensorrt-cicd, xrq-phys, yuxianq, zhenhuaw-me
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-28T18:05:39Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 10 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4191309221)
- `2026-04-29T03:38:49Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4193899879)
- `2026-04-29T03:39:25Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4193901089)
- `2026-04-29T03:40:58Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4193904830)
- `2026-04-29T03:41:34Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4193906508)
- `2026-04-29T16:42:24Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4198954884)
- `2026-04-29T16:43:00Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4198959509)
- `2026-04-29T17:24:57Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4199156090)
- `2026-04-29T18:07:21Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4199529464)
- `2026-04-29T18:18:04Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4199568642)
- `2026-04-29T22:55:53Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4201317249)
- `2026-04-29T22:59:14Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4201327794)
- `2026-04-30T16:26:07Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4206786978)
- `2026-04-30T17:47:26Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4207308226)
- `2026-04-30T17:55:14Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4207369219)
- `2026-05-01T04:25:05Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4209912580)
- `2026-05-01T04:25:25Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4209913360)
- `2026-05-01T04:28:42Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4209920076)
- `2026-05-01T04:29:46Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4209922145)
- `2026-05-01T07:29:34Z` `COMMENTED` by `xrq-phys` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4210422390)
- `2026-05-01T07:29:53Z` `COMMENTED` by `coderabbitai` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4210423462)
- `2026-05-11T03:16:45Z` `APPROVED` by `zhenhuaw-me` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4260555137)
- `2026-05-11T03:48:07Z` `APPROVED` by `yuxianq` - Attention part LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4260648383)
- `2026-05-11T20:26:14Z` `APPROVED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4267145019)
- ... 1 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `tests/unittest/_torch/visual_gen/test_attention_perf.py`: 8 inline comment(s)
- `tensorrt_llm/_torch/visual_gen/attention_backend/trtllm.py`: 6 inline comment(s)
- `examples/visual_gen/README.md`: 5 inline comment(s)
- `tensorrt_llm/_torch/visual_gen/config.py`: 5 inline comment(s)
- `tensorrt_llm/_torch/visual_gen/attention_backend/utils.py`: 3 inline comment(s)
- `tensorrt_llm/_torch/visual_gen/modules/attention.py`: 3 inline comment(s)
- `examples/visual_gen/visual_gen_wan_i2v.py`: 2 inline comment(s)
- `examples/visual_gen/visual_gen_wan_t2v.py`: 2 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/trtllm.py`: 2 inline comment(s)
- `examples/visual_gen/visual_gen_flux.py`: 2 inline comment(s)
- `tests/unittest/_torch/visual_gen/test_attention_integration.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-28T18:05:33Z` `issue` by `coderabbitai`; signals: attention, benchmark, block, hang, kernel, mla, perf, performance; excerpt: "📝 Walkthrough Walkthrough This pull request introduces SageAttention support to the visual generation pipeline. Changes include adding a new SageAttentionConfig schema, integrating it into ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#issuecomment-4337912349)
- `2026-04-29T18:13:09Z` `inline` by `xrq-phys` `tensorrt_llm/_torch/visual_gen/attention_backend/trtllm.py`:171; signals: attention, block, cache, kernel, kv cache, tensorrt; excerpt: "That's right. This looks like a verbose comment block dumped by CC 😆 I thinks we can simply rephrase it as: Handles: - Fused ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#discussion_r3163188585)
- `2026-04-28T18:05:39Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, hang, perf, pipeline, tensorrt; excerpt: "Actionable comments posted: 10 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#pullrequestreview-4191309221)
- `2026-05-01T04:29:46Z` `inline` by `coderabbitai` `tests/unittest/_torch/visual_gen/test_attention_perf.py`:1050; signals: attention, benchmark, kernel, perf, performance; excerpt: "@xrq-phys, great idea — using Pearson correlation between per-iteration timing series is a lightweight, zero-dependency heuristic: if both calls ran the same underlying kernel ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#discussion_r3172079748)
- `2026-04-28T18:05:36Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/visual_gen/attention_backend/trtllm.py`:270; signals: attention, benchmark, cute, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 1181 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#discussion_r3156245641)
- `2026-04-28T18:05:37Z` `inline` by `coderabbitai` `tests/unittest/_torch/visual_gen/test_attention_perf.py`:919; signals: attention, cute, perf, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 1293 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#discussion_r3156245672)
- `2026-04-28T18:05:37Z` `inline` by `coderabbitai` `tests/unittest/_torch/visual_gen/test_attention_perf.py`:1050; signals: attention, benchmark, cute, perf; excerpt: "⚠️ Potential issue 🟠 Major These tests don't currently prove that the SageAttention path actually executed. All of the new assertions are just “benchmark ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#discussion_r3156245676)
- `2026-04-29T18:17:51Z` `inline` by `xrq-phys` `tensorrt_llm/_torch/visual_gen/config.py`:86; signals: bf16, fp8, kernel, tensorrt; excerpt: "Not really. Currently (0,0,1) has no kernel support. BF16QK+FP8PV is not available yet. I'm planning to work on it as the next step." (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#discussion_r3163215129)
- `2026-05-01T04:28:42Z` `inline` by `xrq-phys` `tests/unittest/_torch/visual_gen/test_attention_perf.py`:1050; signals: attention, cute, hang, perf; excerpt: "@coderabbitai Un-resolving this. I just thought of one possible solution here: can we calculate covariance of trtllm vs sage time measurements? If covariance is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#discussion_r3172077883)
- `2026-04-28T18:05:37Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/visual_gen/modules/attention.py`:327; signals: attention, layout, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major seq len/seq len kv are wrong for HND layout after reshape. For HND ([B, H, S, D]), q.shape[1] is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#discussion_r3156245668)
- `2026-04-28T18:05:37Z` `inline` by `coderabbitai` `tests/unittest/_torch/visual_gen/test_attention_integration.py`:387; signals: attention, benchmark, oom; excerpt: "⚠️ Potential issue 🟠 Major SageAttention parametrization is too heavy for default unit-test execution. Lines [291]-[294] include very large sequence lengths, and this test ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#discussion_r3156245669)
- `2026-05-01T04:25:25Z` `inline` by `coderabbitai` `tests/unittest/_torch/visual_gen/test_attention_perf.py`:1050; signals: attention, perf, performance; excerpt: "@xrq-phys, understood — relying on perf numbers as a manual signal is a reasonable short-term approach for a performance-only test suite. Would you like ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13570#discussion_r3172071824)
