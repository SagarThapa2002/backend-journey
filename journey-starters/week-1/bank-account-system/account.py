from exceptions import InvalidAmountError, InsufficientFundsError

class BankAccount:
    def __init__(self, holder_name: str, balance: float= 0.0):
        if not holder_name:
            raise ValueError("Account holder name cannot be empty.\nPlease enter the account holder name and try again!")
        if balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative.")
        
        self.holder_name= holder_name
        self.balance=balance

    def deposit(self, amount:float)-> None:
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be grater than 0.")
        self.balance+= amount

    def withdraw(self, amount:float)-> None:
        if amount <=0:
            raise InvalidAmountError("withdrawal amount must be greater than 0")
        if amount > self.balance:
            raise InsufficientFundsError("Not enough balance. ")
        self.balance -= amount
    
    def get_balance(self)->float:
        return self.balance