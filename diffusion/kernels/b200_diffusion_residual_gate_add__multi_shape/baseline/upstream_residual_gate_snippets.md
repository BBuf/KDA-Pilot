# Upstream residual-gate / broadcast-add source excerpts (provenance)

Verbatim extracts from sgl-project/sglang @ `8314247d9de0fa2c58e34756b3e1dbc6cf815dfd` (branch main).
Evidence for the recovered kernel semantics; the runnable local baseline is
`baseline/binding.py`. Do not import sglang at runtime. (Relevant lines are
byte-identical to the earlier 67b2a9ed resolution.)

## ideogram.py — Ideogram4TransformerBlock.forward (lines 320-340)

```python
            prefix=f"{prefix}.adaln_modulation",
        )

    def forward(self, x, cos, sin, adaln_input, attn_mask, attn_mask_meta):
        scale_msa, gate_msa, scale_mlp, gate_mlp = self.adaln_modulation(
            adaln_input
        ).chunk(4, dim=-1)
        gate_msa = torch.tanh(gate_msa)
        gate_mlp = torch.tanh(gate_mlp)
        attn_out = self.attention(
            self.attention_norm1(x) * (1.0 + scale_msa),
            cos=cos,
            sin=sin,
            attn_mask=attn_mask,
            attn_mask_meta=attn_mask_meta,
        )
        x = x + gate_msa * self.attention_norm2(attn_out)
        x = x + gate_mlp * self.ffn_norm2(
            self.feed_forward(self.ffn_norm1(x) * (1.0 + scale_mlp))
        )
        return x
```

## ltx_2.py — residual-gate updates (lines 1015-1100)

```python

        # 1. Video and Audio Self-Attention
        vshift_msa, vscale_msa, vgate_msa = self.get_ada_values(
            self.scale_shift_table, batch_size, temb, slice(0, 3)
        )
        norm_hidden_states = (
            self.rms_norm(hidden_states, self.norm_eps) * (1 + vscale_msa) + vshift_msa
        )
        attn_hidden_states = self.attn1(
            norm_hidden_states,
            mask=video_self_attention_mask,
            pe=video_rotary_emb,
            perturbation_mask=video_self_attn_perturbation_mask,
            all_perturbed=skip_video_self_attn,
            gather_context_kv_for_sp=audio_replicated_for_sp,
        )
        hidden_states = hidden_states + attn_hidden_states * vgate_msa

        ashift_msa, ascale_msa, agate_msa = self.get_ada_values(
            self.audio_scale_shift_table, batch_size, temb_audio, slice(0, 3)
        )
        norm_audio_hidden_states = (
            self.rms_norm(audio_hidden_states, self.norm_eps) * (1 + ascale_msa)
            + ashift_msa
        )
        attn_audio_hidden_states = self.audio_attn1(
            norm_audio_hidden_states,
            mask=audio_self_attention_mask,
            pe=audio_rotary_emb,
            perturbation_mask=audio_self_attn_perturbation_mask,
            all_perturbed=skip_audio_self_attn,
            skip_sequence_parallel_override=audio_replicated_for_sp,
        )
        audio_hidden_states = audio_hidden_states + attn_audio_hidden_states * agate_msa
        # 2. Prompt Cross-Attention
        if self.cross_attention_adaln:
            # LTX2.3
            if temb_prompt is None or temb_audio_prompt is None:
                raise ValueError(
                    "cross_attention_adaln requires prompt modulation tensors."
                )
            vshift_q, vscale_q, vgate_q = self.get_ada_values(
                self.scale_shift_table, batch_size, temb, slice(6, 9)
            )
            v_prompt_shift, v_prompt_scale = self.get_ada_values(
                self.prompt_scale_shift_table, batch_size, temb_prompt, slice(None)
            )
            norm_hidden_states = (
                self.rms_norm(hidden_states, self.norm_eps) * (1 + vscale_q) + vshift_q
            )
            mod_encoder_hidden_states = (
                encoder_hidden_states * (1 + v_prompt_scale) + v_prompt_shift
            )
            attn_hidden_states = self.attn2(
                norm_hidden_states,
                context=mod_encoder_hidden_states,
                mask=encoder_attention_mask,
            )
            hidden_states = hidden_states + attn_hidden_states * vgate_q

            ashift_q, ascale_q, agate_q = self.get_ada_values(
                self.audio_scale_shift_table, batch_size, temb_audio, slice(6, 9)
            )
            a_prompt_shift, a_prompt_scale = self.get_ada_values(
                self.audio_prompt_scale_shift_table,
                batch_size,
                temb_audio_prompt,
                slice(None),
            )
            norm_audio_hidden_states = (
                self.rms_norm(audio_hidden_states, self.norm_eps) * (1 + ascale_q)
                + ashift_q
            )
            mod_audio_encoder_hidden_states = (
                audio_encoder_hidden_states * (1 + a_prompt_scale) + a_prompt_shift
            )
            attn_audio_hidden_states = self.audio_attn2(
                norm_audio_hidden_states,
                context=mod_audio_encoder_hidden_states,
                mask=audio_encoder_attention_mask,
            )
            audio_hidden_states = (
                audio_hidden_states + attn_audio_hidden_states * agate_q
            )
        else:
            norm_hidden_states = self.rms_norm(hidden_states, self.norm_eps)
```

## ltx_2.py — 4D cross-attn-gate broadcast add (lines 1120-1146)

```python
        video_per_layer_ca_scale_shift = self.video_a2v_cross_attn_scale_shift_table[
            :4, :
        ]
        video_per_layer_ca_gate = self.video_a2v_cross_attn_scale_shift_table[4:, :]

        video_ca_scale_shift_table = (
            video_per_layer_ca_scale_shift[None, None, :, :].to(
                dtype=temb_ca_scale_shift.dtype, device=temb_ca_scale_shift.device
            )
            + temb_ca_scale_shift.reshape(
                batch_size, temb_ca_scale_shift.shape[1], 4, -1
            )
        ).unbind(dim=2)
        video_ca_gate = (
            video_per_layer_ca_gate[None, None, :, :].to(
                dtype=temb_ca_gate.dtype, device=temb_ca_gate.device
            )
            + temb_ca_gate.reshape(batch_size, temb_ca_gate.shape[1], 1, -1)
        ).unbind(dim=2)

        (
            video_a2v_ca_scale,
            video_a2v_ca_shift,
            video_v2a_ca_scale,
            video_v2a_ca_shift,
        ) = [t.squeeze(2) for t in video_ca_scale_shift_table]
        a2v_gate = video_ca_gate[0].squeeze(2)
```

## flux_2.py — modulation residual gate (lines 740-760, 838-895)

```python
            hidden_states = torch.cat([encoder_hidden_states, hidden_states], dim=1)

        mod_shift, mod_scale, mod_gate = temb_mod_params

        norm_hidden_states = self.norm(hidden_states)
        norm_hidden_states = (1 + mod_scale) * norm_hidden_states + mod_shift

        joint_attention_kwargs = joint_attention_kwargs or {}
        attn_output = self.attn(
            hidden_states=norm_hidden_states,
            freqs_cis=freqs_cis,
            num_replicated_prefix=num_replicated_prefix,
            **joint_attention_kwargs,
        )

        hidden_states = hidden_states + mod_gate * attn_output
        if hidden_states.dtype == torch.float16:
            hidden_states = hidden_states.clip(-65504, 65504)

        if split_hidden_states:
            encoder_hidden_states, hidden_states = (

# ... (double-stream block) ...


        # Modulation parameters shape: [1, 1, self.dim]
        (shift_msa, scale_msa, gate_msa), (
            shift_mlp,
            scale_mlp,
            gate_mlp,
        ) = temb_mod_params_img
        (c_shift_msa, c_scale_msa, c_gate_msa), (
            c_shift_mlp,
            c_scale_mlp,
            c_gate_mlp,
        ) = temb_mod_params_txt

        # Img stream
        norm_hidden_states = self.norm1(hidden_states)
        norm_hidden_states = (1 + scale_msa) * norm_hidden_states + shift_msa

        # Conditioning txt stream
        norm_encoder_hidden_states = self.norm1_context(encoder_hidden_states)
        norm_encoder_hidden_states = (
            1 + c_scale_msa
        ) * norm_encoder_hidden_states + c_shift_msa

        # Attention on concatenated img + txt stream
        attention_outputs = self.attn(
            hidden_states=norm_hidden_states,
            encoder_hidden_states=norm_encoder_hidden_states,
            freqs_cis=freqs_cis,
            num_replicated_prefix=num_replicated_prefix,
            **joint_attention_kwargs,
        )

        attn_output, context_attn_output = attention_outputs

        # Process attention outputs for the image stream (`hidden_states`).
        attn_output = gate_msa * attn_output
        hidden_states = hidden_states + attn_output

        norm_hidden_states = self.norm2(hidden_states)
        norm_hidden_states = norm_hidden_states * (1 + scale_mlp) + shift_mlp

        ff_output = self.ff(norm_hidden_states)
        hidden_states = hidden_states + gate_mlp * ff_output

        # Process attention outputs for the text stream (`encoder_hidden_states`).
        context_attn_output = c_gate_msa * context_attn_output
        encoder_hidden_states = encoder_hidden_states + context_attn_output

        norm_encoder_hidden_states = self.norm2_context(encoder_hidden_states)
        norm_encoder_hidden_states = (
            norm_encoder_hidden_states * (1 + c_scale_mlp) + c_shift_mlp
        )

        context_ff_output = self.ff_context(norm_encoder_hidden_states)
        encoder_hidden_states = encoder_hidden_states + c_gate_mlp * context_ff_output
        if encoder_hidden_states.dtype == torch.float16:
            encoder_hidden_states = encoder_hidden_states.clip(-65504, 65504)

```
