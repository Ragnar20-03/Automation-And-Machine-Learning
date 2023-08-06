import sys


def main():
    print("Demonstartion of Command Line Arguments ");
    print("Number of Command Line Arguments are : " , len(sys.argv))

    print(sys.argv[0])
    print(sys.argv[1])
    print(sys.argv[2])

if (__name__ == "__main__"):
    main()