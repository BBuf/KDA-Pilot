# PR Discussion Digest

- Source PR: [vllm-project/vllm#34109](https://github.com/vllm-project/vllm/pull/34109)
- Source page: `sources/prs/vllm/PR-34109.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-34109`
- Generated at: `2026-05-20T15:39:45.105606+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-09T02:47:44Z`
- Merged: `2026-02-26T03:17:21Z`

## Discussion Counts

- Issue comments: 21
- Review submissions: 12 (approved=4, commented=8)
- Inline review comments: 8
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: ProExpertProg, hjjq, ilmarkov, mergify, mgoin, wzhao18, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-09T02:48:54Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the FlashInfer all-reduce integration to use a new, more structured API. This ... (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3770932486)
- `2026-02-24T20:51:30Z` `COMMENTED` by `ProExpertProg` - Can you add a comment somewhere that the AR+rms fusion pass requires FI AR device communicator to be ... (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3850451205)
- `2026-02-24T21:09:59Z` `COMMENTED` by `ilmarkov` - Overall, looks good. Could you add a new AR in benchmarks/kernels/benchmark device communicators.py and compare it against the ... (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3850495172)
- `2026-02-25T01:56:42Z` `COMMENTED` by `ProExpertProg` - Re:communicator being needed for fusion pass (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3851408751)
- `2026-02-25T01:57:32Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3851412834)
- `2026-02-25T09:04:16Z` `APPROVED` by `ilmarkov` - Thanks for the update! LGTM (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3852814636)
- `2026-02-25T16:11:32Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3855274552)
- `2026-02-25T16:58:45Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3855543873)
- `2026-02-25T18:52:52Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3856182494)
- `2026-02-25T19:09:50Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3856288986)
- `2026-02-25T19:10:37Z` `COMMENTED` by `wzhao18` (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3856293225)
- `2026-02-26T00:54:20Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3857772469)

## Inline Comment Hotspots

- `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`: 5 inline comment(s)
- `vllm/distributed/device_communicators/flashinfer_all_reduce.py`: 2 inline comment(s)
- `vllm/distributed/device_communicators/cuda_communicator.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-24T21:09:59Z` `review` `COMMENTED` by `ilmarkov`; signals: benchmark, kernel, perf; excerpt: "Overall, looks good. Could you add a new AR in benchmarks/kernels/benchmark device communicators.py and compare it against the others so that it was possible ..." (https://github.com/vllm-project/vllm/pull/34109#pullrequestreview-3850495172)
- `2026-02-25T02:43:16Z` `issue` by `wzhao18`; signals: b200, benchmark, flashinfer, perf; excerpt: "@ilmarkov @ProExpertProg Thanks for reviewing! I added the flashinfer AR to benchmark device communicators.py. I included the results on B200 below. Among all the ..." (https://github.com/vllm-project/vllm/pull/34109#issuecomment-3956376768)
- `2026-02-24T21:00:18Z` `inline` by `ilmarkov` `vllm/distributed/device_communicators/cuda_communicator.py`:164; signals: benchmark, cuda, flashinfer; excerpt: "Do you have allreduce benchmark results to confirm that we want to use Flashinfer AR before Custom Allreduce and symm mem?" (https://github.com/vllm-project/vllm/pull/34109#discussion_r2849517993)
- `2026-02-10T02:10:51Z` `issue` by `yuan-luo`; signals: flashinfer, sm100, sm90; excerpt: "@hjjq Does this FI AR for MNNVL backend support SM90? I saw there was a restriction to use SM100+ in your code, but I ..." (https://github.com/vllm-project/vllm/pull/34109#issuecomment-3874914729)
- `2026-02-12T08:44:39Z` `issue` by `yuan-luo`; signals: cuda, sm100, sm90; excerpt: "@yuan-luo You're right, I think SM90 is supported but I didn't test it. You can try removing the SM100 check and see if it ..." (https://github.com/vllm-project/vllm/pull/34109#issuecomment-3889521078)
- `2026-02-24T21:02:23Z` `inline` by `ilmarkov` `vllm/distributed/device_communicators/flashinfer_all_reduce.py`:237; signals: flashinfer, perf; excerpt: "We need to pick max num tokens such that for this input FI AR performs better than alternatives." (https://github.com/vllm-project/vllm/pull/34109#discussion_r2849526975)
- `2026-02-10T02:26:58Z` `issue` by `hjjq`; signals: sm100, sm90; excerpt: "@yuan-luo You're right, I think SM90 is supported but I didn't test it. You can try removing the SM100 check and see if it ..." (https://github.com/vllm-project/vllm/pull/34109#issuecomment-3874961416)
- `2026-02-10T02:45:00Z` `issue` by `yuan-luo`; signals: sm100, sm90; excerpt: "@yuan-luo You're right, I think SM90 is supported but I didn't test it. You can try removing the SM100 check and see if it ..." (https://github.com/vllm-project/vllm/pull/34109#issuecomment-3875007468)
- `2026-02-12T22:26:17Z` `issue` by `hjjq`; signals: correctness, hang; excerpt: "I think the correctness issues I'm seeing is related to Pushed my changes to both backends simultaneously for now." (https://github.com/vllm-project/vllm/pull/34109#issuecomment-3893726962)
- `2026-02-24T20:19:08Z` `issue` by `wzhao18`; signals: accuracy, fp4; excerpt: "@ProExpertProg The accuracy issue has been resolved. In models with both ar-rms-fp4 and ar-rms, both mnnvl and trtllm backends will be used. This is ..." (https://github.com/vllm-project/vllm/pull/34109#issuecomment-3954499202)
- `2026-02-25T01:58:53Z` `issue` by `ProExpertProg`; signals: benchmark, hang; excerpt: "Okay given that the fusion pass does not require the FI device communicator, let's split this up into two separate PRs, one for fusion ..." (https://github.com/vllm-project/vllm/pull/34109#issuecomment-3956225518)
- `2026-02-25T02:34:51Z` `issue` by `mergify`; signals: failing, hang; excerpt: "Hi @hjjq, the pre-commit checks have failed. Please run: Then, commit the changes and push to your branch. For future commits, pre-commit will run ..." (https://github.com/vllm-project/vllm/pull/34109#issuecomment-3956352183)
