FOLDER="inclusion_ring26"
MODEL="inclusionAI/Ring-2.6-1T"
CLEANUP_NAME="InclusionAI Ring-2.6-1T FP8"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp-size 8
  --trust-remote-code
  --host 0.0.0.0
  --port "${PORT}"
  --mem-fraction-static 0.8
  --model-loader-extra-config '{"enable_multithread_load":"true","num_threads":64}'
  --tool-call-parser glm
  --reasoning-parser deepseek-r1
)
