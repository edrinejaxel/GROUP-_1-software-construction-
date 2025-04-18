
from account import Account

class SavingsAccount(Account):
    def __init__(self, account_id, balance=0.0, interest_rate=0.02, status='active', creation_date=None):
        super().__init__(account_id, account_type='Savings', balance=balance, status=status, creation_date=creation_date)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Apply interest to the current balance."""
        interest_amount = self.balance * self.interest_rate
        self.deposit(interest_amount)

    def get_account_info(self):
        """Override to include interest rate in account info."""
        info = super().get_account_info()
        info['interest_rate'] = self.interest_rate
        return info
