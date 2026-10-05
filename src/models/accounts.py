from src.models import generate_id
from src.app.errors import InvalidAmount
from src.config import RUPEE
class Account:

    def __init__(self,name : str, balance : float = 0):
        
        self._id = generate_id() # protected attribute
        self.name = name # public attribute
        self.__balance = balance # private attribute

    def deposit(self, value: float):
        if value < 10:
            raise InvalidAmount(f"Deposit amount must be more than {RUPEE}10.")

        self.__balance += value
        return self.__balance

    def withdraw(self, value: float):
        if value < 10:
            raise InvalidAmount(f"Amount must be more than {RUPEE}10.")  
        
        if self.__balance < value:
            raise InvalidAmount(f"Amount must be within {RUPEE}{self.__balance}.")      
        
        self.__balance -= value
        return self.__balance

    def balance(self):
        return self.__balance