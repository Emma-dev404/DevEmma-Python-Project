#encapsulation - protects data and controls how it is accessed or changed

class BankAccount:
    def __init__(self,balance):
        self.balance = balance #private attribute

account = BankAccount(1000)
print(account.balance)
account.balance = -500
print(account.balance)


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  #Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


    def get_balance(self):
        return self.__balance

#Creating an account
account = BankAccount("Reynold",1000)
account.deposit(500)
print(account.get_balance())




