class Account:
  def __init__(self, owner, balance = 0):
    self.owner = owner
    self.__balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.__balance += amount
      return f"Added {amount} to the balance"
    else:
      return 'Deposit amount must be greater than 0'
    

  def withdraw(self, amount):
    if 0 < amount <= self.__balance:
      self.__balance -= amount
      return f"Withdrew {amount} from the balance"
    else:
      return 'Insufficient balance or invalid amount'
    

  def get_balance(self):
    return self.__balance
  

# using the Account class
account = Account('John Doe', 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance()) # 1300

# print(account.__balance) # AttributeError: 'Account' object has no attribute '__balance'