# PR Discussion Digest

- Source PR: [vllm-project/vllm#38794](https://github.com/vllm-project/vllm/pull/38794)
- Source page: `sources/prs/vllm/PR-38794.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38794`
- Generated at: `2026-05-20T15:40:36.909180+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-02T08:10:43Z`
- Merged: `2026-04-10T07:03:26Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 10 (approved=1, commented=9)
- Inline review comments: 10
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=3
- Human participants with discussion text: Isotr0py, JackWang2120, jackcfwang, mergify
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-02T08:16:34Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces caching for the mm prefix range tensor within TritonAttentionMetadata and refactors its ... (https://github.com/vllm-project/vllm/pull/38794#pullrequestreview-4049091366)
- `2026-04-02T12:00:35Z` `COMMENTED` by `JackWang2120` (https://github.com/vllm-project/vllm/pull/38794#pullrequestreview-4050193131)
- `2026-04-03T05:56:53Z` `COMMENTED` by `jackcfwang` (https://github.com/vllm-project/vllm/pull/38794#pullrequestreview-4054402844)
- `2026-04-03T07:25:59Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/38794#pullrequestreview-4054625691)
- `2026-04-03T08:45:40Z` `COMMENTED` by `jackcfwang` (https://github.com/vllm-project/vllm/pull/38794#pullrequestreview-4054880784)
- `2026-04-03T08:49:46Z` `COMMENTED` by `jackcfwang` (https://github.com/vllm-project/vllm/pull/38794#pullrequestreview-4054892619)
- `2026-04-03T14:55:46Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/38794#pullrequestreview-4056044399)
- `2026-04-07T09:05:59Z` `COMMENTED` by `jackcfwang` (https://github.com/vllm-project/vllm/pull/38794#pullrequestreview-4066944852)
- `2026-04-08T11:48:40Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/38794#pullrequestreview-4074851617)
- `2026-04-09T08:28:11Z` `APPROVED` by `Isotr0py` - LGTM, thanks for your patience! (https://github.com/vllm-project/vllm/pull/38794#pullrequestreview-4080824638)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/triton_attn.py`: 10 inline comment(s)

## High-Signal Discussion

- `2026-04-07T09:05:59Z` `inline` by `jackcfwang` `vllm/v1/attention/backends/triton_attn.py`:98; signals: attention, cache, perf, performance, triton; excerpt: "@Isotr0py Thank you for your proposal on using hash mm prefix range to determine whether the cache needs to be updated. I wrote a ..." (https://github.com/vllm-project/vllm/pull/38794#discussion_r3043958827)
- `2026-04-08T11:48:40Z` `inline` by `Isotr0py` `vllm/v1/attention/backends/triton_attn.py`:98; signals: attention, benchmark, perf, performance, triton; excerpt: "I wrote a version of the code based on your idea, but on our internal stress testing platform, we found that the hash solution ..." (https://github.com/vllm-project/vllm/pull/38794#discussion_r3051103842)
- `2026-04-03T07:25:29Z` `inline` by `Isotr0py` `vllm/v1/attention/backends/triton_attn.py`:98; signals: attention, cache, hang, triton; excerpt: "I remember that mm prefix range will probably change after scheduler step (old request finished / new request inserted). But seems that mm prefix ..." (https://github.com/vllm-project/vllm/pull/38794#discussion_r3031796302)
- `2026-04-03T08:45:39Z` `inline` by `jackcfwang` `vllm/v1/attention/backends/triton_attn.py`:98; signals: attention, cache, hang, triton; excerpt: "@Isotr0py Thank you for your suggestion. I did indeed overlook this case. Currently, I have overridden the setattr method. When mm prefix range changes, ..." (https://github.com/vllm-project/vllm/pull/38794#discussion_r3032036113)
- `2026-04-02T12:00:35Z` `inline` by `JackWang2120` `vllm/v1/attention/backends/triton_attn.py`:127; signals: attention, memory, triton; excerpt: "If we do this, will it generate a res tensor that is too large on the CPU side, affecting the memory space on the ..." (https://github.com/vllm-project/vllm/pull/38794#discussion_r3027627430)
- `2026-04-03T08:49:46Z` `inline` by `jackcfwang` `vllm/v1/attention/backends/triton_attn.py`:98; signals: attention, cache, triton; excerpt: "@Isotr0py I'm not sure if there is a more optimized way to implement this. At present, I can only think of this approach to ..." (https://github.com/vllm-project/vllm/pull/38794#discussion_r3032048776)
- `2026-04-03T14:55:46Z` `inline` by `Isotr0py` `vllm/v1/attention/backends/triton_attn.py`:98; signals: attention, cache, triton; excerpt: "Hmmm, overrides setattr maybe a little bit hacky. How about hashing the mm prefix range to match the cached tensor? So when the previous ..." (https://github.com/vllm-project/vllm/pull/38794#discussion_r3033177625)
- `2026-04-03T05:56:53Z` `inline` by `jackcfwang` `vllm/v1/attention/backends/triton_attn.py`:127; signals: attention, triton; excerpt: "When I used the internal pressure testing platform to test the code you suggested, with the batch size ranging from 3 to 35, the ..." (https://github.com/vllm-project/vllm/pull/38794#discussion_r3031570064)
- `2026-04-09T08:39:38Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @jackcfwang, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/38794#issuecomment-4212802585)
- `2026-04-10T02:27:24Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @jackcfwang." (https://github.com/vllm-project/vllm/pull/38794#issuecomment-4219590781)
