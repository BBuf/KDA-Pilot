# Correctness contract (and why synthetic inputs are not acceptable here)

An autonomous kernel agent optimizes whatever the verifier measures. If the
verifier feeds i.i.d. Gaussian tensors and accepts a relative-error tolerance,
several *statistically valid* shortcuts pass while destroying model quality. We
have hit these, so every state-carrying task in this handoff ships real captured
tensors and a chained gate instead.

## Gate 1: chained final state, not per-step tolerance

For any kernel that carries state across steps (Mamba-2 SSM, GDN / KDA recurrent
decode, conv1d state update):

> Run the captured N consecutive steps as a chain, feeding each step's produced
> state into the next, and compare the **final** state and the full output
> sequence against the captured ground truth.

The captured chains satisfy
`step[n+1].state_before == step[n].state_after` byte-exactly, so the chain is
well-posed. This matters because the state recursion compounds error:

```
S_t = S_{t-1} * Diag(alpha_t) + beta_t * (v_t - S_{t-1} * Diag(alpha_t) * k_t) * k_t^T
```

Our own replay-SSM work failed exactly here: every per-step output looked correct
while the state quietly drifted. Per-step tolerance cannot see it; the chained
final-state comparison can. For scale, the per-step relative change of the state
differs per kernel and is printed by `tools/verify_state_chain.py`: ~92-120% for the
rolling conv1d window in A1 (the window turns over every step), and 14-20% for a
linear-attention SSM state - judge a deviation against that kernel's own number, not
against a fixed tolerance.

## Gate 2: real inputs, because the shortcuts are distribution-dependent

Three concrete shortcuts that pass a synthetic-Gaussian verifier:

1. **Skip the L2/RMS normalization reduction.** With i.i.d. N(0,1) inputs and
   d=128, `||q||^2 ~ chi2(128)`: mean 128, sd 16, so `||q|| = 11.31 +- 0.71` - a
   6.3% spread. Replacing the divisor with the constant `1/sqrt(128)` passes a
   few-percent tolerance and deletes a cross-channel warp-shuffle reduction plus a
   sync point, which is the actual latency bottleneck at 1 token x 128 dims. Same
   family: quantization `amax ~ sqrt(2 ln n)` is a known prior under Gaussians.
2. **Prune channels by magnitude.** Under N(0,1) the energy carried by the
   smallest-magnitude channels is analytically known
   (`(2*Phi(c)-1) - 2*c*phi(c)`): dropping the smallest 25% of channels loses
   0.86% of energy, 50% loses 7.1%. The point is not that the approximation is
   good - it is that its error is *predictable under the synthetic distribution*,
   so the sparsity rate can be tuned to sit just inside the tolerance.
3. **Truncate the recurrence window.** `g` is a per-channel gate that becomes the
   decay `alpha`. Synthetic Gaussian gates imply uniform, short effective memory,
   so computing only the last W tokens passes. Real learned gates keep `alpha`
   near 1 on the channels that must remember - truncation destroys long-range
   recall and *only the chained final-state gate detects it*.

`tools/check_hacks.py` prints these numbers on the shipped tensors so the gate can
be sanity-checked against them, and `tools/verify_state_chain.py` proves a shipped
chain actually chains (A1's ships verified: 15/15 links byte-identical).

## Gate 3: real-workload structure the synthetic path never produces

These are in the captured data and a candidate must handle them:

* Gate / beta buffers padded to a multiple of 16, so their sequence dimension is
  **larger** than q/k/v's.
* Non-contiguous inputs: decode-side tensors are slices of a fused QKV buffer
  (`contiguous: false` in the manifest, with the real strides).
* Mixed dtypes in one call: `initial_state` fp32 while q/k/v/g are bf16, `beta`
  fp32.
* Padded CUDA-graph slots: rows with a negative cache index are padding and only
  their output is zeroed (these rows are filtered out of the shipped payloads).
* Ragged batches: real `cu_seqlens` / `query_start_loc`, not uniform lengths.

## Gate 4: bit-exactness where we require it

Where a diffusion change is meant to be lossless we gate on **bit-exact** output -
md5-identical frames - because a 1e-6 difference compounds over 50 denoise steps into
visible drift. We have met that bar before by replicating aten LayerNorm at SASS level
(Welford accumulation order, FFMA sequence, `rcp`/`rsqrtf` choice), so it is
achievable, not aspirational.

## Where the numbers in the gate come from

Nothing in this directory picks a tolerance by hand. Every numeric gate uses
`torch.testing.assert_close` with the **rtol/atol that SGLang's own test for that kernel
uses**, and each task's `config.json` records the value together with the test file and
line it was copied from (`tools/tolerances.py` is the table; `python tools/tolerances.py`
prints it). Examples: `causal_conv1d` bf16 1e-2/5e-2
(`test/registered/layers/mamba/test_causal_conv1d.py:163-165`), the Mamba-2 SSD pipeline
5e-2/5e-2 (`test_mamba_ssm_ssd.py:244-248`, where SGLang's own comment notes the bf16 case
needs the looser threshold), GDN chunk 1e-2/2e-2
(`test_chunk_gated_delta_rule.py:28-29`), KDA fused decode 2e-2/2e-2 with the conv half
asserted exactly (`test_kda_fused_decode.py:207-209`), Triton attention 1e-2/1e-3
(`test_triton_attention_kernels.py:309`), Triton fused MoE 1e-5/1e-5
(`test_triton_fused_moe.py:45-49`), the CuTe TGV GEMM 2e-2/2.5
(`test_cutedsl_bf16_gemm.py:53`), and index transforms exactly
(`test_dsa_transform_index.py:120`).

If one of those tolerances is wrong for a kernel, the fix is upstream in SGLang's test,
not looser in a task here.

## What "faster" is measured against

The baseline is the **shipped SGLang implementation**, copied into each task's
`baseline/` at a pinned commit - not a naive PyTorch loop, and not a
reimplementation. See `baseline_policy.md`.
