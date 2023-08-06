def Fun():
    print("Hello From Fun")

def ChkEnen(No):
    if (No % 2 == 0 ):
        return True
    else :
        return False;

def Add(No1 , No2):
    return No1 + No2

def Display(No):
    for iCnt in range(0 , No , 1):
        print("Marvellous")

def DisplayNum(No):
    while (No > 0 ):
        print(No)
        No = No - 1

def ChkPositive(No):
    if (No >= 0):
        return True;
    else :
        return False;

def Divisible(No1 , No2):
    if ( No1 % No2 == 0 ):
        return True;
    else :
        return False;

def Pattern(No):
    for iCnt in range (0 , No , 1):
        print("*\t",end ="")