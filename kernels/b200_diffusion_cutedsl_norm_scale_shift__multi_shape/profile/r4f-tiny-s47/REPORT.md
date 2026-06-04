# NCU Report: r4f — nss 47x3072 bf16 (tiny bucket, SHIPPED config)

- Final-config profile of the tiny-row case (47 CTAs of 192 threads on 148
  SMs = 0.04 waves). Locked clocks, GPU1 idle.
- **Kernel duration 7.3-7.7us locked** (boost ≈ 5us); occ 9.6% (grid too
  small to fill the machine); dram SOL ~2.5% (0.6 MB moved); stalls spread
  thin.

Verdict: backs the tiny-bucket statement in docs/results.md — the kernel
itself is single-digit microseconds while the public-op call costs ~65us
(candidate) / ~92-96us (baseline) end-to-end through identical custom-op
layers. The bucket's floor is host/launch issue, not the device kernel:
device-side improvements are a supported no-go; the candidate's 1.39-1.49x
end-to-end win is host-path economics (fewer Python/broadcast/dlpack steps
inside the op body).
