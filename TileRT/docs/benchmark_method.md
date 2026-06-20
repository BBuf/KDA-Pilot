# TileRT kernel benchmark method

Target = the measured TileRT op latency (and HBM %) in each task's
`config.toml [reference]` / `docs/tilert_reference.md`, obtained by calling the
real `libtilert_dsv32.so` op and profiling with **ncu** on B200. A candidate
"matches TileRT" when its median latency over `num_trials` is within noise of the
TileRT number on the same shape, at matching correctness.

## Why ncu, not CUDA events
Eager per-op latency via `torch.cuda.Event` is ~160 µs and is **pure host
dispatch overhead, not kernel time** — that is exactly why TileRT runs the whole
decode as one CUDA graph. So the TileRT reference latency MUST come from ncu's
`gpu__time_duration.avg` (real on-GPU kernel time), measured on a single isolated
launch. The harness `harness/tilert_oracle.py` builds the op + synthetic inputs;
`harness/run_once.py --op X --seq N` does one launch for ncu to profile.

## The ≥3× stable-measurement rule (required)
Every TileRT reference number in a task's `config.toml [reference]` and
`docs/tilert_reference.md` must be a **median of ≥3 independent ncu runs** with
**low dispersion** (report min/median/max; max−min should be a few % of median).
A single profiler/ncu run is NOT acceptable as the optimization target. Use:

```
ncu --clock-control none --kernel-name regex:<KernelName> --launch-count 1 \
    --metrics gpu__time_duration.avg,\
dram__throughput.avg.pct_of_peak_sustained_elapsed,dram__bytes.sum \
    python run_once.py --op <op> --seq <seq>
```

Run it ≥3× (the driver `harness/measure_ncu.py` loops and reports
min/median/max + dispersion). Only the **median over the ≥3 runs** becomes the
target. Do this for **every workload shape** (each seq, each KeComputeType variant
the op compiles for). Profile on an otherwise-idle B200 (no other GPU jobs).

`seq` coverage = the op's full compiled set from the SASS symbol table (decode 1,
MTP verify 4, +2/3/8/16 where the symbol exists), not just seq=1 — see
`../KERNEL_REGISTRY.md`.

## Correctness gate before timing
A candidate is only timed after it passes `bench/correctness.py` on every workload
shape (tolerances in `tilert_correctness_contract.md`): the candidate is compared
to `baseline/*.py` (TileRT's golden_forward math), which itself is validated against
the real `torch.ops.tilert.*` op by `harness/tilert_oracle.py`.
