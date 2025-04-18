from typing import Optional, List, Type
from datetime import datetime
from uuid import uuid4
from domain.entities.account import Account
from domain.entities.checkingAccount import CheckingAccount
from domain.entities.savingsAccount import SavingsAccount
from domain.Exceptions.exception_error import (
    OverdraftExceededError, 
    InsufficientDepositError  # Now this will work
)
from domain.services.business_rules import BusinessRuleService

class AccountCreationService:
    def __init__(self, account_repository, business_rule_service=None):
        self.account_repository = account_repository
        self.business_rules = business_rule_service or BusinessRuleService()

    def create_account(
        self,
        account_class: Type[Account],  # Pass CheckingAccount or SavingsAccount directly
        initial_deposit: float = 0.0,
        owner_name: Optional[str] = None
    ) -> str:
        """Create an account using the class."""
        min_deposit = self.business_rules.get_minimum_initial_deposit(account_class)
        if initial_deposit < min_deposit:
            raise InsufficientDepositError(f"Minimum deposit: {min_deposit}")

        account = account_class(
            account_id=str(uuid4()),
            balance=initial_deposit,
            owner_name=owner_name
        )
        self.account_repository.create_account(account)
        return account.account_id

    
