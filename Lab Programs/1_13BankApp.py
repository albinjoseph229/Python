class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdraw amount or insufficient funds.")

    def check_balance(self):
        print(f"Account balance: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, overdraft_limit):
        super().__init__(account_number, account_holder)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdraw amount or exceeds overdraft limit.")


savings = SavingsAccount("A100", "Albin", 5.0)
savings.deposit(1000)
savings.check_balance()
savings.add_interest()

checking = CheckingAccount("A200", "Joseph", 500)
checking.deposit(500)
checking.check_balance()
checking.withdraw(800)
checking.check_balance()
