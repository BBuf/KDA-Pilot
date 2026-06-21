FOLDER="mistral_medium35"
MODEL="mistralai/Mistral-Medium-3.5-128B"
CLEANUP_NAME="Mistral Medium 3.5 FP8"
EXTRA_MODEL_IDS="mistralai/Mistral-Medium-3.5-128B-EAGLE"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1}

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --tp 2
  --reasoning-parser mistral
  --tool-call-parser mistral
  --dtype bfloat16
  --speculative-algorithm EAGLE
  --speculative-draft-model-path mistralai/Mistral-Medium-3.5-128B-EAGLE
  --speculative-num-steps 3
  --speculative-eagle-topk 1
  --speculative-num-draft-tokens 4
  --mem-fraction-static 0.85
  --context-length 32768
  --host 0.0.0.0
  --port "${PORT}"
)
