from random import randrange
from unittest import TestCase
from account import Account, make_transaction, bank

__author__ = 'fomars'


class AccountTest(TestCase):
    initial_balance = 250
    random_amount = lambda self: randrange(1, 200)

    def test_user_user_transaction(self):
        print "___ test user-user transaction ___"
        initial_balance = self.initial_balance
        user1 = Account('user1', initial_balance)
        user2 = Account('user2', initial_balance)
        amount = self.random_amount()
        make_transaction(user1, user2, amount)
        print amount, user1.balance, user2.balance
        assert user1.balance == initial_balance-amount
        assert user2.balance == initial_balance+amount
        print '___ end ___\n'
        
    def test_three_users_transactions(self):
        print '___ test three users ___'
        ib = self.initial_balance
        amount1 = self.random_amount()
        amount2 = self.random_amount()
        amount3 = self.random_amount()
        user1 = Account('user1', ib)
        user2 = Account('user2', ib)
        user3 = Account('user3', ib)
        make_transaction(user1, user2, amount1)
        make_transaction(user2, user3, amount2)
        make_transaction(user3, user1, amount3)
        print amount1, amount2, amount3
        print user1.balance, user2.balance, user3.balance
        assert user1.balance == ib-amount1+amount3
        assert user2.balance == ib+amount1-amount2
        assert user3.balance == ib+amount2-amount3
        print '___ end ___\n'

    def test_user_bank(self):
        print '___ test user-bank transaction ___'
        amount = randrange(-200, 200)
        user = Account('user', self.initial_balance)
        make_transaction(user, bank, amount)
        print amount
        print user.balance
        assert user.balance == self.initial_balance-amount
        print '___ end ___\n'