# PR Discussion Digest

- Source PR: [vllm-project/vllm#30647](https://github.com/vllm-project/vllm/pull/30647)
- Source page: `sources/prs/vllm/PR-30647.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-30647`
- Generated at: `2026-05-20T15:39:04.026745+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-14T13:40:05Z`
- Merged: `2026-03-18T15:01:27Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 23 (approved=3, commented=20)
- Inline review comments: 19
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=0, outdated=4
- Human participants with discussion text: BowenBao, ProExpertProg, bnellnm, chatgpt-codex-connector, elvischenv, mergify, nvpohanh, zyongye
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-12-14T13:42:20Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a performance optimization for Mixture-of-Experts (MoE) layers in GPT-OSS models using Flashinfer ... (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3575308859)
- `2025-12-18T23:58:57Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review . Because moe config.hidden dim stays at the unpadded value, any DP+EP run that uses ... (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3595754666)
- `2026-02-07T15:28:24Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3767299282)
- `2026-02-07T17:51:14Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3767492453)
- `2026-02-07T23:23:48Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3768425110)
- `2026-02-08T14:09:41Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3769800273)
- `2026-02-08T14:10:48Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3769802228)
- `2026-02-08T14:19:35Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3769814633)
- `2026-02-09T03:26:35Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3770988807)
- `2026-02-10T18:10:28Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3780700202)
- `2026-02-10T18:12:08Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3780708624)
- `2026-02-10T18:16:44Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3780729126)
- `2026-02-11T03:04:21Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3782602779)
- `2026-02-11T14:01:15Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3785008960)
- `2026-02-13T00:58:51Z` `COMMENTED` by `BowenBao` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3794503221)
- `2026-02-13T03:05:36Z` `COMMENTED` by `nvpohanh` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3794797239)
- `2026-02-13T03:45:51Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3794888731)
- `2026-02-13T19:34:57Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3799125431)
- `2026-03-16T22:31:15Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3957055952)
- `2026-03-17T19:53:28Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3963392851)
- `2026-03-18T06:34:01Z` `COMMENTED` by `elvischenv` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3965421190)
- `2026-03-18T12:20:11Z` `APPROVED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3967415653)
- `2026-03-18T13:55:03Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3968027211)

## Inline Comment Hotspots

- `tests/compile/fusions_e2e/conftest.py`: 9 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 8 inline comment(s)
- `vllm/model_executor/layers/fused_moe/runner/default_moe_runner.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-02-07T23:23:48Z` `inline` by `elvischenv` `tests/compile/fusions_e2e/conftest.py`:69; signals: compile, flashinfer, fp4, fp8, kernel, moe, mxfp4; excerpt: "Do you mean we want to deprecate the kernel envs(e.g. VLLM USE FLASHINFER MOE MXFP4 MXFP8), and migrate to KernelConfig(e.g. use flashinfer moe mxfp4 ..." (https://github.com/vllm-project/vllm/pull/30647#discussion_r2778223785)
- `2026-02-13T03:05:35Z` `inline` by `nvpohanh` `tests/compile/fusions_e2e/conftest.py`:69; signals: compile, flashinfer, fp4, fp8, moe, mxfp4; excerpt: "My original proposal would be make it part of the quantization config. for example: --quantization mxfp4 mxfp8 act @elvischenv Could you open a GitHub ..." (https://github.com/vllm-project/vllm/pull/30647#discussion_r2802043745)
- `2026-02-13T03:45:51Z` `inline` by `elvischenv` `tests/compile/fusions_e2e/conftest.py`:69; signals: compile, flashinfer, fp4, fp8, moe, mxfp4; excerpt: "Could you open a GitHub issue so that we can discuss how to eliminate VLLM USE FLASHINFER MOE MXFP4 MXFP8? Created 34486" (https://github.com/vllm-project/vllm/pull/30647#discussion_r2802126962)
- `2025-12-18T23:58:57Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: aligned, kernel, memory, moe; excerpt: "💡 Codex Review . Because moe config.hidden dim stays at the unpadded value, any DP+EP run that uses the all2all kernels will size dispatch ..." (https://github.com/vllm-project/vllm/pull/30647#pullrequestreview-3595754666)
- `2026-02-10T18:10:28Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/layer.py`:268; signals: fp4, kernel, moe, mxfp4; excerpt: "I just ran into a situation where the mxfp4 marlin kernels require 256 element padding. Will this PR also address that or is it ..." (https://github.com/vllm-project/vllm/pull/30647#discussion_r2789494317)
- `2026-02-11T03:00:35Z` `inline` by `elvischenv` `vllm/model_executor/layers/fused_moe/layer.py`:268; signals: fp4, moe, mxfp4; excerpt: "If you look into the create weights() inside vllm/model executor/layers/quantization/mxfp4.py, you will see a completely duplicated logic with this function. So the current padding ..." (https://github.com/vllm-project/vllm/pull/30647#discussion_r2791200600)
- `2026-02-11T03:04:15Z` `inline` by `elvischenv` `vllm/model_executor/layers/fused_moe/layer.py`:578; signals: fp4, moe, mxfp4; excerpt: "Answered in the previous comment. The calling order is like maybe roundup hidden size - create MoE config self.moe config: FusedMoEConfig = FusedMoEConfig() - ..." (https://github.com/vllm-project/vllm/pull/30647#discussion_r2791208248)
- `2026-02-09T03:29:00Z` `issue` by `elvischenv`; signals: accuracy, benchmark, perf; excerpt: "@elvischenv could you post the new benchmarking numbers once you have them? This is the perf number based on main ToT: PR main accuracy ..." (https://github.com/vllm-project/vllm/pull/30647#issuecomment-3869086652)
- `2026-02-08T14:10:48Z` `inline` by `ProExpertProg` `tests/compile/fusions_e2e/conftest.py`:69; signals: compile, kernel; excerpt: "But yeah for E2E tests this is fine for now. Later once migrated to kernel config, we can just add it to model kwargs!" (https://github.com/vllm-project/vllm/pull/30647#discussion_r2779319915)
- `2026-02-13T00:58:51Z` `inline` by `BowenBao` `vllm/model_executor/layers/fused_moe/layer.py`:578; signals: kernel, moe; excerpt: "fyi I have a (wip) draft to refactor the roundup logic at 34285, to move the kernel dependent rounding logic to quant method. fused ..." (https://github.com/vllm-project/vllm/pull/30647#discussion_r2801767680)
- `2026-02-07T17:51:14Z` `inline` by `ProExpertProg` `tests/compile/fusions_e2e/conftest.py`:69; signals: compile, kernel; excerpt: "KernelConfig was just merged recently, you can add to that!" (https://github.com/vllm-project/vllm/pull/30647#discussion_r2777853575)
- `2026-02-04T06:14:06Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @elvischenv, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/30647#issuecomment-3845569999)
