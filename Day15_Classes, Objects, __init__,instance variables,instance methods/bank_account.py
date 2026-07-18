class BankAccount:

    def __init__(self,owner_name,balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    

    def withdraw(self,amount):
        if amount > self.balance:
            print('you donot have that much balance!')
        else:
            self.balance -= amount
        return self.balance


    def get_balance(self):
        return self.balance

Account1 = BankAccount('AbdulRafay',5000)
Account2 = BankAccount('AbdulWasay',6000)
Account3 = BankAccount('Manahil',7000)


# Account1.withdraw(99999)---> error msg 