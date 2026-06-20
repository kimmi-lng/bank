from bank_account import BankAccount

class InterestAccountReward(BankAccount):
    def deposit(self, amount):
        self._account_balance = self._account_balance + (amount*1.05)
        print(f"\nDeposit of P{amount:.2f} successful with 5% interest reward.")
        self.get_balance()