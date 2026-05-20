# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13873](https://github.com/NVIDIA/TensorRT-LLM/pull/13873)
- Source page: `sources/prs/tensorrt-llm/PR-13873.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13873`
- Generated at: `2026-05-20T15:18:55.996369+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-08T00:33:40Z`
- Merged: `2026-05-14T01:36:13Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 21 (approved=4, commented=17)
- Inline review comments: 23
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=2
- Human participants with discussion text: LarryXFly, NVShreyas, chang-l, coderabbitai, ruodil, tensorrt-cicd, yibinl-nvidia, zhenhuaw-me
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-08T00:34:20Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4248571083)
- `2026-05-08T00:45:00Z` `COMMENTED` by `coderabbitai` - [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4248616589)
- `2026-05-08T03:25:39Z` `COMMENTED` by `yibinl-nvidia` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4249285688)
- `2026-05-08T05:29:00Z` `APPROVED` by `zhenhuaw-me` - LGTM in general. (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4249707083)
- `2026-05-08T09:13:57Z` `COMMENTED` by `zhenhuaw-me` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4251027773)
- `2026-05-08T15:45:51Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4253458571)
- `2026-05-08T16:41:09Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4253777213)
- `2026-05-08T16:41:25Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4253778995)
- `2026-05-12T06:06:15Z` `COMMENTED` by `chang-l` - Retracted — re-posting as a pending review for staging. Please disregard. (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4269543515)
- `2026-05-12T06:31:53Z` `COMMENTED` by `chang-l` - Do we have any e2e tests or pipeline tests with this feature, i.e.,world size parallel vae size? (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4269573705)
- `2026-05-12T17:52:44Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4274859425)
- `2026-05-12T17:52:49Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4274860060)
- `2026-05-12T17:53:43Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4274867259)
- `2026-05-12T17:53:48Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4274867781)
- `2026-05-12T17:53:54Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4274868504)
- `2026-05-12T17:53:59Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4274868922)
- `2026-05-12T22:52:57Z` `APPROVED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4276799617)
- `2026-05-12T22:54:23Z` `COMMENTED` by `chang-l` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4276816371)
- `2026-05-12T23:18:10Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4276908316)
- `2026-05-14T01:28:54Z` `APPROVED` by `LarryXFly` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4286595488)
- `2026-05-14T01:29:36Z` `APPROVED` by `ruodil` (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4286597785)

## Inline Comment Hotspots

- `tests/integration/defs/perf/visual_gen_perf_utils.py`: 5 inline comment(s)
- `tensorrt_llm/_torch/visual_gen/pipeline.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/visual_gen/mapping.py`: 4 inline comment(s)
- `examples/visual_gen/configs/wan2.2-t2v-fp8-8gpu.yaml`: 4 inline comment(s)
- `tensorrt_llm/_torch/visual_gen/config.py`: 2 inline comment(s)
- `examples/visual_gen/visual_gen_wan_t2v.py`: 2 inline comment(s)
- `tests/unittest/_torch/visual_gen/multi_gpu/test_wan_pipeline_parallel.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-08T00:45:00Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, blackwell, block, fp4, fp8, hang, perf, pipeline; excerpt: "[!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range comments (4) tensorrt llm/ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#pullrequestreview-4248616589)
- `2026-05-08T00:44:56Z` `issue` by `coderabbitai`; signals: attention, block, compile, cuda, hang, perf, performance, pipeline; excerpt: "[ , the mapping layer computes VAE ranks and process groups from the size, attention modules accept optional process groups, and the pipeline uses ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#issuecomment-4402250048)
- `2026-05-12T06:12:15Z` `inline` by `chang-l` `tensorrt_llm/_torch/visual_gen/pipeline.py`:637; signals: hang, perf, pipeline, tensorrt; excerpt: "The new docstring says "only ranks in the VAE process group perform decoding; non-participating ranks return None placeholders" — but the body wasn't updated. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#discussion_r3224093861)
- `2026-05-12T23:18:10Z` `inline` by `NVShreyas` `examples/visual_gen/configs/wan2.2-t2v-fp8-8gpu.yaml`:26; signals: b200, fp8, latency; excerpt: "Yes, it helps the most when cfg=2, ulysses=4. In very early tests, it brought down latency by 7.65% on 8 gpus. I'm curious to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#discussion_r3230427337)
- `2026-05-08T00:34:20Z` `inline` by `NVShreyas` `tests/integration/defs/perf/visual_gen_perf_utils.py`:180; signals: hang, perf; excerpt: "@zhenhuaw-me please review this and let me know if we wanna keep backward compat or if I need to change anything else." (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#discussion_r3205474521)
- `2026-05-08T03:25:39Z` `inline` by `yibinl-nvidia` `tensorrt_llm/_torch/visual_gen/pipeline.py`:485; signals: pipeline, tensorrt; excerpt: "This early return could violate the PyTorch new group enter this function, even if they are not going to be members of the group. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#discussion_r3206076039)
- `2026-05-08T09:13:50Z` `inline` by `zhenhuaw-me` `tests/integration/defs/perf/visual_gen_perf_utils.py`:180; signals: hang, perf; excerpt: "@NVShreyas we may need to change this to something like b parallel vae size since these are part of the matching keys." (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#discussion_r3207642180)
- `2026-05-08T16:41:09Z` `inline` by `NVShreyas` `tensorrt_llm/_torch/visual_gen/pipeline.py`:485; signals: pipeline, tensorrt; excerpt: "thanks, good point! I have moved vae adj group creation to mapping so every rank calls it but is only used by VAE ranks." (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#discussion_r3210036978)
- `2026-05-12T06:12:15Z` `inline` by `chang-l` `tensorrt_llm/_torch/visual_gen/mapping.py`:124; signals: hang, tensorrt; excerpt: "vae ranks is computed without reference to the DiT mesh. Today, with the default dit dim order, the first parallel vae size ranks happen ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#discussion_r3224093866)
- `2026-05-12T06:12:15Z` `inline` by `chang-l` `tensorrt_llm/_torch/visual_gen/config.py`:99; signals: block, tensorrt; excerpt: "Minor: ge=1 plus parallel vae size <= world size in VisualGenMapping cover the basics, but a couple of mismatches will still fail late, deep ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#discussion_r3224093874)
- `2026-05-12T06:12:15Z` `inline` by `chang-l` `tensorrt_llm/_torch/visual_gen/mapping.py`:253; signals: deadlock, tensorrt; excerpt: "One-line comment would help future readers: use local synchronization=False because PyTorch requires every rank to participate in new group, otherwise non-VAE ranks deadlock on ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#discussion_r3224093876)
- `2026-05-12T17:52:44Z` `inline` by `NVShreyas` `tensorrt_llm/_torch/visual_gen/pipeline.py`:637; signals: pipeline, tensorrt; excerpt: "good point. I have made self. parallel vae enabled a global flag for all ranks so that all ranks know which ranks should participate ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13873#discussion_r3228626808)
