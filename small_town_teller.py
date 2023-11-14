class Person:
    def __init__(self, identification, first_name, last_name):
        self.identification = identification
        self.first_name = first_name
        self.last_name = last_name


class Account:
    def __init__(self, number, account_type, owner, balance=0):
        self.number = number
        self.account_type = account_type
        self.owner = owner
        self.balance = balance


class Bank(Account, Person):
    def __init__(self):
        self.customer = {}

    def add_customer(self, customer, account):
        if customer not in self.customer:
            self.customer.update({customer: account})
        else:
            print("Customer already exists")

    def add_account(self, customer, account):
        if customer in self.customer:
            self.customer[customer] += account



dict1 = {"Test": ["a string", "another string"]}

dict1["Test"] += ["and another string", "one more string"]

print(dict1)



zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
bob_checking = Account(2001, "CHECKING", bob)
zc_bank.add_customer(bob, bob_checking)
bob_savings = Account(1001, "SAVINGS", bob)
zc_bank.add_account(bob, bob_savings)
# zc_bank.balance_inquiry(1001)
# # 0
# zc_bank.deposit(1001, 256.02)
# zc_bank.balance_inquiry(1001)
# # 256.02
# zc_bank.withdrawal(1001, 128)
# (zc_bank.balance_inquiry(1001))
# print(zc_bank.balance_inquiry(1001))
# # 128.02
#
# wsfs_bank = Bank()
# imir = Person(7, "Imir", "Ransom")
# wsfs_bank.add_account(imir)
# imir_checking = Account(7707, "CHECKING", imir)
# wsfs_bank.add_account(imir_checking)
# wsfs_bank.balance_inquiry(7707)
# # 0
# wsfs_bank.deposit(7707, 1300)
# wsfs_bank.balance_inquiry(7077)
# # 1300
# wsfs_bank.withdrawal(7707, 200)
# wsfs_bank.balance_inquiry(7707)
# print(wsfs_bank.balance_inquiry(7707))




# wsfs_bank = Bank()
#
# imir = Person(7, "Imir", "Ransom")




