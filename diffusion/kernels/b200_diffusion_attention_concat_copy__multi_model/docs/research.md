# Research / Candidate Direction Ranking

Kept/rejected optimization ideas for the attention concat/copy/slice kernels,
from Codex Analysis v1 (gen-plan) and a dedicated Codex direction-ranking pass
(`gpt-5.5:high`). These are evidence priorities; final claims require B200 A/B
numbers (see `docs/results.md`).

## Ranking (Codex, integrated)

| Direction | Verdict | Reasoning |
|-----------|---------|-----------|
| 128-bit / `uint4` vectorized row copy (D=128 → 256 B bf16 = 16×16 B) | **WIN (low risk)** | required baseline for a custom kernel; win over naive code, parity vs ATen which also vectorizes |
| Single fused kernel, linear output-space mapping, branch on `seq < prefix_len` | **WIN for slice_concat; PARITY for copy/concat** | removes scratch write+re-read and a launch for slice; pure copy/cat just matches ATen |
| Batched multi-tensor (Q/K/V or K/V) selector variant | **WIN (medium risk)** | top non-algorithmic lever after fusion: fewer launches, better tail amortization; bytes unchanged |
| Shape-specialized block/grid tuning (D=128, h_local=24/32) | **PARITY → small WIN** | avoid branchy generic indexing; no miracles once bandwidth-bound |
| `cp.async` / TMA bulk copy | **NO-GO** | staging through SMEM helps reuse-by-compute, not one-pass global→global copy; adds traffic/complexity |
| PDL | **PARITY / NO-OP** | hides launch tail, does not reduce bytes |

## Pure copy_contiguous / concat_sequence
Expected **near-parity / honest no-go** vs ATen `copy_` / `CatArrayBatchedCopy` (already vectorized + coalesced). A real win requires reducing bytes or launch count; otherwise realized HBM bandwidth decides and ATen is hard to beat. This is an acceptable evidence-backed no-go per the plan if the geomean on those rows is ~1.0.

## slice_heads_then_concat traffic model (the headline opportunity)
- Baseline 2-stage (`prefix.contiguous()` into scratch, then `cat`): ≈ `4P + 2S` (read prefix, write scratch, read scratch, read shard, write output).
- Fused candidate: ≈ `2P + 2S` (read prefix-slice, read shard, write output once).
- Ideal speedup `= (4P+2S)/(2P+2S) = 1 + P/(P+S)`.
  - FLUX.2 `P=512, S=4096` → ≈ **1.11×** (~10% less logical traffic).
  - JoyAI `P=1004, S=8048` → ≈ **1.11×**.
- Realistic ~5–12%; B200's large L2 may keep the baseline scratch hot, shrinking the apparent HBM advantage (scratch still costs L2 bandwidth + a launch).

## B200 pitfalls (applied in v1)
- Do not hardcode SM count; size grid for several waves over runtime SM count (v1 uses a grid-stride loop).
- A bf16 row is only 256 B — use a flat per-vector mapping (one thread per 16 B), not one-CTA-per-tiny-row.
- Keep 16 B alignment for `uint4` (guarded; scalar fallback otherwise).
- Single linear output mapping (no separate prefix/shard launches that tail-limit the small prefix).
- Streaming ops: no L2-reuse wins expected.

## v1 implemented
`solution/kernel.cu`: one selector function; output rows `(b, out_seq, out_head)` of D contiguous elems mapped to source rows; one thread copies one 16 B `uint4` (`__ldcs`/`__stcs`); fused slice+concat reads the head-sliced prefix directly and writes output once. Scalar fallback for non-16 B-aligned/oddly-sized rows.

## Bounded iterations queued (task11)
1. Batched multi-tensor (Q/K/V or K/V) variant — reduce launches / amortize tail.
2. Tune rows-per-CTA / vector lanes / cache policy for the two production shapes; measure effective GB/s; check prefix-branch imbalance.
