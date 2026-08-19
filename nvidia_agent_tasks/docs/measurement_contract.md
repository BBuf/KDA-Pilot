# Measurement contract

Every task in this directory is accepted or rejected against this contract. It
exists because we have repeatedly shipped kernels that were faster in isolation
and invisible - or negative - in production.

## 1. A kernel win is only a win at the serving level

Two examples from our own tracker:

* An fp8 GEMV replacement measured **1.8x** standalone and made dense decode
  **18% slower** end to end (the fast path was gated by an AND that also
  disabled a better path).
* A router `topk` kernel measured real and bit-exact, then turned out to be
  **fused away entirely** on the recommended Blackwell deployment - the kernel we
  optimized ran 0 times in production.

So each task states the kernel's measured share of real serving GPU time, and
the acceptance criterion is: standalone speedup **and** a plausible, stated path
to end-to-end effect on the operating point where that share was measured.

## 2. Flush L2 before every call

B300 has **132.6 MB of L2** - enough to hold an m=1 GEMM's entire weight. Replaying a
kernel back to back therefore measures it reading its own leftovers, while in a real decode
step roughly 1900 other kernels run between two calls of the same one.

`tools/bench_harness.py` flushes L2 before every call by default (`--l2 cold`), writing a
buffer twice the size of L2, and brackets **only the call** with the event pair, so the
flush cost is not in the number. Measured difference on this box, same rows, same harness:

| row | hot L2 | cold L2 |
| --- | ---: | ---: |
| `kimi_k3_tiny_gemm` m=1 | 4.37 us | 7.97 us |
| `cutedsl_bf16_gemm` (6016x7168, m=1) | 16.74 us | 26.43 us |
| `cutedsl_bf16_gemm_out` | 8.44 us | 14.18 us |
| `causal_conv1d_update` decode | 6.20 us | 10.08 us |

That is 58-82% - large enough that a bandwidth-saving candidate would look far less useful
in the hot regime than it is. `--l2 hot` and `--l2 both` remain available for comparison,
and the regime is recorded in every row of the JSON report.

## 3. Time inside a CUDA graph, not in eager

Eager launch overhead dominates small kernels and inflates any "before" number.
Measured on this hardware class: an MoE decode kernel is 401 us eager and 53 us
replayed inside a CUDA graph - 348 us of the "baseline" was launch overhead that
the real deployment does not pay. Marginal in-graph launch cost on B300 is
~1.7 us per kernel node.

Corollary: do not multiply per-launch cost by kernel count to claim a launch
overhead budget. With ~1.5x kernel overlap the floor is overlapped too; the
saving only converts 1:1 for kernels removed from the critical path.

## 4. A reference you cannot reproduce is not a reference

Before any comparison, the harness calls the baseline **three times on identical inputs**
and rejects the row if the outputs contain NaN/Inf or disagree beyond the op's tolerance.
This is not paranoia: a row whose index or segment arguments had to be allocated (because
the task ships no payload for it) can leave part of the output unwritten, or route several
sequences to the same state slot where they race. Such rows print `NO VALID REFERENCE` and
are excluded from both timing and correctness, rather than producing a verdict against
uninitialized memory.

Rows are also marked when their integer index arguments are synthetic, and when the spread
across trials exceeds 10% - a speedup from an unstable row is noise until the instability
is fixed.

## 5. Nsight Compute durations are inflated

Per-kernel replay inflates absolute time: `ncu` reported 21.50 us for a GEMV
that CUDA-graph timing measures at 14.91 us. Use ncu for *bottleneck attribution*
(stall reasons, memory throughput, occupancy), and CUDA-graph timing for
*duration*. Judge bandwidth against HBM peak from graph timing.

Low occupancy is not automatically a bug: a TMA GEMV at 13% occupancy and
0.6 waves was running at 72% of HBM peak.

## 6. Microbenchmark traps that produced wrong conclusions here

* **Weights must exceed L2.** A 4-copy rotation of a 22 MB weight fits entirely
  in B300 L2 and inverted a known-good result to 0.87x. Size the working set
  above ~126 MB or rotate over enough distinct buffers.
* **In-place kernels need a fresh input every iteration.** Iterating an in-place
  op on its own output collapsed the values (86% of elements below 1e-30), which
  pushed fp32 `expf` onto the denormal slow path and produced a fake 500 us
  baseline; with fresh inputs the same kernel measured 115 us (4.25x). Copy the
  input back each iteration and measure the copy separately.
* **Interleave A and B.** Clock and power state drift on air-cooled B300 parts
  (sustained load pins the 1100 W wall). Interleave baseline and candidate
  samples inside one process; never compare a morning number to an afternoon
  number.
* **Profilers perturb what you are measuring.** CUPTI instrumentation changed the
  sign of a launch-gap measurement for us. Any timing claim must come from an
  un-profiled run.

## 7. Noise floors on this box

At the decode operating points we use, 1 tok/s is ~120 us/step. Trace noise is
+-20-35 us of summed kernel duration, +-10 us of span; cross-restart end-to-end
noise is +-200 us. A single end-to-end A/B therefore cannot resolve one kernel
candidate - attribute per kernel inside one trace, then confirm the sum.

## 8. Correctness gates before performance is even read

See `anti_hack_contract.md`. A candidate that fails the correctness gate has no
performance number, and "within tolerance" is not the gate for state-carrying
kernels - the chained final-state comparison is.

## 9. What to report

For each task: kernel time (graph-timed) baseline vs candidate per workload row,
geomean, the correctness gate result, the ncu evidence for the claimed
bottleneck, and - when the task touches a production path - the end-to-end
number at the stated operating point with the noise floor quoted.
