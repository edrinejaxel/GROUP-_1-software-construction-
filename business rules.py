# services.py

class BankingService:
    @staticmethod
    def check_negative_balance(account):
        if account.get_balance() < 0:
            raise ValueError("Account balance cannot be negative.")

    @staticmethod
    def validate_deposit_amount(amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
