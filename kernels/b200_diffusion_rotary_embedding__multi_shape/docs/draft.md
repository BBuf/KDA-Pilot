# Candidate-direction ranking — b200_diffusion_rotary_embedding__multi_shape

These RoPE kernels are **memory-bandwidth / launch-latency bound** (elementwise rotation, trivial
arithmetic). SM100 tensor-core / TMEM / TMA / tcgen05 are irrelevant; the levers are coalesced
128-bit traffic, launch-overhead reduction, and cos/sin-reuse. Strategy (Codex Round-0 review +
qknorm ~1.11x precedent): direct vectorized CUDA port first, then optimize from measured deltas.

## Directions, ranked by expected benefit / risk / directness

1. **128-bit (int4) vectorized loads/stores + fp32 compute** — highest benefit, low risk, directly
   attacks the DRAM-bandwidth bound. ADOPTED in cuda-v1 (both kernels). DONE.
2. **Standard: one CTA per token, cos/sin staged in shared and reused across the 24 heads** — removes
   the redundant per-head cos/sin reload the baseline carries. ADOPTED. DONE.
3. **LTX-2: stride-addressed cos/sin with contiguous innermost half, HALF∈{32,64} templated** — honors
   the non-contiguous `[B,H,S,half]` layout without a copy; one CTA per (batch,token). ADOPTED. DONE.
4. **Exact baseline numeric order (bf16-round on x*cos for LTX-2)** — required for a tight match; gives
   bit-exact LTX-2 output. ADOPTED. DONE.
5. **Persistent / multi-token-per-CTA for the large LTX-2 (24576-token) bucket** — the 24576-token
   shapes show the smallest wins (1.06-1.29x); likely launch/occupancy or tail bound. CANDIDATE for
   Round 2 pending NCU.
6. **Standard: full-row staging / better coalescing** — standard already 1.79x; NCU will say if more
   bandwidth is reachable. LOWER priority.

## cuda-v1 measured result (round 1, B200 GPU3, idle; benchmark.csv)

| bucket | baseline_us | cand_us | speedup |
|---|---|---|---|
| standard hunyuanvideo (27030 tok) | 134.0 | 75.1 | **1.79x** |
| LTX-2 small (126 tok) | ~21.7-22.2 | ~14.5 | 1.49-1.54x |
| LTX-2 mid (1536/6144 tok) | 21.7-61.6 | 14.6-55.8 | 1.10-1.50x |
| LTX-2 large (24576 tok) | 71.6-104.4 | 55.6-98.5 | 1.06-1.29x |
| **geomean (11 unique sigs)** | — | — | **1.3756x** |

Correctness: candidate vs baseline 17/17 (LTX-2 bit-exact, standard within 1 ulp); pytest 7/7.

## Next (Round 2)
- NCU + roofline on standard-large / LTX-2 small / mid / large to name the active bound per bucket
  (AC-6); confirm whether the large LTX-2 bucket has reachable headroom (direction 5) or is near-bound.
- `docs/dispatch.md` decision table (AC-7); promotion via `export.py` (AC-9) — candidate already
  beats baseline on every shape, so promotion is the expected outcome pending the roofline evidence.

## Source lineage
- SGLang baseline `rotary.py` / `ltx2_rotary.py` @ commit 0b65588c1 — rotation semantics + numeric order ported.
- Repo precedent `kernels/b200_diffusion_qknorm_rope__multi_shape` — wrapper/guard/_LAST_DISPATCH/EXPORTS pattern.
- No external (KernelWiki) PR ideas incorporated yet; the design is a straightforward vectorized port.
