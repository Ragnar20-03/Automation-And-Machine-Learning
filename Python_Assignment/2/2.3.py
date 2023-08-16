def main():
    fact = 1 ;
    No = int(input("Enter Number"))
    for i in range(No , 0 , -1):
        fact *= i
    print("Factorail of a number is : " , fact)

if __name__ == "__main__":
    main()