# PR Discussion Digest

- Source PR: [vllm-project/vllm#23964](https://github.com/vllm-project/vllm/pull/23964)
- Source page: `sources/prs/vllm/PR-23964.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23964`
- Generated at: `2026-05-20T15:37:44.537466+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-29T20:53:32Z`
- Merged: `2025-09-18T15:52:58Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 7 (approved=3, commented=4)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: mergify, nvpohanh, simon-mo, tlrmchlsmth, varun-sundar-rabindranath, wenscarl, zejunchen-zejun
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-09-04T22:59:10Z` `COMMENTED` by `simon-mo` (https://github.com/vllm-project/vllm/pull/23964#pullrequestreview-3187498860)
- `2025-09-04T22:59:20Z` `APPROVED` by `simon-mo` (https://github.com/vllm-project/vllm/pull/23964#pullrequestreview-3187499075)
- `2025-09-09T03:26:04Z` `COMMENTED` by `varun-sundar-rabindranath` (https://github.com/vllm-project/vllm/pull/23964#pullrequestreview-3198902936)
- `2025-09-09T03:27:59Z` `APPROVED` by `varun-sundar-rabindranath` - Nice and clean change. Thanks @wenscarl (https://github.com/vllm-project/vllm/pull/23964#pullrequestreview-3198907417)
- `2025-09-09T15:20:54Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/23964#pullrequestreview-3202138832)
- `2025-09-09T15:22:34Z` `COMMENTED` by `tlrmchlsmth` - Don't we need to add a prepare/finalize implementation that uses this backend? (https://github.com/vllm-project/vllm/pull/23964#pullrequestreview-3202144991)
- `2025-09-11T21:31:32Z` `APPROVED` by `tlrmchlsmth` - I didn't realize how this was hooked up. Tried it and LGTM! I also switched the default All2All ... (https://github.com/vllm-project/vllm/pull/23964#pullrequestreview-3213699158)

## Inline Comment Hotspots

- `vllm/envs.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-09-15T13:37:00Z` `issue` by `tlrmchlsmth`; signals: hang, perf, performance; excerpt: "If we can confirm that the performance is good, could we enable it by default so that users do not need to add VLLM ..." (https://github.com/vllm-project/vllm/pull/23964#issuecomment-3292208049)
- `2025-09-11T17:27:17Z` `issue` by `wenscarl`; signals: kernel, moe; excerpt: "Don't we need to add a prepare/finalize implementation that uses this backend? Not a this moment. Since trtllm-moe kernel's API is quite different from ..." (https://github.com/vllm-project/vllm/pull/23964#issuecomment-3281993258)
- `2025-09-15T13:27:17Z` `issue` by `nvpohanh`; signals: perf, performance; excerpt: "If we can confirm that the performance is good, could we enable it by default so that users do not need to add VLLM ..." (https://github.com/vllm-project/vllm/pull/23964#issuecomment-3292162451)
- `2025-09-09T15:22:34Z` `review` `COMMENTED` by `tlrmchlsmth`; signals: general review; excerpt: "Don't we need to add a prepare/finalize implementation that uses this backend?" (https://github.com/vllm-project/vllm/pull/23964#pullrequestreview-3202144991)
- `2025-09-11T23:09:18Z` `issue` by `tlrmchlsmth`; signals: hang; excerpt: "failures might actually be related as well changed the default All2All backend. I’m on my phone so can’t read the logs well right now" (https://github.com/vllm-project/vllm/pull/23964#issuecomment-3282918854)
- `2025-09-09T03:26:03Z` `inline` by `varun-sundar-rabindranath` `vllm/envs.py`:1132; signals: general review; excerpt: "I think this is a better default. [edit] I'd recommend making this switch in a followup PR with some testing" (https://github.com/vllm-project/vllm/pull/23964#discussion_r2331908822)
- `2025-09-09T03:27:59Z` `review` `APPROVED` by `varun-sundar-rabindranath`; signals: hang; excerpt: "Nice and clean change. Thanks @wenscarl" (https://github.com/vllm-project/vllm/pull/23964#pullrequestreview-3198907417)
- `2025-09-04T22:59:10Z` `inline` by `simon-mo` `vllm/envs.py`:1132; signals: general review; excerpt: "@tlrmchlsmth wdyt if we turn this on as the default?" (https://github.com/vllm-project/vllm/pull/23964#discussion_r2323715219)
- `2025-09-09T15:20:54Z` `inline` by `tlrmchlsmth` `vllm/envs.py`:1132; signals: general review; excerpt: "yeah, we should make this the default" (https://github.com/vllm-project/vllm/pull/23964#discussion_r2333996028)
- `2025-09-11T21:31:32Z` `review` `APPROVED` by `tlrmchlsmth`; signals: general review; excerpt: "I didn't realize how this was hooked up. Tried it and LGTM! I also switched the default All2All backend to this one." (https://github.com/vllm-project/vllm/pull/23964#pullrequestreview-3213699158)
- `2025-09-17T04:09:51Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @wenscarl." (https://github.com/vllm-project/vllm/pull/23964#issuecomment-3301237045)
- `2025-09-18T13:32:29Z` `issue` by `wenscarl`; signals: general review; excerpt: "@wenscarl Could the failure be related? The distributed tests are green on a very recent nightly I didn't see significant failures. Do I miss ..." (https://github.com/vllm-project/vllm/pull/23964#issuecomment-3307484059)
