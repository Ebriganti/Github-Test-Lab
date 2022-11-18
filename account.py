class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self,amount):
        if amount <= 0 or amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

    def get_balance(self):
        return self.balance

    def get_name(self):
        return self.name