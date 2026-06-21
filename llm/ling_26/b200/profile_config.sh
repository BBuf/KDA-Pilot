FOLDER="ling_26"
MODEL="inclusionAI/Ling-2.6-flash"
CLEANUP_NAME="Ling-2.6-flash BF16"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}
export SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp-size 4
  --trust-remote-code
  --host 0.0.0.0
  --port "${PORT}"
  --context-length 262144
  --json-model-override-args '{"rope_scaling": {"rope_type": "yarn", "factor": 2.0, "rope_theta": 6000000, "partial_rotary_factor": 0.5, "original_max_position_embeddings": 131072}}'
  --tool-call-parser qwen25
)
