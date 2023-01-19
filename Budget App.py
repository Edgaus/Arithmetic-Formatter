class Category:


    def __init__(self):
        self.ledger = []
        self.description = []
    
    def deposit(self, deposit_amount, deposit_description = "" ):

        self.ledger.append(deposit_amount)
        self.description.append(deposit_description)

        self.budget = dict( amount = self.ledger[-1], description = self.description[-1]  )
        return self.budget
    
    def withdraw(self, withdraw_amount, withdraw_description = ''):
        if withdraw_amount > sum(self.ledger):
            return False
        else:
            self.ledger.append(-1*withdraw_amount)
            self.description.append(withdraw_description)

            self.budget = dict( amount = self.ledger[-1], description = self.description[-1]  )


            return True, self.budget
    def get_balance(self):
        return sum(self.ledger)


food = Category()
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")

print(food.get_balance())





