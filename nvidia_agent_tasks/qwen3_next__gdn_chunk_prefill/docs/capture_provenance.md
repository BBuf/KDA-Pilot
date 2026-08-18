# Capture provenance

| field | value |
| --- | --- |
| model | `/scratch/models/qwen3_next` |
| serving args | `--trust-remote-code --tp 8` (SGLang cookbook recipe for Qwen3-Next: `--tp 8`) |
| host | light-face-hides-fin-03-1 (RadixArk devbox b300-diffusion-kernel-opt) |
| GPUs used | 0,1,2,3,4,5,6,7 |
| SGLang commit | `43226af` |
| torch / triton / transformers | 2.13.0+cu130 / 3.7.1 / 5.12.1 |
| GPU | NVIDIA B300 SXM6 AC |

## Capture-only modifiers

- --disable-cuda-graph (python-level ops are invisible inside a captured graph)
- tensors phase adds --disable-radix-cache (radix cache rewrites mamba/state pool rows outside the kernel call and breaks the state chain; shapes phase keeps radix ON so prefix-hit-driven chunk lengths stay realistic)

## Capture matrix actually walked

| group | phase | started (UTC) | GSM8K accuracy |
| --- | --- | --- | --- |
| `random_1k1k_cc1` | shapes | 13:11:25 | - |
| `sharegpt_cc32` | short | 13:16:34 | - |
| `gsm8k_5shot_cc1` | gsm | 13:22:51 | 1.000 |
| `gsm8k_16shot_cc16` | gsm | 13:23:56 | 1.000 |
| `gsm8k_5shot_cc32` | gsm | 13:26:42 | - |

The synthetic `random 1k/1k` groups were cut short on this model: at TP8 with CUDA
graphs disabled (required for the capture) a 1024-token-output group takes tens of
minutes, and the GDN chunk path was already covered. The real-GSM8K groups were run
instead and are the ones that matter for this kernel family - the gate statistics of
a Gated DeltaNet only look realistic on real text.

## What fired, and what did not

The FLA Triton chunk path (`chunk_gated_delta_rule_fwd` and its `chunk_delta_h` /
`chunk_o` / `recompute_w_u` sub-kernels) fires on every prefill in every group -
3,744 real calls across 13 distinct signatures. `fused_recurrent_gated_delta_rule_fwd`
(the FLA decode path) did **not** fire on B300: Qwen3-Next decode is served by the
Blackwell-specific linear-attention kernels (`linear/gdn_blackwell`, and for the KDA
variant NVIDIA's own `linear/kda_nvidia_prefill`), so the FLA recurrent kernel is a
non-Blackwell path here. The chunk prefill kernels are the live target on this GPU.

Qwen3-Next also drives the Triton unified attention backend for its full-attention
layers (258,992 real decode calls) - that shape family is shipped as
`bench/workloads_qwen3_next_secondary.json` in task A2, which is about that kernel.
