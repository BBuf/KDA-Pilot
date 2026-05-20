# PR Discussion Digest

- Source PR: [sgl-project/sglang#22822](https://github.com/sgl-project/sglang/pull/22822)
- Source page: `sources/prs/sglang/PR-22822.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22822`
- Generated at: `2026-05-20T15:29:32.570637+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-14T19:25:18Z`
- Merged: `2026-05-18T01:36:43Z`

## Discussion Counts

- Issue comments: 12
- Review submissions: 11 (approved=2, commented=9)
- Inline review comments: 22
- Review threads observed: 18
- Resolved/outdated thread markers: resolved=18, outdated=14
- Human participants with discussion text: OrangeRedeng, ch-wan, iforgetmyname, ping1jing2
- Automation comments/reviews omitted from high-signal summary: 15
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-05T08:26:49Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the DeepEP dispatcher to use a structured DeepOutputDtype and a new server ... (https://github.com/sgl-project/sglang/pull/22822#pullrequestreview-4226381347)
- `2026-05-08T06:14:29Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/22822#pullrequestreview-4248652814)
- `2026-05-08T09:39:47Z` `COMMENTED` by `OrangeRedeng` (https://github.com/sgl-project/sglang/pull/22822#pullrequestreview-4251220867)
- `2026-05-08T09:59:00Z` `COMMENTED` by `OrangeRedeng` (https://github.com/sgl-project/sglang/pull/22822#pullrequestreview-4251361474)
- `2026-05-08T10:23:12Z` `COMMENTED` by `OrangeRedeng` (https://github.com/sgl-project/sglang/pull/22822#pullrequestreview-4251519988)
- `2026-05-10T23:08:55Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/22822#pullrequestreview-4260035196)
- `2026-05-10T23:12:19Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/22822#pullrequestreview-4260043605)
- `2026-05-13T10:23:18Z` `APPROVED` by `ch-wan` - LGTM. We can merge it when it passes all CI tests. (https://github.com/sgl-project/sglang/pull/22822#pullrequestreview-4280589485)
- `2026-05-14T11:54:35Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces the --deepep-dispatcher-output-dtype server argument to replace deprecated environment variables for DeepEP configuration, ... (https://github.com/sgl-project/sglang/pull/22822#pullrequestreview-4289670809)
- `2026-05-14T13:16:18Z` `COMMENTED` by `OrangeRedeng` (https://github.com/sgl-project/sglang/pull/22822#pullrequestreview-4290205693)
- `2026-05-18T01:34:51Z` `APPROVED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/22822#pullrequestreview-4275443534)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/utils.py`: 6 inline comment(s)
- `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`: 4 inline comment(s)
- `python/sglang/srt/server_args.py`: 2 inline comment(s)
- `python/sglang/srt/environ.py`: 2 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 2 inline comment(s)
- `test/registered/4-gpu-models/test_deepseek_v3_cutedsl_4gpu.py`: 2 inline comment(s)
- `test/manual/layers/moe/test_moe_runners_4gpu.py`: 1 inline comment(s)
- `test/manual/test_w4a8_deepseek_v3.py`: 1 inline comment(s)
- `docs/platforms/ascend/ascend_npu_best_practice.md`: 1 inline comment(s)
- `python/sglang/srt/layers/quantization/compressed_tensors/schemes/compressed_tensors_wNa16_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-15T07:43:37Z` `issue` by `OrangeRedeng`; signals: bf16, dtype, fp4, fp8, nvfp4; excerpt: "yes, export SGLANG DEEPEP BF16 DISPATCH=1 hase been deleted. you can fix the bug and restore SGLANG DEEPEP BF16 DISPATCH=1 functionality，but FP8 DISPATCH may ..." (https://github.com/sgl-project/sglang/pull/22822#issuecomment-4250167767)
- `2026-04-15T07:13:48Z` `issue` by `iforgetmyname`; signals: bf16, dtype, fp8; excerpt: "yes, export SGLANG DEEPEP BF16 DISPATCH=1 hase been deleted. you can fix the bug and restore SGLANG DEEPEP BF16 DISPATCH=1 functionality，but FP8 DISPATCH may ..." (https://github.com/sgl-project/sglang/pull/22822#issuecomment-4250010438)
- `2026-05-08T02:29:39Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/utils.py`:196; signals: dtype, moe; excerpt: "We can directly pass output dtype to dispatcher's quant config. This would simplify code logic here." (https://github.com/sgl-project/sglang/pull/22822#discussion_r3205896404)
- `2026-04-15T06:38:19Z` `issue` by `OrangeRedeng`; signals: bf16, fp8; excerpt: "OK, but for users, right now there’s no assertion, so it defaults to FP8.However, setting the env var export SGLANG DEEPEP BF16 DISPATCH=1 will ..." (https://github.com/sgl-project/sglang/pull/22822#issuecomment-4249842622)
- `2026-05-08T10:23:11Z` `inline` by `OrangeRedeng` `python/sglang/srt/layers/moe/utils.py`:196; signals: moe; excerpt: "Thanks for the suggestion! Now the output type of the dispatcher is parsed directly from the quantization config, which reduces the amount of code" (https://github.com/sgl-project/sglang/pull/22822#discussion_r3208024216)
- `2026-05-08T03:08:12Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/layer.py`:54; signals: moe; excerpt: "can we remove this?" (https://github.com/sgl-project/sglang/pull/22822#discussion_r3206032057)
- `2026-05-08T09:39:47Z` `inline` by `OrangeRedeng` `python/sglang/srt/layers/moe/ep_moe/layer.py`:54; signals: moe; excerpt: "Of course! Thanks for detecting this artifacts after the pre-commit" (https://github.com/sgl-project/sglang/pull/22822#discussion_r3207793763)
- `2026-05-14T13:16:18Z` `inline` by `OrangeRedeng` `python/sglang/srt/layers/moe/token_dispatcher/deepep.py`:331; signals: moe; excerpt: "346 string - self.quant config: Optional[dict] = None" (https://github.com/sgl-project/sglang/pull/22822#discussion_r3241576660)
- `2026-05-08T09:59:00Z` `inline` by `OrangeRedeng` `python/sglang/srt/environ.py`:414; signals: general review; excerpt: "Thanks for the helpful suggestion! The variable has been restored, deprecation warnings have been added." (https://github.com/sgl-project/sglang/pull/22822#discussion_r3207900360)
- `2026-05-08T00:52:15Z` `inline` by `ch-wan` `python/sglang/srt/environ.py`:414; signals: general review; excerpt: "We'd better keep it for backward compatibility and add a deprecation message." (https://github.com/sgl-project/sglang/pull/22822#discussion_r3205550997)
