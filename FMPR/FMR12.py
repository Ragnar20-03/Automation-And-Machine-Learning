from FMR_module import filterX
from FMR_module import mapX
from FMR_module import reduceX


CheckEven = lambda No  : (No % 2 == 0)
Increase = lambda No : (No + 2)
Add =  lambda  No1 , No2    : ( No1 + No2)

def main ():
    
    Data = []
    Size = int (input("Enter number of elements"))

    for i in range(Size):
        Data.append(int(input()))

    output = list(filterX(CheckEven,Data))
    print(output)

    moutput = list(mapX(Increase,output))
    print(moutput)

    result = reduceX(Add,moutput)
    print(result)



if __name__ == "__main__":
    main()