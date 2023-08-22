from functools import *

def Minimum_ (List1) :
    iMin = List1 [0]

    for i in range (len(List1)):
        if (List1[i] < iMin):
            iMin = List1[i]

    return iMin

def main():

    list1 = []

    print("Enter number of elemnts")
    size =  int(input())

    print("Enter elements")
    for i in range(size):
        list1.append(int(input()));

    iMin = Minimum_(list1)

    print("Smallest Number is " ,iMin)





if __name__ == "__main__":
    main()