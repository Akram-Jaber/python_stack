class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient funds")
        else:
            print("Withdrawal amount must be positive")

    def get_balance(self):
        return self.balance


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.username}, Balance: ${self.account.get_balance()}")
        return self

    def transfer_money(self, other_user, amount):
        if self.account.get_balance() >= amount:
            self.account.withdraw(amount)
            other_user.account.deposit(amount)
            print(f"Transferred ${amount} from {self.username} to {other_user.username}")
        else:
            print("Insufficient funds for transfer")
        return self


user1 = User("akram", "akram@example.com")
user2 = User("Jane", "jane@example.com")

user1.make_deposit(100).make_deposit(200).display_user_balance()
user2.make_deposit(300).display_user_balance()

user1.transfer_money(user2, 150).display_user_balance()
user2.display_user_balance()
