# PR Discussion Digest

- Source PR: [vllm-project/vllm#23171](https://github.com/vllm-project/vllm/pull/23171)
- Source page: `sources/prs/vllm/PR-23171.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23171`
- Generated at: `2026-05-20T15:37:21.171398+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-19T09:26:29Z`
- Merged: `2025-08-25T09:09:36Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 22 (approved=2, commented=20)
- Inline review comments: 21
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=7
- Human participants with discussion text: Josephasafg, LucasWilkinson, ayushsatyam146, heheda12345, killershrimp, mergify
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-19T09:28:09Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request effectively unifies the attention backend selection logic for Mamba and standard attention layers, ... (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3131494483)
- `2025-08-19T09:59:36Z` `COMMENTED` by `ayushsatyam146` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3131595432)
- `2025-08-19T16:02:05Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3132960811)
- `2025-08-19T18:26:13Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3133384737)
- `2025-08-19T18:26:23Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3133385219)
- `2025-08-19T23:22:31Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3134236241)
- `2025-08-19T23:23:33Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3134239271)
- `2025-08-20T02:18:47Z` `COMMENTED` by `killershrimp` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3134566792)
- `2025-08-20T02:57:05Z` `COMMENTED` by `ayushsatyam146` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3134611444)
- `2025-08-20T02:58:43Z` `COMMENTED` by `ayushsatyam146` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3134613282)
- `2025-08-20T04:03:20Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3134712917)
- `2025-08-20T04:04:54Z` `COMMENTED` by `ayushsatyam146` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3134714686)
- `2025-08-20T04:08:15Z` `COMMENTED` by `heheda12345` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3134718454)
- `2025-08-20T05:39:26Z` `COMMENTED` by `ayushsatyam146` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3134848567)
- `2025-08-21T16:10:33Z` `COMMENTED` by `Josephasafg` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3141379178)
- `2025-08-21T16:11:51Z` `COMMENTED` by `ayushsatyam146` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3141383521)
- `2025-08-21T16:32:29Z` `COMMENTED` by `ayushsatyam146` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3141451920)
- `2025-08-24T18:46:18Z` `COMMENTED` by `heheda12345` - Thanks! Only a few small comments. (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3149470688)
- `2025-08-25T04:00:59Z` `COMMENTED` by `ayushsatyam146` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3149837717)
- `2025-08-25T04:01:20Z` `COMMENTED` by `ayushsatyam146` (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3149838090)
- `2025-08-25T04:42:46Z` `APPROVED` by `heheda12345` - LGTM! Thanks for the clean-up. (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3149888654)
- `2025-08-25T04:55:29Z` `APPROVED` by `LucasWilkinson` - LGTM; thanks for doing this! (https://github.com/vllm-project/vllm/pull/23171#pullrequestreview-3149904543)

## Inline Comment Hotspots

- `tests/v1/attention/test_mamba_selectors.py`: 12 inline comment(s)
- `vllm/v1/worker/gpu_model_runner.py`: 9 inline comment(s)

## High-Signal Discussion

- `2025-08-20T02:58:43Z` `inline` by `ayushsatyam146` `tests/v1/attention/test_mamba_selectors.py`:7; signals: attention, hang; excerpt: "Initially yapf and isort were negating each others changes, and it was stuck in a loop of pre-commit hooks. I won't need it after ..." (https://github.com/vllm-project/vllm/pull/23171#discussion_r2286857860)
- `2025-08-21T16:10:33Z` `inline` by `Josephasafg` `tests/v1/attention/test_mamba_selectors.py`:9; signals: attention, hang; excerpt: "I think the file name (and path) for the test should change since mamba selectors.py was removed" (https://github.com/vllm-project/vllm/pull/23171#discussion_r2291528480)
- `2025-08-21T16:34:55Z` `issue` by `ayushsatyam146`; signals: attention, hang; excerpt: "Hi @heheda12345 @LucasWilkinson @Josephasafg, this PR needed rebase because ShortConvAttentionBackend was added and my PR needed to accommodate it's changes as well. I have ..." (https://github.com/vllm-project/vllm/pull/23171#issuecomment-3211325447)
- `2025-08-19T18:26:13Z` `inline` by `LucasWilkinson` `vllm/v1/worker/gpu_model_runner.py`:2808; signals: attention; excerpt: "can we make a common ancestor for MambaBase and Attention maybe AttentionLayerBase with the abstract method .get attn backend()" (https://github.com/vllm-project/vllm/pull/23171#discussion_r2286010086)
- `2025-08-20T02:57:04Z` `inline` by `ayushsatyam146` `tests/v1/attention/test_mamba_selectors.py`:23; signals: attention; excerpt: "Thanks, this makes sense. I am sorry I am new to this project and didn't pay attention on this, thanks for pointing out." (https://github.com/vllm-project/vllm/pull/23171#discussion_r2286856258)
- `2025-08-20T04:04:54Z` `inline` by `ayushsatyam146` `tests/v1/attention/test_mamba_selectors.py`:7; signals: attention; excerpt: "I resolved it without needing to disable it. So I will remove it completely in next commit. Is that fine?" (https://github.com/vllm-project/vllm/pull/23171#discussion_r2286927028)
- `2025-08-24T18:43:58Z` `inline` by `heheda12345` `vllm/v1/worker/gpu_model_runner.py`:2770; signals: attention; excerpt: "nit: can you move attn layers = get layers from vllm config(self.vllm config, Attention) (line 2760 now) to the line that this variable is ..." (https://github.com/vllm-project/vllm/pull/23171#discussion_r2296766181)
- `2025-08-19T09:59:35Z` `inline` by `ayushsatyam146` `tests/v1/attention/test_mamba_selectors.py`:117; signals: attention; excerpt: "Improvement suggestion accepted" (https://github.com/vllm-project/vllm/pull/23171#discussion_r2284756533)
- `2025-08-19T23:23:33Z` `inline` by `heheda12345` `tests/v1/attention/test_mamba_selectors.py`:7; signals: attention; excerpt: "why do you need this?" (https://github.com/vllm-project/vllm/pull/23171#discussion_r2286600124)
- `2025-08-20T02:18:46Z` `inline` by `killershrimp` `tests/v1/attention/test_mamba_selectors.py`:23; signals: attention; excerpt: "maybe can use this existing fixture instead?" (https://github.com/vllm-project/vllm/pull/23171#discussion_r2286817701)
- `2025-08-20T04:03:20Z` `inline` by `heheda12345` `tests/v1/attention/test_mamba_selectors.py`:7; signals: attention; excerpt: "can you enable it after line 9?" (https://github.com/vllm-project/vllm/pull/23171#discussion_r2286925560)
- `2025-08-20T04:08:15Z` `inline` by `heheda12345` `tests/v1/attention/test_mamba_selectors.py`:7; signals: attention; excerpt: "That's great!" (https://github.com/vllm-project/vllm/pull/23171#discussion_r2286930105)
