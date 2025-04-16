# transaction_repository.py

from collections import defaultdict
from domain.entities.transactions  import Transaction

class TransactionRepository:
    def __init__(self):
        self.transactions = defaultdict(list)
        self.next_transaction_id = 1

    def save_transaction(self, transaction: Transaction) -> int:
        transaction.transaction_id = self.next_transaction_id
        self.transactions[transaction.account_id].append(transaction)
        self.next_transaction_id += 1
        return transaction.transaction_id

    def get_transactions_for_account(self, account_id: int) -> list:
        return self.transactions.get(account_id, [])

    def get_next_transaction_id(self) -> int:
        return self.next_transaction_id
