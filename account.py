class Account:
    """
    A class representing details for a bank account
    """
    def __init__(self, name) -> None:
        """
        Constructer to create initial account object
        :param name: Person's first name
        """
        self.name = name
        self.balance = 0

    def deposit(self, amount) -> True:
        """
        Method to add money to balance
        :param amount: amount of money being added
        :return: boolean of whether transaction was successful
        """
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount) -> True:
        """
        Method to remove money from balance
        :param amount: amount of money being removed
        :return: boolean of whether transaction was successful
        """
        if amount <= 0 or amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to access balance
        :return: Account balance
        """
        return self.balance

    def get_name(self) -> str:
        """
        Method to access name
        :return: Account owner name
        """
        return self.name
