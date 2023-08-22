from functools import *

def Maximum_ (List1) :
    iMax = List1 [0]

    for i in range (len(List1)):
        if (List1[i] > iMax):
            iMax = List1[i]

    return iMax

def main():

    list1 = []

    print("Enter number of elemnts")
    size =  int(input())

    print("Enter elements")
    for i in range(size):
        list1.append(int(input()));

    iMax = Maximum_(list1)

    print(iMax)





if __name__ == "__main__":
    main()