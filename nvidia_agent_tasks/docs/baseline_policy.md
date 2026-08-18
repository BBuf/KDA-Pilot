# Baseline policy

**The baseline is the kernel the deployment actually runs.**

Each task's `baseline/` holds the relevant SGLang source files, copied verbatim
from the commit named in `config.json` (`main @ 43226af`), with the file list in
`baseline/SOURCES.txt`. That means:

* **Not** a naive PyTorch/`einsum` reference. Several of these kernels are already
  heavily tuned (our own fused diffusion kernels are 2-2.3x over their Triton
  predecessors and run at 70-88% of achievable bandwidth), so a naive reference
  would make any candidate look like a win.
* **Not** the upstream FLA / mamba-ssm / flash-attn package version, where it
  differs from ours. Where SGLang has patched or specialized a kernel, the patched
  file is what is copied.
* **Not** an older release. Two tasks in this set exist *because* an earlier
  "optimization" was invisible or negative at the real operating point, so the
  baseline must be current main.

## Symmetry rules

1. Baseline and candidate are exposed through **matching local interfaces** and
   are called identically by the harness. The candidate must not import SGLang at
   run time, monkey-patch the baseline, or reach into the server.
2. Outputs are **preallocated** and reused across iterations for both arms; the
   allocation is not part of the measured region for either.
3. Sampling is **interleaved** (baseline, candidate, baseline, ... within one
   process), CUDA-graph timed, and reported with per-row numbers, not just a
   geomean. See `measurement_contract.md`.
4. Both arms see the **same inputs from the same file**. For in-place kernels the
   input is restored (`copy_`) before every iteration and the restore cost is
   measured separately and subtracted - skipping this produced a fake 4x for us
   once (values collapsed into the denormal range and pushed fp32 `expf` onto a
   slow path).
5. If a candidate handles only a subset of the rows, that is a legitimate result -
   report it as a subset with a fallback, do not silently widen the tolerance or
   drop rows. Several of our shipped kernels are staged fast paths with a guard.

## Where the baseline dispatch itself is the target

For some tasks (A3 DSA, C2 diffusion attention) SGLang chooses between several
implementations at run time - TileLang / Triton / DeepGEMM / CuTe-DSL, or FA4 vs
cuDNN. In those tasks the *selection* is part of the problem: a candidate that
wins on some shapes and loses on others should ship with the shape predicate, and
the predicate is reviewed like the kernel.

## Provenance is auditable

Each task carries `docs/capture_provenance.md` (exact serving command, capture
matrix, GSM8K accuracy of that run, library versions, GPU, sglang commit) so any
number in the task can be re-derived, and any claim that a kernel is "hot" can be
checked against the call counts in `bench/workloads.json`.
