# Optimization Directions (ranked) — round 0 prior-art + Codex analysis

Source: `/humanize:ask-codex` (gpt-5.5:high), informed by the recovered SGLang baselines and KernelWiki (`wiki/patterns/memory-bound.md`, `wiki/hardware/pdl-gdc.md`, `sources/docs/nvidia-blackwell-tuning-guide.md`). These guide the round-1+ optimization (tasks 9–10); they are NOT commitments.

Correction carried from baseline recovery: the Triton `_norm_infer_kernel` already loads each row **once** into registers and reduces twice — there is no second DRAM read to remove. The roofline floor for LN is read-x-once + write-y-once + cached w/b.

## Family A — fp32 LayerNorm, helios `[8640, 5120]`
1. **Single-CTA-per-row, exact N=5120, vectorized `float4`** — 256 threads × 20 fp32 elems/thread (vs Triton's BLOCK_N=8192 masked lanes). Low-med risk; preserves the 1-read/1-write roofline. **Top pick.**
2. Warp-shuffle reductions + one shared-mem warp-sum stage, keeping `mean` then `sum((x-mean)^2)/N` in fp32 exactly (no `E[x^2]-mean^2`). Med risk (1e-5 tol).
3. Cache-policy split: stream x/y, treat w/b (40 KB) as read-mostly/evict-last. Low-med.
4. Compile-time specialization (is_rms_norm=False, fp32 out, eps fixed, width/alignment fixed). Low-med.
5. Thread-count sweep 128/256/512 + register caps — do not assume more threads win. Med risk (spills/occupancy).
6. AVOID split-row / multi-CTA / scratch-buffer reductions — 8640 independent rows already saturate 148 SMs.

## Family B — bf16 RMSNorm, D=128, S ∈ {1320, 4096, 16384, 648720, 650040}
1. **Hard-code D=128 warp-per-row**: 32 lanes × 4 bf16 via one 64-bit (or 128-bit packed) load, fp32 square accumulation, warp-shuffle reduction, packed bf16 store. High benefit, med risk (bf16 rounding). **Top pick.**
2. Per-S dispatch configs for the exact S values (not one generic tile policy). High benefit, low-med risk.
3. Reuse `w[128]` (256 B) within a CTA via shared mem / cached registers across rows. Med (huge S).
4. Tune rows-per-CTA per regime: large S → 8–16 rows/CTA for bandwidth; S=1320/4096 → keep enough CTAs/waves to cover 148 SMs without tiny-block overhead. Med-high.
5. Streaming cache policy for x/y, read-only/evict-last w, aligned 128/64-bit ops. Med.
6. Persistent / grid-stride variant ONLY for S=1320 as an A/B candidate (cannot remove bare launch cost). Low-med.

## Cross-cutting
- No `--use_fast_math`; fp32 accumulation throughout; LN keeps `sum((x-mean)^2)/N`.
- PDL: optional A/B only (helped dependent chains on SM100 in refs, but neutral/worse for isolated bare-norm latency — consistent with the qknorm pilot).
- tcgen05 / TMEM / TMA tensor-core paths: NOT promising — these are streaming elementwise reductions with tiny/no reuse, not matmul pipelines. Deprioritize.
- Per-shape validation must report: latency, achieved DRAM bandwidth, register count/spills, occupancy, eligible warps, tail behavior.