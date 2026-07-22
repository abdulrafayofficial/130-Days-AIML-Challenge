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
        

class SavingsAccount(BankAccount):
    def __init__(self, owner_name, balance, interest_rate):
        super().__init__(owner_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self,interest_rate):
        return self.balance * (interest_rate/100)



class CurrentAccount(BankAccount):
    def __init__(self, owner_name, balance,overdraft_limit):
        super().__init__(owner_name, balance)
        self.overdraft_limit = overdraft_limit


    def withdraw(self, amount):
        if amount > (self.balance + self.overdraft_limit):
            print("Overdraft limit exceeded!")
        else:
            self.balance -= amount
        return self.balance
    
s1 = SavingsAccount('Ali', 5000, 5) 
print(s1.get_balance())               
print(s1.add_interest(5))              

c1 = CurrentAccount('Sara', 1000, 5000)
c1.withdraw(3000)                     
print(c1.get_balance())
c1.withdraw(10000)                    

print(isinstance(s1, BankAccount))    
print(isinstance(c1, SavingsAccount))  
