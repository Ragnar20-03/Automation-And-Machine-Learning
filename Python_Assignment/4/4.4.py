from functools import *


def CheckEven (No) : 
    return (No % 2 == 0)

def Square_ (No) : 
    return No * No

def Add_ ( No , No2):

    return No + No2

def main():

    list1 = []

    print("Enter number of   Elements")
    Size = int (input("\n"))

    print("Enter number of elements")
    for i in range(Size):
        list1.append(int(input()))

    foutput = list(filter (CheckEven , list1))
    print("Filter Output  :  " , foutput)
    
    moutput = list(map(Square_ , foutput))
    print("Map Output  :  " , moutput)

    total = reduce(Add_ , moutput)
    print("Add_ is : " , total)

if __name__ == "__main__":
    main()