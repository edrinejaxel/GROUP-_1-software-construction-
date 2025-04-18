

from collections import defaultdict
from domain.entities.account import Account

class AccountRepository:
    def __init__(self):
        self.accounts = {}
        self.next_account_id = 1

    def create_account(self, account: Account) -> int:
        self.accounts[account.account_id] = account
        return account.account_id

    def get_account_by_id(self, account_id: int) -> Account or None:
        return self.accounts.get(account_id)

    def update_account(self, account: Account) -> None:
        self.accounts[account.account_id] = account

    def get_next_account_id(self) -> int:
        next_id = self.next_account_id
        self.next_account_id += 1
        return next_id
