import sys


def main():
    print("Demonstartion of List ")

    print("HetroGeneious ")
    List1 = [ 10, "Roshan " , 99.60 , True]
    print(List1);


    print("Indexed ")
    print(List1[0]);


    print("Duplication ")
    List2 = [11,78,90,11,45,78]
    print(List2)

    print("Data is Mutable")
    List2[1] = 79;
    print(List2)

    print("List is also Mutable")
    List2.append(101);
    print(List2)

    List2.remove(101);
    print(List2)

if (__name__ == "__main__"):
    main()