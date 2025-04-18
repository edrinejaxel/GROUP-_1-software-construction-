"""
Transaction Service in the Application Layer.
This orchestrates transaction creation and processing.
"""
from typing import List, Dict, Any, Union
from uuid import uuid4

from domain.entities.account import Account
from domain.entities.transaction import Transaction, TransactionType
from domain.services.business_rules import BusinessRuleService


class TransactionService:
    """
    Service for handling deposits and withdrawals.
    Coordinates between domain entities and repositories.
    """
    
    def __init__(self, account_repository, transaction_repository):
        """
        Initialize the service with required repositories.
        
        Args:
            account_repository: Repository for account persistence
            transaction_repository: Repository for transaction persistence
        """
        self.account_repository = account_repository
        self.transaction_repository = transaction_repository
        self.business_rules = BusinessRuleService()
    
    def deposit(self, account_id: str, amount: Union[str, float], description: str = None) -> Transaction:
        """
        Deposit funds into an account.
        
        Args:
            account_id: ID of the account
            amount: Amount to deposit (string or numeric)
            description: Optional description
            
        Returns:
            Transaction: The created transaction
            
        Raises:
            ValueError: For invalid deposits
        """
        try:
            # Convert amount to float if it's a string
            amount_float = float(amount) if isinstance(amount, str) else float(amount)
            
            # Validate amount
            if amount_float <= 0:
                raise ValueError("Deposit amount must be positive")
            
            # Get account
            account = self.account_repository.get_account_by_id(account_id)
            if not account:
                raise ValueError(f"Account not found: {account_id}")
            
            # Perform deposit (returns new account instance)
            updated_account = account.deposit(amount_float)
            
            # Save updated account
            self.account_repository.update_account(updated_account)
            
            # Create and save transaction
            transaction = Transaction(
                transaction_id=str(uuid4()),
                account_id=account_id,
                transaction_type=TransactionType.DEPOSIT,
                amount=amount_float,  # Use converted float
                description=description
            )
            
            self.transaction_repository.save_transaction(transaction)
            return transaction
            
        except ValueError as e:
            raise ValueError(f"Deposit failed: {str(e)}")
        except TypeError:
            raise ValueError("Amount must be a number")
    
    def withdraw(self, account_id: str, amount: Union[str, float], description: str = None) -> Transaction:
        """
        Withdraw funds from an account.
        
        Args:
            account_id: ID of the account
            amount: Amount to withdraw (string or numeric)
            description: Optional description
            
        Returns:
            Transaction: The created transaction
            
        Raises:
            ValueError: For invalid withdrawals
        """
        try:
            # Convert amount to float if it's a string
            amount_float = float(amount) if isinstance(amount, str) else float(amount)
            
            # Validate amount
            if amount_float <= 0:
                raise ValueError("Withdrawal amount must be positive")
            
            # Get account
            account = self.account_repository.get_account_by_id(account_id)
            if not account:
                raise ValueError(f"Account not found: {account_id}")
            
            # Perform withdrawal (returns new account instance)
            updated_account = account.withdraw(amount_float)
            
            # Save updated account
            self.account_repository.update_account(updated_account)
            
            # Create and save transaction
            transaction = Transaction(
                transaction_id=str(uuid4()),
                account_id=account_id,
                transaction_type=TransactionType.WITHDRAW,
                amount=amount_float,  # Use converted float
                description=description
            )
            
            self.transaction_repository.save_transaction(transaction)
            return transaction
            
        except ValueError as e:
            raise ValueError(f"Withdrawal failed: {str(e)}")
        except TypeError:
            raise ValueError("Amount must be a number")
        
    def get_transaction_history(self, account_id):
        """
        Get the transaction history for an account.
        
        Args:
            account_id: ID of the account
            
        Returns:
            List[Transaction]: List of transactions for the account
            
        Raises:
            ValueError: If the account doesn't exist
        """
        # Verify account exists
        account = self.account_repository.get_account_by_id(account_id)
        if not account:
            raise ValueError(f"Account not found: {account_id}")
        
        # Get transactions
        return self.transaction_repository.get_transactions_for_account(account_id)
    
    def get_transaction_by_id(self, transaction_id):
        """
        Get a specific transaction by ID.
        
        Args:
            transaction_id: ID of the transaction
            
        Returns:
            Transaction: The transaction if found
            
        Raises:
            ValueError: If the transaction doesn't exist
        """
        transaction = self.transaction_repository.get_transaction_by_id(transaction_id)
        if not transaction:
            raise ValueError(f"Transaction not found: {transaction_id}")
        
        return transaction
    
    def get_account_summary(self, account_id):
        """
        Get a summary of account activity.
        
        Args:
            account_id: ID of the account
            
        Returns:
            Dict: Summary of account activity
            
        Raises:
            ValueError: If the account doesn't exist
        """
        # Verify account exists
        account = self.account_repository.get_account_by_id(account_id)
        if not account:
            raise ValueError(f"Account not found: {account_id}")
        
        # Get transactions
        transactions = self.transaction_repository.get_transactions_for_account(account_id)
        
        # Calculate metrics
        total_deposits = sum(t.amount for t in transactions if t.transaction_type == TransactionType.DEPOSIT)
        total_withdrawals = sum(t.amount for t in transactions if t.transaction_type == TransactionType.WITHDRAW)
        transaction_count = len(transactions)
        
        return {
            "account_id": account_id,
            "current_balance": account.balance,
            "total_deposits": total_deposits,
            "total_withdrawals": total_withdrawals,
            "transaction_count": transaction_count
        }