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






def create_spend_chart(categories):

  Total_bugdet = []
  Name_budget = []
  for category in categories:
    Total_bugdet.append( category.get_balance()  )
    Name_budget.append( str(category.category) )
  
  Total = sum(Total_bugdet)
  Porcentage = []

  for suma in Total_bugdet:
    if  divmod(suma/Total*100 , 10 )[1]>5:
      Porcentage.append(   int(  divmod(suma/Total*100 , 10 )[0]+1)  )
    else:
       Porcentage.append(  int( divmod(suma/Total*100 , 10 )[0] ) )
  
  Chart = ""

  Barra_vertical = [ '100|', ' 90|',' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|',' 20|', ' 10|', '  0|', ]

  longitudes_de_nombres = [ len(x.category) for x in categories ]
  longitud_vertical = max(longitudes_de_nombres )  + 11
  
  longitud_horizontal = 3 * len(categories) 

  chart= "Percentage spent by category " + '\n'

  for i in range (longitud_vertical+1):

    if i<11:
      chart += Barra_vertical[i]
      for porcen in Porcentage:
        if porcen>= 10-i:
           chart += " o "
        else:
            chart += "   "
      chart += ' \n'
    elif i==11:
      chart += "    " + (len(categories))*"---" + "-" "\n"
    else:
      chart += "    " 
      for j in range(len(categories)):
        if longitudes_de_nombres[j]>i-12:
          if i == 12:
            chart += " " + str.upper(categories[j].category[i-12]) + " "
          else:
            chart += " " + categories[j].category[i-12] + " "
        else:
          chart += "   "
      if i<longitud_vertical:
        chart += "\n"


  return chart


    
food = Category('food')
business = Category('business')
entertainment = Category('entertainment')

food.deposit(900, "deposit")
entertainment.deposit(300, "deposit")
business.deposit(50, "deposit")
food.withdraw(15.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)



solution = (create_spend_chart([business, food ,entertainment]))

expected =("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
)

sol_cd = str.split( expected )
sol_rpblem = str.split(   solution     )





print(  sol_cd)
print('\n \n \n \n')
print(  sol_rpblem )

print( sol_cd == sol_rpblem )

print( solution == expected  )
