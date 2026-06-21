FOLDER="step35_flash"
MODEL="stepfun-ai/Step-3.5-Flash"
CLEANUP_NAME="Step-3.5-Flash BF16"
COOKBOOK_PAGE="StepFun/Step3.5.md"
DOCKER_IMAGE="lmsysorg/sglang:dev-pr-18084"
PORT=${PORT:-30000}
CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}

# Cookbook NVIDIA/H200 command: TP4 BF16; enable the documented Step-3.5 reasoning parser.
SERVER_ARGS=(
  sglang serve
  --model-path "${MODEL}"
  --tp 4
  --trust-remote-code
  --reasoning-parser step3p5
  --host 0.0.0.0
  --port "${PORT}"
)
