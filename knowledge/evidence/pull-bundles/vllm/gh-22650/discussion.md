# PR Discussion Digest

- Source PR: [vllm-project/vllm#22650](https://github.com/vllm-project/vllm/pull/22650)
- Source page: `sources/prs/vllm/PR-22650.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22650`
- Generated at: `2026-05-20T15:37:06.515660+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-11T13:39:27Z`
- Merged: `2025-10-03T06:12:15Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 29 (approved=1, commented=28)
- Inline review comments: 36
- Review threads observed: 16
- Resolved/outdated thread markers: resolved=16, outdated=11
- Human participants with discussion text: ArthurZucker, Isotr0py, ProExpertProg, hmellor, mergify
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-11T13:42:52Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for Mixture-of-Experts (MoE) models within the Transformers backend. The changes are ... (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3105966839)
- `2025-08-11T14:40:20Z` `COMMENTED` by `ArthurZucker` - looks nice already! (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3106212733)
- `2025-08-11T16:57:28Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3106843451)
- `2025-08-11T17:26:21Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3106949397)
- `2025-09-26T14:34:49Z` `COMMENTED` by `Isotr0py` - Some intial comments. PTAL! (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272435716)
- `2025-09-26T14:41:20Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272593429)
- `2025-09-26T14:44:26Z` `COMMENTED` by `ArthurZucker` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272603482)
- `2025-09-26T14:47:38Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272616447)
- `2025-09-26T14:48:38Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272619747)
- `2025-09-26T14:53:02Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272633810)
- `2025-09-26T14:53:18Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272634612)
- `2025-09-26T15:00:08Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272658398)
- `2025-09-26T15:05:34Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272677740)
- `2025-09-26T15:10:09Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272692802)
- `2025-09-26T15:18:53Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272720285)
- `2025-09-26T15:25:26Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272745145)
- `2025-09-26T15:42:05Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3272812523)
- `2025-09-26T17:27:05Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3273173795)
- `2025-09-26T18:12:04Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3273349981)
- `2025-09-29T13:29:33Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3279740311)
- `2025-09-29T14:30:57Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3280182252)
- `2025-09-30T03:17:25Z` `APPROVED` by `Isotr0py` - Overall LGTM. But we need to wait merge, otherwise nightly Transformers CI can't pass the MoE test. (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3282429092)
- `2025-09-30T07:35:09Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3283020009)
- `2025-09-30T07:38:00Z` `COMMENTED` by `hmellor` (https://github.com/vllm-project/vllm/pull/22650#pullrequestreview-3283030000)
- ... 5 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `vllm/model_executor/models/transformers.py`: 13 inline comment(s)
- `vllm/model_executor/models/transformers_moe.py`: 12 inline comment(s)
- `vllm/model_executor/models/utils.py`: 8 inline comment(s)
- `vllm/model_executor/models/registry.py`: 2 inline comment(s)
- `tests/models/test_transformers.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-26T14:53:02Z` `inline` by `hmellor` `vllm/model_executor/models/transformers_moe.py`:61; signals: compile, hang, moe, perf; excerpt: "In this implementation, we choose to perform the routing on the Transformers side for maximum flexibility. This means that: - experts.forward must accept: hidden ..." (https://github.com/vllm-project/vllm/pull/22650#discussion_r2382666952)
- `2025-09-26T18:12:04Z` `inline` by `hmellor` `vllm/model_executor/models/transformers_moe.py`:254; signals: compile, cuda, moe; excerpt: "Added a test which usees Qwen/Qwen1.5-MoE-A2.7B-Chat because I want to also ensure that the MoE's are torch.compile/CUDA graphs compatible. Right now Granite MoE is ..." (https://github.com/vllm-project/vllm/pull/22650#discussion_r2383136804)
- `2025-09-26T14:23:07Z` `inline` by `Isotr0py` `vllm/model_executor/models/transformers_moe.py`:61; signals: moe, register; excerpt: "I think there is no need to register an extra transformers moe forward ops, seems the only difference is the handling of top k ..." (https://github.com/vllm-project/vllm/pull/22650#discussion_r2382587346)
- `2025-09-26T14:48:38Z` `inline` by `hmellor` `vllm/model_executor/models/utils.py`:270; signals: block, moe; excerpt: "I disagree, this block of code operates directly on the output of FusedMoE.make expert params mapping, which is as generic as it can be." (https://github.com/vllm-project/vllm/pull/22650#discussion_r2382655897)
- `2025-09-30T07:35:09Z` `inline` by `hmellor` `vllm/model_executor/models/transformers.py`:150; signals: fp4, mxfp4; excerpt: "This is already caught at the start of TransformersBase. init . So IMO we either leave this as is or completely remove any MXFP4 ..." (https://github.com/vllm-project/vllm/pull/22650#discussion_r2390163924)
- `2025-09-26T14:47:38Z` `inline` by `hmellor` `vllm/model_executor/models/transformers_moe.py`:37; signals: moe, register; excerpt: "How so? FusedMoE registers itself this way too. Or is that what makes it reduntant here?" (https://github.com/vllm-project/vllm/pull/22650#discussion_r2382653398)
- `2025-08-11T16:55:44Z` `inline` by `Isotr0py` `vllm/model_executor/models/transformers.py`:637; signals: moe; excerpt: "Can we avoid hardcoding these names? Some models like mixtral and granite MoE will use a differnet name (w1, w2 and w3 etc)." (https://github.com/vllm-project/vllm/pull/22650#discussion_r2267436747)
- `2025-09-26T14:15:07Z` `inline` by `Isotr0py` `vllm/model_executor/models/utils.py`:270; signals: moe; excerpt: "I feel like this should be moved to TransformersMoEBase's load weights, because it looks too specific." (https://github.com/vllm-project/vllm/pull/22650#discussion_r2382567389)
- `2025-09-26T15:05:33Z` `inline` by `Isotr0py` `vllm/model_executor/models/utils.py`:270; signals: moe; excerpt: "Hmmm, but these lines can only be reached by Transformers backend, while native MoE implementation usually has load weights function bypassing these lines. And ..." (https://github.com/vllm-project/vllm/pull/22650#discussion_r2382699159)
- `2025-09-26T15:18:53Z` `inline` by `hmellor` `vllm/model_executor/models/utils.py`:270; signals: moe; excerpt: "these lines can only be reached by Transformers backend Currently yes, but there is nothing stopping other model implementations leveraging this improvement to the ..." (https://github.com/vllm-project/vllm/pull/22650#discussion_r2382730286)
- `2025-09-26T14:00:53Z` `inline` by `Isotr0py` `vllm/model_executor/models/transformers_moe.py`:37; signals: moe; excerpt: "Hmmm, seems the custom op registration is redundant here." (https://github.com/vllm-project/vllm/pull/22650#discussion_r2382529774)
- `2025-09-26T14:41:19Z` `inline` by `Isotr0py` `vllm/model_executor/models/transformers_moe.py`:254; signals: moe; excerpt: "Let's add some generation tests for MoE models." (https://github.com/vllm-project/vllm/pull/22650#discussion_r2382637585)
