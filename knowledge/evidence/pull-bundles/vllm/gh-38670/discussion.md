# PR Discussion Digest

- Source PR: [vllm-project/vllm#38670](https://github.com/vllm-project/vllm/pull/38670)
- Source page: `sources/prs/vllm/PR-38670.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-38670`
- Generated at: `2026-05-20T15:40:36.900714+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-01T00:03:13Z`
- Merged: `2026-04-03T14:54:16Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 13 (approved=1, commented=12)
- Inline review comments: 14
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=2, outdated=3
- Human participants with discussion text: YM2132, mergify, yewentao256
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-04-01T00:08:26Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates determinism tests to use automatic data type selection and enhances the batch ... (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4040945047)
- `2026-04-01T06:36:09Z` `COMMENTED` by `YM2132` (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4042020915)
- `2026-04-01T17:12:00Z` `COMMENTED` by `YM2132` (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4045733240)
- `2026-04-01T21:09:53Z` `COMMENTED` by `yewentao256` - Thanks for the work! Verified this works on H200 as well (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4047107398)
- `2026-04-01T22:20:00Z` `COMMENTED` by `YM2132` (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4047398936)
- `2026-04-01T22:20:45Z` `COMMENTED` by `YM2132` (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4047401090)
- `2026-04-02T13:32:02Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4050684865)
- `2026-04-02T17:19:40Z` `COMMENTED` by `YM2132` (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4052046645)
- `2026-04-02T17:55:52Z` `COMMENTED` by `YM2132` (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4052246805)
- `2026-04-02T18:56:55Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4052579590)
- `2026-04-03T07:11:36Z` `COMMENTED` by `YM2132` (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4054588645)
- `2026-04-03T08:42:55Z` `COMMENTED` by `YM2132` (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4054870585)
- `2026-04-03T13:28:36Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4055730511)

## Inline Comment Hotspots

- `vllm/model_executor/layers/batch_invariant.py`: 12 inline comment(s)
- `vllm/model_executor/layers/quantization/awq.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-03T07:11:36Z` `inline` by `YM2132` `vllm/model_executor/layers/batch_invariant.py`:180; signals: block, h200, hang, regression; excerpt: "I made a change in latest commit, which dynamically sets the block size now. Could you please test on h200 to confirm no regression?" (https://github.com/vllm-project/vllm/pull/38670#discussion_r3031757908)
- `2026-04-01T22:20:44Z` `inline` by `YM2132` `vllm/model_executor/layers/batch_invariant.py`:180; signals: hang, memory, shared memory; excerpt: "Yes and no. This is needed for SM 86 GPUs (e.g. RTX 3090 and other 80 series) which have 101KB shared memory per SM ..." (https://github.com/vllm-project/vllm/pull/38670#discussion_r3024948591)
- `2026-04-02T17:55:51Z` `inline` by `YM2132` `vllm/model_executor/layers/batch_invariant.py`:180; signals: block, memory, shared memory; excerpt: "Hi @yewentao256, perhaps for this part we could introduce a per SM check and then decide the block size based on that? There exists ..." (https://github.com/vllm-project/vllm/pull/38670#discussion_r3029496175)
- `2026-04-01T17:12:00Z` `inline` by `YM2132` `vllm/model_executor/layers/batch_invariant.py`:180; signals: block, hang; excerpt: "I am not sure it is needed to change the BLOCK SIZE N in bmm batch invariant, I would appreciate the advice of the ..." (https://github.com/vllm-project/vllm/pull/38670#discussion_r3023461057)
- `2026-04-01T21:09:53Z` `review` `COMMENTED` by `yewentao256`; signals: h200; excerpt: "Thanks for the work! Verified this works on H200 as well" (https://github.com/vllm-project/vllm/pull/38670#pullrequestreview-4047107398)
- `2026-04-03T07:16:20Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @YM2132, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/38670#issuecomment-4182274291)
- `2026-04-01T22:20:00Z` `inline` by `YM2132` `vllm/model_executor/layers/batch_invariant.py`:943; signals: hang; excerpt: "Yes family 80 would cover 89, I think given 38427 is going to be merged this change is resolved. Shall I wait for that ..." (https://github.com/vllm-project/vllm/pull/38670#discussion_r3024946167)
- `2026-04-01T21:09:04Z` `inline` by `yewentao256` `vllm/model_executor/layers/batch_invariant.py`:180; signals: hang; excerpt: "I recommend not to change it as it is tuned, is this a must-have for the fix?" (https://github.com/vllm-project/vllm/pull/38670#discussion_r3024678168)
- `2026-04-01T06:41:27Z` `issue` by `YM2132`; signals: hang; excerpt: "Hi @yewentao256, this change is probably worth testing on newer hardware too. I only have a 3090 but if someone has a more recent ..." (https://github.com/vllm-project/vllm/pull/38670#issuecomment-4167891361)
- `2026-04-01T22:22:44Z` `issue` by `YM2132`; signals: h200; excerpt: "Thanks for the work! Verified this works on H200 as well Happy to help! Nice, good to know it works on other hardware. Looking ..." (https://github.com/vllm-project/vllm/pull/38670#issuecomment-4173314340)
- `2026-04-01T06:36:08Z` `inline` by `YM2132` `vllm/model_executor/layers/quantization/awq.py`:278; signals: general review; excerpt: "Resolved - moved imports to top of files" (https://github.com/vllm-project/vllm/pull/38670#discussion_r3020098089)
- `2026-04-01T21:09:30Z` `inline` by `yewentao256` `vllm/model_executor/layers/batch_invariant.py`:943; signals: general review; excerpt: "Would family(80) covers 89?" (https://github.com/vllm-project/vllm/pull/38670#discussion_r3024679945)
