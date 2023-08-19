# Default Arguments should be at the end
def Display(*Arguments):
    for i in range(len(Arguments)):
        print(Arguments[i]  ,end = " ")
    print(end = "\n")

def main():
    print("Demonstration of Positional Arguments")
    Display(10 , 20 , "Roshan " , True)
    Display(11 , 21 , "22 ")


if (__name__ == "__main__"):
    main()

