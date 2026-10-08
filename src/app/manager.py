from src.app.storage import (
    load_accounts, 
    save_accounts, 
    save_transaction, 
    delete_transactions_by_account
)
from src.config import RUPEE
from src.app.errors import AccountNotFound
from src.models import Account, Transaction, generate_id

class BankManager:
    def __init__(self):
        self.__accounts = load_accounts()

    def create(self, name: str, balance: float = 0.0) -> Account:
        acc = Account(
            account_id=generate_id(),
            name=name,
            balance=balance
        )
        self.__accounts.append(acc)
        save_accounts(self.__accounts)
        return acc

    def find_account(self, acc_id: str) -> Account:
        for acc in self.__accounts:
            if acc._id == acc_id:
                return acc
        raise AccountNotFound(f"{acc_id} does not exist.")

    def deposit(self, acc_id: str, amount: float) -> str:
        acc = self.find_account(acc_id)
        acc.deposit(amount)

        txn = Transaction(
            "deposit",
            amount,
            acc._id,
        )
        save_accounts(self.__accounts)
        save_transaction(txn)
        return f"Deposited! New balance: {RUPEE}{acc.balance}"

    def withdraw(self, acc_id: str, amount: float) -> str:
        acc = self.find_account(acc_id)
        acc.withdraw(amount)

        txn = Transaction(
            "withdraw",
            amount,
            acc._id,
        )
        save_accounts(self.__accounts)
        save_transaction(txn)
        return f"Withdrawn! New balance: {RUPEE}{acc.balance}"

    def transfer(self, acc_id: str, trg_id: str, amount: float) -> str:
        acc = self.find_account(acc_id)
        trg = self.find_account(trg_id)

        acc.withdraw(amount)
        trg.deposit(amount)

        txn = Transaction("transfer", amount, acc._id, trg._id)
        save_accounts(self.__accounts)
        save_transaction(txn)
        return f"Transferred {RUPEE}{amount}! New balance: {RUPEE}{acc.balance}"

    def delete_account(self, acc_id: str) -> str:
        # Check if account exists, raises AccountNotFound if not
        acc = self.find_account(acc_id)

        # 1. Remove account from memory and update accounts JSON
        self.__accounts = [a for a in self.__accounts if a._id != acc_id]
        save_accounts(self.__accounts)

        # 2. Automatically remove transactions linked to this account from JSON
        delete_transactions_by_account(acc_id)

        return f"Account {acc_id} ({acc.name}) and all associated transactions deleted successfully."