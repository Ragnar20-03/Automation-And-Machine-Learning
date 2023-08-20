
from functools import reduce

def CheckEven(No):
    if(No % 2 == 0):
        return No
    else:
        return False

def Increase(No):
    return No+2

def Add(A,B):
    return A+B

def main():


    Data = []
    Size = int (input("Enter number of elements"))

    for i in range(Size):
        Data.append(int(input()))

    output = list(filter(CheckEven,Data))
    print(output)

    moutput = list(map(Increase,output))
    print(moutput)

    result = reduce(Add,moutput)
    print(result)

if __name__ == "__main__":
    main()