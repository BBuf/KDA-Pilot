# NCU Report: r4f — nss 11040x5120 per-token fp32 (SHIPPED config)

- Final-config profile of the vec16 specialization (block=640, 8 elems/
  thread), the fix derived from r0v1's diagnosis. Locked clocks, GPU1 idle.
- dur ≈ 140-142us locked (boost benchmark 106.7us); regs **32** (was 52 at
  vec32), occ **79%** (was 41%), mem_SOL **71%** (was 62%), dram 4.7 TB/s
  locked; long_scoreboard 15.9 (was 16.4), barrier 5.9.

Verdict: the vec16 change restored the baseline-class profile (CuTe baseline:
occ 82%, mem_SOL 72%) — register pressure was the occupancy limiter exactly
as diagnosed. Candidate and baseline now sit at the same DRAM operand-stream
bound (12 B/elem; fp32 scale+shift streams dominate); benchmark parity
(0.98-1.00x device) is the expected outcome, and the end-to-end win (1.11x)
comes from the host path. No further in-kernel headroom claimed — supported
no-go for additional device gains in this bucket.
