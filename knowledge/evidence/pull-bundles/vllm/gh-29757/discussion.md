# PR Discussion Digest

- Source PR: [vllm-project/vllm#29757](https://github.com/vllm-project/vllm/pull/29757)
- Source page: `sources/prs/vllm/PR-29757.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29757`
- Generated at: `2026-05-20T15:38:47.436417+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-30T22:50:05Z`
- Merged: `2025-12-02T10:29:00Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 28 (approved=1, commented=27)
- Inline review comments: 29
- Review threads observed: 14
- Resolved/outdated thread markers: resolved=3, outdated=6
- Human participants with discussion text: DarkLight1337, TheLocalDrummer, benchislett, chatgpt-codex-connector, juliendenize, mergify, mgoin, mickaelseznec, patrickvonplaten, tlrmchlsmth, ywang96, zou3519
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-30T22:51:53Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for Mistral Large 3 and its Eagle variant by reusing the ... (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3522593909)
- `2025-11-30T23:49:17Z` `COMMENTED` by `mgoin` - 🥳 Make sure to update the supported model page and the testing registry with is available online=False for ... (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3522725498)
- `2025-12-01T14:49:33Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3525391091)
- `2025-12-01T14:51:18Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3525401527)
- `2025-12-01T15:50:10Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3525733878)
- `2025-12-01T15:54:44Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3525756682)
- `2025-12-01T16:12:37Z` `COMMENTED` by `juliendenize` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3525836840)
- `2025-12-01T16:13:50Z` `COMMENTED` by `juliendenize` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3525842191)
- `2025-12-01T16:33:36Z` `COMMENTED` by `mickaelseznec` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3525941896)
- `2025-12-01T16:40:49Z` `COMMENTED` by `juliendenize` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3525978085)
- `2025-12-01T16:41:33Z` `COMMENTED` by `juliendenize` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3525981522)
- `2025-12-01T16:46:11Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3526008335)
- `2025-12-01T17:36:59Z` `COMMENTED` by `juliendenize` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3526219695)
- `2025-12-01T19:14:17Z` `COMMENTED` by `juliendenize` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3526587640)
- `2025-12-01T20:59:24Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3526970115)
- `2025-12-01T21:38:55Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3527158713)
- `2025-12-01T21:39:45Z` `COMMENTED` by `patrickvonplaten` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3527162215)
- `2025-12-01T21:42:39Z` `COMMENTED` by `patrickvonplaten` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3527176176)
- `2025-12-01T21:48:47Z` `COMMENTED` by `juliendenize` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3527206730)
- `2025-12-01T22:18:18Z` `COMMENTED` by `zou3519` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3527290190)
- `2025-12-01T22:25:15Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3527308416)
- `2025-12-01T22:28:03Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3527314333)
- `2025-12-01T22:36:33Z` `COMMENTED` by `juliendenize` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3527331079)
- `2025-12-01T22:37:48Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3527333490)
- ... 4 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/transformers_utils/configs/eagle.py`: 10 inline comment(s)
- `tests/models/registry.py`: 4 inline comment(s)
- `vllm/model_executor/models/deepseek_v2.py`: 3 inline comment(s)
- `vllm/tokenizers/mistral.py`: 3 inline comment(s)
- `vllm/model_executor/layers/mla.py`: 2 inline comment(s)
- `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`: 2 inline comment(s)
- `vllm/config/speculative.py`: 1 inline comment(s)
- `vllm/transformers_utils/config.py`: 1 inline comment(s)
- `vllm/transformers_utils/configs/mistral.py`: 1 inline comment(s)
- `vllm/model_executor/models/mistral_large_3_eagle.py`: 1 inline comment(s)
- `vllm/config/utils.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-01T16:12:37Z` `inline` by `juliendenize` `vllm/model_executor/layers/mla.py`:164; signals: mla; excerpt: "Just a choice but no strong opinion about this that i can think of now. We also did in llama.py would it be necessary ..." (https://github.com/vllm-project/vllm/pull/29757#discussion_r2577731174)
- `2025-12-01T16:33:35Z` `inline` by `mickaelseznec` `vllm/transformers_utils/configs/eagle.py`:44; signals: hang; excerpt: "I run into a bug when disabling --enforce-eager. vLLM tries to compute a hash of the config, and this PretrainedConfig is called from transformers ..." (https://github.com/vllm-project/vllm/pull/29757#discussion_r2577805816)
- `2025-11-30T23:47:19Z` `inline` by `mgoin` `vllm/model_executor/layers/mla.py`:164; signals: mla; excerpt: "Why not just put this in a rotary embedding layer?" (https://github.com/vllm-project/vllm/pull/29757#discussion_r2575221747)
- `2025-11-30T23:49:17Z` `review` `COMMENTED` by `mgoin`; signals: general review; excerpt: "🥳 Make sure to update the supported model page and the testing registry with is available online=False for now" (https://github.com/vllm-project/vllm/pull/29757#pullrequestreview-3522725498)
- `2025-12-01T14:51:18Z` `inline` by `DarkLight1337` `vllm/transformers_utils/configs/eagle.py`:44; signals: hang; excerpt: "Could you elaborate on why this change is needed?" (https://github.com/vllm-project/vllm/pull/29757#discussion_r2577405945)
- `2025-12-01T22:42:40Z` `inline` by `patrickvonplaten` `vllm/transformers_utils/configs/eagle.py`:44; signals: hang; excerpt: "We reverted the change here, should be good" (https://github.com/vllm-project/vllm/pull/29757#discussion_r2578965819)
- `2025-12-01T16:13:50Z` `inline` by `juliendenize` `vllm/model_executor/models/deepseek_v2.py`:398; signals: general review; excerpt: "I think this could done yes, we also have it in llama.py question would be do we do it now ? It is not ..." (https://github.com/vllm-project/vllm/pull/29757#discussion_r2577734971)
- `2025-12-01T16:40:49Z` `inline` by `juliendenize` `vllm/entrypoints/openai/tool_parsers/mistral_tool_parser.py`:83; signals: general review; excerpt: "Had to add this to make sure tool calls worked as expected for some examples, will rerun some xp to see if i didn't ..." (https://github.com/vllm-project/vllm/pull/29757#discussion_r2577830991)
- `2025-12-01T19:14:17Z` `inline` by `juliendenize` `vllm/tokenizers/mistral.py`:170; signals: general review; excerpt: "as we got some requests we also give a bit more flexibility for tool definition. though extra args are not supported by mistral-common. this ..." (https://github.com/vllm-project/vllm/pull/29757#discussion_r2578310752)
- `2025-12-01T20:59:23Z` `inline` by `zou3519` `vllm/transformers_utils/configs/eagle.py`:44; signals: general review; excerpt: "I think we can put the use diff=False back, do you want to do this in this PR or should I do it in ..." (https://github.com/vllm-project/vllm/pull/29757#discussion_r2578633986)
- `2025-12-01T21:48:47Z` `inline` by `juliendenize` `vllm/tokenizers/mistral.py`:100; signals: general review; excerpt: "it's the same we do for all functions in this file we import at use because some people don't want to install mistral-common." (https://github.com/vllm-project/vllm/pull/29757#discussion_r2578847664)
- `2025-12-01T14:49:32Z` `inline` by `DarkLight1337` `vllm/model_executor/models/mistral_large_3_eagle.py`:125; signals: general review; excerpt: "No need to lazy import" (https://github.com/vllm-project/vllm/pull/29757#discussion_r2577398683)
