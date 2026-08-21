"""Reference for Qwen3-Next packed GDN decode (one token per sequence).

Independent of the kernel under test: unpack the fused projection, apply the gated
delta rule to this sequence's state slot in float32, write the slot back, and read the
output off the updated state. The head split is recovered from the shapes exactly as
the kernel recovers it - `mixed_qkv` carries q and k at `H * K` each and v at `HV * V`,
so `H` follows from the remainder.
"""

import torch
import torch.nn.functional as F


def _l2norm(x):
    return x / x.norm(dim=-1, keepdim=True).clamp_min(1e-6)


@torch.no_grad()
def run(
    mixed_qkv,
    a,
    b,
    A_log,
    dt_bias,
    scale,
    ssm_states,
    cache_indices,
    num_v_heads,
    head_v_dim,
):
    num_seqs = mixed_qkv.shape[0]
    heads_v, value_dim, key_dim = ssm_states.shape[-3:]
    qk_dim = mixed_qkv.shape[1] - heads_v * value_dim
    q_dim = qk_dim // 2
    heads_qk = q_dim // key_dim
    repeats = heads_v // heads_qk

    out = mixed_qkv.new_empty(num_seqs, 1, heads_v, value_dim)
    decay = torch.exp(A_log.float())
    for seq in range(num_seqs):
        slot = int(cache_indices[seq].item())
        query = _l2norm(mixed_qkv[seq, :q_dim].float().view(heads_qk, key_dim))
        key = _l2norm(mixed_qkv[seq, q_dim : 2 * q_dim].float().view(heads_qk, key_dim))
        value = mixed_qkv[seq, 2 * q_dim :].float().view(heads_v, value_dim)
        query = query.repeat_interleave(repeats, dim=0)
        key = key.repeat_interleave(repeats, dim=0)

        # softplus with the kernel's threshold: above it the function is the identity
        # to within float32, and evaluating log1p(exp(x)) there overflows.
        gate_in = a[seq].float() + dt_bias.float()
        gate = torch.exp(-decay * F.softplus(gate_in, beta=1.0, threshold=20.0))
        beta = torch.sigmoid(b[seq].float())

        state = ssm_states[slot].float() * gate.view(heads_v, 1, 1)
        recalled = (state * key.view(heads_v, 1, key_dim)).sum(-1)
        state = state + ((value - recalled) * beta.view(heads_v, 1)).unsqueeze(
            -1
        ) * key.view(heads_v, 1, key_dim)
        ssm_states[slot] = state.to(ssm_states.dtype)
        out[seq, 0] = (
            (state * query.view(heads_v, 1, key_dim)).sum(-1) * float(scale)
        ).to(out.dtype)
    # The state pool is the second output: this kernel advances it in place, and a
    # candidate that gets `out` right while drifting the state is wrong in a way that
    # only shows up on the next token.
    return out.transpose(0, 1), ssm_states
