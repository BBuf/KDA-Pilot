FOLDER="nemotron3_super"
MODEL="nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16"
CLEANUP_NAME="Nemotron3-Super 120B-A12B BF16"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --host 0.0.0.0
  --port "${PORT}"
  --trust-remote-code
  --tp 4
  --tool-call-parser qwen3_coder
  --reasoning-parser nemotron_3
)
