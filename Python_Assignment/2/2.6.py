def Display ( No):
    for i in range (No , 0 , -1):
        for j in range (No , 0 , -1):
            if (j<=i):
                print("*" , end = "\t")
        print()

def main():
    No = int(input("Enter Number"))
    Display(No);

if __name__ == "__main__":
    main()