# PR Discussion Digest

- Source PR: [vllm-project/vllm#36361](https://github.com/vllm-project/vllm/pull/36361)
- Source page: `sources/prs/vllm/PR-36361.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36361`
- Generated at: `2026-05-20T15:40:10.779454+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-07T23:21:15Z`
- Merged: `2026-03-11T15:36:12Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 7
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: IzzyPutterman, benchislett, jhaotingc, leihuang-sketch, mergify
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-07T23:24:03Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for Eagle3 speculative decoding for Deepseek and Kimi models. The changes ... (https://github.com/vllm-project/vllm/pull/36361#pullrequestreview-3910072959)
- `2026-03-10T18:12:26Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/36361#pullrequestreview-3924441229)
- `2026-03-10T18:53:25Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/36361#pullrequestreview-3924673117)
- `2026-03-10T19:11:08Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/36361#pullrequestreview-3924765099)
- `2026-03-10T20:35:28Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/36361#pullrequestreview-3925264340)
- `2026-03-10T21:09:05Z` `COMMENTED` by `jhaotingc` (https://github.com/vllm-project/vllm/pull/36361#pullrequestreview-3925449803)
- `2026-03-10T21:14:59Z` `COMMENTED` by `benchislett` (https://github.com/vllm-project/vllm/pull/36361#pullrequestreview-3925485437)
- `2026-03-11T15:36:10Z` `APPROVED` by `benchislett` (https://github.com/vllm-project/vllm/pull/36361#pullrequestreview-3930536079)

## Inline Comment Hotspots

- `vllm/model_executor/models/deepseek_eagle3.py`: 7 inline comment(s)

## High-Signal Discussion

- `2026-03-11T03:05:10Z` `issue` by `leihuang-sketch`; signals: perf, performance, throughput; excerpt: "@jhaotingc In my tests, I found that there was no improvement in performance, and the throughput remained almost the same without additional parameters for ..." (https://github.com/vllm-project/vllm/pull/36361#issuecomment-4035886005)
- `2026-03-10T16:33:51Z` `issue` by `IzzyPutterman`; signals: mla; excerpt: "See 35966: why does this PR need a new model implementation and the other one doesn't? This one implements the MLA based eagle3 not ..." (https://github.com/vllm-project/vllm/pull/36361#issuecomment-4032825401)
- `2026-03-11T01:48:21Z` `issue` by `benchislett`; signals: failing; excerpt: "will rerun failed tests a couple times and update from main once again if that doesn't work. failing that, we'll force-merge tomorrow." (https://github.com/vllm-project/vllm/pull/36361#issuecomment-4035612291)
- `2026-03-11T01:30:36Z` `issue` by `jhaotingc`; signals: hang; excerpt: "The failed tests seem unrelated to our change @benchislett" (https://github.com/vllm-project/vllm/pull/36361#issuecomment-4035554317)
- `2026-03-10T18:12:26Z` `inline` by `benchislett` `vllm/model_executor/models/deepseek_eagle3.py`:79; signals: general review; excerpt: "Why is this needed?" (https://github.com/vllm-project/vllm/pull/36361#discussion_r2913582305)
- `2026-03-10T18:53:25Z` `inline` by `jhaotingc` `vllm/model_executor/models/deepseek_eagle3.py`:79; signals: general review; excerpt: "Seems like we have this deepseek yarm rope scaling" (https://github.com/vllm-project/vllm/pull/36361#discussion_r2913787622)
- `2026-03-10T19:11:08Z` `inline` by `benchislett` `vllm/model_executor/models/deepseek_eagle3.py`:365; signals: general review; excerpt: "This is valid, but also seems to be copied from llama eagle3.py which has the same issue" (https://github.com/vllm-project/vllm/pull/36361#discussion_r2913872598)
- `2026-03-10T20:35:27Z` `inline` by `benchislett` `vllm/model_executor/models/deepseek_eagle3.py`:79; signals: general review; excerpt: "Why can't the config just say "rope type": "deepseek yarn" ??" (https://github.com/vllm-project/vllm/pull/36361#discussion_r2914321308)
- `2026-03-10T21:09:05Z` `inline` by `jhaotingc` `vllm/model_executor/models/deepseek_eagle3.py`:79; signals: general review; excerpt: "Seems that deepseek has this issue as well." (https://github.com/vllm-project/vllm/pull/36361#discussion_r2914496540)
- `2026-03-10T21:14:59Z` `inline` by `benchislett` `vllm/model_executor/models/deepseek_eagle3.py`:79; signals: general review; excerpt: "alrighty then lol" (https://github.com/vllm-project/vllm/pull/36361#discussion_r2914528406)
- `2026-03-07T23:21:53Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @jhaotingc." (https://github.com/vllm-project/vllm/pull/36361#issuecomment-4017625995)
- `2026-03-10T20:36:12Z` `issue` by `benchislett`; signals: general review; excerpt: "I was able to get this working locally. Seems fine but does not run. Two other EAGLE heads, one internal and one public, work ..." (https://github.com/vllm-project/vllm/pull/36361#issuecomment-4034308369)
