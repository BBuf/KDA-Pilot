# Design notes: b200_diffusion_qknorm_rope__multi_shape

> **FINAL OUTCOME:** ships via an **in-tree `.cuh` placement** in SGLang (keeps SGLang's own
> `register_custom_op` → **torch.compile-safe**), device geomean ~1.07–1.12x (large 1.10–1.33x,
> small parity), correctness 10/10 — see `docs/sglang_jit_export.md`. The `kda_kernels` overlay is
> NOT promoted (it drops `register_custom_op`, not torch.compile-safe). The historical sections
> below (the overlay no-go narrative) are kept for the record.

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

This is an elementwise kernel — already vectorized, fused across q+k, and
occupancy-capped — so the headroom story differs sharply by bucket. It is NOT simply
"bandwidth-bound": NCU (below) shows the small shapes are host-dispatch/launch-bound and
the large device kernel is memory-**latency** bound (only ~13% DRAM peak), not
DRAM-bandwidth-bound.

> **Final outcome (Round 8 — read first).** The candidate is an **evidence-backed no-go**;
> it is **not promoted**. A CTA-per-token cos/sin-staging kernel is a real DEVICE win
> (device-fair geomean **1.0679x**, large 1.10–1.26x, NCU-confirmed), but on the **literal
> `kda_kernels.install()` production path** it is a **net regression (geomean 0.9301x /
> 0.9185x)**: the overlay's per-call Python dispatch tax (~7µs over the baseline's C-level
> `register_custom_op`) erases the modest device win on 9 of 10 shapes (only joyai
> B7904/H32 wins). The active bound on the production path is **host-side dispatch
> overhead**, not the device kernel. Authoritative evidence: `docs/sglang_jit_export.md`,
> `docs/dispatch.md`, `benchmark.csv` (`GEOMEAN_install`), `solutions.jsonl`
> (`id=export_r8`). The "## Status" section at the bottom carries the full final state.

## Two regimes (NCU-confirmed bounds)

- **Large (4096–8424 tokens, heads 24/30/32):** memory-**latency** bound / cos-sin-reuse
  limited — **NOT DRAM-bandwidth-bound** (NCU: ~12.8% DRAM read %peak, `long_scoreboard`
  dominant at ~89% occupancy; q+k read+write traffic is mandatory). Any device gain comes
  from L2 reuse of the per-head-reread float32 `cos_sin_cache` (the staged kernel does
  exactly this), not a bandwidth rewrite.
- **Small (19–195 tokens):** launch / dispatch / tail-effect / low-occupancy bound. The
  work barely fills the GPU; most wall-clock is launch + Python wrapper + dispatch, not the
  device kernel (NCU: device ~7.55µs vs ~60µs end-to-end). This is the regime where the
  prior H200 run lost its wins to a ~5µs/call dispatcher tax — and where, in Round 8, the
  overlay dispatch tax made the whole candidate a net install-path regression.

## Seed roofline (HISTORICAL, pre-NCU back-of-envelope — SUPERSEDED)

> This was the pre-profiling back-of-envelope. Its "large = near the bandwidth bound" guess
> was **WRONG** and was corrected by NCU (see "## NCU correction (Round 3)" below): the large
> kernel is memory-**latency** bound at only ~13% DRAM peak. Kept for history / lineage; do
> not use its bound conclusions — the NCU correction and the Round 8 install-path result are
> authoritative.

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

> Historical exploration ranking. The bounds here use the **NCU-corrected** read (large =
> memory-latency, not bandwidth — see the NCU correction below), not the seed roofline. Net
> result after Rounds 4–8: direction #2 (cos/sin staging) produced a real DEVICE win but a
> net **install-path regression** (overlay dispatch tax) → evidence-backed no-go; direction #1
> (overhead reduction) cannot help because the overlay tax exceeds the baseline's custom-op on
> the dispatch-bound shapes. See "## Status".

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

## Resolved evidence questions (ANSWERED — NCU Round 3 + Round 8 install validation)

These were the pre-profiling open questions; all are now answered (see "## NCU correction
(Round 3)" and "## Status" below). None remain open.

- **Large shapes — is the baseline at the bandwidth bound? NO.** NCU shows only **~12.8% DRAM
  read %peak** (≈1.4 TB/s of ~8 TB/s) — the large kernel is **memory-LATENCY bound /
  cos-sin-reuse limited**, not bandwidth-bound: dominant stall `long_scoreboard` 11.9 at
  ~89% occupancy, L2 hit ~50% on the per-head-reread float32 `cos_sin_cache`. The staged
  kernel attacks exactly this (device-fair 1.10–1.26x; B8424 device 109.6→88.1 µs).
- **Small shapes — launch vs device split? Mostly host.** NCU: device ~**7.55 µs** vs
  ~**60 µs** end-to-end (~88% host dispatch/launch); tiny-grid (114<148 SMs, 0.10 waves/SM).
  PDL-off was not kept (no win on the real workload). The device kernel is not the
  small-shape bottleneck.
- **Does the device win reach production? NO (the decisive answer).** On the literal
  `kda_kernels.install()` path the candidate is a **net regression (0.9301x / 0.9185x)**:
  the overlay's per-call Python dispatch tax (~7 µs > the baseline's C-level
  `register_custom_op`) erases the modest device win on 9 of 10 shapes → **evidence-backed
  no-go**. Active production bound = host dispatch overhead.

## Frozen baseline (Round 2, B200, commit 43a8fd164, GPU phys 4) — SUPERSEDED

> **SUPERSEDED by the Round 3 refreeze (commit 68a32061; see `interface.md` and
> `solutions.jsonl` id=`baseline`).** These Round 2 numbers used an asymmetric timed
> baseline (the fused-baseline callable was resolved inside the CUDA-event closure
> while the candidate path was cached), inflating the baseline ~3µs/small-shape. The
> geomean 1.0149x below is NOT trustworthy; use the Round 3 numbers
> (small ~61µs, geomean 0.9957x). Kept for history only. The two-regime conclusion
> still holds (NCU-confirmed below).

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
kernel. Large shapes scale 45→98µs with token count (device regime; NCU later showed this
is memory-**LATENCY**-bound, NOT bandwidth — see the NCU correction below).

Implication for direction ranking (pre-NCU, since corrected): the only real headroom is the
**small-shape overhead** (a CUDA-event measurement already shows it dominates). The lever is a
leaner call path (zero-overhead dispatcher, avoiding the custom-op wrapper, PDL-off), not the
device kernel — and it MUST be proven on the integrated install path. Large shapes were
*guessed* near a bandwidth bound here; the NCU correction below revised that to
memory-**LATENCY**-bound, and the Round 8 literal install-path result is the final arbiter.

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
  not a bandwidth rewrite. (RESOLVED: Round 5's CTA-per-token cos/sin-staging candidate
  did capture a device win here — device-fair 1.10–1.26x, B8424 109.6→88.1 µs — but
  Round 8's literal install path made it a net regression → no-go; see "## Status".)

This is why the roofline was a *seed* and NCU is the arbiter.

## Status — FINAL (Round 8): evidence-backed NO-GO, candidate not promoted

- Local scaffold + benchmark/correctness corrections complete and committed.
- Remote B200: REMOTE_KDA_DIR created; correctness (production + full 2400 CI grid +
  negatives) PASS; baseline refrozen with symmetric timing + provenance
  (`benchmark.csv`, commit 68a32061); first NCU pass done with named bounds
  (`profile/baseline_b200/REPORT.md`).
- Round 4: first native CUDA candidate (faithful port) builds via load_jit + correct;
  isolated 1.3x diagnosed as a call-path artifact (no device win).
- Round 5: CTA-per-token cos/sin shared-staging kernel (`QKNormRopeStagedKernel`)
  implemented + correct; a **device-fair** interleaved benchmark shows a real DEVICE win
  (large 1.10–1.26x), NCU-confirmed on B8424 (device 109.6→88.1 µs, `long_scoreboard`
  11.9→9.29). Device-fair is a DIAGNOSTIC (both kernels via direct JIT, no custom op).
- Round 6–7: exact-shape, fail-closed dispatcher (no env; routes only the captured large
  rows to staged, everything else to the baseline). Round 7's "integrated" 1.0793x was a
  **proxy** (timing `optimized_wrapper` directly) and was later found to overstate the win.
- **Round 8 (terminal): the LITERAL `kda_kernels.install()` path is the arbiter, and it is a
  NET REGRESSION.** Made the candidate exportable (thin `register.py` + `EXPORTS` + impl
  `wrapper.py`, recursion-safe baseline capture, full `(tokens,heads,eps)`+metadata gate),
  ran the real `scripts/export_kda_kernels/export.py` → `kda_kernels.install(force=True,
  strict=True)`, and timed the INSTALLED public symbol vs the captured baseline:
  - install-path geomean **0.9301x / 0.9185x** (two runs) — only joyai B7904/H32 wins
    (1.21x); the other large shapes are 0.93–1.00x and the 5 small shapes 0.85–0.87x;
  - device-fair (diagnostic) reproduces the device win (geomean **1.0679x**; warp
    faithful-port sanity **0.9999x**);
  - the gap is the **overlay per-call Python dispatch tax** (~7µs > the baseline's C-level
    `register_custom_op`), which on this dispatch-bound workload erases the modest device
    win on 9/10 shapes — **named active bound = host dispatch overhead**;
  - drop-in correctness PASSED (install swapped; large→staged + small/int32→captured
    baseline; oracle-matched; no recursion; uninstall restores);
  - the export was **REVERTED** so the shipped `kda_kernels` overlay stays the un-promoted
    stub (`KDA_OPTIMIZED=False`) — no regression is shipped; the export-ready `src/` +
    evidence remain and `export.py` reproduces the overlay.
- **Verdict:** well-supported evidence-backed no-go (frozen baseline R3 + real candidate
  attempts R4/R5 + NCU evidence R5 + named bound + literal install-path measurement R8). The
  staged optimization would only net-win with a near-zero-overhead (C-level) overlay dispatch
  or under CUDA graphs — both outside this single-op, no-CUDA-graph task boundary.
- **Authoritative final evidence:** `docs/sglang_jit_export.md` (export + drop-in + no-go
  write-up), `docs/dispatch.md` (decision table + device-fair-vs-install + named bound),
  `benchmark.csv` (`GEOMEAN_install` 0.9301x; `GEOMEAN_production` 0.9957x baseline-vs-baseline),
  `solutions.jsonl` (`id=export_r8` no-go; `dispatcher_r7` proxy correction), `interface.md`.
