class Arithmatic:
    def __init__(self ):
        self.value1 = 0 
        self.value2 = 0 ; 

    def Accept(self , value1 , value2):
        self.value1 = value1 
        self.value2 = value2
    
    def Addition (self):
        return self.value1 + self.value2

    def Subtraction (self ):
        return self.value1 - self.value2

    def Multiplication (self ):
        return self.value1 * self.value2

    def Division (self ):
        return self.value1 / self.value2


def main():
    obj = Arithmatic()
    No1 = int(input("Enter First Number \n"))
    No2 = int(input("Enter Second Number \n"))

    obj.Accept(No1 , No2)

    print("Addition is "  , obj.Addition())
    print("Subtraction is "  , obj.Subtraction())
    print("Multiplication is "  , obj.Multiplication())
    print("Division is "  , obj.Division())

if __name__ == "__main__":
    main()