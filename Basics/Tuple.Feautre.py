


def main() :
    print("Demonstration of Tuple ");
    print("HetroGenious ");
    Tuple1 = (11 , "Roshan" , 96.23 , False);
    print(Tuple1)

    print(type(Tuple1))
    print(len(Tuple1))

    print("Indexed : " , end = " :")
    print(Tuple1[1]);    

    print("Tuple Data is Immutable")
    # Tuple1[0] = 12;
    # print(Tuple1)

    # Tuple1.append(101);
    # print(Tuple1)


    Tuple2 = (11 , 89 , 11 , 67 , 11 );
    print(Tuple2)


    for val in Tuple2 :
        print(val , end =" ")

    print()
    for i in range(len(Tuple2)):
        print(Tuple2[i]);

if(__name__ == "__main__"):
    main()