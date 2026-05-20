# PR Discussion Digest

- Source PR: [vllm-project/vllm#36574](https://github.com/vllm-project/vllm/pull/36574)
- Source page: `sources/prs/vllm/PR-36574.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36574`
- Generated at: `2026-05-20T15:40:13.285490+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-10T02:20:02Z`
- Merged: `2026-03-25T19:00:42Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 10 (approved=3, commented=7)
- Inline review comments: 7
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: SKPsanjeevi, dllehr-amd, gshtras, mergify, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-10T02:24:14Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for a persistent mode MLA decode kernel on ROCm, aimed at ... (https://github.com/vllm-project/vllm/pull/36574#pullrequestreview-3919290330)
- `2026-03-17T20:33:30Z` `COMMENTED` by `dllehr-amd` (https://github.com/vllm-project/vllm/pull/36574#pullrequestreview-3963608961)
- `2026-03-17T21:30:33Z` `COMMENTED` by `dllehr-amd` (https://github.com/vllm-project/vllm/pull/36574#pullrequestreview-3963872677)
- `2026-03-18T18:48:54Z` `COMMENTED` by `SKPsanjeevi` (https://github.com/vllm-project/vllm/pull/36574#pullrequestreview-3970114642)
- `2026-03-18T18:52:56Z` `COMMENTED` by `SKPsanjeevi` (https://github.com/vllm-project/vllm/pull/36574#pullrequestreview-3970140372)
- `2026-03-19T04:25:41Z` `COMMENTED` by `SKPsanjeevi` (https://github.com/vllm-project/vllm/pull/36574#pullrequestreview-3972775166)
- `2026-03-23T08:07:47Z` `COMMENTED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/36574#pullrequestreview-3989971232)
- `2026-03-24T22:00:23Z` `APPROVED` by `gshtras` (https://github.com/vllm-project/vllm/pull/36574#pullrequestreview-4002549073)
- `2026-03-25T06:08:31Z` `APPROVED` by `dllehr-amd` - Approved (https://github.com/vllm-project/vllm/pull/36574#pullrequestreview-4004241453)
- `2026-03-25T19:00:27Z` `APPROVED` by `tjtanaa` - LGTM. (https://github.com/vllm-project/vllm/pull/36574#pullrequestreview-4009110180)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`: 6 inline comment(s)
- `vllm/_aiter_ops.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-23T08:07:47Z` `inline` by `tjtanaa` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:126; signals: attention, kernel, mla, perf, regression; excerpt: "Would prefer the way it is because the improvements are noted for specifc models. Please share more information about this information. We should try ..." (https://github.com/vllm-project/vllm/pull/36574#discussion_r2973467693)
- `2026-03-25T14:53:49Z` `issue` by `tjtanaa`; signals: bf16, cache, fp8, mla; excerpt: "@SKPsanjeevi I am trying to validate this across different models to understand whether the constraint of using the MLA backend becomes smaller. Kimi K2.5 ..." (https://github.com/vllm-project/vllm/pull/36574#issuecomment-4127253070)
- `2026-03-25T15:41:48Z` `issue` by `SKPsanjeevi`; signals: hang, mla, perf, performance; excerpt: "@tjtanaa this particular PR does not change the existing constraint/limitations. It focuses only the performance. Current AITER MLA backend, I believe, supports only 16 ..." (https://github.com/vllm-project/vllm/pull/36574#issuecomment-4127638396)
- `2026-03-25T15:49:33Z` `issue` by `tjtanaa`; signals: hang, mla, perf, performance; excerpt: "@tjtanaa this particular PR does not change the existing constraint/limitations. It focuses only the performance. Current AITER MLA backend, I believe, supports only 16 ..." (https://github.com/vllm-project/vllm/pull/36574#issuecomment-4127700210)
- `2026-03-17T20:33:30Z` `inline` by `dllehr-amd` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:126; signals: attention, kernel, mla; excerpt: "we are now strongly discouraged from using ENVVARS for triggering paths. So in this case we need to decide whether to leave it all ..." (https://github.com/vllm-project/vllm/pull/36574#discussion_r2949419954)
- `2026-03-17T21:30:33Z` `inline` by `dllehr-amd` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:275; signals: attention, mla; excerpt: "why are we setting an intermediate variable here? this shouldn't be needed. In addition. I would strongly recommend we pass this information as part ..." (https://github.com/vllm-project/vllm/pull/36574#discussion_r2949667227)
- `2026-03-18T18:52:56Z` `inline` by `SKPsanjeevi` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:126; signals: attention, mla; excerpt: "Would prefer the way it is because the improvements are noted for specifc models. Once more datapoints emerge, we could flip the default to ..." (https://github.com/vllm-project/vllm/pull/36574#discussion_r2955570862)
- `2026-03-18T18:48:54Z` `inline` by `SKPsanjeevi` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:275; signals: attention, mla; excerpt: "updated" (https://github.com/vllm-project/vllm/pull/36574#discussion_r2955547248)
- `2026-03-19T04:25:40Z` `inline` by `SKPsanjeevi` `vllm/v1/attention/backends/mla/rocm_aiter_mla.py`:126; signals: attention, mla; excerpt: "Update: Removed the persistent env variable." (https://github.com/vllm-project/vllm/pull/36574#discussion_r2957785363)
- `2026-03-10T02:31:06Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @SKPsanjeevi, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/36574#issuecomment-4028171407)
- `2026-03-10T03:19:27Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @SKPsanjeevi, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/36574#issuecomment-4028333484)
- `2026-03-12T23:57:06Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @SKPsanjeevi, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/36574#issuecomment-4051183635)
