FOLDER="deepseek_math_v2"
MODEL="deepseek-ai/DeepSeek-Math-V2"
CLEANUP_NAME="DeepSeek-Math-V2 BF16"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

export HF_HUB_DOWNLOAD_TIMEOUT=${HF_HUB_DOWNLOAD_TIMEOUT:-600}
export HF_HUB_ETAG_TIMEOUT=${HF_HUB_ETAG_TIMEOUT:-60}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --trust-remote-code
  --model-path "${MODEL}"
  --tp 8
  --ep 8
  --reasoning-parser deepseek-r1
  --host 0.0.0.0
  --port "${PORT}"
)
