"""
Main application file for the Banking Application.
This serves as the entry point to run the API.
"""
import uvicorn
import random
from typing import List, Dict, Any
from datetime import datetime

import config as config
from domain.entities.checkingAccount import CheckingAccount
from domain.entities.savingsAccount import SavingsAccount
from api.api import app, account_service, transaction_service

def create_demo_data():
    """Create some demo accounts and transactions for testing."""
    # Create a checking account
    checking_id = account_service.create_account(
        CheckingAccount, 1000.0, "John Doe"
    )
    
    # Create a savings account
    savings_id = account_service.create_account(
        SavingsAccount, 5000.0, "Jane Smith"
    )
    
    # Add some transactions to the checking account
    transaction_service.deposit(
        checking_id, 500.0, "Initial salary deposit"
    )
    transaction_service.withdraw(
        checking_id, 200.0, "ATM withdrawal"
    )
    transaction_service.deposit(
        checking_id, 300.0, "Refund from online store"
    )
    transaction_service.withdraw(
        checking_id, 150.0, "Grocery shopping"
    )
    
    # Add some transactions to the savings account
    transaction_service.deposit(
        savings_id, 1000.0, "Bonus payment"
    )
    transaction_service.deposit(
        savings_id, 250.0, "Interest payment"
    )
    
    print(f"Created demo checking account: {checking_id}")
    print(f"Created demo savings account: {savings_id}")
    
    return {
        "checking_id": checking_id,
        "savings_id": savings_id
    }

def print_welcome_banner():
    """Print a welcome banner to the console."""
    banner = """
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   BANKING APPLICATION API                                 ║
    ║                                                           ║
    ║   Version: {0}                                            ║
    ║   Server: http://{1}:{2}                                  ║
    ║   Documentation: http://{1}:{2}/docs                      ║
    ║                                                           ║
    ║   {3}                                                     ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """.format(
        config.APP_VERSION,
        config.API_HOST if config.API_HOST != "0.0.0.0" else "localhost",
        config.API_PORT,
        random.choice(config.WELCOME_MESSAGES)
    )
    
    print(banner)

if __name__ == "__main__":
    print_welcome_banner()
    
    # Create demo data if running in debug mode
    if config.DEBUG:
        demo_accounts = create_demo_data()
        
        # Print demo account IDs for easy testing
        print("\nDemo Accounts:")
        for name, account_id in demo_accounts.items():
            print(f"  - {name}: {account_id}")
        print("\nAPI is running. Press Ctrl+C to stop.")
    
    # Run the FastAPI application using uvicorn
    uvicorn.run(
        "api.api:app", 
        host=config.API_HOST, 
        port=config.API_PORT,
        reload=config.DEBUG
    )