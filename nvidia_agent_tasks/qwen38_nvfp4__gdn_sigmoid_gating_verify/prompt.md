# qwen38_nvfp4__gdn_sigmoid_gating_verify

Target GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (sm_120). Model: RadixArk/Qwen3.8-27B-NVFP4, GDN hybrid (48 linear-attention layers).

The DSpark verify path runs the GDN family per layer per verify step at a fixed
**T=9** window (block 8): `fused_sigmoid_gating_delta_rule_update` (2.6% of the
verify step, sequential in T), the qkvzba split/cat (1.4%) and the causal-conv1d
update (1.3%) - **~5.3% combined**, and it is the only non-GEMM family that grows
with the draft block size, capping how far DSpark's block can be pushed.

bs=1 4k-in/1k-out: no-spec 66.7 tok/s (ITL 14.78 ms); DSpark 153.3 tok/s (ITL 3.48 ms, accept 3.47) - 2.30x. Verify forwards are fixed M=T=9 (block 8 + 1).

Goal: a packed T<=9 verify update that keeps the in-T loop in registers/smem
(single launch per layer for the delta-rule update; folding conv-update and/or the
split is fair game), functional state updates (fresh state tensors - rejected
drafts roll back), bf16 state pool semantics preserved. Geometry is exact from the
model config (16 k-heads / 48 v-heads x 128, ratio 3, conv 4). Real tensor payloads
for this family are queued (nvcap re-run with bound signatures); until then the
correctness reference is the copied baseline on identical random inputs plus the
state-chain check in `tools/verify_state_chain.py`. Evidence:
`docs/profile_evidence.md`.
