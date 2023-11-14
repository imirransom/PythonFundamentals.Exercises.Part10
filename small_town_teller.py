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


class Bank():
    def __init__(self):
        self.customer = []
        self.account = []

    def add_customer(self, customer):
        number = False
        for item in self.customer:
            if item.id == customer:
                number = False
                print("ID number already exists")
            else:
                if not number:
                    self.customer.append(customer)

    def add_account(self, customer):
        number = False
        for item in self.account:
            if item.id == customer:
                number = False
                print("ID number already exists")
            else:
                if not number:
                    self.account.append(customer)


    def deposit(self, account, num):
        for item in self.account:
            if item.number == account:
                item.balance += num


    def withdrawal(self, account, num):
        for item in self.account:
            if item.number == account:
                item.balance -= num


    def balance_inquiry(self, account):
        for item in self.account:
            if item.number == account:
                return item.balance

    def remove_account(self, account):
        for item in account:
            if item.number == account:
                self.account.remove(account)



            # if customer not in self.customer:
            #     self.customer.append(customer)
            # self.customer = [customer for customer in self.customer]
            # else:
            #     print("This person already have an account")


    # def add_customer(self, customer, account):
    #     if customer not in self.customer:
    #         self.customer.update({customer: account})
    #     else:
    #         print("Customer already exists")
    #
    # def add_account(self, customer, account):
    #     if customer in self.customer:
    #         self.customer[customer] += account






zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
bob_checking = Account(2001, "CHECKING", bob)
zc_bank.add_customer(bob)
bob_savings = Account(1001, "SAVINGS", bob)
zc_bank.add_account(bob)
zc_bank.balance_inquiry(1001)
# 0
zc_bank.deposit(1001, 256.02)
print(zc_bank.balance_inquiry(1001))
# 256.02
zc_bank.withdrawal(1001, 128)
(zc_bank.balance_inquiry(1001))
print(zc_bank.balance_inquiry(1001))
# 128.02
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




