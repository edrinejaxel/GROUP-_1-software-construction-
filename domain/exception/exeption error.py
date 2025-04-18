

class BankingError(Exception):
    """Base class for other exceptions in the banking system."""
    pass

class InsufficientBalanceError(BankingError):
    """Raised when a withdrawal is attempted with insufficient balance."""
    def __init__(self, message="Insufficient balance for this operation."):
        self.message = message
        super().__init__(self.message)

class InvalidAmountError(BankingError):
    """Raised when an invalid amount is provided for deposit or withdrawal."""
    def __init__(self, message="Amount must be positive."):
        self.message = message
        super().__init__(self.message)

class AccountClosedError(BankingError):
    """Raised when an operation is attempted on a closed account."""
    def __init__(self, message="This account is closed."):
        self.message = message
        super().__init__(self.message)
