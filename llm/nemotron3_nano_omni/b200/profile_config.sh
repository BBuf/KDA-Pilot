FOLDER="nemotron3_nano_omni"
MODEL="nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4"
CLEANUP_NAME="Nemotron3-Nano-Omni 30B-A3B NVFP4"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --host 0.0.0.0
  --port "${PORT}"
  --tp 4
  --trust-remote-code
  --tool-call-parser qwen3_coder
  --reasoning-parser deepseek-r1
  # The default SM100 NemotronH MoE path hit a ModelOpt mixed FP4
  # cutlass_moe_fp4 shape assertion during FlashInfer autotune and then
  # CUDA graph capture dummy forwards. Eager mode then required page_size=1
  # for MambaRadixCache, so avoid the trtllm_mha page_size=64 override.
  --attention-backend flashinfer
  --page-size 1
  --disable-flashinfer-autotune
  --disable-cuda-graph
)
