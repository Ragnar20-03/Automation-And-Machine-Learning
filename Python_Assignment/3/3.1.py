from functools import *

Add = lambda No1 , No2 : (No1 + No2)

def main():

    list1 = []

    print("Enter number of elemnts")
    size =  int(input())

    print("Enter elements")
    for i in range(size):
        list1.append(int(input()));

    iSum = reduce(Add , list1)

    print(iSum)





if __name__ == "__main__":
    main()