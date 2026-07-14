class BankAccount:
    ROI=10.5

    def __init__(self,Name,Amount):
        self.Name=Name
        self.Amount=Amount
        

    def Display(self):
        print("Account holder name is",self.Name)
        print("Current balance in account is",self.Amount)

    def Deposit(self):
        print("Enter amount to add")
        self.addamount=int(input())
        self.addamount=self.Amount+self.addamount
        print("Now total alance is",self.addamount)

    def withdraw(self):
        print("Enter amount to withdraw")
        self.subbamount=int(input())
        if self.Amount>self.subbamount:
            self.subbamount=self.Amount-self.subbamount
        print("Now total balance is",self.subbamount)
        
    def CalculateInterest(self):

        self.interest=((self.Amount)*(BankAccount.ROI)/100)
        print("Interest is",self.interest)
obj1=BankAccount("sakshi",12000)

obj1.Display()
obj1.Deposit()
obj1.withdraw()
obj1.CalculateInterest()

        


