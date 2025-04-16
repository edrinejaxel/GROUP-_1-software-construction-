

from account import Account
from domain.exeptions import InvalidAmountError, InsufficientBalanceError, AccountClosedError

class CheckingAccount(Account):
    def __init__(self, account_id, balance=0.0, overdraft_limit=0.0, status='active', creation_date=None):
        super().__init__(account_id, account_type='Checking', balance=balance, status=status, creation_date=creation_date)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.status == 'closed':
            raise AccountClosedError()
        if amount <= 0:
            raise InvalidAmountError()
        if amount > self.balance + self.overdraft_limit:
            raise InsufficientBalanceError("Withdrawal exceeds balance and overdraft limit.")
        self.balance -= amount

    def get_account_info(self):
        """Override to include overdraft limit in account info."""
        info = super().get_account_info()
        info['overdraft_limit'] = self.overdraft_limit
        return info
