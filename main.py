from bank_account import BankAccount
from interest_account_reward import InterestAccountReward
from savings_account import SavingsAccount

kim = BankAccount(6767, "Kim")
kim.get_balance()

russel = InterestAccountReward(5000, "Russel")
russel.deposit(1000)

shanny = SavingsAccount(10000, "Shanny")
shanny.withdraw(2000)