import datetime
from typing import Literal
from .utils import generate_id

class Transaction:
    def __init__(
        self,
        txn_type:Literal["deposit","withdraw","transfer"],
        amount : float,
        source_id:str,
        target_id:str | None = None,
    ):
        self._id= generate_id()
        self.txn_type=txn_type
        self.amount=amount
        self.source_id = source_id
        self.target_id =target_id
        self.timestamp=datetime.datetime.now().isoformat()

    def to_dict(self):
        """return all the data in a dictionary"""
        return {
            "id":self._id,
            "txn_type":self.txn_type,
            "amount":self.amount,
            "source_id":self.source_id,
            "target_id":self.target_id,
            "timestamp":self.timestamp,
        }