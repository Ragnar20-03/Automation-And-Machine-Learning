from functools import *


def ChkPrime (No) : 
    bflag = True
    for i in range( 2  ,int (  (No / 2 ) )):
        if ( No % i == 0 ):
            bflag = True
    return bflag


def Mult_2 (No) : 
    return No * 2

def Max_  ( No , No2):
    if (No2 > No):
        return No2
    

def main():

    list1 = []

    print("Enter number of   Elements")
    Size = int (input("\n"))

    print("Enter number of elements")
    for i in range(Size):
        list1.append(int(input()))

    foutput = list(filter (ChkPrime , list1))
    print("Filter Output  :  " , foutput)
    
    moutput = list(map(Mult_2 , foutput))
    print("Map Output  :  " , moutput)

    total = reduce(Max_  , moutput)
    print("Max_  is : " , total)

if __name__ == "__main__":
    main()