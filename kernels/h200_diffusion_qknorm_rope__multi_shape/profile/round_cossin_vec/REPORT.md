# NCU Report — round_cossin_vec (variant `6669bd218e336c9d` vs incumbent `4f70cda745940c96`)

**Question.** The cos/sin float4 rewrite measured 1.134–1.148× module-level over the incumbent on
large shapes (all-9 geomean 1.0622×) — bigger than the expected few percent. Confirm the mechanism,
re-establish registers/thread under nvcc 13, and decide whether shared-memory cos/sin staging
(direction 1b) has remaining headroom.

**Setup.** qwen_t4096 captured shape (q/k [4096,24,128] bf16, rope 128, GPT-J, int64 positions),
`fused_qknorm_rope_warp2`, ion8-h200 GPU 7 (idle before 0%/50MiB, after 0%/44MiB), container
`sglang_bbuf`, torch 2.11.0+cu130 / nvcc 13.0, SGLang pin `c47f0e7cd` (detached worktree),
`KDA_LINEINFO=1` builds, harness `harness/profile_target.py`, `--launch-skip 10 --launch-count 10`,
sets: full (both builds) + source (variant). Reports (remote, REMOTE_KDA_DIR
`/home/sglang-omni/bbuf/kda_runs/h200_diffusion_qknorm_rope__multi_shape/k04-20260604-185804`):
`profile/round_cossin_vec/reports/{full_variant,full_incumbent,source_variant}.ncu-rep`; parsed
CSVs in `analysis/`. The two large parsed detail CSVs (`analysis/full_{variant,incumbent}_details.csv`)
are local scratch — intentionally untracked, regenerated on demand from the remote `.ncu-rep` files
via `ncu --import <report> --csv --page details`.

## Key metrics (median over 10 launches)

| Metric | Incumbent | Variant | Reading |
|---|---|---|---|
| Duration | 38.13 µs | **33.97 µs** | matches interleaved A/B/C 1.1344× |
| Registers/thread | 38 | **32** | the rewrite REMOVED 6 registers |
| Theoretical occupancy | 75% | **100%** | 32 regs is exactly the 2048-thread/SM boundary |
| Achieved occupancy | 72.47% | **90.39%** | +18 pp |
| Grid size (occupancy-capped) | 792 (6 blk/SM) | **1056 (8 blk/SM)** | launcher's `get_blocks_per_sm` rose |
| Memory throughput | 2.005 TB/s | **2.245 TB/s** | +12% extracted bandwidth |
| DRAM throughput (% peak) | 41.7% | 46.8% | still not BW-saturated |
| Compute (SM) throughput | 60.6% | 61.4% | flat |
| L2 hit rate | 50.0% | 50.0% | unchanged |
| Executed IPC | 2.625 | 2.695 | flat |
| Warp cycles/issued inst | 17.98 | 21.38 | higher per-inst latency, far more warps to hide it |
| Long-scoreboard (cycles/issued inst) | 10.64 | 11.80 | still the dominant stall in both |

## Mechanism (why the win is ~14% on large shapes, not a few percent)

The intended effect (8 scalar `__ldg` cos/sin loads → 2×`LDG.E.128.CONSTANT`) landed — SASS now has
exactly 5 global loads per work item (q/k `LDG.E.128`, weight `LDG.E.128`, positions `LDG.E.64`,
cos+sin `LDG.E.128.CONSTANT`). But the dominant effect is a SECOND-ORDER one: dropping the per-pair
`half_idx` integer math and scalar-load bookkeeping freed **6 registers (38 → 32)**, and 32
registers/thread is precisely the 100%-theoretical-occupancy boundary on H200 (64K regs/SM ÷ 2048
threads). Theoretical occupancy 75→100%, achieved 72.5→90.4%, and the occupancy-derived grid cap
grew 792→1056 blocks. For a memory-latency-bound kernel this is the textbook fix — more resident
warps hide the same q/k load latency (memory throughput +12%, duration −10.9%). The direction-2
goal (registers 38→≤32 for occupancy) was therefore achieved BY the direction-1 edit.

## Long-scoreboard attribution (source set, variant, per consuming SASS line)

| Share | Consumer | Producer it waits on |
|---|---|---|
| 45.3% | `PRMT R25, R12, 0x7632, R25` | q/k input `LDG.E.128` (bf16→fp32 unpack) — irreducible input traffic |
| 34.1% | `FMUL R27, R24, R10` | norm-apply chain (weight load / normalized elems) |
| 14.5% | `LEA R20, P0, R8, UR18, 0x9` | positions `LDG.E.64` feeding the cos/sin row address (×512 = `<<9`) |
| 5.9% | `FFMA R10, R29, R14, -R27` | rope math consuming the cos/sin quartets |
| 0.2% | `SHF.L.U32` | address math |

## Decisions

1. **Direction 1b (shared-memory cos/sin staging): SKIP, evidence-backed.** The cos/sin consumers
   carry only ~6% of remaining long-scoreboard cycles; ~79% sits on the irreducible q/k
   load→unpack and norm chains that staging cannot touch. Best-case upside is ~1–2% for the cost
   of block-wide synchronization in a 34 µs kernel at 90% occupancy.
2. **Direction 1 iteration 2 (hoist pos/cos/sin fetches above the RMS reduction): TRIED →
   REJECTED.** The hoist extended the quartet live ranges across the reduction: registers
   32 → 40 (`reports/basic_v2.ncu-rep`), theoretical occupancy back to 75%, achieved 63.8–65.0%.
   Latency-hiding compensated in isolation (v2/v1 large geomean 1.0148 run 1, but only 1.0085 in
   the repeat run; all-9 1.0090 → 1.0018) — small, shrinking, and in violation of the
   pre-declared regs≤32 rule. Source restored byte-identical to v1 (`6669bd218e336c9d`),
   local and remote.
3. **Direction 2 (separate register iteration): RESOLVED-BY-DIRECTION-1.** Registers already at
   32 with 100% theoretical occupancy; going below 32 cannot raise theoretical occupancy further
   (2048 threads/SM ceiling) and risks spills. Mechanism evidence: this report. No separate
   iteration warranted.

## Six-dimension walk

- **Compute**: SM ~61% both — not compute-bound.
- **Memory**: DRAM 46.8% of peak, L2 hit 50% — latency-bound, not bandwidth-saturated; 2.245 TB/s
  achieved.
- **Occupancy**: was the binding lever (75%→100% theoretical); now near-saturated at 90.4% achieved.
- **Latency hiding**: long-scoreboard still dominant (11.8 of 21.4 cycles/inst) but now amortized
  over 57.8 active warps/SM (was 46.4).
- **Launch overhead**: irrelevant at this shape (34 µs body); tiny shapes remain launch-bound
  (unchanged conclusion from the prior round).
- **Tail**: waves/SM = 1 at grid 1056 on 132 SMs — single-wave, no tail effect.
