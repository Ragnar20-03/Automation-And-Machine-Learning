import FMR_module 


CheckEven = lambda No  : (No % 2 == 0)
Increase = lambda No : (No + 2)
Add =  lambda  No1 , No2    : ( No1 + No2)

def main ():
    
    Data = []
    Size = int (input("Enter number of elements"))

    for i in range(Size):
        Data.append(int(input()))

    output = list(FMR_module.filterX(CheckEven,Data))
    print(output)

    moutput = list(FMR_module.mapX(Increase,output))
    print(moutput)

    result = FMR_module.reduceX(Add,moutput)
    print(result)



if __name__ == "__main__":
    main()