def SumDigits ( No):
    iDigit = 0 
    iSum = 0 
    while ( No != 0 ):
        iDigit = int(No % 10) 
        iSum = iSum + iDigit
        No = int(No /  10)
    return iSum

def main():
    No = int(input("Enter Number"))
    print(SumDigits(No))

if __name__ == "__main__":
    main()