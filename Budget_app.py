class Budget:

    def __init__(self, **categories):
        self.categories = categories
        print(self.categories)

    def deposit_fund(self, amount, category):
        self.categories[category] = self.categories[category] + amount
        print (f'Deposit successful! \nYour balance is now {self.categories[category]}')
    
    def withdraw_fund(self, amount, category):
        
        if amount > self.categories[category]:
            print(f'Insufficient funds, your balance is {self.categories[category]}')

        else:
            self.categories[category] = self.categories[category] - amount
            print (f'Withdrawal successful! \nYour balance is now {self.categories[category]}')
            
    def transfer_fund(self, amount, debit_category, credit_category):

        if amount > self.categories[debit_category]:
            print(f'Insufficient funds, your balance is {self.categories[debit_category]}')
            
        else:
            self.categories[debit_category] = self.categories[debit_category] - amount
            self.categories[credit_category] =  self.categories[credit_category] + amount
            print('Transfer successful! \nYou transfered '+ str(amount) + ' ' + 'from ' + debit_category + ' to '+ credit_category )
    
    def display_balance(self,category):
        print('Your '+ category + ' budget balance is ' + str(self.categories[category]))