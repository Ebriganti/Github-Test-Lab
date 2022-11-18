import pytest
from account import *

class Account:
    def setup_method(self):
        self.a1 = Account("John")

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == "John"

    def test_deposit(self):
        assert self.a1.deposit(30) is True
        assert self.a1.get_balance == 30
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance == 30
        assert self.a1.deposit(-30) is False
        assert self.a1.get_balance == 30

    def test_withdraw(self):
        assert self.a1.withdraw(10) is True
        assert self.a1.get_balance == 20
        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance == 20
        assert self.a1.withdraw(40) is False
        assert self.a1.get_balance == 20
        assert self.a1.withdraw(-10) is False
        assert self.a1.get_balance == 20
