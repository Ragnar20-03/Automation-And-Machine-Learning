
def Addition ( No1 , No2 ):
    Ans = 0  
    Ans = No1 + No2
    return Ans

def Subtraction (No1 , No2):
    Ans = 0  
    Ans = No1 - No2 
    return Ans

def main():
    Value1 = int(input("Enter First Number \n"))
    Value2 = int (input("Enter Second Number \n"))

    Ret  = Addition(Value1 , Value2)
    print("Addition is : " , Ret)

    Ret = Subtraction ( Value1 , Value2)
    print("Subtraction is : " , Ret)



if __name__== "__main__" : 
    main()