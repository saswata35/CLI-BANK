from src.app.storage import ensure_files
from src.app.manager import BankManager
from src.app.errors import AccountNotFound, InvalidAmount

def main():
    manager = BankManager()
    print("=== Welcome to CLI Bank ===")
    
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Delete Account\n6. Exit")
        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            name = input("Enter account holder name: ").strip()
            balance = float(input("Enter initial balance: ") or 0)
            acc = manager.create(name, balance)
            print(f"Account created successfully! ID: {acc._id}")

        elif choice == "2":
            acc_id = input("Enter Account ID: ").strip()
            amount = float(input("Enter amount to deposit: "))
            try:
                print(manager.deposit(acc_id, amount))
            except (AccountNotFound, ValueError) as e:
                print(f"Error: {e}")

        elif choice == "3":
            acc_id = input("Enter Account ID: ").strip()
            amount = float(input("Enter amount to withdraw: "))
            try:
                print(manager.withdraw(acc_id, amount))
            except (AccountNotFound, ValueError) as e:
                print(f"Error: {e}")

        elif choice == "4":
            src_id = input("Enter Source Account ID: ").strip()
            trg_id = input("Enter Target Account ID: ").strip()
            amount = float(input("Enter transfer amount: "))
            try:
                print(manager.transfer(src_id, trg_id, amount))
            except (AccountNotFound, ValueError) as e:
                print(f"Error: {e}")
        elif choice == "5":
            acc_id = input("Enter Account ID to delete: ").strip()
            try:
                print(manager.delete_account(acc_id))
            except AccountNotFound as e:
                print(f"Error: {e}")
        elif choice == "6":
            print("Thank you for using CLI Bank. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    ensure_files()
    main()