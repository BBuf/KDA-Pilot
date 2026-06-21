FOLDER="kimi_k25"
MODEL="moonshotai/Kimi-K2.5"
CLEANUP_NAME="Kimi-K2.5 INT4"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 8
  --reasoning-parser kimi_k2
  --tool-call-parser kimi_k2
  --trust-remote-code
  --host 0.0.0.0
  --port "${PORT}"
)
