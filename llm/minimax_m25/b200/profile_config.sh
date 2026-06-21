FOLDER="minimax_m25"
MODEL="MiniMaxAI/MiniMax-M2.5"
CLEANUP_NAME="MiniMax-M2.5 FP8"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 8
  --ep 8
  --reasoning-parser minimax-append-think
  --trust-remote-code
  --mem-fraction-static 0.85
  --tool-call-parser minimax-m2
  --host 0.0.0.0
  --port "${PORT}"
)
