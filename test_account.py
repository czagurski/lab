import pytest
from account import*


class Test:
    def setup_method(self):
        self.a1 = Account('John')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'Jane'
        assert self.a1.get_age() == 10
        assert self.a1.get_name() == 'John'
        assert self.a1.get_age() == 20

    def test_deposit(self):
        assert self.a1.deposit(-1.5) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(1.5) is True
        assert self.a1.get_balance() == pytest.approx(1.5, abs=0.01)

    def test_withdraw(self):
        pass