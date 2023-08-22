# filterX  mapX ReduxeX

CheckEven = lambda No  : (No % 2 == 0)
Increase = lambda No : (No + 2)
Add =  lambda  No1 , No2    : ( No1 + No2)


# Task  : Name of Function
# Elements : List of data elements

def filterX (Task , Elements) : 
    Result = []
    for no in Elements :
        if (Task(no) == True ):
            Result.append(no)    
    return Result

# Task  : Name of Function
# Elements : List of data elements

def mapX ( Task  , Elements):
    Result = []
    for no in Elements :
        Result.append(Task(no))
    return Result

# Task  : Name of Function
# Elements : List of data elements

def reduceX (Task , Elements) : 
    Sum = 0  
    for no in Elements :
        Sum =  Task ( Sum , no)
    return Sum 


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