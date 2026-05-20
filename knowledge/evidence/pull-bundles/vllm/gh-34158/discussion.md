# PR Discussion Digest

- Source PR: [vllm-project/vllm#34158](https://github.com/vllm-project/vllm/pull/34158)
- Source page: `sources/prs/vllm/PR-34158.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-34158`
- Generated at: `2026-05-20T15:39:45.108350+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-09T18:02:59Z`
- Merged: `2026-03-16T15:20:51Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: Etelis, mergify, mgoin, pavanimajety, vadiklyutiy
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-02-09T18:04:33Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request relaxes the contiguity assertion for the TRTLLM KV cache to allow its use ... (https://github.com/vllm-project/vllm/pull/34158#pullrequestreview-3774608600)
- `2026-03-09T14:48:22Z` `COMMENTED` by `mgoin` - This seems reasonable to me given your investigation cc @vadiklyutiy @pavanimajety to confirm (https://github.com/vllm-project/vllm/pull/34158#pullrequestreview-3915966095)
- `2026-03-10T20:34:13Z` `COMMENTED` by `Etelis` (https://github.com/vllm-project/vllm/pull/34158#pullrequestreview-3925255776)
- `2026-03-13T19:15:01Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/34158#pullrequestreview-3946421498)
- `2026-03-13T19:17:10Z` `COMMENTED` by `Etelis` (https://github.com/vllm-project/vllm/pull/34158#pullrequestreview-3946436483)
- `2026-03-13T21:04:00Z` `APPROVED` by `pavanimajety` - Thanks @Etelis! (https://github.com/vllm-project/vllm/pull/34158#pullrequestreview-3946940870)
- `2026-03-16T14:14:03Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/34158#pullrequestreview-3954168481)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/flashinfer.py`: 5 inline comment(s)

## High-Signal Discussion

- `2026-03-13T19:15:01Z` `inline` by `pavanimajety` `vllm/v1/attention/backends/flashinfer.py`:1565; signals: attention, flashinfer, hang, tma; excerpt: "I think we shouldn't completely remove the check. The issue wasn't that TRTLLM can't process strides, it was that the strides were wrong (caused ..." (https://github.com/vllm-project/vllm/pull/34158#discussion_r2933288291)
- `2026-03-13T19:17:10Z` `inline` by `Etelis` `vllm/v1/attention/backends/flashinfer.py`:1565; signals: attention, flashinfer, layout; excerpt: "Thanks @pavanimajety. Reviewed 36867 — looks good to me, agree with keeping the minimal stride check there. For the decode path here, good point ..." (https://github.com/vllm-project/vllm/pull/34158#discussion_r2933298681)
- `2026-03-09T14:47:43Z` `inline` by `mgoin` `vllm/v1/attention/backends/flashinfer.py`:577; signals: attention, flashinfer; excerpt: "@Etelis this seems like a real bug" (https://github.com/vllm-project/vllm/pull/34158#discussion_r2905926272)
- `2026-03-10T20:34:13Z` `inline` by `Etelis` `vllm/v1/attention/backends/flashinfer.py`:577; signals: attention, flashinfer; excerpt: "@mgoin Done, thanks." (https://github.com/vllm-project/vllm/pull/34158#discussion_r2914313689)
- `2026-03-12T08:01:49Z` `issue` by `vadiklyutiy`; signals: flashinfer, kernel; excerpt: "I introduced is strictly contiguous check in 32008 and 32417. There was a problem in degenerate strides 4608 != 32 128 So, the quote ..." (https://github.com/vllm-project/vllm/pull/34158#issuecomment-4044753769)
- `2026-03-12T09:17:18Z` `issue` by `vadiklyutiy`; signals: cache, fp8; excerpt: "I did dig/think a bit more about the topic. Fully disabling TRTLLM attn when using kv-cache offloading (implemented in 33192) is really expensive workaround ..." (https://github.com/vllm-project/vllm/pull/34158#issuecomment-4045166291)
- `2026-03-12T10:09:28Z` `issue` by `vadiklyutiy`; signals: cache, fp8; excerpt: "I did dig/think a bit more about the topic. Fully disabling TRTLLM attn when using kv-cache offloading (implemented in 33192) is really expensive workaround ..." (https://github.com/vllm-project/vllm/pull/34158#issuecomment-4045491247)
- `2026-03-09T14:48:22Z` `review` `COMMENTED` by `mgoin`; signals: general review; excerpt: "This seems reasonable to me given your investigation cc @vadiklyutiy @pavanimajety to confirm" (https://github.com/vllm-project/vllm/pull/34158#pullrequestreview-3915966095)
- `2026-03-13T19:20:34Z` `issue` by `Etelis`; signals: kernel; excerpt: "Thanks @vadiklyutiy — your analysis of the degenerate stride issue and the kernel fix in 36867 are great. I've updated this PR to use ..." (https://github.com/vllm-project/vllm/pull/34158#issuecomment-4057441579)
- `2026-03-10T20:36:53Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @Etelis." (https://github.com/vllm-project/vllm/pull/34158#issuecomment-4034313622)
- `2026-03-13T19:04:34Z` `issue` by `pavanimajety`; signals: general review; excerpt: "@Etelis Just FYI on what happens if the strides are not canonical I vote to keep the stride check like Vadim has in 36867" (https://github.com/vllm-project/vllm/pull/34158#issuecomment-4057359068)
