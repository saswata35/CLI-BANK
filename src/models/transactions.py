import datetime
from typing import Literal
from src.models import generate_id
class Transaction:
    def __init__(
        self, 
        txn_type: Literal["deposit", "withdraw","transfer"],
        amount: float,
        source_id: str,
        target_id: str
    ):
        self._id = generate_id()  # private attribute
        self.txn_type = txn_type  # public attribute
        self.amount = amount  # public attribute
        self.source_id = source_id  # public attribute
        self.target_id = target_id  # public attribute
        self.timestamp = datetime.datetime.now().isoformat()  # public attribute
