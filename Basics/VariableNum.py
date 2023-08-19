# Default Arguments should be at the end
def Display(*Arguments):
    print(type(Arguments))
    print(len(Arguments))
    print(*Arguments)


def main():
    print("Demonstration of Positional Arguments")
    Display(10 , 20 , "Roshan " , True)


if (__name__ == "__main__"):
    main()
