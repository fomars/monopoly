__author__ = 'fomars'


class Transaction(object):
    def __init__(self, partner, amount):
        self.partner = partner
        self.amount = amount


class Account(object):

    def __init__(self, username, balance):
        self.username = username
        self._balance = balance
        self._list_of_all_transactions = []
        self._list_of_pending_transactions = []

    @property
    def balance(self):
        for transaction in self._list_of_pending_transactions:
            self._balance += transaction.amount
            self._list_of_all_transactions.append(transaction)
        del self._list_of_pending_transactions[:]
        return self._balance

    def add_transaction(self, partner, amount):
        if isinstance(partner, Account):
            partner = partner.username
        self._list_of_pending_transactions.append(Transaction(partner, amount))

bank = Account('BANK', 0)


def make_transaction(_from, _to, amount):
    """
    adds amount to _to and subtracts it from _from
    :type _from: Account
    :type _to: Account
    :type amount: int
    """
    _from.add_transaction(_to, -amount)
    _to.add_transaction(_from, amount)