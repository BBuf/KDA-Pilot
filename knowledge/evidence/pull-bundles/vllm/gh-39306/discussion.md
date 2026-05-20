# PR Discussion Digest

- Source PR: [vllm-project/vllm#39306](https://github.com/vllm-project/vllm/pull/39306)
- Source page: `sources/prs/vllm/PR-39306.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-39306`
- Generated at: `2026-05-20T15:40:43.584131+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-08T14:21:21Z`
- Merged: `2026-05-10T02:57:10Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=3
- Human participants with discussion text: Etelis, ivanium, mergify, orozery
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-08T14:24:59Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the CUDA memory copy attributes in csrc/cache kernels.cu by changing the source ... (https://github.com/vllm-project/vllm/pull/39306#pullrequestreview-4075841260)
- `2026-04-20T16:22:00Z` `COMMENTED` by `orozery` (https://github.com/vllm-project/vllm/pull/39306#pullrequestreview-4141662159)
- `2026-04-23T06:35:28Z` `APPROVED` by `orozery` - Thanks @Etelis ! (https://github.com/vllm-project/vllm/pull/39306#pullrequestreview-4160186769)

## Inline Comment Hotspots

- `vllm/_custom_ops.py`: 2 inline comment(s)
- `csrc/cache_kernels.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-09T10:48:39Z` `issue` by `Etelis`; signals: benchmark, blackwell, block, cache, cuda, h200, hopper, kernel; excerpt: "Thanks for the work. Can you add some benchmark results? NVIDIA GH200 480GB (Grace Hopper, NVLink-C2C, sm 90) Driver: 580.105.08, CUDA Toolkit 12.8 Built ..." (https://github.com/vllm-project/vllm/pull/39306#issuecomment-4213550458)
- `2026-04-20T16:18:18Z` `inline` by `orozery` `csrc/cache_kernels.cu`:131; signals: cache, kernel; excerpt: "The rest is specific to the offloading connector implementation." (https://github.com/vllm-project/vllm/pull/39306#discussion_r3112099380)
- `2026-04-09T12:56:30Z` `issue` by `Etelis`; signals: block, cuda; excerpt: "The only place we're using swap blocks batch today is in the cpu gpu.py where we already have stream.wait event(last event) in place (for ..." (https://github.com/vllm-project/vllm/pull/39306#issuecomment-4214382054)
- `2026-04-20T14:36:01Z` `issue` by `Etelis`; signals: cache, kv cache; excerpt: "@orozery you were right, thanks for the pushback. The subtlety is that CU MEMCPY SRC ACCESS ORDER ANY only relaxes the source-read ordering — ..." (https://github.com/vllm-project/vllm/pull/39306#issuecomment-4281733739)
- `2026-04-29T06:22:48Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @Etelis, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/39306#issuecomment-4341387590)
- `2026-05-04T05:38:14Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @Etelis, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/39306#issuecomment-4368567719)
- `2026-04-09T11:27:06Z` `issue` by `Etelis`; signals: block; excerpt: "@Etelis I think we want to make this a parameter. For GPU- CPU I believe we still want stream order. The only place we're ..." (https://github.com/vllm-project/vllm/pull/39306#issuecomment-4213786202)
- `2026-04-09T12:12:17Z` `issue` by `orozery`; signals: block; excerpt: "The only place we're using swap blocks batch today is in the cpu gpu.py where we already have stream.wait event(last event) in place (for ..." (https://github.com/vllm-project/vllm/pull/39306#issuecomment-4214104070)
- `2026-04-09T17:06:01Z` `issue` by `Etelis`; signals: block; excerpt: "What is it reads at call time, and writes at "stream time"? I think this is the difference between STREAM and ANY. Both guarantee ..." (https://github.com/vllm-project/vllm/pull/39306#issuecomment-4216058766)
- `2026-04-08T18:06:22Z` `issue` by `ivanium`; signals: benchmark; excerpt: "Thanks for the work. Can you add some benchmark results?" (https://github.com/vllm-project/vllm/pull/39306#issuecomment-4208405838)
- `2026-04-20T16:19:36Z` `inline` by `orozery` `vllm/_custom_ops.py`:2799; signals: general review; excerpt: "the e.g. part is specific to the offloading connector implementation. Let's remove it." (https://github.com/vllm-project/vllm/pull/39306#discussion_r3112108104)
- `2026-04-20T16:21:06Z` `inline` by `orozery` `vllm/_custom_ops.py`:2803; signals: general review; excerpt: "src access order any is a big confusing. Maybe rename it to is src access order any?" (https://github.com/vllm-project/vllm/pull/39306#discussion_r3112119547)
