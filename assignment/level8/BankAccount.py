import random
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.account_number = random.randint(10000, 99999)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print(f"You balance is {self.balance}, please withdraw a valid amount!")
    def account_statement(self):
        print(f"Name: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")
