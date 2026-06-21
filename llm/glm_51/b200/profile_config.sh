FOLDER="glm_51"
MODEL="zai-org/GLM-5.1-FP8"
CLEANUP_NAME="GLM-5.1 FP8"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}

export SGLANG_ENABLE_SPEC_V2=${SGLANG_ENABLE_SPEC_V2:-1}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --trust-remote-code
  --model-path "${MODEL}"
  --tp 8
  --tool-call-parser glm47
  --reasoning-parser glm45
  --speculative-algorithm EAGLE
  --speculative-num-steps 3
  --speculative-eagle-topk 1
  --speculative-num-draft-tokens 4
  --mem-fraction-static 0.85
  --host 0.0.0.0
  --port "${PORT}"
)
