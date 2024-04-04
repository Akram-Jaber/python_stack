class bank_account:
    def __init__(self,rate,balance):
        self.rate=rate
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self
    def withdraw(self,amount):
        self.balance-=amount
        return self
    def display_account_info(self):
        print("balance:",self.balance)
        return self
    def yield_interest(self):
        if (self.balance>=0):
            self.balance+=self.balance
            return self
akram=bank_account(4,0)
akram.deposit(500).deposit(700).withdraw(200).yield_interest().display_account_info()
