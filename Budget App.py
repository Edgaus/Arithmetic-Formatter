import re
class Category:

  def __init__(self, category):

    self.category = category
    self.ledger = []

  def deposit(self, deposit_amount, deposit_description=""):

    dict_movements = {
      'amount': deposit_amount,
      'description': deposit_description
    }
    self.ledger.append(dict_movements)

    return self.ledger[-1]

  def withdraw(self, withdraw_amount, withdraw_description=''):
    self.suma = 0
    for movement in self.ledger:
      self.suma = movement['amount'] + self.suma

    if withdraw_amount > self.suma:
      return False
    else:
      deposit_amount = -1 * withdraw_amount
      dict_movements = {
        'amount': deposit_amount,
        'description': withdraw_description
      }
      self.ledger.append(dict_movements)
      return True

  def get_balance(self):
    self.suma = 0
    for movement in self.ledger:
      self.suma = movement['amount'] + self.suma
    return self.suma

  def transfer(self, amount, budget_category):

    self.budget_category = budget_category

    if amount <= (self.get_balance()):
      name = str(budget_category.category)
      self.withdraw(amount, 'Transfer to '+str.upper(name[0])+name[1:])
      budget_category.deposit(amount, 'Transfer from {}'.format(self.category))
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  def __str__(self):
    espacio = int((30-len(self.category))/2)
    lineas = espacio*"*" + self.category + espacio*"*"
    for movement in self.ledger:
        lineas += '\n'+ movement['description'][:23] + (23-len(movement['description'][:23]))*" "
        
        number_str = str(movement['amount'])
        len_number = len(number_str)
        if len_number > 7:
            lineas += number_str[:7]
        else:
            decimal_number = re.findall('[0-9]+', number_str)
            try:
                if len(decimal_number[1])<3:
                    lineas += (7-len(number_str))*" "+number_str
                else:
                    lineas += (3-len(decimal_number[0]))*" " + decimal_number[0] + "." + decimal_number[1]

            except:
                number_str = number_str + ".00"
                if len_number > 4:  
                    number_str = number_str[:7]

                lineas += (7-len(number_str))*" "+number_str

    lineas += '\n' 'Total: {}'.format(self.get_balance())

    return lineas
