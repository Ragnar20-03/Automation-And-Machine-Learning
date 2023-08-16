def CountDigits ( No):
    iDigit = 0 
    iCount = 0 
    while ( No != 0 ):
        iDigit = int(No % 10) 
        No = int(No /  10)
        iCount = iCount + 1
    return iCount

def main():
    No = int(input("Enter Number"))
    print(CountDigits(No))

if __name__ == "__main__":
    main()