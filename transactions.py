# transaction.py

from datetime import datetime

class Transaction:
    DEPOSIT = 'DEPOSIT'
    WITHDRAW = 'WITHDRAW'

    def __init__(self, transaction_id, transaction_type, amount, account_id):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()
        self.account_id = account_id

    def get_transaction_info(self):
        return {
            "transaction_id": self.transaction_id,
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "account_id": self.account_id
        }
