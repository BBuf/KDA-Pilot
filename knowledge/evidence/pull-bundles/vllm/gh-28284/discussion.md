# PR Discussion Digest

- Source PR: [vllm-project/vllm#28284](https://github.com/vllm-project/vllm/pull/28284)
- Source page: `sources/prs/vllm/PR-28284.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28284`
- Generated at: `2026-05-20T15:38:27.934046+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-07T09:46:12Z`
- Merged: `2026-01-12T14:23:04Z`

## Discussion Counts

- Issue comments: 68
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 26
- Review threads observed: 25
- Resolved/outdated thread markers: resolved=14, outdated=17
- Human participants with discussion text: 22quinn, ForeverDJ-ux, Kairosxy, QPHutu, ann-qin-lu, awcvec, chatgpt-codex-connector, cursor, david6666666, faresobeid, gxm651182644, heheda12345, linlinlinzhao, litianjian, lkm2835, mergify, mzusman, robertgshaw2-redhat, scut-zx, shenh10
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-11-07T09:49:14Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for recording expert routing decisions for MoE models, a feature named ... (https://github.com/vllm-project/vllm/pull/28284#pullrequestreview-3432649782)
- `2025-12-16T11:09:49Z` `COMMENTED` by `sungyubkim` - First of all, thanks for this great feature! Really appreciate the work here. 🙏 I have a small ... (https://github.com/vllm-project/vllm/pull/28284#pullrequestreview-3582528903)
- `2025-12-30T11:28:23Z` `COMMENTED` by `gxm651182644` (https://github.com/vllm-project/vllm/pull/28284#pullrequestreview-3617949025)
- `2025-12-30T11:30:01Z` `COMMENTED` by `gxm651182644` (https://github.com/vllm-project/vllm/pull/28284#pullrequestreview-3617951612)
- `2026-01-08T14:16:28Z` `APPROVED` by `22quinn` - thanks for the work! just some nits (https://github.com/vllm-project/vllm/pull/28284#pullrequestreview-3639520509)
- `2026-01-09T02:05:33Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/28284#pullrequestreview-3642062482)
- `2026-01-09T02:41:10Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/28284#pullrequestreview-3642109210)
- `2026-01-10T10:15:15Z` `COMMENTED` by `xhx1022` (https://github.com/vllm-project/vllm/pull/28284#pullrequestreview-3646685180)
- `2026-01-12T06:29:57Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/28284#pullrequestreview-3649320279)
- `2026-01-12T11:36:32Z` `COMMENTED` by `cursor` (https://github.com/vllm-project/vllm/pull/28284#pullrequestreview-3650353551)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`: 11 inline comment(s)
- `vllm/v1/core/sched/scheduler.py`: 5 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 3 inline comment(s)
- `vllm/v1/worker/gpu_model_runner.py`: 3 inline comment(s)
- `vllm/config/model.py`: 2 inline comment(s)
- `vllm/engine/arg_utils.py`: 1 inline comment(s)
- `vllm/config/vllm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-09T02:41:10Z` `inline` by `cursor` `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`:203; signals: block, latency, memory, moe, perf, performance, regression, shared memory; excerpt: "Performance regression with expert recording enabled High Severity As reported in the PR discussion, enabling enable return routed experts causes a 10x latency increase. ..." (https://github.com/vllm-project/vllm/pull/28284#discussion_r2674603949)
- `2026-01-09T02:05:34Z` `inline` by `cursor` `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`:300; signals: cache, kv cache, memory, moe, race, shared memory; excerpt: "Race Condition: Reader Tries to Attach Before Shared Memory Exists High Severity The RoutedExpertsReaderReal.attach buffer() method opens the lock file with mode "rb+" (read+write, ..." (https://github.com/vllm-project/vllm/pull/28284#discussion_r2674553875)
- `2026-01-09T02:05:33Z` `inline` by `cursor` `vllm/v1/worker/gpu_model_runner.py`:3503; signals: attention, block, cache, kv cache; excerpt: "Uninitialized self.slot mapping Attribute May Cause AttributeError High Severity self.slot mapping is only conditionally set in get block table and slot mapping() (line 1617-1618) ..." (https://github.com/vllm-project/vllm/pull/28284#discussion_r2674553873)
- `2026-01-09T02:05:34Z` `inline` by `cursor` `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`:212; signals: memory, moe, shared memory; excerpt: "Lock File Resource Leak - Never Cleaned Up Low Severity The RoutedExpertsCapturerReal class creates a lock file at {LOCK FILE PREFIX} {instance id}.lock (line ..." (https://github.com/vllm-project/vllm/pull/28284#discussion_r2674553878)
- `2026-01-09T02:41:10Z` `inline` by `cursor` `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`:201; signals: memory, moe, shared memory; excerpt: "No bounds checking for shared memory indices Medium Severity In save captured experts, the code writes to shared memory using self. host buffer view[indices, ..." (https://github.com/vllm-project/vllm/pull/28284#discussion_r2674603948)
- `2026-01-09T02:41:10Z` `inline` by `cursor` `vllm/v1/core/sched/scheduler.py`:1209; signals: block, memory, shared memory; excerpt: "Slot mapping calculation mismatch with context parallelism High Severity The scheduler computes slot mapping using a simple formula: slot = block id block size ..." (https://github.com/vllm-project/vllm/pull/28284#discussion_r2674603956)
- `2026-01-12T06:29:57Z` `inline` by `cursor` `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`:102; signals: memory, moe, shared memory; excerpt: "Singleton pattern prevents engine reinitialization Medium Severity The RoutedExpertsCapturer.create() and RoutedExpertsReader.create() methods raise RuntimeError if the global singleton already exists, but there's no mechanism ..." (https://github.com/vllm-project/vllm/pull/28284#discussion_r2681011878)
- `2025-12-16T11:09:49Z` `review` `COMMENTED` by `sungyubkim`; signals: dtype, hang; excerpt: "First of all, thanks for this great feature! Really appreciate the work here. 🙏 I have a small suggestion regarding dtype compatibility. The current ..." (https://github.com/vllm-project/vllm/pull/28284#pullrequestreview-3582528903)
- `2025-12-14T13:09:54Z` `issue` by `awcvec`; signals: attention, cache, kv cache; excerpt: "It looks like the current implementation only supports a single KV cache group (len(self.kv cache config.kv cache groups) == 1). Does it also support ..." (https://github.com/vllm-project/vllm/pull/28284#issuecomment-3650963577)
- `2025-12-16T02:10:37Z` `issue` by `xhx1022`; signals: attention, cache, kv cache; excerpt: "It looks like the current implementation only supports a single KV cache group (len(self.kv cache config.kv cache groups) == 1). Does it also support ..." (https://github.com/vllm-project/vllm/pull/28284#issuecomment-3658396430)
- `2025-12-16T04:33:39Z` `issue` by `lkm2835`; signals: attention, cache, kv cache; excerpt: "It looks like the current implementation only supports a single KV cache group (len(self.kv cache config.kv cache groups) == 1). Does it also support ..." (https://github.com/vllm-project/vllm/pull/28284#issuecomment-3658759469)
- `2025-12-16T08:35:31Z` `issue` by `xhx1022`; signals: attention, cache, kv cache; excerpt: "It looks like the current implementation only supports a single KV cache group (len(self.kv cache config.kv cache groups) == 1). Does it also support ..." (https://github.com/vllm-project/vllm/pull/28284#issuecomment-3659394912)
