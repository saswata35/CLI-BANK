import json
import os
from src.config import DB_DIR, ACC_JSON, TXN_JSON
from src.models import Account, Transaction

ACC_FILE = os.path.join(DB_DIR, ACC_JSON)
TXN_FILE = os.path.join(DB_DIR, TXN_JSON)

def ensure_files():
    """Ensure all the files and folders exist without wiping existing data."""
    os.makedirs(DB_DIR, exist_ok=True)
    for file_path in (ACC_FILE, TXN_FILE):
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([], f, indent=4)

def save_accounts(accounts: list[Account]):
    """Save all account details to the relevant JSON file."""
    with open(ACC_FILE, "w") as f:
        json.dump([acc.to_dict() for acc in accounts], f, indent=4)

def save_transaction(txn: Transaction):
    """Save transaction details to the relevant JSON file."""
    with open(TXN_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []

    data.append(txn.to_dict())

    with open(TXN_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_accounts() -> list[Account]:
    """Load all accounts from the relevant JSON file."""
    if not os.path.exists(ACC_FILE):
        return []
    with open(ACC_FILE, "r") as f:
        try:
            result = json.load(f)
        except json.JSONDecodeError:
            result = []
    return [Account.from_dict(acc) for acc in result]

def delete_transactions_by_account(acc_id: str):
    """Automatically remove transactions related to acc_id from the JSON file."""
    if not os.path.exists(TXN_FILE):
        return
    with open(TXN_FILE, "r") as f:
        try:
            transactions = json.load(f)
        except json.JSONDecodeError:
            transactions = []

    # Keep only transactions that do not belong to the deleted account
    filtered = [
        txn for txn in transactions
        if txn.get("source_id") != acc_id and txn.get("target_id") != acc_id
    ]

    with open(TXN_FILE, "w") as f:
        json.dump(filtered, f, indent=4)