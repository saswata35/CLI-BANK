import os
import json
from src.config import DB_DIR, ACC_JSON, TXN_JSON

def ensure_files():
    """Ensure all the files and folders exists when the code runs."""
    os.makedirs(DB_DIR, exist_ok=True)
    # os.makedirs(DB_DIR)
    for i in (ACC_JSON, TXN_JSON):
        with open(f"{DB_DIR}/{i}", "w") as f:
            json.dump([], f, indent=4)
    