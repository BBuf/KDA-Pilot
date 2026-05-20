# PR Discussion Digest

- Source PR: [vllm-project/vllm#15732](https://github.com/vllm-project/vllm/pull/15732)
- Source page: `sources/prs/vllm/PR-15732.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-15732`
- Generated at: `2026-05-20T15:34:39.251899+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-28T23:45:05Z`
- Merged: `2025-04-03T21:23:28Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 12 (approved=4, changes_requested=1, commented=7)
- Inline review comments: 9
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: DarkLight1337, NickLucche, brittrock, bvrockwell, mergify, mgoin, robertgshaw2-redhat, vanbasten23, yaochengji
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-04-01T04:06:14Z` `COMMENTED` by `yaochengji` (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2731044635)
- `2025-04-01T18:31:15Z` `COMMENTED` by `vanbasten23` (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2733714744)
- `2025-04-01T22:00:52Z` `COMMENTED` by `yaochengji` (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2734132438)
- `2025-04-02T00:02:38Z` `COMMENTED` by `vanbasten23` (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2734266520)
- `2025-04-02T00:02:49Z` `COMMENTED` by `vanbasten23` (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2734266657)
- `2025-04-02T05:48:52Z` `APPROVED` by `yaochengji` - LGTM, thanks! Note that the CI is not green. (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2734723578)
- `2025-04-02T08:48:16Z` `APPROVED` by `NickLucche` - Great job! I think some of the commits need signing, please take a look (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2735346432)
- `2025-04-02T17:18:44Z` `COMMENTED` by `vanbasten23` (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2737033065)
- `2025-04-02T17:22:07Z` `COMMENTED` by `NickLucche` (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2737040486)
- `2025-04-02T18:27:40Z` `CHANGES_REQUESTED` by `bvrockwell` - waiting for multi chip validation - thank you! (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2737202927)
- `2025-04-02T23:28:05Z` `APPROVED` by `bvrockwell` (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2737830825)
- `2025-04-03T00:19:47Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2737974499)

## Inline Comment Hotspots

- `tests/v1/tpu/test_pallas.py`: 7 inline comment(s)
- `tests/entrypoints/llm/test_accuracy.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-02T22:02:31Z` `issue` by `vanbasten23`; signals: block, gemm, kernel; excerpt: "@yaochengji we shouldn't merge this until @vanbasten23 validates 27B as well. Let's wait for these results . I tested the 27b and it fails: ..." (https://github.com/vllm-project/vllm/pull/15732#issuecomment-2773833697)
- `2025-04-02T23:27:49Z` `issue` by `bvrockwell`; signals: block, gemm, kernel; excerpt: "@yaochengji we shouldn't merge this until @vanbasten23 validates 27B as well. Let's wait for these results . I tested the 27b and it fails: ..." (https://github.com/vllm-project/vllm/pull/15732#issuecomment-2773957349)
- `2025-04-01T18:31:15Z` `inline` by `vanbasten23` `tests/entrypoints/llm/test_accuracy.py`:26; signals: accuracy, gemm; excerpt: "Thanks for the suggestion! I ran on GPU and got the same accuracy (0.25) for gemma-3-1b (test output on GPU:" (https://github.com/vllm-project/vllm/pull/15732#discussion_r2023480234)
- `2025-04-02T00:02:37Z` `inline` by `vanbasten23` `tests/v1/tpu/test_pallas.py`:35; signals: attention, kernel; excerpt: "This PR just pipes the sliding window and logits soft cap from PallasAttentionBackendImpl.forward to the kernel. So this test verifies the 2 parameters are ..." (https://github.com/vllm-project/vllm/pull/15732#discussion_r2023822143)
- `2025-04-01T04:06:13Z` `inline` by `yaochengji` `tests/entrypoints/llm/test_accuracy.py`:26; signals: accuracy; excerpt: "Have you compared this score with GPU?" (https://github.com/vllm-project/vllm/pull/15732#discussion_r2022104875)
- `2025-04-02T08:46:18Z` `inline` by `NickLucche` `tests/v1/tpu/test_pallas.py`:35; signals: correctness; excerpt: "can you comment this is just checking args and correctness is tested in torch xla/jax experimental?" (https://github.com/vllm-project/vllm/pull/15732#discussion_r2024374311)
- `2025-03-30T19:09:17Z` `issue` by `brittrock`; signals: gemm; excerpt: "This is great @vanbasten23 thanks for piping this in! Would we be able to add a Gemma 3 [text-only] test in please? Cc @robertgshaw2-redhat ..." (https://github.com/vllm-project/vllm/pull/15732#issuecomment-2764702545)
- `2025-04-02T18:27:40Z` `review` `CHANGES_REQUESTED` by `bvrockwell`; signals: general review; excerpt: "waiting for multi chip validation - thank you!" (https://github.com/vllm-project/vllm/pull/15732#pullrequestreview-2737202927)
- `2025-04-01T21:57:24Z` `inline` by `yaochengji` `tests/v1/tpu/test_pallas.py`:35; signals: general review; excerpt: "Why vmem limites is only 1024 bytes?" (https://github.com/vllm-project/vllm/pull/15732#discussion_r2023731304)
- `2025-04-01T22:00:45Z` `inline` by `yaochengji` `tests/v1/tpu/test_pallas.py`:84; signals: general review; excerpt: "Should we also check the result?" (https://github.com/vllm-project/vllm/pull/15732#discussion_r2023734336)
- `2025-04-02T00:02:49Z` `inline` by `vanbasten23` `tests/v1/tpu/test_pallas.py`:84; signals: general review; excerpt: "replied in" (https://github.com/vllm-project/vllm/pull/15732#discussion_r2023822266)
- `2025-04-02T17:18:44Z` `inline` by `vanbasten23` `tests/v1/tpu/test_pallas.py`:35; signals: general review; excerpt: "done" (https://github.com/vllm-project/vllm/pull/15732#discussion_r2025270623)
