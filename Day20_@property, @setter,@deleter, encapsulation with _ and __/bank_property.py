class LogMixin:
    def print_Action(self):
        print('LOG: [action] performed')

class NotificationMixin:
    def simulate_notification(self):
        print('Notification: [message] sent to user')

class BankAccount:

    total_accounts = 0

    def __init__(self,owner_name,balance):
        self.owner_name = owner_name
        self.__balance = balance
        self.__transaction_log = []
        BankAccount.total_accounts +=1

    def deposit(self,amount):
        if self.validate_amount(amount):
            self.__balance += amount
            self.__transaction_log.append(f"Deposited: Rs.{amount}")
            return self.balance
        else:
            print('invalid Amount')
    

    def withdraw(self,amount):
        if self.validate_amount(amount):
            if amount > self.balance:
                print('you donot have that much balance!')
            else:
                self.__balance -= amount
                self.__transaction_log.append(f"Withdrew: Rs.{amount}")
        else:
            print('invalid Amount')

        return self.balance

    @property
    def transaction_log(self):
        return self.__transaction_log.copy()


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


    def __str__(self):
        return f"{self.owner_name} your balance is {self.balance} Rs."


    def __repr__(self):
        return f"BankAccount('{self.owner_name}', {self.balance})"

    
    def __len__(self):
        return int(self.balance)

    def __add__(self, other):
        if isinstance(other, BankAccount):
             return self.balance + other.balance
        elif isinstance(other, (int, float)):
             return self.balance + other
        return NotImplemented


    def __eq__(self, value):
        return self.__balance == value.balance
    
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Balance negative nahi ho sakta!")
        else:
            self.__balance = value

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


class PremiumAccount(BankAccount,LogMixin,NotificationMixin):
    def __init__(self, owner_name, balance):
        super().__init__(owner_name, balance)

    def deposit(self, amount):
        result = super().deposit(amount)
        self.print_Action() 
        self.simulate_notification()
        return result
        
        
    def withdraw(self, amount):
        result=  super().withdraw(amount)
        self.print_Action()
        self.simulate_notification()
        return result

    
    
s1 = SavingsAccount('Ali', 5000, 5) 
print(s1.get_balance())               
print(s1.add_interest(5))              

c1 = CurrentAccount('Sara', 1000, 5000)
c1.withdraw(3000)                     
print(c1.get_balance())
c1.withdraw(10000)                    

print(isinstance(s1, BankAccount))    
print(isinstance(c1, SavingsAccount))  


p1 = PremiumAccount('Abdul Rafay' , 450)
print(p1.get_balance())
print(p1.deposit(500))


b1 = BankAccount('Abdul Rafay',590)
print(b1)
print(repr(b1))

print(len(b1))

b2 = BankAccount('Ab',340)
b3 = BankAccount('RA', 40)
print(b2+b3)
print(b2 == b3)


f1 = BankAccount('Abdul Rafay', 500)
f1.deposit(200)
f1.withdraw(50)
f1.withdraw(1000) # Failed

print(f1.transaction_log) 
