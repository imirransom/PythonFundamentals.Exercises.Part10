class Person:
    def __int__(self, identification, first_name, last_name):
        self.id = identification
        self.first_name = first_name
        self.last_name = last_name

class Account:
    def __init__(self, number, account_type, owner, balance):
        self.number = number
        self.account_type = account_type
        self.owner = owner
        self.balance = balance



class Bank(Person, Account):

    def add_account(self, customer):
        account_name = (self.number, self.account_type, self. first_name)
        if customer == account_name:
            return customer

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