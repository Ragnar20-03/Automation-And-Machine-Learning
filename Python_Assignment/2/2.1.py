import Arithmatic

def main():
    No1 = int(input("Enter first Number"));
    No2 = int(input("Enter Second Number"));

    print("Addition is : " , Arithmatic.Addition(No1 , No2)); 
    print("Subtraction is : " , Arithmatic.Subtraction(No1 , No2)); 
    print("Mulltiplication is : " , Arithmatic.Mulltiplication(No1 , No2)); 
    print("Division is : " , Arithmatic.Division(No1 , No2)); 

if __name__ == "__main__":
    main() 
