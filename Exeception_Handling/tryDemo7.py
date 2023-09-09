

def main():
    try:
        print("Enter First number ")
        no1 = int(input())
    
        print("Enter Second Number")
        no2 = int(input())
    
    
        Ans = 0 
        Ans = no1 / no2
        
    except ZeroDivisionError as zobj :
        print(zobj)
        print("Divide by zero is Not Allowed")
        return
    except Exception as eobj :
        print(eobj)
        print("Divide by zero is Not Allowed")
        return
    
    finally :
        print("Thanku for using Application")

    print("Division is : " , Ans)


if __name__ == "__main__" :
    main()