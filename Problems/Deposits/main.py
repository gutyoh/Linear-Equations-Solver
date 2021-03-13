from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, starting_sum, interest=None):
        self.sum = starting_sum
        self.interest = interest
        super().__init__()

    @abstractmethod
    def add_money(self, amount):
        self.amount = amount

    def add_interest(self, interest):
        ...


# create SavingsAccount and Deposit
class SavingsAccount(Account):
    def add_money(self, amount):
        if amount >= 10:
            self.sum += amount
        else:
            print("Cannot add to SavingsAccount: amount too low.")

    def add_interest(self, interest=0):
        return self.sum


class Deposit(Account):
    def add_money(self, amount):
        if amount >= 50:
            self.sum += amount
        else:
            print("Cannot add to Deposit: amount too low.")

    def add_interest(self, interest=None):
        self.sum = (self.sum * self.interest) + self.sum
        return self.sum


new_savings = SavingsAccount(50)
new_savings.add_money(5)
new_savings.add_money(30)
new_savings.add_interest(5)
print(new_savings.sum)

new_deposit = Deposit(60, 0.078)
new_deposit.add_money(30)
new_deposit.add_money(70)
new_deposit.add_interest()
print(new_deposit.sum)
