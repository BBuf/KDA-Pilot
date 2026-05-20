# PR Discussion Digest

- Source PR: [vllm-project/vllm#13236](https://github.com/vllm-project/vllm/pull/13236)
- Source page: `sources/prs/vllm/PR-13236.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-13236`
- Generated at: `2026-05-20T15:33:58.491297+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-13T20:03:55Z`
- Merged: `2025-02-14T20:53:42Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: dsikka, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-02-14T19:34:30Z` `APPROVED` by `tlrmchlsmth` - Good to land. There is some circular import "weirdness" but it can wait for a future refactor along ... (https://github.com/vllm-project/vllm/pull/13236#pullrequestreview-2618651324)
- `2025-02-14T20:27:17Z` `COMMENTED` by `dsikka` (https://github.com/vllm-project/vllm/pull/13236#pullrequestreview-2618737923)
- `2025-02-14T20:37:32Z` `COMMENTED` by `dsikka` (https://github.com/vllm-project/vllm/pull/13236#pullrequestreview-2618754654)
- `2025-02-14T20:40:19Z` `COMMENTED` by `dsikka` (https://github.com/vllm-project/vllm/pull/13236#pullrequestreview-2618758399)
- `2025-02-14T20:41:10Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/13236#pullrequestreview-2618759684)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/gptq_marlin.py`: 3 inline comment(s)
- `tests/weight_loading/test_weight_loading.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-02-14T19:01:02Z` `issue` by `mgoin`; signals: dtype, failing, moe; excerpt: "I fixed and ran the "Weight Loading Multiple GPU Test - Large Models", however it is failing due to unrelated compressedtensors dtype support issues. ..." (https://github.com/vllm-project/vllm/pull/13236#issuecomment-2660061625)
- `2025-02-13T20:28:45Z` `issue` by `mgoin`; signals: kernel, moe; excerpt: "@jinzhen-lin please see this PR. After this, I think we could remove moe wna16 as a larger quant method and just use it as ..." (https://github.com/vllm-project/vllm/pull/13236#issuecomment-2657644955)
- `2025-02-14T20:41:10Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/gptq_marlin.py`:48; signals: moe; excerpt: "It is just the original config saved from from config so we can forward to MoeWNA16Config" (https://github.com/vllm-project/vllm/pull/13236#discussion_r1956694650)
- `2025-02-14T20:27:17Z` `inline` by `dsikka` `tests/weight_loading/test_weight_loading.py`:15; signals: general review; excerpt: "ah good catch" (https://github.com/vllm-project/vllm/pull/13236#discussion_r1956683132)
- `2025-02-14T20:37:32Z` `inline` by `dsikka` `vllm/model_executor/layers/quantization/gptq_marlin.py`:48; signals: general review; excerpt: "What is full config? Can we add a comment" (https://github.com/vllm-project/vllm/pull/13236#discussion_r1956691616)
- `2025-02-14T20:40:19Z` `inline` by `dsikka` `vllm/model_executor/layers/quantization/gptq_marlin.py`:48; signals: general review; excerpt: "Oh just the config dict, I see" (https://github.com/vllm-project/vllm/pull/13236#discussion_r1956693846)
- `2025-02-13T22:10:15Z` `issue` by `dsikka`; signals: general review; excerpt: "Thanks for taking this on. Please run and/or update the [weight loading large tests]( I believe all the tests were skipped even when enabled ..." (https://github.com/vllm-project/vllm/pull/13236#issuecomment-2657815603)
- `2025-02-14T19:34:30Z` `review` `APPROVED` by `tlrmchlsmth`; signals: general review; excerpt: "Good to land. There is some circular import "weirdness" but it can wait for a future refactor along the lines of this RFC" (https://github.com/vllm-project/vllm/pull/13236#pullrequestreview-2618651324)
