class BankAccount:

    total_accounts = 0

    def __init__(self,owner_name,balance):
        self.owner_name = owner_name
        self.balance = balance
        BankAccount.total_accounts +=1

    def deposit(self,amount):
        if self.validate_amount(amount):
            self.balance += amount
            return self.balance
        else:
            print('invalid Amount')
    

    def withdraw(self,amount):
        if self.validate_amount(amount):
            if amount > self.balance:
                print('you donot have that much balance!')
            else:
                self.balance -= amount
        else:
            print('invalid Amount')

        return self.balance


    def get_balance(self):
        return self.balance
    
    @classmethod
    def get_total_accounts(cls):
        return BankAccount.total_accounts
    
    @classmethod
    def from_dict(cls,data):
        return cls(data['owner'],data['balance'])
    
    
    @staticmethod
    def validate_amount(amount):
        if amount > 0:
            return True
        else:
            return False
        

Account1 = BankAccount('AbdulRafay',5000)
Account2 = BankAccount('AbdulWasay',6000)
Account3 = BankAccount('Manahil',7000)
data = {
    'owner': 'sara',
    'balance': 8000
}
Account4 = BankAccount.from_dict(data)
print(Account4.balance)





print(BankAccount.get_total_accounts())
print(BankAccount.validate_amount(40)) #True
print(BankAccount.validate_amount(-40)) #False


Account1.deposit(90)
print(Account1.get_balance())