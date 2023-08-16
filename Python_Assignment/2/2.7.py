def Display ( No):
    for i in range (1 , No +1 , 1):
        for j in range (1 , No +1 , 1):
            print(j , end = "\t")
        print()

def main():
    No = int(input("Enter Number"))
    Display(No);

if __name__ == "__main__":
    main()