FOLDER="minimax_m2"
MODEL="MiniMaxAI/MiniMax-M2"
CLEANUP_NAME="MiniMax-M2"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp-size 4
  --reasoning-parser minimax-append-think
  --trust-remote-code
  --mem-fraction-static 0.85
  --host 0.0.0.0
  --port "${PORT}"
)
