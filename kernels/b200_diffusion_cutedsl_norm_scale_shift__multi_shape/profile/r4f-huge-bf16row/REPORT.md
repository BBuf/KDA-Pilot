# NCU Report: r4f — nss 176400x5120 bf16 row-bcast (SHIPPED config)

- Final-config profile (two-pass variance, vec32, block=320), `-lineinfo`
  build, ion-b200 GPU1 idle, `ncu --set full` locked clocks.
- dur ≈ 1283us locked (benchmark boost-clock median 787.9us); dram 1.81+1.76
  GB (matches the 4 B/elem model); occ 56.9%; **sm_SOL 59.8% > mem_SOL
  41.9%**; stalls: long_scoreboard 3.34, **barrier 3.01** (up from 1.89 in
  the v1 single-pass profile — the second reduction round), not_selected 2.34.

Six dimensions: occupancy 56.9% (regs 40, block 320; barrier serialization
caps it); balance = instruction-issue-leaning mixed bound; stalls low and
spread; no tensor core; flat timeline across instances; memory traffic exact.

Diagnosis: same as r0v1 — per-element convert/round-trip/epilogue instruction
pressure dominates over DRAM on this 4 B/elem kernel, now plus the
contract-mandated two-pass barrier cost. Achieved 4.58 TB/s boost (~57% peak),
1.35x over the CuTe baseline (3.40 TB/s).

Resulting action: none this round (bounded-iteration policy after three
measured kernel iterations); packed bf16x2 conversion lever recorded in
docs/draft.md for future work.
