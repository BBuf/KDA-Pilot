---
name: humanize-kernel-agent-loop
description: "Run an autonomous Humanize Kernel Agent Loop for GPU kernel optimization: plan/refine K/R/W into task-acceptance pairs, create a clean standalone repo, research with kernel-knowledge, iterate with benchmark/profile evidence, autotune across the workload distribution, emit kernels/dispatcher/tuning decisions, maintain ledgers, and start RLCR."
type: flow
---

# Humanize Kernel Agent Loop

Use this flow when the user wants an autonomous kernel optimization loop, not a
general software feature loop. This is a kernel-specialized wrapper around
Humanize RLCR.

## Algorithm Mapping

This skill follows the paper-style Humanize kernel loop architecture in a
KernelPilot standalone-repo variant. The input contract is:

```text
Require: kernel definition K, correctness reference R, workload distribution W
Ensure: kernel implementation K_hat that passes correctness checks on W and
        minimizes latency, plus dispatcher and tuning decisions when W contains
        multiple regimes.
```

The loop has three stages:

- Research: inspect the target kernel contract, baseline/reference behavior,
  workload distribution, repository context, and `kernel-knowledge` evidence.
  Extract implementation recipes, profile hypotheses, and benchmark priorities.
- Iterate: write candidate kernels in the standalone repo, compile, test,
  benchmark, profile with `ncu-report`/Nsight Compute when useful, query
  `kernel-knowledge` when prior art or hardware evidence can guide the next
  edit, and record every lineage decision.
- Autotune: scan the target workload distribution, benchmark selected variants
  or configurations, build a performance map, and emit a shape-aware dispatcher
  instead of forcing all shapes through one monolithic kernel.

Planning decomposes the work into task-acceptance pairs `P = {(t_i, ac_i)}`.
Each pair is executed until the review gate accepts the evidence:

```text
for each (t_i, ac_i) in P:
    done = false
    while not done:
        writer executes t_i in the standalone repo
        # inspect/edit code, compile, test, benchmark, profile, query evidence
        verdict, feedback = reviewer checks evidence against ac_i
        if verdict == pass:
            done = true
        else:
            writer refines the kernel using feedback
            # if blocked, consult reviewer/tool evidence; ask human only if still unresolved
return final kernels, dispatcher, and tuning decisions
```

In diagrams or papers that say "Claude executes, Codex reviews", read "Claude"
as "the current writer agent". In a Claude Code session that may be Claude; in
a Codex session that may be Codex. The review model is controlled by Humanize
configuration or CLI flags, not by this skill.

The installer hydrates these paths:

```text
Humanize runtime: {{HUMANIZE_RUNTIME_ROOT}}
KernelPilot root: {{KERNELPILOT_ROOT}}
```

If `{{KERNELPILOT_ROOT}}` was not hydrated, locate a repository containing
`knowledge/SKILL.md` and `knowledge/evidence/pull-bundles/`.

## Contract

Run the Humanize steps inside this skill. Do not ask the user to run separate
`gen-plan`, `refine-plan`, or `humanize-rlcr` commands.

Given a kernel task and target, you must recover or define `K`, `R`, and `W`,
then:

1. Build the kernel-specific task-acceptance plan yourself.
2. Refine it yourself.
3. Create or enter a clean standalone optimization repo.
4. Record the workload distribution `W` and benchmark/correctness contract.
5. Encode Stage 1 research, Stage 2 iteration, and Stage 3 autotuning as
   task-acceptance pairs in the refined plan.
6. Start Humanize RLCR on the refined plan.
7. Execute the current round until the Stop hook takes over. The current and
   later rounds run the research, implementation, profiling, benchmark,
   autotuning, dispatcher, and review tasks until accepted.

Ask the user only if the kernel definition `K`, correctness reference `R`,
workload distribution `W`, target GPU, comparison target, or hard scope
constraint is missing and cannot be inferred safely.
After those inputs exist, do not ask the user to approve each implementation
strategy, knowledge query, profiling run, benchmark expansion, or lineage reset.
The loop owns those tactical decisions and records the evidence behind them.

## Loop Defaults

- Candidate implementation language is autonomous unless the user explicitly
  fixes it. If the user specifies CUDA C++/PTX, Triton, CuTe DSL, TileLang,
  CUTLASS/CuTe, ThunderKittens, torch.compile/Inductor, or another kernel stack,
  use that stack.
- If the user does not specify a language, choose and revise the implementation
  system most likely to reach the stated correctness and performance target
  from local context, available baselines, prior art, benchmarks, and profiler
  evidence.
- Treat `W` as a workload distribution, not just a smoke test. If the user gives
  explicit benchmark cases, those cases define `W`. If the user gives a model,
  trace, or serving scenario, derive representative cases and record how they
  were sampled. If only one focused shape exists, record that `W` is a single
  regime and make the dispatcher/tuning decision trivial.
- Treat `kernel-knowledge` and `ncu-report`/Nsight Compute as autonomous tools
  for deciding what to try next. The user should not need to tell the loop when
  to research, profile, or switch implementation strategy.
- Treat "standalone" as a repository, build, benchmark, and runtime boundary.
  The candidate implementation, tests, benchmark harness, profile artifacts,
  and ledgers live in the isolated optimization repo.
- If external source directly affects code, record the exact source path/URL,
  commit or version, license/notice, copied/adapted files, and optimization
  delta in the attempt ledger or lineage.
- Keep the source framework checkout itself read-only for standalone work unless
  the user explicitly asks for an in-place framework patch.
- Run optimization work in a fresh standalone git repo with its own PyTorch
  binding, correctness tests, benchmark harness, ledgers, lineage, and profile
  artifacts.
- Every correct candidate attempt gets an attempt-ledger row. Only correct
  candidates that improve performance get an optimization-ledger row.
- Stage 1 research must leave a concise recipe/evidence artifact before the
  first serious optimization lineage. It should record source/baseline findings,
  candidate implementation routes, expected bottlenecks, and initial benchmark
  priorities. It is not a proof-of-reading ledger; it is the first decision map.
- Prefer collecting one baseline `ncu-report` digest for a representative case
  after baseline correctness/benchmark succeeds. Skip it when Nsight Compute is
  unavailable or when a cheaper measurement is sufficient for the current round,
  and record the reason.
- Use `ncu-report` again whenever profiler evidence is the best available way
  to explain a regression, plateau, surprising win, bottleneck shift, or next
  implementation edit.
- The loop remains incomplete while correctness, benchmark, provenance, lineage,
  workload coverage, dispatcher/tuning, or evidence gaps prevent a trustworthy
  autonomous next decision or final claim.

## Required Files In The Standalone Repo

Create these before starting RLCR, then keep them updated during the loop:

```text
.gitignore
.humanize/kernel-agent/refined-plan.md
README.md
workloads/
src/<task_name>/
bindings/
tests/
benchmarks/
dispatch/
ledgers/attempt-ledger.md
ledgers/optimization-ledger.md
ledgers/lineage.jsonl
ledgers/research-digest.md
ledgers/tuning-decisions.md
benchmarks/performance-map.json
profile-artifacts/README.md
```

The plan file may stay gitignored under `.humanize/` so RLCR can start without
tracking local loop state.

## Knowledge Evidence

KernelPilot provides three peer evidence routes. Use any route, or combine
routes, whenever evidence helps the current plan, implementation choice,
benchmark result, profile digest, plateau/regression explanation, reviewer
question, or next kernel edit.

- Local PR diffs and materialized source snapshots.
- External source-map repositories from `knowledge/index.json`.
- Live web search, official docs, GitHub PR pages, and related upstream source
  code.

The local knowledge base intentionally has no wiki, doc, blog, contest,
pseudocode, or generated topic-index fallback.

Useful entry points from `{{KERNELPILOT_ROOT}}/knowledge`:

```bash
cd {{KERNELPILOT_ROOT}}/knowledge
python3 scripts/query.py "tcgen05" --architecture B200 --limit 10
python3 scripts/search-pr-diffs.py tcgen05 tmem --any --limit 200
python3 scripts/query.py --repo pytorch/pytorch --compact
python3 scripts/get_page.py pr-pytorch-157241
```

`knowledge/index.json` may be used as a source-map reference for live research.
Clone command for the full referenced GitHub repo set:

```bash
python3 scripts/clone-index-repos.py
```

MUST NOT start searching any `index.json` repository before the full clone step
has completed. MUST NOT ignore the current kernel's operator, dtype,
architecture, or framework context during source-map searches.

```bash
python3 scripts/search-index-repos.py SplitKV Sm100 flash_fwd_sm100
```

Live web search, official docs, GitHub PR pages, and upstream source search are
equally valid. Prefer official docs and upstream source code over snippets when
implementation details matter.

Useful PR evidence paths:

```bash
cd {{KERNELPILOT_ROOT}}/knowledge
less evidence/pull-bundles/<repo-id>/gh-<number>/review.diff
find evidence/pull-bundles/<repo-id>/gh-<number>/source-snapshot -type f
```

Prefer materialized bundles under:

```text
knowledge/evidence/pull-bundles/<repo-id>/gh-<number>/
```

Each bundle should contain `review.diff`, `ORIGIN.yaml`, `upstream.json`,
and key changed source/test/benchmark files under `source-snapshot/`.

Typical query flow:

Guardrails for knowledge research:

1. MUST NOT claim full PR-route coverage without diff-level search across all
   repositories when the implementation detail matters.
2. MUST NOT borrow an idea from a PR page before opening the materialized
   `review.diff`, `ORIGIN.yaml`, `upstream.json`, and `source-snapshot/` files.
3. MUST NOT use `knowledge/index.json` source discovery before the complete
   referenced repo set has been cloned.
4. MUST NOT demote live web search, official docs, GitHub PR pages, or related
   upstream source code below the PR/source-map routes.

Shared example: for `FlashAttention SM100 SplitKV`, the PR route can find
`pr-flash-attention-1940`; the source-map route can search all cloned repos for
`SplitKV`, `Sm100`, and `flash_fwd_sm100`; the live route can search the
upstream FlashAttention PR/page and current upstream source.

A separate reading ledger is unnecessary just to prove that pages were opened.
When a source directly affects code, record the actionable provenance in the
relevant attempt row, lineage entry, or profile digest.

## Plan Requirements

Write `.humanize/kernel-agent/refined-plan.md` in the standalone repo. It must
use the Humanize gen-plan schema and include these acceptance criteria:

- Clean standalone repo exists and is committed before RLCR starts.
- Baseline framework checkout is protected from accidental edits unless the
  user asks for an in-place patch.
- Candidate implementation language is documented and follows the user request
  when fixed, otherwise the autonomous selected strategy.
- If external source seeds any candidate, provenance, license/notice,
  copied/adapted files, and the first optimization delta are recorded before
  further mutation.
- `K`, `R`, and `W` are explicit: the kernel semantics, correctness oracle,
  target workload distribution, target GPU, comparison baseline, and hard scope
  exclusions are recorded before the first candidate is selected.
- Correctness tests cover `W`, representative edge cases, dtype/layout/mode
  boundaries, and baseline/reference parity.
- Benchmark harness records per-shape timing, geomean, best/worst cases,
  workload coverage, and environment metadata.
- Stage 1 research digest records baseline/source findings, evidence from the
  selected route or routes that materially affects the plan, candidate
  implementation routes, suspected bottlenecks, and first benchmark/profile
  priorities.
- A baseline profile decision is recorded after baseline benchmark succeeds:
  either capture a representative `ncu-report` digest or explain why the loop is
  using cheaper evidence first.
- Later `ncu-report` profiles are captured autonomously when they are the best
  tool for regressions, plateaus, surprising wins, bottleneck shifts,
  profile-driven edits, or reviewer-requested evidence, then converted into NCU
  Report Digests.
- Attempt ledger records every version, including failed correctness,
  regressions, plateaus, and abandoned ideas.
- Optimization ledger records only correct versions with measured improvement.
- Lineage records parent version, mutation/motivation, influential source or PR
  evidence when it directly affects code, result, and selected/rejected status.
- Stage 3 autotuning builds a performance map over `W`, tests selected variants
  or configurations across all required regimes, and emits dispatcher/tuning
  decisions. If `W` is a single focused case, record why a trivial dispatcher is
  sufficient.
- The final answer and ledgers identify final kernels, fallback paths if any,
  dispatcher policy, tuning decisions, correctness matrix, benchmark matrix, and
  remaining unsupported regimes.
- When progress stalls, expand evidence research across the selected peer
  routes: unread PR bundles, cloned upstream source files, official docs,
  GitHub PR pages, linked tests, benchmarks, and profiler notes, guided by the
  current task context and existing attempt/lineage notes.
- When profiling shows a candidate is far below the target or in a different
  bottleneck class than the baseline, use the profile evidence to reassess the
  lineage. A useful next round either tests a concrete profile-driven edit,
  creates a smaller executable milestone, or records new evidence for
  continuing the current route.
- Experimental GPU kernels that can hang should use timeout-bounded bring-up
  milestones. A timeout marks that lineage rejected until a minimal executable
  tile validates the suspected protocol, descriptor, layout, memory, and
  synchronization semantics.
- Stop only when all ACs are met and the loop has either reached the stated
  target or recorded evidence that further autonomous optimization is no longer
  justified under the current scope, budget, and available implementation
  routes.

## Progress And Timeout Checks

- If an attempt times out or hangs, reproduce the failure with the smallest
  shape/tile under a hard timeout before any target-size benchmark. Record the
  rejected lineage and the suspected root-cause surface.
- If repeated reviews identify the same mainline blocker, narrow the next
  round to an executable milestone or design reset that can falsify the current
  hypothesis.
- If a candidate remains orders of magnitude below the target after a correct
  tensor-core-class attempt, treat further same-lineage tuning as evidence
  maintenance unless `ncu-report` names a specific low-risk edit with plausible
  order-of-magnitude impact.

## NCU Report Evidence

Invoke the `ncu-report` skill autonomously when profiler evidence is the best
next source of truth. These are heuristics, not user-facing gates:

- Baseline benchmark has passed and no baseline profile decision or NCU Report
  Digest exists.
- A correct candidate is within +/-2% of baseline across configured cases.
- A correct candidate regresses on one or more configured cases.
- The benchmark has plateaued or weakly improved and the next edit is unclear.
- A candidate is much faster than expected and needs explanation.
- A reviewer asks for an NCU Report Digest.

Persist `.ncu-rep`, raw CSV, source export, PM-sampling export when available,
and comparison paths in the digest. Each digest must end with one concrete next
kernel edit.

## RLCR Startup

After writing and committing the standalone repo scaffolding, start the loop
from inside the standalone repo:

```bash
"{{HUMANIZE_RUNTIME_ROOT}}/scripts/setup-rlcr-loop.sh" .humanize/kernel-agent/refined-plan.md --yolo
```

If setup exits non-zero, stop and report the error. Do not bypass the gate.
The loop uses Humanize's configured review model and default max iteration
limit unless the caller explicitly passes overrides such as `--max` or a model
flag. The current default max iteration limit is 84 rounds.

After setup succeeds:

1. Read `.humanize/rlcr/<timestamp>/round-0-prompt.md`.
2. Execute the current round.
3. Commit changes.
4. Write the required round summary.
5. Stop normally so the native Humanize Stop hook can review.

If the hook blocks exit, follow the generated next-round prompt exactly.
