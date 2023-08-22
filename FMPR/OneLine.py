from functools import reduce 

def main ():
    
    Data = []
    Size = int (input("Enter number of elements"))

    for i in range(Size):
        Data.append(int(input()))

    print( reduce (lambda  No1 , No2    : ( No1 + No2),list(map(lambda No : (No + 2),list(filter(lambda No  : (No % 2 == 0),Data))))))



if __name__ == "__main__":
    main()