import os

def main():
    print("Enter the name of file that you want to open")
    File_name = input()

    fobj = open(File_name , 'r')
    if fobj:
        print("File opend in Read mode : ")
        print("Data From file is ")
        # for line in fobj:
        for line in fobj:
            print(line)


if __name__ == "__main__":
    main()