# account.py

class Account:
    def __init__(self, account_id, account_type, balance=0.0, status='active', creation_date=None):
        self.account_id = account_id
        self.account_type = account_type
        self.balance = balance
        self.status = status
        self.creation_date = creation_date

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_account_info(self):
        return {
            "account_id": self.account_id,
            "account_type": self.account_type,
            "balance": self.balance,
            "status": self.status,
            "creation_date": self.creation_date
        }
