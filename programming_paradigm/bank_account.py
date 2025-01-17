class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds!")
        else:
            self.account_balance -= amount
            return self.account_balance

    def Current_Balance():
        print(f"Your curent balance {self.account_balance}")

