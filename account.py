class Account:
    """
    A class representing details for a bank account
    """
    def __init__(self, name: str) -> None:
        """
        Constructor to create initial account object
        :param name: Person's first name
        """
        self.__name = name
        self.__balance = 0

    def deposit(self, amount: float) -> True or False:
        """
        Method to add money to balance
        :param amount: amount of money being added
        :return: boolean for whether transaction was successful
        """
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> True or False:
        """
        Method to remove money from balance
        :param amount: amount of money being removed
        :return: boolean for whether transaction was successful
        """
        if amount <= 0 or amount > self.__balance:
            return False
        else:
            self.__balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to access balance
        :return: Account balance
        """
        return self.__balance

    def get_name(self) -> str:
        """
        Method to access name
        :return: Account owner name
        """
        return self.__name
