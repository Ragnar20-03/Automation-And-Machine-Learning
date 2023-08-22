# Unnamed Function (Lamda / Anonnnymus)
# Name = lambda Paramter_List : Function_Logic

def Add(No1 : int , No2 : int):
    return No1 + No2

AddX =  lambda  No1 , No2    : ( No1 + No2)


def ChkEven(No : int):
    return (No %2 == 0 )

ChkEvenX = lambda No  : (No % 2 == 0)

def Increase(No : int):
    return No + 2

IncreaseX = lambda No : (No + 2)


def main ():
    
    print(AddX(10,11))
    print(ChkEvenX(11))
    print(IncreaseX(10))

    print()

    print(AddX(10,11))
    print(ChkEvenX(11))
    print(IncreaseX(10))



if __name__ == "__main__":
    main()