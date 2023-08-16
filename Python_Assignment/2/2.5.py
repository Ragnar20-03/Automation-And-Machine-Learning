def main():
    bFlag = True
    No = int(input("Enter Number"))
    for i in range(2 , int(No /2 ) +1 , 1):
        if (No % i == 0 ):
            bFlag = False;
    print(bFlag)

if __name__ == "__main__":
    main()