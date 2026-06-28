# Dispatch / Candidate-Direction Decision — b200_ltx2_rms_adaln__bitwise

This task has a single production dispatch bucket (bf16, CUDA, last-dim
contiguous, rank-3 `[B,S,D]`, `D % 256 == 0`, `D <= 8192`, scale/shift layout in
`{[D],[B,D],[B,1,D],[B,S,D]}`). All four production rows fall in it. The decision
below is which kernel implementation that bucket routes to.

## Candidate directions considered

| Direction | Bit-exact? | Speedup | Decision |
|-----------|-----------|---------|----------|
| **Staged**: shared `at::rms_norm` + 1 fused modulation kernel | **Yes (proven)** | **~1.96–2.0× geomean** | **SELECTED (production)** |
| Fully-fused: single kernel (custom RMS reduction + modulation) | **No (proven)** | (would remove ~2 array passes) | **NO-GO** |
| Eager (baseline) | Yes (reference) | 1.0× | baseline only |

## Selected: staged candidate
`solution/kernel.cu::ltx2_rms_adaln_candidate` reuses `at::rms_norm` for `normed`
(so the fp32 reduction + bf16 store are identical to the baseline by
construction) and runs one fused, 16B-vectorized modulation kernel that
reproduces eager's three bf16 rounding points. Bit-wise exact on all production +
canonical + grid rows (69/69), geomean ~1.96–2.0× on B200. NCU shows the
modulation kernel is memory-bound (51 % of HBM3e peak on the large video row);
the win comes from fusing eager's three elementwise modulation passes + two
temporaries into one pass.

## NO-GO: fully-fused single kernel (task10, bounded attempt)
A fully-fused kernel would fold the RMS reduction into the modulation pass,
removing the `normed` write+read (~2 of 6 array passes) — the obvious next
bandwidth win. It requires a custom single-kernel fp32 RMS reduction whose
`normed` bf16 output is **bit-identical** to `at::rms_norm`.

Bounded attempt (`bench/probe_fused.py` + `solution/fused_probe.cu`): a standard
one-pass fp32 reduction (thread-strided partial sums + shared-memory tree
reduce, `rstd = rsqrt(mean(x²)+eps)`) was compared raw-`uint16` against
`at::rms_norm` on the production + canonical rows:

```
stage1_video [2,1536,4096]: DIFFER  43/12.6M  (0.0003%)  max_abs 1.56e-02
stage1_audio [2,126,2048] : EQUAL    0/0.52M
stage2_video [1,6144,4096]: DIFFER  43/25.2M  (0.0002%)  max_abs 1.56e-02
stage2_audio [1,126,2048] : EQUAL    0/0.26M
canon [1,8192,3072]       : DIFFER  50/25.2M  (0.0002%)  max_abs 1.56e-02
canon [4,8192,3072]       : DIFFER 248/100.7M (0.0002%)  max_abs 1.56e-02
```

**Conclusion:** the custom reduction's fp32 sum order differs from ATen's, which
flips ~0.0002 % of bf16 values (1 ULP) near round-to-nearest-even boundaries on
the large rows — exactly the failure mode the bitwise contract forbids (and the
likely cause of the original closed PR's full-model inconsistency). Matching
ATen's exact reduction order would require reverse-engineering a version-specific
ATen kernel, which is brittle across PyTorch versions. **The fused single kernel
is a NO-GO for the zero-tolerance contract.** The staged path is the production
choice; the small audio rows happening to match does not change the conclusion
(the large production rows differ).

## Future bandwidth headroom (optional, must keep the bitwise gate)
NCU shows the staged modulation kernel at ~51 % DRAM on the large video row, so a
memory-tuning pass (occupancy / launch shape) could improve it without changing
numerics. Any such change must re-pass `bench/correctness.py` (uint16, 69/69).
