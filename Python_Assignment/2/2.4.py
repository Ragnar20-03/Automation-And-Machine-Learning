def main():
    sum  = 0  ;
    No = int(input("Enter Number"))
    for i in range(1 , int(No /2 ) +1 , 1):
        if (No % i == 0 ):
            sum += i
            print(sum , i)
    print("Addition of Factors is : " , sum)

if __name__ == "__main__":
    main()