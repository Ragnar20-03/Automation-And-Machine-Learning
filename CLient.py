
import Marvellous

def main():
     print("Inside Client.py")
     value1 = int ( input("Enter First Number"));
     value2 = int(input ("Enter Second Number"));
 
     Result = 0 ;
     Result = Marvellous.Addition(value1 , value2)
     print("Addition is : " , Result)
 
     Result = Marvellous.Subtraction(value1 , value2)
     print("Subtraction is : " , Result)
 
     Result = Marvellous.Multiplication(value1 , value2)
     print("Multiplication is : " , Result)
 
     Result = Marvellous.Division(value1 , value2)
     print("Division is : " , Result)
 
if __name__ == "__main__":
    main();