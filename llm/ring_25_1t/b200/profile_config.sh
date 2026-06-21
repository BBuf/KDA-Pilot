FOLDER="ring_25_1t"
MODEL="inclusionAI/Ring-2.5-1T"
CLEANUP_NAME="Ring-2.5-1T FP8"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp-size 8
  --trust-remote-code
  --host 0.0.0.0
  --port "${PORT}"
  --model-loader-extra-config '{"enable_multithread_load":true,"num_threads":64}'
  --watchdog-timeout 1800
  --soft-watchdog-timeout 1800
  --reasoning-parser deepseek-r1
  --tool-call-parser qwen
)
