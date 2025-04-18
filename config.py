"""
Configuration settings for the Banking Application.
"""
import os
from typing import Dict, Any

# Application settings
APP_NAME = "Banking API"
APP_VERSION = "1.0.0"
DEBUG = True

# API settings
API_PREFIX = "/api"
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))

# Account class configuration (updated to use class references)
ACCOUNT_CLASSES = {
    "checking": {
        "class": "CheckingAccount",
        "config": {
            "free_transfers": True,
            "debit_card": True,
            "monthly_fee": 0.0,
            "interest_rate": 0.01,  # 1% annual interest
            "min_balance_fee": 0.0
        }
    },
    "savings": {
        "class": "SavingsAccount",
        "config": {
            "free_transfers": False,
            "debit_card": False,
            "monthly_fee": 0.0,
            "interest_rate": 0.025,  # 2.5% annual interest
            "min_balance_fee": 5.0,  # Fee if balance drops below minimum
            "minimum_initial_deposit": 100.0
        }
    }
}

# Sample welcome messages
WELCOME_MESSAGES = [
    "Welcome to our Banking API! We're here to help you manage your finances.",
    "Thanks for choosing our Banking API. Your financial future starts here!",
    "Banking made simple. Explore our API to manage your accounts and transactions.",
    "Your money, your way. Our Banking API gives you complete control of your finances."
]

# Sample transaction descriptions (for demo purposes)
SAMPLE_DEPOSIT_DESCRIPTIONS = [
    "Salary deposit", 
    "Refund", 
    "Gift", 
    "Interest payment", 
    "Transfer in"
]

SAMPLE_WITHDRAWAL_DESCRIPTIONS = [
    "ATM withdrawal", 
    "Bill payment", 
    "Grocery shopping", 
    "Online purchase", 
    "Transfer out"
]