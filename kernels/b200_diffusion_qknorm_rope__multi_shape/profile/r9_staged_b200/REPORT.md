# `fused_qknorm_rope_cta_token` (staged) vs `fused_qknorm_rope_warp` (baseline) — r9 Profiling Report

**Kernel:** `fused_qknorm_rope_cta_token<128,128,false,true,bf16_t,int64_t>` (candidate staged) vs `fused_qknorm_rope_warp<128,128,false,true,bf16_t,int64_t>` (baseline copy)
**Target GPU:** NVIDIA B200 (148 SM, CC 10.0), host `innomatrix-us-adc-smb200-0003`, physical GPU 1 (idle 0%/0–4 MiB before and after)
**Nsight Compute:** 2025.3.1 (container `sglang_bbuf`)
**Compile flags:** SGLang jit defaults `-std=c++20 -O3 --expt-relaxed-constexpr` + `-lineinfo` (profiling build only, `KDA_LINEINFO=1`; no `--use_fast_math`)
**Profile date:** 2026-06-04 (SGLang `0b65588c1`, task commit `aaf8275b6`/`355f3bf2a`)
**Run directory:** `profile/r9_staged_b200/`

---

## 0. Profiling setup

- Harness: `harness/profile_target.py` — Python driver over the direct JIT modules (`src/wrapper.py::_candidate_module` for staged/staged2, `baseline/loader.py::baseline_module` for the baseline copy). A Python harness is the standalone-harness equivalent for this TVM-FFI kernel family: the device code is `#include`d from workspace-owned `.cuh` sources and built with `-lineinfo`, so SASS maps back to `qknorm_rope_candidate.cuh` lines.
- Workloads: exact captured production rows from `docs/captured_shapes_b200.jsonl` — primary `qwen-edit__large__B8424_H24_D128_R128`, secondary `joyai-edit__large__B7904_H32_D128_R128`. Small rows were NOT re-profiled this round: they route to the byte-identical warp path (no device change) and the prior in-depth small-shape profile (`profile/baseline_b200/REPORT.md`: device 7.55 µs inside a ~60 µs end-to-end call, occupancy 12.7%, launch/dispatch-bound) remains architecturally unchanged.
- Dispatch paths covered: staged CTA-per-token (grid 1184 = occupancy-capped, block 256, 32 reg/thread, 1536 B smem/block) and baseline warp-per-(token,head) (grid 1184, block 256, 32 reg/thread, 1024 B smem/block); both PDL-on (B200 arch default).
- Metric-name caveats: B200/sm_100 names per `external/ncu-report-skill/reference/08-b200-metric-names.md`; metrics parsed with `helpers/analyze_reports.py` (curated key set) — stock `l1tex__average_t_sectors_per_request*` style names are absent on sm_100.
- **Collection trap (lesson):** `--launch-skip/--launch-count` count ALL CUDA launches in the process, including torch input-setup kernels — the first collection captured a 6.4 µs torch elementwise kernel instead of the subject. Always pair them with `-k "regex:fused_qknorm_rope"`.

Runnable commands (from the remote task copy):

    KDA_LINEINFO=1 CUDA_VISIBLE_DEVICES=1 PYTHONPATH=<sglang>/python \
      ncu --set full --target-processes all -k "regex:fused_qknorm_rope" \
          --launch-skip 10 --launch-count 3 -f \
          -o profile/r9_staged_b200/reports/staged_full_b8424 \
          python profile/r9_staged_b200/harness/profile_target.py staged

    # same with `--set source --section SourceCounters` -> staged_source_b8424
    # same with target `baseline`                        -> baseline_full_b8424
    # same with shape joyai-edit__large__B7904_...       -> staged_full_b7904

### Artifacts
- `reports/staged_full_b8424.ncu-rep`, `reports/staged_source_b8424.ncu-rep`, `reports/baseline_full_b8424.ncu-rep`, `reports/staged_full_b7904.ncu-rep` (remote `REMOTE_KDA_DIR/task/profile/r9_staged_b200/reports/`)
- `analysis/compare_staged_b8424_vs_baseline_b8424.txt`, `analysis/metrics_key_*.{txt,json}`, `analysis/stall_hotspots_staged_b8424.txt` (pulled into this folder)

---

## 1. Headline

| Metric (B8424, per launch) | staged | baseline (copy) |
|---|---|---|
| `gpu__time_duration` | **89.0 µs** | **113.3 µs** |
| `sm__throughput` %peak | 59.1 | 60.2 |
| `smsp__issue_active` %peak | 66.7 | 66.2 |
| achieved warps %peak | 84.3 | 88.8 |
| DRAM read %peak (rate) | 15.8% (1.21 TB/s) | 12.4% (0.95 TB/s) |
| global LD instructions | 0.876 M (**3.2× fewer**) | 2.83 M |
| shared ops | 0.84 M | 0 |
| stall long_scoreboard /issue | **9.14** | **11.78** |
| stall short_scoreboard /issue | 2.22 | 1.41 |
| stall barrier /issue | 2.06 | 0 |

NCU-side device delta −21.4% (1.27×); wall-clock interleaved device-fair on the same shape is 1.16× (NCU replay inflates both sides). Direction and magnitude match the prior round (109.6→88.1 µs, 1.24×). B7904/H32 staged shows the same signature (issue 70.7%, DRAM 15.9%, long_scoreboard 9.35, barrier 1.91).

## 2. Six dimensions

1. **Occupancy & launch geometry** — both kernels: grid 1184 (= 148 SM × 8 blocks, the occupancy cap), block 256, `waves_per_multiprocessor = 1.0`, 32 reg/thread, 100% theoretical occupancy (warp-limited, 8 blocks/SM). Achieved warps 84–89%. Nothing to recover here; smem (1.5 KB) is nowhere near the 21-block smem limit.
2. **Thread-block balance / tail** — single full wave; `sm__warps_active` min/max per cycle 51.9/55.5 (staged) — tight spread, no tail effect. Work per token is uniform (fixed head count).
3. **Stalls & per-line hotspots** — long_scoreboard dominates both kernels (52% of staged pcsamp samples, 66% baseline). Per-line (staged, `analysis/stall_hotspots_staged_b8424.txt`): `qknorm_rope_candidate.cuh:336` = 1515/3090 samples (49%) — the first consumption of the q/k global vector load (**mandatory traffic latency**); `:301`/`:325` barriers = 231 samples (7.5%) — the cos/sin staging syncs; `warp.cuh:32` short_scoreboard 277 — reduce shuffles; `:316` long_scoreboard 150 — positions/cos-sin row reads; `:377` short_scoreboard 57 — smem cos/sin reads.
4. **Tensor core** — 0% (elementwise/vector kernel; N/A by design).
5. **Timeline** — with waves = 1.0, uniform per-token work, and min/max active-warp spread under 7%, there is no within-kernel utilization cliff; PM-sampling timeline inspection adds nothing actionable for this shape.
6. **Memory & cache** — DRAM read 107.8 MB ≈ logical mandatory traffic (q+k reads 103.5 MB + cos/sin ≤4.3 MB + positions 67 KB ✓). DRAM writes observed 43.9 MB vs 103.5 MB logical — the in-place q/k lines stay resident in B200's large L2 across the 3 profiled replays (write-back absorbed; `l1tex` st hit 97.5%). Staged moves the per-head cos/sin re-reads (baseline global-ld hit 79.3% — i.e., mostly L1-served but still issuing 2.83 M LDs) into one smem stage per token: global LDs drop 3.2×, L1 ld-hit drops to 49.1% because the remaining loads are the mandatory cold q/k streams. DRAM bandwidth utilization rises to 15.8% — the kernel gets FASTER while bandwidth-light: it is **memory-latency-bound, not bandwidth-bound**.

## 3. Roofline-style bound (large bucket, B8424)

- Mandatory traffic: 103.5 MB read + 103.5 MB write (q+k, bf16, in-place) + ≤4.4 MB cos/sin+positions ≈ **211 MB**.
- Pure-bandwidth floor at ~8 TB/s HBM3e: **~26 µs**. Staged achieves ~70 µs wall (1.7 TB/s effective) — ~2.7× above the floor.
- Compute is negligible (≈0.04 useful FLOP/byte; FMA pipe 30% active, tensor 0%).
- The gap to the bandwidth floor is **latency-hiding capacity at fixed parallelism**: 64 warps/SM resident (max), each thread holding one 8-element vector load in flight; issue stalls are 9.14 cycles/issue on the load-consumption line. More in-flight independent loads per thread would be needed to close it, and the bounded probe below shows intra-CTA restructuring does not deliver that.
- **Named bound (large bucket): device memory-latency-bound at full occupancy on mandatory q+k traffic.** The staged kernel removes the only redundant traffic (per-head cos/sin re-reads). Remaining levers were probed (below) and rejected.
- **Named bound (small bucket, ≤195 tokens): host dispatch/launch-bound** — device 3–8 µs inside a ≥13 µs end-to-end public-op call (prior `profile/baseline_b200/REPORT.md`, unchanged this round: the small route is byte-identical warp code). Device-side work cannot move wall latency; out of task boundary.

## 4. Bounded exploration probe (DEC-2) — result

One NCU-justified direction was probed: **`staged2` two-token-per-CTA** (amortize staging barriers ~7.5% of samples; double independent q/k streams per block). The probe kernel and its harness existed at git `355f3bf2a` and were **removed from the shipped source after rejection** so the promoted `.cuh` byte-matches the arbiter-validated content (sha `874b1bfa`).

- Correctness: 10/10 captured rows (`check_staged2.py` at git `355f3bf2a`).
- Device-fair vs the same baseline lane, same session: `GEOMEAN_devfair_staged2` **1.0658×** vs staged rerun **1.0691×** (earlier staged run 1.0648×) — parity-to-slightly-worse (joyai −2.7%, qwen −2.0%, B8424 equal).
- Why it cannot win: at waves = 1.0 with 8 resident CTAs/SM, **inter-CTA parallelism already hides intra-CTA barriers**; pairing tokens adds smem footprint and pair-tail without adding memory-level parallelism. → **REJECTED** (`solutions.jsonl: cand_staged2_r9`).
- Not attempted, with reasons recorded: `cp.async`/TMA bulk staging (the staged row is 512 B/token — too small for async-copy latency to amortize; adds sync complexity to a 7.5%-of-samples cost already hidden by inter-CTA overlap); block-size 128 (`occupancy_limit_warps` binds — same 64 warps/SM, scheduler-neutral).
- PDL decision rule (explicit, reconciling the "keep PDL only if it wins" contract): **keep the arch default (ON) unless PDL-OFF wins materially (≥2% geomean) and consistently (sign-stable across rows)**. Measured `GEOMEAN_pdlab` 1.0035× nominally favors OFF but is sub-materiality with mixed per-row signs (−1.7%…+2.1%) → arch default ON retained; flipping would also diverge the warp/CI-grid path from SGLang's wrapper-level PDL templating for no measurable gain.

## 5. Conclusion

**Bounded exploration is closed for promotion** (per the round's revalidate-then-bounded-explore decision): the explored space — the staged anchor, the two-token restructuring probe, PDL on/off, and the reasoned-and-recorded non-attempts — leaves the staged CTA-per-token kernel as the best-validated anchor on B200 for the captured workload. Large rows are memory-latency-bound at full occupancy with only mandatory traffic remaining (device-fair 1.06–1.07× geomean, large rows 1.08–1.25×); small rows are host-bound with a byte-identical device path (parity). The ~2.7× gap to the pure-bandwidth floor is a latency-hiding limit that intra-CTA restructuring measurably did not recover; deeper prefetch/`cp.async` schedules remain unprobed and are recorded as out of this round's bounded budget, not disproven. Matches the TRT-LLM fused DiT QKNorm+RoPE design family (KernelWiki `pr-TensorRT-LLM-13052`, `pr-TensorRT-LLM-11869`) — single pass, CTA-level smem staging. Next (and final) step: the in-SGLang in-tree drop-in arbiter.
