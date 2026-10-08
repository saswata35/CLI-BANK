from src.models.transactions import generate_id
from src.app.errors import InvalidAmount, AccountNotFound
from .utils import generate_id
class Account:
    def __init__(self, name: str, balance: float = 0.0, account_id: str | None = None):
        self._id = account_id if account_id else generate_id()
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def to_dict(self) -> dict:
        return {
            "account_id": self._id,
            "name": self.name,
            "balance": self.balance
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name=data["name"],
            balance=data["balance"],
            account_id=data.get("account_id") or data.get("id")
        )