from abc import ABC,abstractmethod

class Account(ABC):
    balance = 0
    def get_balance(self):
        print(f"Current balance is : {self.balance}")

    @abstractmethod
    def deposite(self,amount):
        pass
        
    @abstractmethod
    def withdrow(self, amount):
        pass


class Saving(Account):

    def deposite(self, amount):
        self.balance+=amount

    def withdrow(self, amount):
        if amount>self.balance:
            print("Insuffcient amount")
        else:
            self.balance-=amount

class Loan(Account):

    def withdrow(self, amount):
        self.balance+=amount
    
    def deposite(self, amount):
        if amount>self.balance:
            k = amount-self.balance
            print(f"apne jayad adiye : {k}")
            self.balance=0
        else:
            self.balance-=amount


# s = Saving()
# s.get_balance()
# s.deposite(8000)
# s.get_balance()
# s.withdrow(5000)
# s.get_balance()

l = Loan()
l.withdrow(15000)
l.deposite(115000)
l.get_balance()
