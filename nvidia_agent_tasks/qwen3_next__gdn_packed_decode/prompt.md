# Qwen3-Next: packed Gated-Delta-Net decode

Beat `TritonGDNKernel.packed_decode` on the shapes Qwen3-Next-80B-A3B actually decodes
with. It is the highest-traffic linear-attention entry point in the capture: **266,688
recorded calls**.

One kernel, one entry point:

| op | symbol | rows |
| --- | --- | ---: |
| `gdn_decode_packed_triton` | `sglang.srt.layers.attention.linear.kernels.gdn_triton.TritonGDNKernel.packed_decode` | 8 |

## What the kernel does

One token per sequence. It unpacks QKV from the fused projection output
(`mixed_qkv[B, 1024]` = q`[2,128]` + k`[2,128]` + v`[4,128]`), L2-normalises q and k,
computes the gates (`g = exp(-exp(A_log) * softplus(a + dt_bias))`, `beta = sigmoid(b)`),
applies one delta-rule step to this sequence's slot of the SSM state pool
(`[10715, 4, 128, 128]`, k-last), writes the slot back, and reads the output off the
updated state - all in a single Triton kernel, which is the point: the unfused path pays
four launches and three intermediate tensors.

The state pool is updated **in place**, so it is an output as much as `out` is. It is
declared in `OUTPUT_ARGS`, and the gate compares it after the call: a candidate that gets
`out` right while advancing the state wrongly is wrong in a way that would otherwise only
surface as drift on the *next* token.

`cache_indices` must hold **distinct** slots. Two sequences pointing at one slot is a
read-modify-write race, not a slower kernel, and `tools/derive_inputs.py` refuses a row
it cannot give distinct slots rather than producing one.

## Where the shapes come from

Qwen3-Next-80B-A3B served with its own SGLang cookbook command on 8x B300 SXM6, TP8,
GSM8K 1.000 on the capture run, over four operating points. Batch runs 1, 2, 3, 5, 6, 13,
16 and 32 - the whole decode range a mixed-traffic server sees, which for this kernel is
the axis that matters: the work per sequence is fixed, so batch is the only thing between
launch-bound and occupancy-bound.

The B=1 point ships its captured activations, gate parameters, state slot and state
contents as the first link of a **16-step decode chain** (`bench/tensors/.../step000..015`,
each step's `state_after` byte-identical to the next step's `state_before`). The other
seven ship recorded shapes with distinct slots by construction.

## What a win has to clear

* `docs/measurement_contract.md` - CUDA-graph timing, interleaved arms, cold L2, and the
  in-place state restored between iterations with the restore cost subtracted. This kernel
  is small (5-6 us at B=1): read the noise-floor section before believing a 1.05x.
* `docs/anti_hack_contract.md` - the tolerance is SGLang's own for this kernel family
  (rtol 2e-2 / atol 2e-2, `test_kda_fused_decode.py:207-208`). A truncated recurrence
  window is one of the documented shortcuts that passes a per-call check and fails the
  chain; the shipped 16-step chain is what catches it
  (`python tools/verify_state_chain.py qwen3_next__gdn_packed_decode`).

## Running it

```bash
python tools/check_task.py qwen3_next__gdn_packed_decode
python qwen3_next__gdn_packed_decode/tests/test_contract.py
python tools/bench_harness.py qwen3_next__gdn_packed_decode
cp qwen3_next__gdn_packed_decode/solution/entry.py.template qwen3_next__gdn_packed_decode/solution/entry.py
python tools/bench_harness.py qwen3_next__gdn_packed_decode --json report.json
python qwen3_next__gdn_packed_decode/tests/test_solution.py
```

The same definition is also packaged for KDA-1.5 in `kda15_tasks/` - axes, constraints
and a pure-PyTorch reference instead of a replayed call site.
