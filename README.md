<div align="center">

# KernelPilot

**An autonomous Humanize-powered GPU kernel optimization loop with peer
evidence routes, Nsight Compute report skills, and clean standalone benchmark
repos.**

[![GitHub stars](https://img.shields.io/github/stars/BBuf/kernel-pilot?style=social)](https://github.com/BBuf/kernel-pilot/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/BBuf/kernel-pilot?style=social)](https://github.com/BBuf/kernel-pilot/forks)
[![Last commit](https://img.shields.io/github/last-commit/BBuf/kernel-pilot?style=flat-square)](https://github.com/BBuf/kernel-pilot/commits/main)
[![PR evidence](https://img.shields.io/badge/PR_evidence-3827-2ea44f?style=flat-square)](knowledge/evidence/pull-bundles/)
[![Knowledge cutoff](https://img.shields.io/badge/cutoff-2026--05--20-8250df?style=flat-square)](knowledge/data/refresh-cutoff.yaml)

</div>

KernelPilot is for serious CUDA kernel tuning runs where the important facts
are easy to lose: which upstream PR inspired a candidate, which shape regressed,
what Nsight Compute actually said, which evidence changed the next edit, and
whether the candidate belongs in a framework repo or a clean experiment.

The project packages three cooperating skills:

| Skill | Role |
| --- | --- |
| [`humanize-kernel-agent-loop`](humanize/skills/humanize-kernel-agent-loop/) | Turns kernel definition `K`, reference `R`, and workload distribution `W` into task-acceptance pairs, a standalone optimization repo, autonomous research/iteration/autotuning, correctness tests, benchmarks, ledgers, dispatcher, tuning decisions, and review-gated iteration. |
| [`kernel-knowledge`](knowledge/SKILL.md) | Kernel evidence acquisition through peer routes: local PR diffs, cloned external source-map repos, and live web/official/upstream source research. |
| [`ncu-report`](humanize/skills/ncu-report/) | Converts Nsight Compute reports into a reproducible profile digest: metrics, source counters, PM sampling, PTX/SASS hotspots, bottleneck diagnosis, and exactly one next kernel edit. |

Together they make an optimization loop that can work from a simple request:

```text
[$humanize-kernel-agent-loop] Optimize SGLang's GEMM path for M=64, N=2048, K=2048, fp16, bias=true, and beat the current SGLang baseline by at least 10%.
```

The loop decides how to plan, when to query knowledge, what to profile, how to
record lineage, how to scan the workload distribution, and when to ask the
Humanize review gate whether another round is needed. The human should specify
the target when it is ambiguous; the loop owns the rest.

## Why Use It

- **Peer evidence routes.** The agent can use local PR diffs, cloned upstream
  source-map repositories, and live web/official/upstream research as equal
  ways to gather kernel evidence.
- **Standalone by default.** Candidate kernels do not pollute SGLang, vLLM,
  PyTorch, or other large framework repos. The loop creates an isolated repo
  with bindings, tests, benchmarks, ledgers, lineage, and profile artifacts.
  The standalone repo is where implementation artifacts, provenance, and
  measurements live.
- **Evidence-driven profiling.** The loop decides when `ncu-report` is worth
  running, then uses it to move from vague labels like "memory-bound" toward
  measured bottlenecks and one concrete next edit.
- **Evidence-backed edits.** The agent draws on local upstream PR diffs, cloned
  source-map repositories, and live web/official/upstream source research as
  peer evidence routes, widening the search inside a route or cross-checking
  against another route before letting a thin match shape the kernel.
- **Review-gated iteration.** Humanize RLCR keeps the loop from declaring
  victory too early; default loop budget is 84 iterations unless configured
  otherwise.
- **Shape-aware tuning.** The loop treats benchmark cases as a workload
  distribution, builds a performance map, and emits dispatcher/tuning decisions
  when different regimes need different kernels or configurations.

## Kernel Agent Loop

```mermaid
flowchart LR
    K[Kernel definition K] --> P[Plan P = task and AC pairs]
    R[Correctness reference R] --> P
    W[Workload distribution W] --> P
    P --> S[Clean standalone repo]

    subgraph R0[Stage 1: Research]
        KW[kernel-knowledge / evidence routes]
        B[Baseline and repo inspection]
        RD[Research digest and recipes]
        KW --> RD
        B --> RD
    end

    subgraph I0[Stage 2: Iterate]
        T[Writer executes task t_i]
        E[Inspect, edit, compile, test, benchmark, profile]
        V{Reviewer checks evidence vs ac_i}
        T --> E --> V
        V -->|blocked feedback| T
    end

    subgraph A0[Stage 3: Autotune]
        PM[Performance map over W]
        D[Shape-aware dispatcher]
        TD[Tuning decisions]
        PM --> D --> TD
    end

    S --> RD --> T
    V -->|pass| PM
    E -->|profile evidence needed| NCU[ncu-report / Nsight Compute]
    NCU --> T
    E -->|prior art needed| KW
    TD --> O[Final kernels, dispatcher, correctness/benchmark matrix, fallback paths, unsupported regimes]
```

The writer agent is not hardcoded. In Codex it can be Codex; in Claude Code it
can be Claude. The review backend and model come from Humanize configuration.
Unlike the paper's in-repository version, KernelPilot keeps implementation
artifacts in a clean standalone repo unless the user explicitly asks for an
in-place framework patch.

## Kernel Requests

A useful request names the kernel definition, correctness reference, workload
distribution, target hardware, scope, benchmark method, and performance target.
KernelPilot turns that into a task-acceptance plan, an isolated implementation
workspace, repeatable measurements, profiler evidence, lineage, performance
map, dispatcher/tuning decisions, and Humanize review rounds.

Existing implementations, PR diffs, live upstream sources, official docs, and
profile reports are working materials for the loop. When external source or
design evidence materially influences a candidate, the standalone repo records
the provenance, license or notice requirements, and the optimization delta.

## Knowledge Base

The knowledge base lives in [`knowledge/`](knowledge/). It is a local skill root
and does not need a global environment variable for normal query use.

Current snapshot:

| Corpus layer | Contents |
| --- | --- |
| PR evidence | 3,827 merged CUDA/Triton/CuTe/CUTLASS-related PR pages and bundles from 14 upstream repos (SGLang, vLLM, TensorRT-LLM, PyTorch, FlashAttention, FlashInfer, CUTLASS/CuTe, CCCL, Triton, DeepGEMM, ThunderKittens, TileLang, QuACK, DeepSeek TileKernels), Jan 2024 through May 20 2026. |
| External source map | `knowledge/index.json` points at the **complementary** code repositories not in the PR corpus (NVIDIA developer samples, Colfax research kernels, simveit micro-tutorials) for live clone/search workflows. |
| Candidate ledgers | 14 include/defer ledgers for PR ingestion. Dropped PRs are not kept as per-PR rows. |

Primary organization:

```text
knowledge/
|-- SKILL.md
|-- README.md
|-- scripts/
|   |-- query.py
|   |-- get_page.py
|   |-- fetch-pr-evidence.py
|   `-- validate.py
|-- sources/
|   `-- prs/
|-- evidence/
|   `-- pull-bundles/
|-- candidates/
`-- data/
```

The important rule is **no local summaries as evidence**. The supported routes
are local PR diffs, cloned source-map repositories, and live web/official/
upstream source research. There is no local wiki/doc/blog/contest fallback.

`knowledge/index.json` is kept as an external source map over the
complementary repositories not covered by the PR corpus. Working with it is a
two-step flow: clone the referenced repos with `scripts/clone-index-repos.py`,
then grep them with `scripts/search-index-repos.py`. The search script enforces
the clone step, so the clone is the only gate.

## Query Examples

Run knowledge tools from the knowledge root:

```bash
cd knowledge
python3 scripts/query.py "tcgen05" --architecture B200 --limit 10
python3 scripts/search-pr-diffs.py tcgen05 tmem --any --limit 200
python3 scripts/query.py --repo pytorch/pytorch --compact
python3 scripts/get_page.py pr-pytorch-157241
python3 scripts/clone-index-repos.py
python3 scripts/search-index-repos.py tma swizzle transpose
python3 scripts/validate.py
```

## ncu-report

`ncu-report` standardizes the profiling part of the loop. It creates a digest
that compares a candidate to a baseline or parent version and ends with one
specific edit to try next.

Typical capture:

```bash
mkdir -p profile-artifacts/v000_baseline
ncu --target-processes all \
    --kernel-name regex:"<kernel-name-pattern>" \
    --launch-skip 5 --launch-count 1 \
    --set full --import-source on \
    --section SpeedOfLight \
    --section SchedulerStats \
    --section WarpStateStats \
    --section Occupancy \
    --section LaunchStats \
    --section MemoryWorkloadAnalysis \
    --section SourceCounters \
    -o profile-artifacts/v000_baseline/report \
    python benchmarks/<bench>.py --shape <shape> --dtype <dtype>

ncu --import profile-artifacts/v000_baseline/report.ncu-rep \
    --page raw --csv > profile-artifacts/v000_baseline/raw.csv
ncu --import profile-artifacts/v000_baseline/report.ncu-rep \
    --page details > profile-artifacts/v000_baseline/details.txt
```

The skill inspects SpeedOfLight, scheduler stats, warp state stalls, occupancy,
launch stats, memory workload, source counters, PM sampling when the installed
NCU exposes it, and when relevant PTX/SASS dumps from `cuobjdump` or
`nvdisasm`.

## Install

KernelPilot is not Codex-only. It can be used from Claude Code, Codex, or Kimi.

### Claude Code

Install the Humanize plugin from this repository, then expose the KernelPilot
knowledge skill to Claude Code:

```bash
git clone https://github.com/BBuf/kernel-pilot.git
cd kernel-pilot

# Add the KernelPilot marketplace and install its Humanize plugin.
humanize/scripts/install-skills-claude.sh
```

The installer adds the KernelPilot marketplace, installs
`humanize@KernelPilot`, exposes `knowledge/` as the `kernel-knowledge` skill,
installs the knowledge query dependency, hydrates Claude Code's installed skill
cache with absolute `HUMANIZE_RUNTIME_ROOT` and `KERNELPILOT_ROOT` paths, and
fails if those placeholders remain. Restart Claude Code after installing, then
confirm the plugin and skills are visible:

```bash
claude plugin list
claude plugin details humanize@KernelPilot
```

Inside Claude Code, you should see commands such as
`/humanize:start-rlcr-loop` and skills such as `humanize-kernel-agent-loop`,
`kernel-knowledge`, and `ncu-report`. For a one-session local checkout without
installing the marketplace, start Claude Code with:

```bash
claude --plugin-dir /path/to/kernel-pilot/humanize \
  --add-dir /path/to/kernel-pilot
```

### Codex

```bash
git clone https://github.com/BBuf/kernel-pilot.git
cd kernel-pilot
humanize/scripts/install-skills-codex.sh
```

Generic installer:

```bash
cd kernel-pilot
humanize/scripts/install-skill.sh --target codex
```

The installer hydrates `{{KERNELPILOT_ROOT}}` into installed skills and
validates that the root contains `knowledge/SKILL.md` and
`knowledge/evidence/pull-bundles/`. If the knowledge base is missing, install
fails instead of producing a broken skill.

### Kimi

For Kimi-oriented setups, use:

```bash
cd kernel-pilot
humanize/scripts/install-skills-kimi.sh
```

After installation, restart the agent session and check that these skills are
available:

```text
humanize-kernel-agent-loop
kernel-knowledge
ncu-report
```

If Humanize reports that hooks need review, approve the Stop hook in the client
UI before relying on review-gated loop exits.

## Prompt Card

Kernel optimization:

```text
[$humanize-kernel-agent-loop] Optimize SGLang's int8_scaled_mm kernel on H100 for M=64, N=2048, K=2048, out_dtype=fp16, bias=true. Keep the work in a clean standalone repo, compare correctness and latency against the current SGLang baseline, and beat that baseline by at least 10% p50 latency on this focused case.
```

Keep the prompt focused on the target kernel, environment, correctness checks,
benchmark, and performance target.

Example result from this shape:

| Shape | Candidate | SGLang baseline | Result |
| --- | ---: | ---: | ---: |
| `M=64, N=2048, K=2048, fp16+bias` | `0.015184 ms` p50 | `0.017888 ms` p50 | `15.12%` faster |

The stop hook summary should make the round outcome and review decision easy to
inspect:

![Humanize stop hook summary](docs/assets/humanize-stop-hook-summary.png)

The optimization ledger should make selected versions and rejected follow-ups
easy to scan:

![KernelPilot optimization ledger](docs/assets/kernelpilot-optimization-ledger.png)

## Maintenance

Validate the knowledge base:

```bash
cd knowledge
pip install -r requirements.txt
python3 scripts/validate.py
```

Materialize missing PR evidence bundles during corpus maintenance:

```bash
cd knowledge
python3 scripts/fetch-pr-evidence.py --repo pytorch/pytorch --max-files 16
python3 scripts/validate.py
```

Run Humanize tests after changing skills:

```bash
cd humanize
tests/run-all-tests.sh
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=BBuf/kernel-pilot&type=Date)](https://www.star-history.com/#BBuf/kernel-pilot&Date)

## Related

- [Humanize](https://github.com/PolyArch/humanize): the RLCR runtime that
  KernelPilot specializes for GPU kernel optimization.
- [AI-Infra-Auto-Driven-SKILLS](https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS):
  broader serving, profiling, SGLang, incident, and model optimization skills.
