class BankAccount:
  interest_rate = 0.05

  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance


  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"{amount} deposited. New balance is {self.balance}.")
    else:
      print("Deposit amount must be positive.")


  def withdraw(self, amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      print(f"{amount} withdrawn. New balance is {self.balance}.")
    else:
      print("Invalid withdrawal amount.")


  def check_balance(self):
    print(f"Current balance: {self.balance}.")


  @classmethod
  def update_interest_rate(cls, new_rate):
    cls.interest_rate = new_rate
    print(f"New interest rate across all accounts is {cls.interest_rate}.")


  @staticmethod
  def validate_transaction(transaction_amount):
    return transaction_amount > 0
  


## Interacting with banking system
def main():

  # Creating an account
  account = BankAccount("John Doe", 1000)


  # Depositing money
  deposit_amount = 500
  if BankAccount.validate_transaction(deposit_amount):
    account.deposit(deposit_amount)
  else:
    print("Invalid deposit amount.")


  # Withdraw money
  withdrawal_amount = 200
  if BankAccount.validate_transaction(withdrawal_amount):
    account.withdraw(withdrawal_amount)
  else:
    print("Invalid withdrawal amount.")


  # Update interest rate for all accounts
  BankAccount.update_interest_rate(0.03)


if __name__ == "__main__":
    main()

