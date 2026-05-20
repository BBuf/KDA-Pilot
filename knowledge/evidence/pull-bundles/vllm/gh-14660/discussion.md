# PR Discussion Digest

- Source PR: [vllm-project/vllm#14660](https://github.com/vllm-project/vllm/pull/14660)
- Source page: `sources/prs/vllm/PR-14660.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14660`
- Generated at: `2026-05-20T15:34:31.231777+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-12T07:13:59Z`
- Merged: `2025-03-12T15:36:33Z`

## Discussion Counts

- Issue comments: 22
- Review submissions: 16 (approved=1, commented=15)
- Inline review comments: 15
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: DarkLight1337, Dilesh-chouhan, Swipe4057, WoosukKwon, anunknowperson, devops724, erdaltoprak, francis2tm, hahmad2008, moficodes, pietrobolcato, xihuai18, ywang96
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 19

## Review Decisions

- `2025-03-12T08:25:49Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677523301)
- `2025-03-12T08:36:49Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677551279)
- `2025-03-12T08:44:46Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677573272)
- `2025-03-12T08:46:19Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677577282)
- `2025-03-12T08:48:30Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677583037)
- `2025-03-12T08:50:01Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677588398)
- `2025-03-12T08:51:36Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677593463)
- `2025-03-12T08:52:34Z` `COMMENTED` by `ywang96` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677596033)
- `2025-03-12T08:54:11Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677601187)
- `2025-03-12T08:54:39Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677602402)
- `2025-03-12T08:54:58Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677603293)
- `2025-03-12T08:56:17Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677606819)
- `2025-03-12T08:57:05Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677608999)
- `2025-03-12T09:00:37Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677618620)
- `2025-03-12T09:01:47Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2677621769)
- `2025-03-12T12:36:07Z` `APPROVED` by `ywang96` - Fixed a few issues and I think this PR is good to be shipped. We can follow up ... (https://github.com/vllm-project/vllm/pull/14660#pullrequestreview-2678318658)

## Inline Comment Hotspots

- `vllm/model_executor/models/gemma3_mm.py`: 6 inline comment(s)
- `docs/source/models/supported_models.md`: 6 inline comment(s)
- `tests/models/registry.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-03-12T08:36:49Z` `inline` by `WoosukKwon` `vllm/model_executor/models/gemma3_mm.py`:32; signals: gemm; excerpt: "Actually, other models (e.g., InternVL) also hardcode the values. IIIUC, not all methods (e.g, get mm max tokens per item) that need this value ..." (https://github.com/vllm-project/vllm/pull/14660#discussion_r1990950970)
- `2025-03-12T08:44:46Z` `inline` by `DarkLight1337` `vllm/model_executor/models/gemma3_mm.py`:32; signals: gemm; excerpt: "Other models hardcode the values only when they can't be easily read from the config. We generally avoid using hardcoded values. In any case ..." (https://github.com/vllm-project/vllm/pull/14660#discussion_r1990964221)
- `2025-03-12T09:01:47Z` `inline` by `WoosukKwon` `docs/source/models/supported_models.md`:957; signals: gemm; excerpt: "Updated! I removed the error msg in gemma3 mm.py since users will likely get an error before loading the file (when instantiating Gemma3Config)." (https://github.com/vllm-project/vllm/pull/14660#discussion_r1990994504)
- `2025-03-12T08:25:49Z` `inline` by `ywang96` `vllm/model_executor/models/gemma3_mm.py`:32; signals: gemm; excerpt: "You can get this from hf config.mm tokens per image" (https://github.com/vllm-project/vllm/pull/14660#discussion_r1990933341)
- `2025-03-12T08:46:18Z` `inline` by `WoosukKwon` `vllm/model_executor/models/gemma3_mm.py`:32; signals: gemm; excerpt: "@DarkLight1337 @ywang96 Never mind. I've removed the hardcoded values in the mean time." (https://github.com/vllm-project/vllm/pull/14660#discussion_r1990966591)
- `2025-03-12T08:51:36Z` `inline` by `DarkLight1337` `tests/models/registry.py`:244; signals: failing; excerpt: "Avoid failing CI due to incorrect transformers version" (https://github.com/vllm-project/vllm/pull/14660#discussion_r1990976757)
- `2025-03-12T08:54:11Z` `inline` by `WoosukKwon` `docs/source/models/supported_models.md`:957; signals: gemm; excerpt: "I left a similar comment in gemma3 mm.py. Do we need it here as well?" (https://github.com/vllm-project/vllm/pull/14660#discussion_r1990981277)
- `2025-03-12T08:54:38Z` `inline` by `WoosukKwon` `vllm/model_executor/models/gemma3_mm.py`:404; signals: gemm; excerpt: "Fixed." (https://github.com/vllm-project/vllm/pull/14660#discussion_r1990982037)
- `2025-03-12T12:42:10Z` `issue` by `devops724`; signals: gemm; excerpt: "great, this mean we have Gemma 3 support in next release , thanks" (https://github.com/vllm-project/vllm/pull/14660#issuecomment-2717761813)
- `2025-03-12T08:48:30Z` `inline` by `DarkLight1337` `docs/source/models/supported_models.md`:957; signals: general review; excerpt: "HF side has merged the PR, so we can ask users to install it now." (https://github.com/vllm-project/vllm/pull/14660#discussion_r1990970216)
- `2025-03-12T08:54:57Z` `inline` by `DarkLight1337` `docs/source/models/supported_models.md`:957; signals: general review; excerpt: "Yeah, most users won't look at the code..." (https://github.com/vllm-project/vllm/pull/14660#discussion_r1990982641)
- `2025-03-12T08:56:17Z` `inline` by `DarkLight1337` `docs/source/models/supported_models.md`:957; signals: general review; excerpt: "Also that branch has been merged into main already" (https://github.com/vllm-project/vllm/pull/14660#discussion_r1990984936)
