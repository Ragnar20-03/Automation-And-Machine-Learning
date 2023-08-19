
def Display(Name ,  Age , Marks ):
    print("Name is : " , Name)
    print("Age is : " , Age)
    print("Marks are  : ", Marks)



def main():
    print("Demonstration of Positional Arguments")

    Display("Amit"  ,  59 , 22)
    print()
    Display("Roshan" , 25 , 56 )


if (__name__ == "__main__"):
    main()