import os 

def main():
    print("Enter name of file that you want tooprn for reading purpose :")
    File_name = input()

    if os.path.exists(File_name):
        fobj: open(File_name , 'r')
        if fobj:
            print("File Succesfully opened")
        else:
            print("File FAiled to opened")
    else:
        print("Their is no such file ")

if __name__=="__main__":
    main()