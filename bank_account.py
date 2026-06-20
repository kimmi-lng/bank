from base_bank_account import Account

class BankAccount(Account):
    def __init__(self, account_balance, account_name):
        self._account_balance = account_balance
        self.account_name = account_name