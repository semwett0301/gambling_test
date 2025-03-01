from datetime import datetime

_timestamp_dir = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
SCREEN_DIR = f"./data/screenshots/{_timestamp_dir}"

RESULT_DIR = f"./data/results/{_timestamp_dir}"
JSON_PATH = f"{RESULT_DIR}/result.jsonl"