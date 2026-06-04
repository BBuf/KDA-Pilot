# Results — b200_diffusion_qknorm_rope__multi_shape (continuation round r9, 2026-06-04)

Fresh evidence on the SGLang `jit_kernel`/tvm-ffi stack (the round that clears the
"Blocked" row in `../../docs/tvm_ffi_benchmark_status.md`). Environment: `ion-b200`
(`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf`, physical GPU 1 (NVIDIA B200,
idle-verified before/after every run), `PYTHONPATH` pinned to the bbuf checkout at SGLang
`0b65588c1`, task commits `aaf8275b6` → `355f3bf2a`. Raw rows: `benchmark.csv`; raw logs:
`REMOTE_KDA_DIR=/home/sglang-omni/bbuf/kda_runs/b200_diffusion_qknorm_rope__multi_shape/20260604-185755-r9/logs/`.

## Correctness (AC gate for every claim below)

- `tests/test_correctness.py` (subset grid): **10 passed, 1 skipped** (retired-overlay test
  auto-skip), 118.6 s — production 10 rows, CI-subset grid, 3 negatives, dispatch routing,
  fail-closed gate, fallback, wrong-eps fallback.
- Full canonical grid (default mode): **10 passed, 1 skipped**, 11.65 s warm
  (`logs/cigrid_full_r9.log`).
- staged2 probe: 10/10 module-direct (`profile/r9_staged_b200/harness/check_staged2.py`).

## Device-fair (hermetic `baseline/` copy vs candidate, interleaved, full stats in benchmark.csv)

| shape | bucket | staged speedup (run1 / rerun) |
|---|---|---|
| joyai-edit B7904 H32 | large | 1.2458x |
| qwen B4096 H24 | large | 1.1144x |
| qwen-edit B8424 H24 | large | 1.1623x |
| zimage B4096 H30 | large | 1.0945x |
| zimage B4128 H30 | large | 1.0818x |
| qwen B19 / B47, qwen-edit B195 / B189, zimage B32 | small | 0.986–1.001x (parity) |
| **GEOMEAN_devfair** | all 10 | **1.0648x / 1.0691x** |

Controls: upstream-module base cross-check `GEOMEAN_devfair_sglbase` 1.0701x (copy ≡
upstream); PDL A/B `GEOMEAN_pdlab` 1.0035x (neutral → arch-default PDL ON kept); the old
warp-sanity lane is no longer a control (the candidate `.cuh`'s launcher delegates ≥512-token
production rows to staged — verified in source, recorded in `solutions.jsonl`).

## Bound closure (roofline; full report `profile/r9_staged_b200/REPORT.md`)

- **Large bucket: device memory-latency-bound at full occupancy on mandatory q+k traffic.**
  B8424: NCU staged 89.0 µs vs baseline 113.3 µs (−21.4%); DRAM read 15.8% of peak
  (1.21 TB/s) — ~2.7× above the ~26 µs pure-bandwidth floor; long_scoreboard 9.14/issue with
  49% of pcsamp on the q/k load-consumption line; global LDs cut 3.2× by smem cos/sin
  staging; waves/SM = 1.0, achieved warps 84%.
- **Small bucket: host dispatch/launch-bound** — device path byte-identical to baseline
  (parity by construction); prior small-shape NCU stands (device ~7.5 µs in a ~60 µs call).
- **Bounded exploration (DEC-2): closed.** One NCU-justified probe (`staged2`, two-token CTA)
  was implemented, validated 10/10, and **rejected**: 1.0658x vs staged's same-session
  1.0691x (parity-to-worse; inter-CTA overlap already hides intra-CTA barriers at
  waves = 1.0). `cp.async` staging and block-128 were ranked and not attempted (reasons in
  REPORT.md §4); PDL flip measured neutral. The staged anchor is the operating point —
  consistent with TRT-LLM's fused DiT QKNorm+RoPE kernels (KernelWiki
  `pr-TensorRT-LLM-13052`, `pr-TensorRT-LLM-11869`) and the H200 row-norm family findings.

## Shipping-integration arbiter (in-SGLang in-tree drop-in)

Pending in this round's final step: isolated SGLang worktree at `0b65588c1` with the
candidate `.cuh` under `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh`
(`register_custom_op` byte-unchanged), measured by `profile/in_sglang/validate_in_tree.py`
(discard-run1/record-run2 warm protocol) + `compile_smoke.py` (fullgraph torch.compile
parity). Promotion gate per DEC-1: parity-or-speedup, no material per-shape regression;
geomean reported as an outcome metric. Results land in `docs/sglang_jit_export.md` and the
`*__intree` rows of `benchmark.csv` when run.
