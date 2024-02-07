'''Create a bank account class that has attributes owner, 
balance and two methods deposit and withdraw. 
Withdrawals may not exceed the available balance.
 Instantiate your class, make several deposits and withdrawals, 
 and test to make sure the account can't be overdrawn.'''

class account :
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,sum):
        if sum>0:
            self.balance+=sum
            print("deposit: ", self.balance)
        else:
            print("error")
    def withdraw(self,sum):
        if sum>0:
            if sum<=self.balance:
                self.balance-=sum
                print("deposit after withdraw: ", self.balance)
            else:
                print("insufficient funds")
        else:
            print("error")
account=account("Aya", 360000)
account.deposit(500)
account.withdraw(500)

