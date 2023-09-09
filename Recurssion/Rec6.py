import sys



def main():
    print("Recurssion Limit is :" , sys.getrecursionlimit())

    sys.setrecursionlimit(5000)

if __name__ =="__main__":
    main()

