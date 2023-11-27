from bank_account import BankAccount

account=BankAccount("102030", 1000)
print(account)
account.deposit(100)
account.withdraw(50)
account.get_balance()
print(account)