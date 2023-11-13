class Person:
    def __init__(self, identification, first_name, last_name):
        self.identification = identification
        self.first_name = first_name
        self.last_name = last_name

class Account:
    def __init__(self, number=1001, account_type="CHECKING", owner=Person(7, "", ""), balance=0):
        self.number = number
        self.account_type = account_type
        self.owner = owner
        self.balance = balance


class Bank(Account):
    def add_account(self, customer):
        if customer == (self.number, self.account_type, self.owner):
            return self.owner

    def deposit(self, num, money):
        if num == self.number:
            self.balance += money
        else:
            print("Sorry, your account number was not recognized")

    def withdrawal(self, num, money):
        if num == self.number:
            self.balance -= money
        else:
            print("Sorry, the account number you entered is not correct")

    def balance_inquiry(self, num):
        if num == self.number:
            return self.balance
        else:
            print("Sorry. that was the wrong account number.")


zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
zc_bank.add_account(bob)
bob_savings = Account(1001, "SAVINGS", bob)
zc_bank.add_account(bob_savings)
zc_bank.balance_inquiry(1001)
# 0
zc_bank.deposit(1001, 256.02)
zc_bank.balance_inquiry(1001)
# 256.02
zc_bank.withdrawal(1001, 128)
(zc_bank.balance_inquiry(1001))
# 128.02







# wsfs_bank = Bank()
#
# imir = Person(7, "Imir", "Ransom")




