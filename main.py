from BankAccount import BankAccount
if __name__ == "__main__":
    #creates hardcoded bank account name and balance
    account=BankAccount("Tyler", 10000)

    #calls deposit 
    account.deposit(3000)

    #calls withdrawl
    account.withdraw(7000)

    #calls getbalance
    print(account.get_balance())