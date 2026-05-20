# PR Discussion Digest

- Source PR: [vllm-project/vllm#34758](https://github.com/vllm-project/vllm/pull/34758)
- Source page: `sources/prs/vllm/PR-34758.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-34758`
- Generated at: `2026-05-20T15:39:55.004509+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-17T23:16:34Z`
- Merged: `2026-02-18T15:42:37Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=4
- Human participants with discussion text: SurealCereal, eugr, mgoin, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2026-02-17T23:18:57Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a highly optimized fused GEMM kernel for DeepSeek V2/V3 models on Hopper ... (https://github.com/vllm-project/vllm/pull/34758#pullrequestreview-3816800713)
- `2026-02-18T01:23:45Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/34758#pullrequestreview-3817140842)
- `2026-02-18T02:27:26Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/34758#pullrequestreview-3817337906)
- `2026-02-18T03:02:52Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/34758#pullrequestreview-3817446839)
- `2026-02-18T03:03:45Z` `APPROVED` by `mgoin` - LGTM just need to fix sm120 restriction (https://github.com/vllm-project/vllm/pull/34758#pullrequestreview-3817449834)

## Inline Comment Hotspots

- `vllm/model_executor/models/deepseek_v2.py`: 4 inline comment(s)
- `csrc/gemm/dsv3_fused_a_gemm.cu`: 1 inline comment(s)
- `CMakeLists.txt`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-18T01:22:59Z` `inline` by `mgoin` `CMakeLists.txt`:779; signals: gemm, hopper, kernel, sm100, sm90; excerpt: "Is this kernel Hopper only or SM90? You need to update this like the router gemm if so to include sm100f" (https://github.com/vllm-project/vllm/pull/34758#discussion_r2819853982)
- `2026-02-18T01:22:20Z` `inline` by `mgoin` `vllm/model_executor/models/deepseek_v2.py`:738; signals: kernel; excerpt: "should be is device capability? unless you update the kernel to build for more SMs" (https://github.com/vllm-project/vllm/pull/34758#discussion_r2819852474)
- `2026-02-18T03:02:52Z` `inline` by `mgoin` `vllm/model_executor/models/deepseek_v2.py`:738; signals: sm120; excerpt: "We still need to restrict so sm120 isn't valid" (https://github.com/vllm-project/vllm/pull/34758#discussion_r2820108068)
- `2026-02-18T01:20:54Z` `inline` by `mgoin` `vllm/model_executor/models/deepseek_v2.py`:822; signals: general review; excerpt: "as spoke offline, DeepSeekV2FusedQkvAProjWithMqa should probably be on self.fused qkv a proj instead you need to fuse these two to get 2112" (https://github.com/vllm-project/vllm/pull/34758#discussion_r2819849346)
- `2026-02-18T03:03:45Z` `review` `APPROVED` by `mgoin`; signals: sm120; excerpt: "LGTM just need to fix sm120 restriction" (https://github.com/vllm-project/vllm/pull/34758#pullrequestreview-3817449834)
- `2026-02-18T02:27:25Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/models/deepseek_v2.py`:738; signals: general review; excerpt: "updated" (https://github.com/vllm-project/vllm/pull/34758#discussion_r2820010248)
