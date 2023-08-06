import sys


def main():
    print("Demonstartion of Command Line Arguments ");

    Value1 = int(sys.argv[1])
    Value2 = int(sys.argv[2])

    print("addition is : " , Value1 + Value2)

if (__name__ == "__main__"):
    main()