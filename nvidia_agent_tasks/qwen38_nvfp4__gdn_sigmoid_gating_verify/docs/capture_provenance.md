# Capture provenance

| field | value |
| --- | --- |
| model | RadixArk/Qwen3.8-27B-NVFP4 (revision 554ebba9b5f1b79dc11246341960360e6ef05ef4) |
| draft | RadixArk/Qwen3.8-27B-0811-DSpark-Stage2 (DSPARK block 8) |
| serving args | `python3 -m sglang.launch_server --model-path <snap> --trust-remote-code --tp-size 1 --disable-radix-cache --mem-fraction-static 0.85 --max-running-requests 8 --cuda-graph-max-bs 8 --mamba-ssm-dtype bfloat16 --kv-cache-dtype fp8_e4m3 --speculative-algorithm DSPARK --speculative-draft-model-path RadixArk/Qwen3.8-27B-0811-DSpark-Stage2 --speculative-dspark-block-size 8` |
| host | jimmy-sglang-kimi-ae1a-node-2 (GCP sglang-jax-1126, asia-east1-a) |
| GPU | NVIDIA RTX PRO 6000 Blackwell Server Edition (sm_120), CUDA_VISIBLE_DEVICES=0 |
| SGLang tree | main @ 8922bb98e2 + PR #34859 (conflict-resolved) + PR #34934 fusions (= BBuf/sglang qwen35-prefill-quant-fusions @ 611d8aaf94) |
| flashinfer / torch | 0.6.18 / 2.13.0+cu130 |
| capture date | 2026-08-19 |

### Capture-only modifiers

- tensors phase adds `--disable-cuda-graph` (python-level ops are invisible inside a captured graph)

### Operating points walked

| group | output tok/s | ITL median | accept |
| --- | ---: | ---: | ---: |
| `dspark_bs1_4k1k` (graphs ON, measured) | 153.3 | 3.48 ms | 3.47 |
| `nospec_bs1_4k1k` (graphs ON, measured) | 66.7 | 14.78 ms | - |

Workload source: `sglang.bench_serving` random 4096/1024, bs=1, seed 1234,
apply-chat-template. Verify tier geometry is exact by construction:
DSPARK block 8 makes every verify forward M=T=9.
