# PR Discussion Digest

- Source PR: [vllm-project/vllm#36022](https://github.com/vllm-project/vllm/pull/36022)
- Source page: `sources/prs/vllm/PR-36022.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-36022`
- Generated at: `2026-05-20T15:40:05.333757+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-04T17:01:52Z`
- Merged: `2026-03-16T06:45:32Z`

## Discussion Counts

- Issue comments: 23
- Review submissions: 12 (approved=1, commented=11)
- Inline review comments: 9
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=4
- Human participants with discussion text: bobboli, elvircrn, leo-cf-tian, llsj14, mergify, robertgshaw2-redhat, tlrmchlsmth, wzhao18
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2026-03-04T17:11:26Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces the FlashInfer MoE A2A kernel, which is a welcome addition for improving ... (https://github.com/vllm-project/vllm/pull/36022#pullrequestreview-3890805613)
- `2026-03-04T21:02:06Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36022#pullrequestreview-3891996228)
- `2026-03-04T21:03:00Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/36022#pullrequestreview-3892000249)
- `2026-03-04T21:37:59Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/36022#pullrequestreview-3892189379)
- `2026-03-04T22:45:46Z` `COMMENTED` by `leo-cf-tian` (https://github.com/vllm-project/vllm/pull/36022#pullrequestreview-3892480504)
- `2026-03-05T07:50:39Z` `COMMENTED` by `bobboli` (https://github.com/vllm-project/vllm/pull/36022#pullrequestreview-3894563437)
- `2026-03-05T16:17:41Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/36022#pullrequestreview-3897867058)
- `2026-03-09T08:47:49Z` `COMMENTED` by `llsj14` - Are there any reasons why the FlashInfer A2A kernel does not support BF16? From what I found, the ... (https://github.com/vllm-project/vllm/pull/36022#pullrequestreview-3913789435)
- `2026-03-14T21:27:25Z` `APPROVED` by `tlrmchlsmth` - This looks good to me, assuming we see correctness and are past the issue @elvircrn was running into (https://github.com/vllm-project/vllm/pull/36022#pullrequestreview-3949300476)
- `2026-03-15T21:24:15Z` `COMMENTED` by `tlrmchlsmth` - I'd like to get this into v0.18.0, which cuts tomorrow. Could you please fix the pre-commit issues? Looks ... (https://github.com/vllm-project/vllm/pull/36022#pullrequestreview-3950665756)
- `2026-03-16T03:06:00Z` `COMMENTED` by `tlrmchlsmth` - Could we get (https://github.com/vllm-project/vllm/pull/36022#pullrequestreview-3951209805)

## Inline Comment Hotspots

- `vllm/config/parallel.py`: 4 inline comment(s)
- `vllm/distributed/device_communicators/all2all.py`: 2 inline comment(s)
- `tests/kernels/moe/test_flashinfer_nvlink_one_sided.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/flashinfer_a2a_prepare_finalize.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-09T16:07:28Z` `issue` by `leo-cf-tian`; signals: bf16, dtype, flashinfer, fp4, kernel, nan, nvfp4, speedup; excerpt: "Are there any reasons why the FlashInfer A2A kernel does not support BF16? From what I found, the current FlashInfer A2A implementation only works ..." (https://github.com/vllm-project/vllm/pull/36022#issuecomment-4024894959)
- `2026-03-09T08:47:49Z` `review` `COMMENTED` by `llsj14`; signals: bf16, flashinfer, fp4, kernel, nan, nvfp4; excerpt: "Are there any reasons why the FlashInfer A2A kernel does not support BF16? From what I found, the current FlashInfer A2A implementation only works ..." (https://github.com/vllm-project/vllm/pull/36022#pullrequestreview-3913789435)
- `2026-03-10T19:34:23Z` `issue` by `elvircrn`; signals: b200, cuda, dtype, fp4, nvfp4; excerpt: "@leo-cf-tian Thank you for that info, I reverted back to 0.6.4 and ran into following issues which happen regardless of R1 NVFP4 model flavor: ..." (https://github.com/vllm-project/vllm/pull/36022#issuecomment-4033939199)
- `2026-03-16T03:05:58Z` `inline` by `tlrmchlsmth` `tests/kernels/moe/test_flashinfer_nvlink_one_sided.py`; signals: flashinfer, kernel, moe; excerpt: "@wzhao18 could you hook up this kernel to CI? needs to be added to .buildkite/test areas/kernels.yaml" (https://github.com/vllm-project/vllm/pull/36022#discussion_r2937922095)
- `2026-03-10T13:46:46Z` `issue` by `elvircrn`; signals: flashinfer, fp4, moe; excerpt: "Hi, thanks for the good work! While attempting to reproduce this via: I hit on flashinfer 0.6.5 with this PR on vllm with both ..." (https://github.com/vllm-project/vllm/pull/36022#issuecomment-4031503995)
- `2026-03-11T21:39:40Z` `issue` by `elvircrn`; signals: block, fp4, nvfp4; excerpt: "@wzhao18 Was able to get past the blocking trtllm scales issue now and got a good lm eval on gsm8k R1 NVFP4. This is ..." (https://github.com/vllm-project/vllm/pull/36022#issuecomment-4042396738)
- `2026-03-04T21:37:59Z` `inline` by `wzhao18` `vllm/config/parallel.py`:47; signals: flashinfer, kernel; excerpt: "The two flashinfer kernels correspond to the one-sided and two-sided A2A kernels in [TRTLLM]( It may be more informative to name them to something ..." (https://github.com/vllm-project/vllm/pull/36022#discussion_r2886267347)
- `2026-03-04T21:02:06Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/flashinfer_a2a_prepare_finalize.py`:229; signals: flashinfer, moe; excerpt: "Can you make a new file for this? and put it under the new prepare finalize directory" (https://github.com/vllm-project/vllm/pull/36022#discussion_r2886083735)
- `2026-03-04T23:04:10Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @leo-cf-tian, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/36022#issuecomment-4000856438)
- `2026-03-05T17:34:41Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @leo-cf-tian, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/36022#issuecomment-4006585995)
- `2026-03-10T15:50:20Z` `issue` by `leo-cf-tian`; signals: flashinfer, fp4; excerpt: "Hi @elvircrn, It is likely not a nvidia/DeepSeek-R1-0528-FP4-v2 specific issue as this is also the model we tested on. My guess would be the ..." (https://github.com/vllm-project/vllm/pull/36022#issuecomment-4032515800)
- `2026-03-10T20:22:55Z` `issue` by `elvircrn`; signals: b200, cuda; excerpt: "vllm hash: 106ff69c4eb4921d33341a96b9c3d6db9d12ba76 CUDA 13 GPU: GB200 Could it be that a recent vllm commit broke this? Would you mind attempting a rebase?" (https://github.com/vllm-project/vllm/pull/36022#issuecomment-4034210883)
