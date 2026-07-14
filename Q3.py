class Numbers:
    def __init__(self):

        print("Enter number")
        self.no=int(input())
        

        
    def Chkprime(self):
        self.count=0
        for i in range(1,self.no+1):
            if self.no%i==0:

                self.count=self.count+1
        if self.count==2:
            print(True,"number is prime")
        else:
            print(False,"Numer is not prime")
    

        
        

    def Chkprefect(self):
        self.sum=0

        for i in range(1,self.no):
            if self.no%i==0:
                self.sum=self.sum+i

        if self.sum==self.no:
            print("Number is perfect")
        else:
            print("Number is not perfect")
    


        
    
    def Factors(self):
        print("Factors are")
        for i in range(1,self.no+1):
            if self.no % i==0:
                print(i,end=" ")
        print()

        
    
    def Sumfactors(self):
        self.sum=0
        for i in range(1,self.no):
             if(self.no%i==0):
                self.sum=self.sum+i
        print("Sum of factors are",self.sum)
        

    



Aobj=Numbers()

Aobj.Chkprime()           
Aobj.Chkprefect()           
Aobj.Factors()          
Aobj.Sumfactors()



