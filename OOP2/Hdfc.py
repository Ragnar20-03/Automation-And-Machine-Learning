

class HDFC :
    ROI = 9.5   #Class Variable

    def __init__(self ,Name  , Amount):  #Constructor
        self.Balence = Amount     #Instance Variable
        self.AccountHolder = Name     #Instance Variable
        print("Welcome " , self.AccountHolder)
        print("Account gets succesfully created with initial Balence : " , self.Balence)

    def DisplayBalence(self):  #Instance Methods
        print("Hello " , self.AccountHolder)
        print()
        print("Your account balence for ", self.AccountHolder ,"  is : " , self.Balence)

    @classmethod
    def DisplayBankInfo(cls):   #Class Method
        print("Welcome to HDFC bank portal : ")
        print("Our bank is private limited Bank : ")
        


    def Withdraw (self , Amount):   
        print("Hello " , self.AccountHolder)
        print()
        if (self.Balence < Amount):
            print("There is No Insuffecient Balence ")

        else :
            self.Balence = self.Balence - Amount
            print("Your Current Balence is : " , self.Balence)
            print("Amount withdrwal successfully ...")

    def Deposit(self , Amount):   #Instance Method
        self.Balence = self.Balence + Amount
        print("Your Current Balence is : " , self.Balence)
        print("Amount Deposit successfully ...")




def main():
    print()
    print("Rate of interest is : " , HDFC.ROI)
    print()

    HDFC.DisplayBankInfo()
    print()

    print("Creating new Account : ")
    obj1 = HDFC ("Amit" , 5000)   # __init__(100 , "Amit" ,5000)

    print()

    print("Creating new Account : ")
    obj2 = HDFC ("Sagar" , 3000)   # __init__(200 , "Sagar " , 3000)
    
    print()

    print("Performing operation on obj1")
    obj1.Deposit(10)
    print()

    obj1.Withdraw(1000)

if __name__ == "__main__":
    main()