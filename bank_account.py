from base_bank_account import Account

class BankAccount(Account):
    def __init__(self, account_balance, account_name):
        self._account_balance = account_balance
        self.account_name = account_name

    def get_balance(self):
        print(f"\nAccount '{self.account_name}' balance is P{self._account_balance.2f}")

    