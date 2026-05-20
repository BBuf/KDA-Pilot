# PR Discussion Digest

- Source PR: [vllm-project/vllm#20736](https://github.com/vllm-project/vllm/pull/20736)
- Source page: `sources/prs/vllm/PR-20736.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-20736`
- Generated at: `2026-05-20T15:36:14.664199+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-10T05:44:00Z`
- Merged: `2025-07-19T22:40:32Z`

## Discussion Counts

- Issue comments: 30
- Review submissions: 22 (approved=3, commented=19)
- Inline review comments: 25
- Review threads observed: 19
- Resolved/outdated thread markers: resolved=16, outdated=16
- Human participants with discussion text: DarkLight1337, Isotr0py, fernandaspets, jeejeelee, luccafong, mergify, zRzRzRzRzRzRzR, zchen-gitch
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-07-10T05:44:29Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @zRzRzRzRzRzRzR, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3004018864)
- `2025-07-10T05:50:48Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request adds support for GLM-4 MoE models to vLLM. The changes include modifying the ... (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3004035127)
- `2025-07-11T07:41:07Z` `COMMENTED` by `jeejeelee` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3009050865)
- `2025-07-11T07:48:25Z` `COMMENTED` by `jeejeelee` - Thank you, we also need to update the document. (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3009057782)
- `2025-07-11T14:21:53Z` `COMMENTED` by `zRzRzRzRzRzRzR` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3010522802)
- `2025-07-15T07:17:47Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3019017053)
- `2025-07-15T07:17:53Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3019017863)
- `2025-07-15T09:02:47Z` `COMMENTED` by `zRzRzRzRzRzRzR` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3019431840)
- `2025-07-15T09:04:16Z` `COMMENTED` by `zRzRzRzRzRzRzR` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3019437513)
- `2025-07-15T09:13:56Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3019470124)
- `2025-07-15T13:11:28Z` `COMMENTED` by `zRzRzRzRzRzRzR` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3020232135)
- `2025-07-15T18:29:03Z` `COMMENTED` by `luccafong` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3021783045)
- `2025-07-16T16:29:34Z` `COMMENTED` by `luccafong` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3025823528)
- `2025-07-16T17:17:44Z` `COMMENTED` by `luccafong` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3026007122)
- `2025-07-16T18:10:57Z` `COMMENTED` by `zRzRzRzRzRzRzR` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3026256786)
- `2025-07-16T19:03:09Z` `COMMENTED` by `luccafong` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3026447045)
- `2025-07-17T14:51:38Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3029885673)
- `2025-07-17T14:58:28Z` `COMMENTED` by `DarkLight1337` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3029913123)
- `2025-07-17T20:07:04Z` `APPROVED` by `luccafong` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3030867480)
- `2025-07-19T12:50:47Z` `COMMENTED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3035365210)
- `2025-07-19T16:07:45Z` `APPROVED` by `Isotr0py` - LGTM if all tests can pass. Assuming that model outputs are aligned on your side. (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3035418676)
- `2025-07-19T16:11:49Z` `APPROVED` by `DarkLight1337` - Same, thanks for working on this! (https://github.com/vllm-project/vllm/pull/20736#pullrequestreview-3035419839)

## Inline Comment Hotspots

- `vllm/config.py`: 8 inline comment(s)
- `benchmarks/kernels/benchmark_moe.py`: 5 inline comment(s)
- `vllm/model_executor/models/glm4_moe_mtp.py`: 3 inline comment(s)
- `vllm/model_executor/models/glm4_moe.py`: 2 inline comment(s)
- `vllm/transformers_utils/configs/ovis.py`: 2 inline comment(s)
- `benchmarks/kernels/benchmark_moe_permute_unpermute.py`: 2 inline comment(s)
- `tests/tool_use/test_glm4_moe_tool_parser.py`: 2 inline comment(s)
- `tests/models/registry.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-15T07:17:46Z` `inline` by `DarkLight1337` `benchmarks/kernels/benchmark_moe.py`:572; signals: benchmark, kernel, moe; excerpt: "Do all of these configs use moe intermediate size now?" (https://github.com/vllm-project/vllm/pull/20736#discussion_r2206623826)
- `2025-07-15T07:17:53Z` `inline` by `DarkLight1337` `benchmarks/kernels/benchmark_moe.py`:572; signals: benchmark, kernel, moe; excerpt: "cc @mgoin" (https://github.com/vllm-project/vllm/pull/20736#discussion_r2206624262)
- `2025-07-15T09:02:47Z` `inline` by `zRzRzRzRzRzRzR` `benchmarks/kernels/benchmark_moe.py`:572; signals: benchmark, kernel, moe; excerpt: "yes we use moe intermediate size." (https://github.com/vllm-project/vllm/pull/20736#discussion_r2206915431)
- `2025-07-15T09:04:16Z` `inline` by `zRzRzRzRzRzRzR` `benchmarks/kernels/benchmark_moe.py`:572; signals: benchmark, kernel, moe; excerpt: "Oh this model no I will put back this" (https://github.com/vllm-project/vllm/pull/20736#discussion_r2206918720)
- `2025-07-15T13:11:28Z` `inline` by `zRzRzRzRzRzRzR` `benchmarks/kernels/benchmark_moe_permute_unpermute.py`:327; signals: benchmark, kernel, moe; excerpt: "Now we use deepseek config" (https://github.com/vllm-project/vllm/pull/20736#discussion_r2207439974)
- `2025-07-15T14:46:33Z` `issue` by `zRzRzRzRzRzRzR`; signals: accuracy, alignment; excerpt: "We expect to conduct the test tomorrow, and we also need to complete the model accuracy alignment test using the vLLM model. If I ..." (https://github.com/vllm-project/vllm/pull/20736#issuecomment-3073926490)
- `2025-07-19T04:14:13Z` `issue` by `DarkLight1337`; signals: failing, moe; excerpt: "You can ignore the problem related to Voxtral. However, the GLM-4-MoE-MTP model is also failing the test which needs to be fixed here" (https://github.com/vllm-project/vllm/pull/20736#issuecomment-3091509340)
- `2025-07-11T14:21:53Z` `inline` by `zRzRzRzRzRzRzR` `vllm/transformers_utils/configs/ovis.py`:76; signals: register; excerpt: "This issue is because when transformers was upgraded to the latest version(main branch not release), aimv2 had already been registered, you need to modify ..." (https://github.com/vllm-project/vllm/pull/20736#discussion_r2200867608)
- `2025-07-16T16:29:33Z` `inline` by `luccafong` `vllm/config.py`:2782; signals: moe; excerpt: "we need also check if self.target model config.hf text config.model type is glm4 moe to assign the target model as draft in line 2689" (https://github.com/vllm-project/vllm/pull/20736#discussion_r2210917593)
- `2025-07-11T07:41:06Z` `inline` by `jeejeelee` `vllm/model_executor/models/glm4_moe.py`:465; signals: moe; excerpt: "Can we move the load weights to Glm4MoeModel, see:" (https://github.com/vllm-project/vllm/pull/20736#discussion_r2199929378)
- `2025-07-15T18:29:02Z` `inline` by `luccafong` `vllm/model_executor/models/glm4_moe_mtp.py`:224; signals: moe; excerpt: "check if get spec layer idx from weight name needs to be re-written for glm4 moe" (https://github.com/vllm-project/vllm/pull/20736#discussion_r2208312726)
