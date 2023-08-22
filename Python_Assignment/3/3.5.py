from functools import *
import MarvellousNum

Add = lambda No1 , No2 : (No1 + No2)


def main():

    list1 = []

    print("Enter number of elemnts")
    size =  int(input())

    print("Enter elements")
    for i in range(size):
        list1.append(int(input()));


    list2 = list (filter (MarvellousNum.CheckPrime , list1 ))
    print("Prime number are " , list2)

    SumPrime = reduce(Add , list2)
    
    print( "Sum of Prime number are " , SumPrime)



if __name__ == "__main__":
    main()