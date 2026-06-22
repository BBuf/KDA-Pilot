# FlashLabs/Chroma-4B B200 Kernel Interface Task Index

- Generated at: `2026-06-22T05:37:25Z`
- Model slug: `chroma_10`
- Source capture dir: `/data/bbuf/kda-pilot/llm/chroma_10/b200/capture`
- Task count: `6`
- Evidence policy: runtime capture at SGLang kernel Python interfaces.
- Workload labels: `chroma_audio_low`, `chroma_audio_mid`, `chroma_audio_high`

## Category Counts

| Category | Tasks |
|---|---:|
| `norm` | 1 |
| `other` | 4 |
| `quantization` | 1 |

## Tasks

| Task id | Category | Interface | Calls | Variants | Workloads |
|---|---|---|---:|---:|---|
| `sglang_srt_layers_quantization_unquant_unquantized_linear_method_apply` | `quantization` | `sglang.srt.layers.quantization.unquant.UnquantizedLinearMethod.apply` | 29328 | 24 | `chroma_audio_low`, `chroma_audio_mid`, `chroma_audio_high` |
| `sglang_srt_layers_layernorm_rmsnorm` | `norm` | `sglang.srt.layers.layernorm.rmsnorm` | 14868 | 6 | `chroma_audio_low`, `chroma_audio_mid`, `chroma_audio_high` |
| `sglang_srt_layers_linear_column_parallel_linear_forward` | `other` | `sglang.srt.layers.linear.ColumnParallelLinear.forward` | 14664 | 6 | `chroma_audio_low`, `chroma_audio_mid`, `chroma_audio_high` |
| `sglang_srt_layers_linear_row_parallel_linear_forward` | `other` | `sglang.srt.layers.linear.RowParallelLinear.forward` | 14664 | 12 | `chroma_audio_low`, `chroma_audio_mid`, `chroma_audio_high` |
| `sglang_srt_layers_activation_silu_and_mul` | `other` | `sglang.srt.layers.activation.silu_and_mul` | 7332 | 6 | `chroma_audio_low`, `chroma_audio_mid`, `chroma_audio_high` |
| `sglang_srt_layers_vocab_parallel_embedding_vocab_parallel_embedding_forward` | `other` | `sglang.srt.layers.vocab_parallel_embedding.VocabParallelEmbedding.forward` | 446 | 12 | `chroma_audio_low`, `chroma_audio_mid`, `chroma_audio_high` |
