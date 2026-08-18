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

## 2. Time inside a CUDA graph, not in eager

Eager launch overhead dominates small kernels and inflates any "before" number.
Measured on this hardware class: an MoE decode kernel is 401 us eager and 53 us
replayed inside a CUDA graph - 348 us of the "baseline" was launch overhead that
the real deployment does not pay. Marginal in-graph launch cost on B300 is
~1.7 us per kernel node.

Corollary: do not multiply per-launch cost by kernel count to claim a launch
overhead budget. With ~1.5x kernel overlap the floor is overlapped too; the
saving only converts 1:1 for kernels removed from the critical path.

## 3. Nsight Compute durations are inflated

Per-kernel replay inflates absolute time: `ncu` reported 21.50 us for a GEMV
that CUDA-graph timing measures at 14.91 us. Use ncu for *bottleneck attribution*
(stall reasons, memory throughput, occupancy), and CUDA-graph timing for
*duration*. Judge bandwidth against HBM peak from graph timing.

Low occupancy is not automatically a bug: a TMA GEMV at 13% occupancy and
0.6 waves was running at 72% of HBM peak.

## 4. Microbenchmark traps that produced wrong conclusions here

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

## 5. Noise floors on this box

At the decode operating points we use, 1 tok/s is ~120 us/step. Trace noise is
+-20-35 us of summed kernel duration, +-10 us of span; cross-restart end-to-end
noise is +-200 us. A single end-to-end A/B therefore cannot resolve one kernel
candidate - attribute per kernel inside one trace, then confirm the sum.

## 6. Correctness gates before performance is even read

See `anti_hack_contract.md`. A candidate that fails the correctness gate has no
performance number, and "within tolerance" is not the gate for state-carrying
kernels - the chained final-state comparison is.

## 7. What to report

For each task: kernel time (graph-timed) baseline vs candidate per workload row,
geomean, the correctness gate result, the ncu evidence for the claimed
bottleneck, and - when the task touches a production path - the end-to-end
number at the stated operating point with the noise floor quoted.
