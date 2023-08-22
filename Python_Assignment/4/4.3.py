from functools import *


def ChkRange (No) : 
    if (No >= 70 and No <= 90):
        return No
    
def Add_10 (No) : 
    return No + 10

def product ( No , No2):

    return No * No2

def main():

    list1 = []

    print("Enter number of   Elements")
    Size = int (input("\n"))

    print("Enter number of elements")
    for i in range(Size):
        list1.append(int(input()))

    foutput = list(filter (ChkRange , list1))
    print("Filter Output  :  " , foutput)

    moutput = list(map(Add_10 , foutput))
    print("Map Output  :  " , moutput)

    total = reduce(product , moutput)
    print("Product is : " , total)



if __name__ == "__main__":
    main()