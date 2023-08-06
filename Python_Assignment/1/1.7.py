import Marvellous

def main():
    value = int(input("Enter The Number"))
    valueX = int (input("Enter divisible Number"))
    if (Marvellous.Divisible(value , valueX)):
        print("True")
    else :
        print("False")

if __name__ == "__main__":
    main();