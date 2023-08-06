# Default Arguments should be at the end
def Display(Name ,  Age , Marks = 90 ):
    print("Name is : " , Name)
    print("Age is : " , Age)
    print("Marks are  : ", Marks)



def main():
    print("Demonstration of Positional Arguments")

    Display( "Amit"  ,  59 )
    print(end = "       99 __ ")
    Display("Roshan" , 25 , 56 )


if (__name__ == "__main__"):
    main()
