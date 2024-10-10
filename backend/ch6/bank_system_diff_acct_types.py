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
  
class SavingsAccount(BankAccount):
  def __init__(self, owner, balance=0):
    super().__init__(owner, balance)
    self.minimum_balance = 500


  def withdraw(self, amount):
    if self.balance - amount < self.minimum_balance:
      print("Withdrawal would bring account below minimum balance. Transaction cancelled.")
    else:
      super().withdraw(amount)


  def add_interest(self):
    # assuming monthly interest calc for simplicity
    interest_earned = self.balance * self.interest_rate / 12
    self.deposit(interest_earned)
    print(f"Interest added: {interest_earned}. New balance: {self.balance}.")


class CheckingAccount(BankAccount):
  transaction_fee = 1.00 # fix fee per transaction in checking account but no interest earned and no min balance

  def __init__(self, owner, balance=0):
    super().__init__(owner, balance)


  def withdraw(self, amount):
    if self.balance - amount - self.transaction_fee < 0:
      print("Withdrawal and transaction fee would overdraw the account. Transaction cancelled.")
    else:
      super().withdraw(amount)
      self.balance -= self.transaction_fee
      print(f"Transaction fee of {self.transaction_fee} applied. New balance: {self.balance}.")


class BusinessAccount(BankAccount):
  transaction_fee_percentage = 0.01

  def __init__(self, owner, balance=0):
    super().__init__(owner, balance)
    self.interest_rate = 0.1  # higher interest rate for business accounts

  
  def withdraw(self, amount):
    fee = amount * self.transaction_fee_percentage
    if self.balance - amount - fee < 0:
      print(f"Withdrawal and transaction fee would overdraw the account. Transaction cancelled.")
    else:
      super().withdraw(amount)
      self.balance -= fee  # apply percentage based transaction fee
      print(f"Transaction fee of {fee} applied. New balance: {self.balance}.")


#
## Interacting with banking system
#
def main():

  # Creating an account
  account = BankAccount("John Doe", 1000)
  savings = SavingsAccount("Alice", 1000)
  checking = CheckingAccount("Bob", 500)
  business = BusinessAccount("Charlie", 2000)

  savings.add_interest()
  checking.withdraw(100)
  business.withdraw(200)

  # Demonstrating polymorphism
  accounts = [savings, checking, business]
  for account in accounts:
    print(f"Processing monthly maintenance for {account.owner}'s account.")
    account.withdraw(50)


  """   # Depositing money
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
    print("Invalid withdrawal amount.") """


  # Update interest rate for all accounts
  BankAccount.update_interest_rate(0.03)


if __name__ == "__main__":
    main()
