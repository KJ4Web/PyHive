class InsufficientFundsError(Exception):
    def __init__(self, message):
        super().__init__(message)
class BankAccount:
    def __init__(self, balance, min_balance):
        self.balance = balance
        self.min_balance = min_balance
    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print()
            raise InsufficientFundsError(f"Withdrawal of {amount} exceeds the minimum balance requirement. "
                                          f"Current balance: {self.balance}, Minimum balance: {self.min_balance}.")
        self.balance -= amount
        print()
        print(f"Withdrawal successful! New balance: {self.balance}")

if __name__ == "__main__":
    account = BankAccount(balance=1000, min_balance=200)
    try:
        account.withdraw(900)  
    except InsufficientFundsError as e:
        print(e)
    try:
        account.withdraw(300)  
    except InsufficientFundsError as e:
        print(e)
    try:
        account.withdraw(200)  
    except InsufficientFundsError as e:
        print(e)
    print()
    print(f"Final balance: {account.balance}")
    print()