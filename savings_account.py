from interest_account_reward import InterestAccountReward

class SavingsAccount(InterestAccountReward):
    def __init__(self, account_balance, account_name):
        super().__init__(account_balance, account_name)
        self.fee = 5