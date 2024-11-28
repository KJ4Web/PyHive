class BankAccount:
    def __init__(self):
        self.__balance = 0.0
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.2f}.\n New balance: ${self.__balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.__balance:.2f}.")

    def check_balance(self):
        return f"Current balance: ${self.__balance:.2f}"
account = BankAccount()
account.deposit(100.00)
account.withdraw(150.00)
print(account.check_balance())