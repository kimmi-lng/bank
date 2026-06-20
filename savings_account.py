from interest_account_reward import InterestAccountReward

class SavingsAccount(InterestAccountReward):
    def __init__(self, account_balance, account_name):
        super().__init__(account_balance, account_name)
        self.fee = 5

    def withdraw(self, amount):
        deduction = amount + self.fee
        if self._account_balance >= deduction:
            self._account_balance = self._account_balance - deduction
            print(f"\nWithdrawal of P{amount:.2f} successful with P{self.fee:.2f} fee.")
            self.get_balance()
        else:
            print(f"\nInsufficient funds for withdrawal of P{amount:.2f} with P{self.fee:.2f} fee.")