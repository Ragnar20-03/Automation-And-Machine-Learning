import sys

i = 0

def  Display(no):
    global i
    
    if ( i<= no ):
        print(i)
        i += 1 
        Display(no)

def main():
    Display(15)

if __name__ =="__main__":
    main()
