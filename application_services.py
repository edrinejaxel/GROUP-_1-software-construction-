# application/application_services.py

from domain.checking import CheckingAccount
from domain.entities.import SavingsAccount
from domain.exeptions. import InvalidAmountError, InsufficientBalanceError
from domain.entities.transactions  import Transaction

class AccountCreationService:
    def __init__(self, account_repo):
        self.account_repo = account_repo

    def create_account(self, account_type: str, initial_deposit: float) -> int:
        if account_type == 'SAVINGS':
            if initial_deposit < 100.0:  # Assuming minimum deposit for savings
                raise InvalidAmountError("Minimum deposit for Savings account is $100.")
            account = SavingsAccount(account_id=self.account_repo.get_next_account_id(), balance=initial_deposit)
        elif account_type == 'CHECKING':
            account = CheckingAccount(account_id=self.account_repo.get_next_account_id(), balance=initial_deposit)
        else:
            raise ValueError("Invalid account type specified.")

        account_id = self.account_repo.create_account(account)
        return account_id


class TransactionService:
    def __init__(self, account_repo, transaction_repo):
        self.account_repo = account_repo
        self.transaction_repo = transaction_repo

    def deposit(self, account_id: int, amount: float):
        account = self.account_repo.get_account_by_id(account_id)
        if account is None:
            raise ValueError("Account not found.")

        account.deposit(amount)
        self.account_repo.update_account(account)
        transaction = Transaction(transaction_id=self.transaction_repo.get_next_transaction_id(),
                                   transaction_type=Transaction.DEPOSIT,
                                   amount=amount,
                                   account_id=account_id)
        self.transaction_repo.save_transaction(transaction)
        return transaction

    def withdraw(self, account_id: int, amount: float):
        account = self.account_repo.get_account_by_id(account_id)
        if account is None:
            raise ValueError("Account not found.")

        account.withdraw(amount)
        self.account_repo.update_account(account)
        transaction = Transaction(transaction_id=self.transaction_repo.get_next_transaction_id(),
                                   transaction_type=Transaction.WITHDRAW,
                                   amount=amount,
                                   account_id=account_id)
        self.transaction_repo.save_transaction(transaction)
        return transaction
