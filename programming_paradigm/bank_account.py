class BankAccount:
    def __init__(self, initial_balance = 0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
        elif amount <= 0: 
            print("Withdrawal amount must be positive.")
        else:
            self.account_balance -= amount
            return self.account_balance

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

