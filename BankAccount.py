#BankAccount class
class BankAccount:
    #Contructor that creates account
    def __init__(self,account_name, starting_balance) :
        self.account_name=account_name
        self.balance=starting_balance

    #method to deposit
    def deposit(self,amount):
        self.balance=self.balance+amount

    #method to withdraw
    def withdraw(self, amount):

        if self.balance >= amount : 
            self.balance=self.balance-amount
        else:
            print("You do not have enough available funds to make this withdrawl")

    #methods that return balance
    def get_balance(self):
        return str(self.account_name)+" has a balance of $"+str(self.balance)