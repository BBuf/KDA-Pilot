# PR Discussion Digest

- Source PR: [vllm-project/vllm#17004](https://github.com/vllm-project/vllm/pull/17004)
- Source page: `sources/prs/vllm/PR-17004.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-17004`
- Generated at: `2026-05-20T15:35:04.451658+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-22T20:13:45Z`
- Merged: `2025-05-21T15:35:00Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 8 (approved=3, commented=5)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: DarkLight1337, SageMoore, gshtras, hyoon1, liangshen68, mergify, robertgshaw2-redhat, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-02T13:16:59Z` `COMMENTED` by `SageMoore` - I didn't go through the kernel line by line but the dispatching logic looks reasonable. I think we ... (https://github.com/vllm-project/vllm/pull/17004#pullrequestreview-2811960346)
- `2025-05-02T16:31:20Z` `COMMENTED` by `hyoon1` (https://github.com/vllm-project/vllm/pull/17004#pullrequestreview-2812440012)
- `2025-05-02T16:31:40Z` `COMMENTED` by `hyoon1` (https://github.com/vllm-project/vllm/pull/17004#pullrequestreview-2812440579)
- `2025-05-05T18:04:51Z` `COMMENTED` by `gshtras` (https://github.com/vllm-project/vllm/pull/17004#pullrequestreview-2815649945)
- `2025-05-05T19:50:43Z` `COMMENTED` by `hyoon1` (https://github.com/vllm-project/vllm/pull/17004#pullrequestreview-2815928838)
- `2025-05-06T13:10:38Z` `APPROVED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/17004#pullrequestreview-2818227273)
- `2025-05-06T17:05:10Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/17004#pullrequestreview-2819042273)
- `2025-05-21T15:25:52Z` `APPROVED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/17004#pullrequestreview-2858201378)

## Inline Comment Hotspots

- `vllm/_custom_ops.py`: 4 inline comment(s)
- `csrc/rocm/attention.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2025-05-20T14:18:16Z` `issue` by `tjtanaa`; signals: attention, hang, regression; excerpt: "@hyoon1 Has this been evaluated on server gpus e.g. mi300x to ensure there is no regression? The line changes to the code of attention.cu ..." (https://github.com/vllm-project/vllm/pull/17004#issuecomment-2894608795)
- `2025-05-02T13:16:59Z` `review` `COMMENTED` by `SageMoore`; signals: kernel; excerpt: "I didn't go through the kernel line by line but the dispatching logic looks reasonable. I think we can clean it up a bit, ..." (https://github.com/vllm-project/vllm/pull/17004#pullrequestreview-2811960346)
- `2025-05-05T19:50:42Z` `inline` by `hyoon1` `csrc/rocm/attention.cu`:3492; signals: attention, cache; excerpt: "Agreed, I updated to cache the result so that hipGetDeviceProperties is called once." (https://github.com/vllm-project/vllm/pull/17004#discussion_r2074094341)
- `2025-04-29T19:21:36Z` `issue` by `liangshen68`; signals: perf, performance; excerpt: "@tlrmchlsmth and @WoosukKwon, really appreciate if you could help to review and approve this PR so that vLLM V1 could work out-of-box with optimized ..." (https://github.com/vllm-project/vllm/pull/17004#issuecomment-2839983446)
- `2025-05-02T16:30:49Z` `issue` by `hyoon1`; signals: hang, kernel; excerpt: "I didn't go through the kernel line by line but the dispatching logic looks reasonable. I think we can clean it up a bit, ..." (https://github.com/vllm-project/vllm/pull/17004#issuecomment-2847638523)
- `2025-05-20T20:15:44Z` `issue` by `hyoon1`; signals: hang, regression; excerpt: "Has this been evaluated on server gpus e.g. mi300x to ensure there is no regression? Hi @tjtanaa Unfortunately, I don't have access to a ..." (https://github.com/vllm-project/vllm/pull/17004#issuecomment-2895722221)
- `2025-05-02T13:16:07Z` `inline` by `SageMoore` `vllm/_custom_ops.py`:140; signals: kernel; excerpt: "Can we determine if we are running on navi hardware inside of the kernel? Looking at the archname in the kernel dispatching function seems ..." (https://github.com/vllm-project/vllm/pull/17004#discussion_r2071597571)
- `2025-05-21T15:27:59Z` `issue` by `tjtanaa`; signals: bf16, regression; excerpt: "@hyoon1 I have helped validated on MI300X with model Mixtral Tp1 BF16 and I see no regression." (https://github.com/vllm-project/vllm/pull/17004#issuecomment-2898379007)
- `2025-05-05T18:04:51Z` `inline` by `gshtras` `csrc/rocm/attention.cu`:3492; signals: attention; excerpt: "Probably an overkill to call this each time attention is called" (https://github.com/vllm-project/vllm/pull/17004#discussion_r2073927346)
- `2025-04-28T14:49:30Z` `issue` by `hyoon1`; signals: attention; excerpt: "Hi @tlrmchlsmth @ProExpertProg @robertgshaw2-redhat I've added a v1 custom paged attention support for AMD Radeon GPUs based on This basically follows the custom paged ..." (https://github.com/vllm-project/vllm/pull/17004#issuecomment-2835510946)
- `2025-05-02T13:03:33Z` `inline` by `SageMoore` `vllm/_custom_ops.py`:120; signals: general review; excerpt: "Nit: Can you delete this argument. It looks like its unused." (https://github.com/vllm-project/vllm/pull/17004#discussion_r2071582348)
- `2025-05-02T16:31:20Z` `inline` by `hyoon1` `vllm/_custom_ops.py`:120; signals: general review; excerpt: "updated" (https://github.com/vllm-project/vllm/pull/17004#discussion_r2071866261)
