class Account:

    def __init__(self, balance, interest_rate):
        self.balance = 0.0
        self.withdraw_count = 0
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.withdraw_count += 1

class CheckingAccount(Account):
    ## it does not have constructor
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Cannot withdraw")
            self.balance = self.balance - 15
        else:
            super().withdraw(amount)

account1 = CheckingAccount(10, .001)
account1.withdraw(50.00)
#account1.withdraw(5.00)

# run with debug both cases

print(account1.balance)
