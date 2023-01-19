class Category:

  budgets = {}

  def __init__(self, category):

    self.category = category
    self.ledger = []
    self.description = []

    Category.budgets[self.category] = self.ledger

  def deposit(self, deposit_amount, deposit_description=""):

    self.ledger.append(deposit_amount)
    self.description.append(deposit_description)

    Category.budgets[self.category] = self.ledger

    return dict(amount=self.ledger[-1], description=self.description[-1])

  def withdraw(self, withdraw_amount, withdraw_description=''):
    if withdraw_amount > sum(self.ledger):
      return False
    else:
      self.ledger.append(-1 * withdraw_amount)
      self.description.append(withdraw_description)

    Category.budgets[self.category] = self.ledger

    return True
    
  def get_balance(self):
    return sum(self.ledger)
    
  def transfer(self, amount, budget_category):

    self.budget_category = budget_category

    if amount <= sum(self.ledger):
      self.withdraw(amount, 'Transfer to {}'.format(budget_category.category))
      budget_category.deposit(amount, 'Transfer from {}'.format(self.category))
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount > sum(self.ledger):
      return False
    else:
      return True


def create_spend_chart(categories):
  pass
