from functools import reduce

# Add =  lambda  No1 , No2    : ( No1 + No2)


# CheckEven = lambda No  : (No % 2 == 0)


# Increase = lambda No : (No + 2)


def main ():
    
    Data = []
    Size = int (input("Enter number of elements"))

    for i in range(Size):
        Data.append(int(input()))

    output = list(filter(lambda No  : (No % 2 == 0),Data))
    print(output)

    moutput = list(map(lambda No : (No + 2),output))
    print(moutput)

    result = reduce(lambda  No1 , No2    : ( No1 + No2),moutput)
    print(result)



if __name__ == "__main__":
    main()