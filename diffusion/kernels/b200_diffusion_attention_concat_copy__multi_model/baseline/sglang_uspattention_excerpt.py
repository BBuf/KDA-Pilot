# ============================================================================
# VERBATIM PROVENANCE EXCERPT — reference only, NOT directly runnable.
#
# Source : https://github.com/sgl-project/sglang
# Branch : main
# Commit : 67b2a9ed0cfba8ec625d3f26548e502646fd914d
# Path   : python/sglang/multimodal_gen/runtime/layers/attention/layer.py
# Lines  : 809-990 (USPAttention replicated-prefix / kv-prefix / suffix methods)
# File sha256 (full layer.py @commit): 094bd4ccc9171a61230f9ed10a4e2a23a4dd0dd91b6917a068cc25e8f0d4665b
# Resolved at: 2026-06-25T01:36:04Z
#
# This excerpt documents the exact attention prefix head-slice + contiguous-copy
# + sequence-concat memory-movement pattern this task models. Module-level helper
# symbols (get_ulysses_parallel_world_size, _usp_input_all_to_all,
# async_a2a_communicate, get_sp_group, attn_impl, ...) are intentionally unresolved
# here; the runnable, standalone-modeled memory movement lives in baseline/binding.py.
# ============================================================================

    def _forward_with_replicated_prefix(
        self,
        q: torch.Tensor,
        k: torch.Tensor,
        v: torch.Tensor,
        ctx_attn_metadata,
        num_rep: int,
    ) -> torch.Tensor:
        """Ulysses attention where the first *num_rep* tokens are replicated
        across SP ranks (e.g. text tokens) and should NOT be duplicated by the
        all-to-all.

        Strategy:
        1. Split q/k/v into replicated prefix and SP-sharded suffix.
        2. All-to-all only the sharded suffix (gathers sequence, shards heads).
        3. Locally slice the replicated prefix to the same head shard.
        4. Concatenate [prefix_h_local, gathered_suffix] and run attention.
        5. Split output, all-to-all back the suffix, all-gather prefix heads.
        """
        sp_size = get_ulysses_parallel_world_size()
        sp_rank = get_sp_parallel_rank()

        q_rep, q_shard = q[:, :num_rep], q[:, num_rep:]
        k_rep, k_shard = k[:, :num_rep], k[:, num_rep:]
        v_rep, v_shard = v[:, :num_rep], v[:, num_rep:]

        q_shard = _usp_input_all_to_all(q_shard, head_dim=2)
        k_shard = _usp_input_all_to_all(k_shard, head_dim=2)
        v_shard = _usp_input_all_to_all(v_shard, head_dim=2)

        h_local = q_shard.shape[2]
        h_start = sp_rank * h_local
        h_end = h_start + h_local
        q_rep = q_rep[:, :, h_start:h_end, :].contiguous()
        k_rep = k_rep[:, :, h_start:h_end, :].contiguous()
        v_rep = v_rep[:, :, h_start:h_end, :].contiguous()

        q = torch.cat([q_rep, q_shard], dim=1)
        k = torch.cat([k_rep, k_shard], dim=1)
        v = torch.cat([v_rep, v_shard], dim=1)

        out = self.attn_impl.forward(q, k, v, ctx_attn_metadata)

        out_rep = out[:, :num_rep]
        out_shard = out[:, num_rep:]

        out_shard = _usp_output_all_to_all(out_shard, head_dim=2)

        gathered = [torch.empty_like(out_rep) for _ in range(sp_size)]
        torch.distributed.all_gather(
            gathered,
            out_rep.contiguous(),
            group=get_sp_group().ulysses_group,
        )
        out_rep = torch.cat(gathered, dim=2)

        return torch.cat([out_rep, out_shard], dim=1)

    def forward_with_replicated_kv_prefix(
        self,
        q: torch.Tensor,
        k_prefix: torch.Tensor,
        v_prefix: torch.Tensor,
        k_suffix: torch.Tensor,
        v_suffix: torch.Tensor,
    ) -> torch.Tensor:
        """attention with replicated K/V prefix supplied separately"""
        forward_context: ForwardContext = get_forward_context()
        ctx_attn_metadata = forward_context.attn_metadata

        if self.skip_sequence_parallel or get_sequence_parallel_world_size() == 1:
            k = torch.cat([k_prefix, k_suffix], dim=1)
            v = torch.cat([v_prefix, v_suffix], dim=1)
            return self.attn_impl.forward(q, k, v, ctx_attn_metadata)

        if get_ulysses_parallel_world_size() == 1:
            k = torch.cat([k_prefix, k_suffix], dim=1)
            v = torch.cat([v_prefix, v_suffix], dim=1)
            return self(q, k, v)

        return self._forward_with_replicated_kv_prefix_split(
            q, k_prefix, v_prefix, k_suffix, v_suffix, ctx_attn_metadata
        )

    def _forward_with_replicated_kv_prefix(
        self,
        q: torch.Tensor,
        k: torch.Tensor,
        v: torch.Tensor,
        ctx_attn_metadata,
        num_rep: int,
    ) -> torch.Tensor:
        """Ulysses cross-attention where only K/V have a replicated prefix.

        Q is sequence-sharded across SP ranks with no replicated portion. K/V
        carry a fully-replicated prefix (``[:num_rep]``, same on every rank,
        e.g. cached text K/V) followed by a sequence-sharded suffix (e.g.
        image tokens) that aligns with Q's sharding.

        Strategy:
        1. All-to-all Q and the sharded K/V suffix (seq → head shard).
        2. Locally slice the replicated K/V prefix to the same head shard.
        3. Concatenate prefix + suffix on the sequence dim and attend.
        4. All-to-all the output back (head shard → seq shard).
        """
        k_rep, k_shard = k[:, :num_rep], k[:, num_rep:]
        v_rep, v_shard = v[:, :num_rep], v[:, num_rep:]

        return self._forward_with_replicated_kv_prefix_split(
            q, k_rep, v_rep, k_shard, v_shard, ctx_attn_metadata
        )

    def _forward_with_replicated_kv_prefix_split(
        self,
        q: torch.Tensor,
        k_rep: torch.Tensor,
        v_rep: torch.Tensor,
        k_shard: torch.Tensor,
        v_shard: torch.Tensor,
        ctx_attn_metadata,
    ) -> torch.Tensor:
        """split form avoids materializing full K/V before Ulysses all-to-all"""
        sp_rank = get_sp_parallel_rank()

        if q.device.type == "cuda":
            q, k_shard, v_shard = async_a2a_communicate(
                [q, k_shard, v_shard],
                get_ulysses_parallel_world_size(),
                get_sp_group().ulysses_group,
                self._get_usp_a2a_stream(),
                local_seq_2_local_head=True,
            )
            q = q.contiguous()
            k_shard = k_shard.contiguous()
            v_shard = v_shard.contiguous()
        else:
            q = _usp_input_all_to_all(q, head_dim=2)
            k_shard = _usp_input_all_to_all(k_shard, head_dim=2)
            v_shard = _usp_input_all_to_all(v_shard, head_dim=2)

        h_kv_local = k_shard.shape[2]
        h_start = sp_rank * h_kv_local
        h_end = h_start + h_kv_local
        k_rep = k_rep[:, :, h_start:h_end, :].contiguous()
        v_rep = v_rep[:, :, h_start:h_end, :].contiguous()

        k = torch.cat([k_rep, k_shard], dim=1)
        v = torch.cat([v_rep, v_shard], dim=1)

        out = self.attn_impl.forward(q, k, v, ctx_attn_metadata)
        return _usp_output_all_to_all(out, head_dim=2)

    def _forward_with_replicated_suffix(
        self,
        q: torch.Tensor,
        k: torch.Tensor,
        v: torch.Tensor,
        ctx_attn_metadata,
        num_rep: int,
    ) -> torch.Tensor:
        """Ulysses attention where the last num_rep tokens are replicated
        across SP ranks and should not be duplicated by the all-to-all."""
        if num_rep <= 0:
            raise ValueError("num_rep must be positive for replicated suffix.")

        q_shard, q_rep = q[:, :-num_rep], q[:, -num_rep:]
        k_shard, k_rep = k[:, :-num_rep], k[:, -num_rep:]
        v_shard, v_rep = v[:, :-num_rep], v[:, -num_rep:]

        # dense self-attention is permutation equivariant for non-causal use.
        # 1. rotate the replicated suffix to the front
        # 2. reuse the validated replicated-prefix path, then
        # 3. rotate the output back
        out = self._forward_with_replicated_prefix(
            torch.cat([q_rep, q_shard], dim=1),
            torch.cat([k_rep, k_shard], dim=1),
            torch.cat([v_rep, v_shard], dim=1),
            ctx_attn_metadata,
            num_rep,
        )
        out_rep, out_shard = out[:, :num_rep], out[:, num_rep:]
        return torch.cat([out_shard, out_rep], dim=1)
