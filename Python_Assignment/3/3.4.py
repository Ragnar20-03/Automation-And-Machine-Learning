from functools import *

def Freq (List1 , No) :
    iFreq = 0

    for i in List1 :
        if (i == No):
            iFreq = iFreq + 1

    return iFreq

def main():

    list1 = []

    print("Enter number of elemnts")
    size =  int(input())

    print("Enter elements")
    for i in range(size):
        list1.append(int(input()));

    No = int(input("ENter the element to count frequency"))

    iFreq = Freq(list1 , No)

    print("Frequency of a Number is " ,iFreq)





if __name__ == "__main__":
    main()