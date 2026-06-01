# Design notes: b200_diffusion_qknorm_rope__multi_shape

Working notes for the B200 optimization of SGLang's `fused_inplace_qknorm_rope`.
Updated as evidence lands. See `interface.md` for the recovered contract and the
top-level RLCR plan for acceptance criteria.

## Baseline (the thing to beat)

`csrc/diffusion/qknorm_rope.cuh` — one warp per `(token, head)` work item, block
= 256 threads (8 warps), grid-stride over `(num_qo_heads + num_kv_heads) * num_tokens`,
grid capped to `occupancy * SM_count`. Each thread owns `head_dim/32` elements
(4 for head_dim=128), vectorized LDG.128/STG.128 via packed bf16x2. Warp-reduce
RMS norm, multiply by weight, RoPE from a float32 `cos_sin_cache` indexed by
`positions[token]`, write back in place. Templated `<head_dim, rope_dim, is_neox,
use_pdl, dtype>`; q and k fused into one launch. On B200 `is_arch_support_pdl()`
is true, so the baseline is built **PDL on**.

This is a pure memory-bound elementwise kernel. It is already vectorized, fused
across q+k, and occupancy-capped — so the headroom story differs sharply by bucket.

## Two regimes

- **Large (4096–8424 tokens, heads 24/30/32):** bandwidth/L2-bound. Effective DRAM
  traffic is dominated by reading q+k and writing q+k.
- **Small (19–195 tokens):** launch / dispatch / tail-effect / low-occupancy bound.
  The work barely fills the GPU; most wall-clock is launch + Python wrapper +
  dispatch, not the device kernel. This is the regime where the prior H200 run lost
  its wins to a ~5µs/call dispatcher tax — so small-shape wins are gated on the
  integrated install path.

## Seed roofline (back-of-envelope, to confirm with NCU)

Largest shape, qwen-edit `[8424, 24, 128]` bf16:
- q = 8424·24·128·2 B ≈ 51.7 MB; k same. Read q+k + write q+k ≈ **207 MB**.
- cos/sin: per `(token,head)` ≈ 512 B (64 cos + 64 sin f32), redundant across the
  48 heads of a token → if L2 holds the per-token line, DRAM cos/sin traffic
  ≈ 8424·512 B ≈ 4.3 MB (the redundancy is L2/instruction pressure, not DRAM).
- On B200 HBM3e (~8 TB/s peak), the ~207 MB lower-bounds latency at ≈ **26 µs**
  (≈ 32 µs at ~80% achieved BW). q/k traffic is mandatory (must read and rewrite
  both), so byte-reduction headroom for large shapes is small. **Expect large
  shapes to be near the bandwidth bound; a no-go there is plausible.**

Smallest shape, qwen `[19, 24, 128]`: 48·19 = 912 work items / 8 warps ≈ 114 blocks
— a single small wave on ~148 SMs. Device time is tiny; total latency is launch +
dispatch bound. **Lever is overhead reduction, not device compute.**

## Candidate directions (ranked; attack the measured bound)

1. **Small-shape overhead reduction** (high ROI *if* any win exists): validate the
   zero-overhead dispatcher on the integrated path; A/B **PDL off** (prior pilot:
   PDL hurt isolated launch); trim wrapper work; pick a launch config that fills the
   GPU with fewer/cheaper blocks. Risk: low; most cost is outside the device kernel,
   so integrated-path timing is the arbiter.
2. **Large-shape L2 / instruction pressure** (medium ROI, gated on NCU): block-level
   cos/sin staging across the heads of one token, and/or q+k paired processing so a
   warp/CTA handles corresponding q and k heads sharing position + cos/sin loads.
   Only pursue if NCU shows cos/sin reads or L2 pressure are material; DRAM bytes for
   q/k cannot shrink. Risk: register pressure, CTA-to-token alignment for 30-head
   cases.
3. **Occupancy / vectorization tuning** (low-medium): per-bucket block size and
   grid cap; confirm LDG.128/STG.128 already optimal. Risk: low.
4. **Per-shape dispatcher** (only if 1–3 show buckets need different tradeoffs):
   evidence-gated, zero per-call tax on the integrated path.

Out of scope (confirmed): `tcgen05`/TMEM/TMA/cluster MMA (no matmul here), video
shape buckets, cross-op fusion, CUDA-graph primary timing, `--use_fast_math`.

## Prior art to check (KernelWiki, at discretion)

- `query.py "fused RMS norm + RoPE inplace sm100"`
- `query.py "qk norm rope blackwell"`
- `query.py --tag qk-norm --type kernel`
- `query.py --repo sglang --tag rope --architecture sm100 --limit 20`
- `query.py --repo flashinfer --tag rope --limit 20`

Record any PR/wiki page that influences a decision here and in `solutions.jsonl`.

## Open evidence questions (resolve with NCU before editing)

- Large shapes: achieved DRAM BW %, L2 hit rate on `cos_sin_cache`, load/store
  instruction counts, occupancy, dominant stall — is the baseline already at the
  bandwidth bound?
- Small shapes: launch overhead vs device time split; does PDL-off reduce isolated
  latency on B200; how much of total latency is Python dispatch vs kernel?

## Frozen baseline (Round 2, B200, commit 43a8fd164, GPU phys 4)

Correctness PASS on B200: 10 production rows + 2400-case CI grid + 3 negative tests.
Fused-baseline median latency (µs), candidate==baseline so geomean 1.0149x ≈ 1.0x:

| bucket | shape | µs |
|--------|-------|----|
| large | qwen B4096/H24 | 45.1 |
| large | zimage B4096/H30 | 76.1 |
| large | zimage B4128/H30 | 76.5 |
| large | joyai-edit B7904/H32 | 89.5 |
| large | qwen-edit B8424/H24 | 98.0 |
| small | qwen B19/H24 | 64.2 |
| small | zimage B32/H30 | 64.9 |
| small | qwen B47/H24 | 64.0 |
| small | qwen-edit B189/H24 | 64.3 |
| small | qwen-edit B195/H24 | 64.1 |

**Empirical confirmation of the two regimes — and a sharper read than the seed
roofline:** small shapes are **flat ~64µs regardless of token count** (19→195) and
are *slower than the 4096-token large shape (45µs)*. That is impossible if the cost
were the device kernel; it is a fixed per-call **dispatch/launch overhead floor**
(torch `register_custom_op` dispatch + JIT module lookup + launch), captured in the
CUDA-event window because the GPU waits on the CPU between the start marker and the
kernel. Large shapes scale 45→98µs with token count (bandwidth regime).

Implication for direction ranking: the only real headroom is the **small-shape
overhead** (a CUDA-event measurement already shows it dominates). The lever is a
leaner call path (zero-overhead dispatcher, avoiding the custom-op wrapper, PDL-off),
not the device kernel — and it MUST be proven on the integrated install path. Large
shapes are near the bandwidth bound; expect a no-go there unless NCU shows otherwise.

## NCU correction (Round 3) — profile, don't guess

NCU (`profile/baseline_b200/REPORT.md`, commit 68a32061, GPU 4) revises the seed
roofline above:

- **Small `qwen B19`: launch/dispatch-overhead bound (confirmed).** Device kernel
  = **7.55 µs**, end-to-end benchmark = 60.67 µs → **~53 µs (~88 %) is host dispatch**
  (torch custom-op + JIT wrapper). Kernel also tiny-grid (114<148 SMs, 0.10 waves/SM,
  12.7 % occupancy). The win is the call path, not the device kernel.
- **Large `qwen-edit B8424`: memory-LATENCY bound, NOT bandwidth-bound (correction).**
  The seed roofline guessed bandwidth; NCU shows only **12.8 % DRAM read %peak**
  (≈1.4 TB/s of ~8 TB/s). Dominant stall `long_scoreboard` 11.9 at 88.9 % occupancy,
  compute SOL 60 % / memory SOL 50 %, L2 hit 50 %. Headroom is limited; any gain is
  from L2 reuse on the per-head-reread float32 cos_sin_cache or load-latency hiding —
  not a bandwidth rewrite. Likely near-bound; confirm vs a candidate before a no-go.

This is why the roofline was a *seed* and NCU is the arbiter.

## Status

- Local scaffold + benchmark/correctness corrections complete and committed.
- Remote B200: REMOTE_KDA_DIR created; correctness (production + full 2400 CI grid +
  negatives) PASS; baseline refrozen with symmetric timing + provenance
  (`benchmark.csv`, commit 68a32061); first NCU pass done with named bounds
  (`profile/baseline_b200/REPORT.md`).
- Next: Codex `analyze` direction-ranking from the corrected baseline + NCU; then the
  first native CUDA candidate (AC-2/AC-4) + PDL A/B; integrated-path validation for
  small shapes. No optimized kernel implemented yet.
