# PR Discussion Digest

- Source PR: [vllm-project/vllm#26098](https://github.com/vllm-project/vllm/pull/26098)
- Source page: `sources/prs/vllm/PR-26098.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-26098`
- Generated at: `2026-05-20T15:38:03.873710+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-02T14:31:15Z`
- Merged: `2025-10-03T15:48:33Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 13 (approved=1, commented=12)
- Inline review comments: 13
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: ProExpertProg, jasl, johnnynunez
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-02T14:33:37Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to fix a build issue for new hardware by enabling compilation of ... (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3294948648)
- `2025-10-02T18:54:41Z` `COMMENTED` by `ProExpertProg` - I do actually have a question about the fix (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3295983028)
- `2025-10-02T18:55:40Z` `COMMENTED` by `jasl` (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3296002667)
- `2025-10-02T19:05:33Z` `COMMENTED` by `johnnynunez` (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3296037493)
- `2025-10-02T19:06:37Z` `COMMENTED` by `johnnynunez` (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3296040398)
- `2025-10-02T19:26:08Z` `COMMENTED` by `jasl` (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3296102334)
- `2025-10-02T20:15:17Z` `COMMENTED` by `johnnynunez` (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3296242402)
- `2025-10-02T20:24:43Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3296277623)
- `2025-10-02T21:11:33Z` `COMMENTED` by `johnnynunez` (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3296413194)
- `2025-10-02T21:27:09Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3296466185)
- `2025-10-02T21:28:07Z` `COMMENTED` by `jasl` (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3296469753)
- `2025-10-02T21:39:38Z` `COMMENTED` by `jasl` (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3296514700)
- `2025-10-03T13:22:44Z` `APPROVED` by `ProExpertProg` - LGTM (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3298955185)

## Inline Comment Hotspots

- `vllm/utils/__init__.py`: 12 inline comment(s)
- `csrc/quantization/cutlass_w8a8/scaled_mm_entry.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-02T19:05:33Z` `inline` by `johnnynunez` `vllm/utils/__init__.py`:2777; signals: cache, cuda, hang, kernel, memory; excerpt: "@ProExpertProg Just to clarify: the problem shows up on unified-memory devices (UMA/iGPU) because cuMemGetInfo and other calls like this returning the kernel’s MemFree value, ..." (https://github.com/vllm-project/vllm/pull/26098#discussion_r2399815626)
- `2025-10-02T21:12:30Z` `issue` by `jasl`; signals: compile, hang, kernel, sm100; excerpt: "@jasl that fixes the issue for pre-10.0 platforms that don't support the function and adds a dummy implementation that just throws an error. You ..." (https://github.com/vllm-project/vllm/pull/26098#issuecomment-3363073589)
- `2025-10-02T21:11:33Z` `inline` by `johnnynunez` `vllm/utils/__init__.py`:2777; signals: cuda, memory; excerpt: "yes @ProExpertProg On Orin, Thor and Spark platforms, where both CPU and GPU rely on system memory, the cudaMemGetInfo function shows the amount of ..." (https://github.com/vllm-project/vllm/pull/26098#discussion_r2400074552)
- `2025-10-02T18:54:30Z` `inline` by `ProExpertProg` `vllm/utils/__init__.py`:2777; signals: memory; excerpt: "How is virtual memory helpful here? Isn;t that referring to CPU virtual memory - what does that have to do with free device (GPU) ..." (https://github.com/vllm-project/vllm/pull/26098#discussion_r2399786195)
- `2025-10-02T20:15:17Z` `inline` by `johnnynunez` `vllm/utils/__init__.py`:2777; signals: compile; excerpt: "Yes. Because now i don’t have one, and i have to compile vllm for take one" (https://github.com/vllm-project/vllm/pull/26098#discussion_r2399955644)
- `2025-10-02T18:45:49Z` `issue` by `jasl`; signals: memory; excerpt: "OK, so I will test it later, and make a pure patch for the memory issue @ProExpertProg is the memory fix commit look good ..." (https://github.com/vllm-project/vllm/pull/26098#issuecomment-3362516928)
- `2025-10-02T18:54:41Z` `review` `COMMENTED` by `ProExpertProg`; signals: general review; excerpt: "I do actually have a question about the fix" (https://github.com/vllm-project/vllm/pull/26098#pullrequestreview-3295983028)
- `2025-10-02T20:24:43Z` `inline` by `ProExpertProg` `vllm/utils/__init__.py`:2777; signals: general review; excerpt: "Okay, thanks for the explanation. Could you add a bit more of this info (can be condensed) as a comment?" (https://github.com/vllm-project/vllm/pull/26098#discussion_r2399979852)
- `2025-10-02T18:55:40Z` `inline` by `jasl` `vllm/utils/__init__.py`:2777; signals: general review; excerpt: "@johnnynunez" (https://github.com/vllm-project/vllm/pull/26098#discussion_r2399791772)
- `2025-10-02T19:06:36Z` `inline` by `johnnynunez` `vllm/utils/__init__.py`:2777; signals: general review; excerpt: "@jasl do you have an image? that i am saying?" (https://github.com/vllm-project/vllm/pull/26098#discussion_r2399817722)
- `2025-10-02T19:26:08Z` `inline` by `jasl` `vllm/utils/__init__.py`:2777; signals: general review; excerpt: "You mean a screenshot? I can give you one" (https://github.com/vllm-project/vllm/pull/26098#discussion_r2399859740)
- `2025-10-02T21:27:09Z` `inline` by `ProExpertProg` `vllm/utils/__init__.py`:2777; signals: general review; excerpt: "Yep that sounds good, can you add that as a comment in the code?" (https://github.com/vllm-project/vllm/pull/26098#discussion_r2400110697)
