

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from application.application_services import AccountCreationService, TransactionService
from infrastructure.repository.account repository import AccountRepository
from infrastructure.transaction_repository import TransactionRepository
from domain.exeptions.exeption error import InvalidAmountError

app = APIRouter()

# Initialize repositories and services
account_repo = AccountRepository()
transaction_repo = TransactionRepository()
account_creation_service = AccountCreationService(account_repo)
transaction_service = TransactionService(account_repo, transaction_repo)

# Models for request bodies
class CreateAccountRequest(BaseModel):
    accountType: str
    initialDeposit: float

class DepositRequest(BaseModel):
    amount: float

# Endpoint to create an account
@app.post("/accounts", status_code=201)
def create_account(request: CreateAccountRequest):
    try:
        account_id = account_creation_service.create_account(request.accountType.upper(), request.initialDeposit)
        account = account_repo.get_account_by_id(account_id)
        return {
            "accountId": account.account_id,
            "accountType": account.account_type,
            "balance": account.balance
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to deposit money
@app.post("/accounts/{account_id}/deposit")
def deposit(account_id: int, request: DepositRequest):
    try:
        transaction = transaction_service.deposit(account_id, request.amount)
        return {
            "transactionId": transaction.transaction_id,
            "amount": transaction.amount,
            "accountId": account_id
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except InvalidAmountError as e:
        raise HTTPException(status_code=400, detail=str(e))
