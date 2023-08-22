from functools import *


Mult = lambda  No  , No2 : (No * No2)


def main():

    list1 = []

    print("Enter  Element")
    No = int(input("\n"))
    print("Enter Another element  Element")
    No2 = int(input("\n"))

    print("Multiplication is  : " , Mult(No , No2))


if __name__ == "__main__":
    main()