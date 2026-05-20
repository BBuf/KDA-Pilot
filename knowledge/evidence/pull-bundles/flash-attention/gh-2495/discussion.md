# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2495](https://github.com/Dao-AILab/flash-attention/pull/2495)
- Source page: `sources/prs/flash-attention/PR-2495.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2495`
- Generated at: `2026-05-20T15:17:09.698824+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-24T22:38:39Z`
- Merged: `2026-05-01T17:25:05Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 8
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=8, outdated=4
- Human participants with discussion text: copilot-pull-request-reviewer, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-24T23:49:20Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview This PR updates benchmarks/tune ex2 emu.py to better support tuning SM100 hd256 forward by sweeping ... (https://github.com/Dao-AILab/flash-attention/pull/2495#pullrequestreview-4174055980)
- `2026-04-27T02:42:27Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview Copilot reviewed 1 out of 1 changed files in this pull request and generated 3 ... (https://github.com/Dao-AILab/flash-attention/pull/2495#pullrequestreview-4177930899)
- `2026-05-01T16:37:31Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2495#pullrequestreview-4212173073)

## Inline Comment Hotspots

- `benchmarks/tune_ex2_emu.py`: 8 inline comment(s)

## High-Signal Discussion

- `2026-04-24T23:49:20Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: benchmark, hang, register, sm100; excerpt: "Pull request overview This PR updates benchmarks/tune ex2 emu.py to better support tuning SM100 hd256 forward by sweeping ex2 emu res for hd256 keys, ..." (https://github.com/Dao-AILab/flash-attention/pull/2495#pullrequestreview-4174055980)
- `2026-04-24T23:49:19Z` `inline` by `copilot-pull-request-reviewer` `benchmarks/tune_ex2_emu.py`:233; signals: benchmark, kernel, register, sm100; excerpt: "The script still only restores flash fwd sm100.py at the very end of main(). If the process is interrupted (Ctrl-C), crashes mid-sweep, or raises ..." (https://github.com/Dao-AILab/flash-attention/pull/2495#discussion_r3140818310)
- `2026-04-24T23:49:19Z` `inline` by `copilot-pull-request-reviewer` `benchmarks/tune_ex2_emu.py`:122; signals: benchmark, cuda, hang; excerpt: "query clocks() / lock clocks() run nvidia-smi without selecting a GPU, then read only the first line. On multi-GPU systems (especially when using CUDA ..." (https://github.com/Dao-AILab/flash-attention/pull/2495#discussion_r3140818295)
- `2026-04-27T02:42:27Z` `inline` by `copilot-pull-request-reviewer` `benchmarks/tune_ex2_emu.py`:113; signals: benchmark, block, hang; excerpt: "nvidia smi cmd() assumes os.geteuid() exists and that invoking sudo nvidia-smi ... is always safe. On non-POSIX platforms os.geteuid will raise, and on typical ..." (https://github.com/Dao-AILab/flash-attention/pull/2495#discussion_r3144658909)
- `2026-04-27T02:42:27Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: hang; excerpt: "Pull request overview Copilot reviewed 1 out of 1 changed files in this pull request and generated 3 comments. --- 💡 Add Copilot custom ..." (https://github.com/Dao-AILab/flash-attention/pull/2495#pullrequestreview-4177930899)
- `2026-04-24T23:49:18Z` `inline` by `copilot-pull-request-reviewer` `benchmarks/tune_ex2_emu.py`:272; signals: benchmark; excerpt: "The hd256 explanatory comment gives an example with freq=4, but freq values in this sweep never includes 4. Either add 4 to freq values ..." (https://github.com/Dao-AILab/flash-attention/pull/2495#discussion_r3140818272)
- `2026-04-24T23:49:19Z` `inline` by `copilot-pull-request-reviewer` `benchmarks/tune_ex2_emu.py`:180; signals: benchmark; excerpt: "The manual instructions printed in setup clocks() always include sudo ..., even when running as root (where nvidia smi cmd() intentionally omits sudo). Consider ..." (https://github.com/Dao-AILab/flash-attention/pull/2495#discussion_r3140818284)
- `2026-04-24T23:49:19Z` `inline` by `copilot-pull-request-reviewer` `benchmarks/tune_ex2_emu.py`:115; signals: benchmark; excerpt: "query clocks() assumes nvidia-smi returns at least one non-empty output line and that the first line contains two fields separated by ", ". If ..." (https://github.com/Dao-AILab/flash-attention/pull/2495#discussion_r3140818302)
- `2026-04-27T02:42:26Z` `inline` by `copilot-pull-request-reviewer` `benchmarks/tune_ex2_emu.py`:136; signals: benchmark; excerpt: "query clocks() documents returning (None, None) on failure, but subprocess.run will raise (e.g., FileNotFoundError if nvidia-smi/sudo is unavailable). Wrap the call in try/except and ..." (https://github.com/Dao-AILab/flash-attention/pull/2495#discussion_r3144658890)
- `2026-04-27T02:42:27Z` `inline` by `copilot-pull-request-reviewer` `benchmarks/tune_ex2_emu.py`:232; signals: benchmark; excerpt: "hdim v is parsed but never used. Consider either removing it or renaming to hdim v to make the intent explicit and avoid confusing ..." (https://github.com/Dao-AILab/flash-attention/pull/2495#discussion_r3144658901)
