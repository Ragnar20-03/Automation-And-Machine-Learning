import Marvellous


def main ():
    value = int(input("Enter Value\n"));
    if (Marvellous.ChkEnen(value)):
        print("Number is Even ");
    else :
        print("Number is Odd");


if __name__ == "__main__":
    main()