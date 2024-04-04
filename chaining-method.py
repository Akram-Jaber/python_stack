class User:
    def __init__(self,username,email,balance):
        self.username=username
        self.email=email
        self.balance=balance

    def make_deposit(self,amount):
        self.balance+=amount
        return self
    def make_withdrawal(self, amount):
        self.balance-=amount
        return self
    def display_user_balance(self):
        print("the user balance",self.username,"your balance is",self.balance) 
        return self
    def transfer_money(self,first_user,my_balance):
        self.make_withdrawal(my_balance)
        first_user.make_deposit(my_balance)
        return self

mohamed=User("mohamed","mohamed@gmail.com",0)
mohamed.make_deposit(200).make_deposit(500).make_deposit(1000).display_user_balance()
Akram=User("akram","akram@gmail.com",500)
Akram.make_deposit(500).make_deposit(300).make_deposit(100)
Akram.make_deposit(500).make_withdrawal(500)
Ziad=User("Ziad","ziad@gmail.com",500)
mohamed.transfer_money(Akram,1000).display_user_balance()

