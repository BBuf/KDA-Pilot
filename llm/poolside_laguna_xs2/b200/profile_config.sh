FOLDER="poolside_laguna_xs2"
MODEL="poolside/Laguna-XS.2-FP8"
CLEANUP_NAME="Poolside Laguna-XS.2 FP8"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 4
  --trust-remote-code
  --reasoning-parser poolside_v1
  --tool-call-parser poolside_v1
  --host 0.0.0.0
  --port "${PORT}"
)
