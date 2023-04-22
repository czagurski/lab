from pytest import*
from account import*


class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        pass

    def test_deposit(self):
        pass

    def test_withdraw(self):
        pass