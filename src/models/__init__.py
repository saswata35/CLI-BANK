import uuid
from .accounts import Account
from .transactions import Transaction
from .utils import generate_id

# def generate_id():
#     parts=str(uuid.uuid4()).split("-")
#     return f"{parts[0]}**{parts[1]}{parts[2]}"

__all__ = ["Account","Transaction","generate_id"]